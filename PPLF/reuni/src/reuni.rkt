#lang racket

(require rackunit)
(require rackunit/text-ui)

;; Este programa encontra horários disponíveis que sejam comuns entre vários
;; horários especificados e que tenham um tamanho mínimo especificado.
;;
;; ** Conceitos **
;;  Horário
;;    Um momento no tempo, definido em termos da hora e minutos
;;  Intervalo (abreviado inter)
;;    Um intervalo no tempo, tem um horário de início e um horário de fim
;;  Disponibilidade do dia (abreviado dispo)
;;    Uma lista de intervalos que estão disponíveis em um determinado dia
;;  Disponibilidade semanal (abreviado dispo-semana)
;;    Uma lista com as disponibilidades de cada dia
;;  Lista de associações
;;    Uma lista de pares. Um par é uma lista com dois elementos. O primeiro
;;    elemento do par é chamado de chave e o segundo elemento é chamado de
;;    valor. Uma lista de associações é uma maneira simples de implementar uma
;;    tabela associativa (dicionário).  Ex: o dicionário
;;    1 -> 4, 20 -> 12, 6 -> 70, pode ser representado pela lista associativa
;;    (list (list 1 4) (list 20 12) (list 6 70)).
;;    A função assoc é utilizada para consultar uma lista associativa.
;;
;; ** Formatação de entrada e saída **
;; Toda operação de entrada e saída deve ser feita respeitando essas
;; formatações. A sua implementação não precisa validar as entradas. Para os
;; testes automatizados as entradas sempre serão válidas.
;;
;;  Horário (HH:MM) (sempre 5 dígitos)
;;  Exemplos
;;     08:30 =  8 horas e 30 minutos
;;     12:07 = 12 horas e  7 minutos
;;
;;  Intervalo (HH:MM-HH:MM) (sempre 11 dígitos)
;;  Exemplos
;;     08:30-12:07 = o intervalo tem início às 8 horas e 30 minutos e tem
;;                   o fim às 12 horas e 7 minutos
;;
;;  Dias da semana
;;    Representados por strings de tamanho 3: dom seg ter qua qui sex sab
;;
;;  Disponibilidade semanal
;;    Uma sequência de linhas. Cada linha contém o dia e a lista de
;;    intervalos disponíveis naquele dia
;;  Exemplo
;;    ter 10:20-12:00 16:10-17:30
;;    sex 08:30-11:30
;;  Observe que nem todos os dias devem estar especificados. Os dias
;;  que não têm disponibilidades não devem ser especificados.


;; exporta as funções que podem ser utilizadas em outros arquivos
(provide horario
         intervalo
         intervalo-vazio
         intervalo-vazio?
         intervalo-intersecao
         encontrar-dispo-em-comum
         encontrar-dispo-semana-em-comum
         main)

