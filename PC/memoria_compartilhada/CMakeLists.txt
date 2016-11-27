cmake_minimum_required(VERSION 3.6)
project(PC_MC_Supermercado)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread")

set(SOURCE_FILES main.c)
find_package (Threads)
add_executable(PC_MC_Supermercado ${SOURCE_FILES})
target_link_libraries (PC_MC_Supermercado ${CMAKE_THREAD_LIBS_INIT})



