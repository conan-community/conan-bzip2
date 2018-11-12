PROJECT(test_package C)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

find_package(BZip2 REQUIRED CONFIG)

ADD_EXECUTABLE(test_package test_package.c)
target_link_libraries(test_package ${CONAN_LIBS})