(struct horario (h m) #:transparent)
;; Horário representa um momento no tempo, definido em termos da hora e minutos
;;    h : Número - horas
;;    m : Número - minutos

(struct intervalo (inicio fim) #:transparent)
;; Intervalo representa um intervalo no tempo, tem um horário de início e um
;; horário de fim
;;    inicio : Horário - horário de início
;;       fim : Horário - horário de fim

;; Constante que define um intervalo vazio
(define intervalo-vazio (void))

;; Horario -> Número
;; Retorna os minutos de umm tempo
(define (minutos h)
  (+ (* (horario-h h) 60) (horario-m h)))

;; Número -> Horario
;; Retorna o tempo dos minutos
(define (tempo m)
  (horario (quotient m 60) (remainder m 60)))

;; Intervalo -> bool
;; Retorna #t se inter representa o intervalo vazio, #f caso contrário
(define (intervalo-vazio? inter)
  (equal? inter intervalo-vazio))

;; Intervalo -> Horario
;; Retorna o tempo do intervalo
(define (intervalo-tempo i)
  (tempo
   (- (minutos (intervalo-fim i)) (minutos (intervalo-inicio i)))))

;; Intervalo, Intervalo -> Intervalo
;; Calcula a interseção entre os intervalos a e b
(define (intervalo-intersecao a b)
  (let ([a-inicio (intervalo-inicio a)]
        [a-fim (intervalo-fim a)]
        [b-inicio (intervalo-inicio b)]
        [b-fim (intervalo-fim b)])
    (let ([a-inicio-minutos (minutos a-inicio)]
          [a-fim-minutos (minutos a-fim)]
          [b-inicio-minutos (minutos b-inicio)]
          [b-fim-minutos (minutos b-fim)])
      (cond
        [(and (< a-inicio-minutos b-inicio-minutos)
              (< a-fim-minutos b-inicio-minutos)) intervalo-vazio]
        [(and (< b-inicio-minutos a-fim-minutos)
              (< b-fim-minutos a-inicio-minutos)) intervalo-vazio]
        [else
         (intervalo
          (if (> (minutos a-inicio) (minutos b-inicio))
              a-inicio
              b-inicio)
          (if (< (minutos a-fim) (minutos b-fim))
              a-fim
              b-fim))]))))

;; list Intervalo, list Intervalo -> list Intervalo
;; Encontra a interseção dos intervalos de list-i-a e list-i-b.
(define (encontrar-dispo-em-comum dispo-a dispo-b tempo)
  (define (encontrar-dispo-recursivo dispo-a dispo-b)
    (define (iter d dispo)
      (if (empty? dispo)
          empty
          (append
           (let ([intersecao (intervalo-intersecao d (first dispo))])
             (cond
               [(equal? intersecao intervalo-vazio) empty]                             
               [else (list intersecao)]))
           (iter d (rest dispo)))))
    (cond
      [(empty? dispo-a) empty]
      [(empty? dispo-b) empty]
      [else (append
             (iter (first dispo-a) dispo-b)
             (encontrar-dispo-recursivo (rest dispo-a) dispo-b))]))
  (cond
    [(empty? dispo-a) dispo-b]
    [(empty? dispo-b) dispo-a]
    [else (filter (lambda (i) (>= (minutos (intervalo-tempo i)) (minutos tempo))) (encontrar-dispo-recursivo dispo-a dispo-b))]))

;; Horário, list dispo-semana -> dispo-semana
;; Esta função encontra os intervalos disponíveis para cada dia da semana que
;; sejam maiores que tempo e que sejam comuns a todas as disponibilidades
;; da lista dispos.
;;
;; dispo-semana é uma lista de associações entre um dia (string) e a
;; disponibilidade naquele dia. Veja a definição de lista de associações no
;; início deste arquivo.
;;
;; Por exemplo, a disponibilidade semanal (dispo-semana):
;; ter 10:20-12:00 16:10-17:30
;; sex 08:30-11:30g
;; é representada da seguinte maneira:
;; (list (list "ter" (list (intervalo (hora 10 20) (hora 12 00))
;;                         (intervalo (hora 16 10) (hora 17 30))))
;;       (list "sex" (list (intervalo (hora 08 30) (hora 11 30)))))
;;
;; Observe que esta função recebe como parâmetro uma lista de disponibilidades
;; semanais, o exemplo acima refere-se a apenas uma disponibilidade semanal.
;; Veja os testes de unidade para exemplos de entrada e saída desta função
;; list dispo-semana  list dispo-semana  -> list dispo-semana
(define (encontrar-dispo-a-b dispo-a dispo-b tempo)
  (define (iter d l-dispo)
    (if (null? l-dispo)
        empty
        (let ([dia-a (car d)]
              [intervalos-a (cadr d)]
              [b (assoc (car d) l-dispo)])
          ( if (not (pair? b))
               empty
               (let ([dispo (encontrar-dispo-em-comum intervalos-a (cadr b) tempo)])
                 (cond
                   [(empty? dispo) empty]                   
                   [else (list dia-a dispo)]))))))    
  (cond
    [(empty? dispo-a) empty]
    [(empty? dispo-b) empty]
    [else (append
           (let ([d-iter  (iter (car dispo-a) dispo-b)])
             (if (empty? d-iter)
                 empty
                 (list (iter (car dispo-a) dispo-b))))
           (encontrar-dispo-a-b (cdr dispo-a) dispo-b tempo))]))

(define (encontrar-dispo-semana-em-comum tempo dispos)
  (foldr (lambda (a b) (encontrar-dispo-a-b a b tempo)) (first dispos) dispos))
;; list string -> void
;; Esta é a função principal. Esta função é chamada a partir do arquivo
;; reuni-main.rkt
;;
;; args é a lista de parâmetros para o programa.
;;
;; O primeiro parâmetro é o tempo mínimo (string) que os intervalos em comum
;; devem ter. O tempo mínimo é especificado usando a formatação de horário.
;;
;; O restante dos parâmetros são nomes de arquivos. Cada arquivo de entrada
;; contêm uma disponibilidade semanal. Veja exemplos de arquivos no diretórios
;; testes.
;;
;; A saída desta função é a escrita na tela dos intervalos em comum que
;; foram encontrados. O formato da saída deve ser o mesmo da disponibilidade
;; semanal.

(define (string->horario s)
  (horario (string->number (substring s 0 2)) (string->number (substring s 3 5))))

(define (string->intervalo s)
  (intervalo (string->horario (substring s 0 5)) (string->horario (substring s 6 11))))

(define (string->list-intervalo s)
  (define (iter lst)
    (cond
      [(empty? lst) empty]
      [else (append
             (list (string->intervalo (first lst)))
             (iter (rest lst)))]))
  (iter (string-split s)))

(define (string->dispo s)
  (list (substring s 0 3)
        (string->list-intervalo (substring s 3))))

(define (string->dispo-semana s)
  (define (iter lst)
    (cond
      [(empty? lst) empty]
      [else (append
             (list (string->dispo (first lst)))
             (iter (rest lst)))]))
  (iter (string-split s "\n")))

(define (args->list-dispo a)
  (cond
    [(empty? a) empty]
    [else (append
           (list (string->dispo-semana (file->string (first a))))
           (args->list-dispo (rest a)))]))

(define (inteiro->string-formatada i)
  (cond
    [(< i 10) (string-append "0" (number->string i))]
    [else (number->string i)]))

(define (horario->string h)
  (string-append (inteiro->string-formatada (horario-h h))
                 ":"
                 (inteiro->string-formatada (horario-m h))))

(define (intervalo->string i)
  (string-append (horario->string (intervalo-inicio i))
                 "-"
                 (horario->string (intervalo-fim i))))

(define (list-intervalo->string lst)
  (define (iter lst)
    (cond
      [(empty? lst) ""]
      [else (string-append  " "
                            (intervalo->string (first lst))                          
                            (iter (rest lst)))]))
  (iter lst))

(define (dispo->string d)  
  (string-append (first d)
                 (list-intervalo->string (first (rest d)))))

(define (dispo-semana->string ds)
  (define (iter lst)
    (cond
      [(empty? lst) ""]
      [else (string-append             
             (dispo->string (first lst))
             "\n"
             (iter (rest lst)))]))
  (iter ds))

(define (main args)
  (display (dispo-semana->string (encontrar-dispo-semana-em-comum (string->horario (first args)) (args->list-dispo (rest args))))))
