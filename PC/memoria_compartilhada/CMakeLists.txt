cmake_minimum_required(VERSION 3.6)
project(memoria_compartilhada)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread")

set(SOURCE_FILES memoria_compartilhada.c)
find_package (Threads)
add_executable(memoria_compartilhada ${SOURCE_FILES})
target_link_libraries (memoria_compartilhada ${CMAKE_THREAD_LIBS_INIT})



