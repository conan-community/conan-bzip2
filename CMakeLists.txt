cmake_minimum_required(VERSION 2.8)
project(bzip2)

include(../conanbuildinfo.cmake)
conan_basic_setup()

if(MSVC OR MSVC90 OR MSVC10)
    set(MSVC ON)
endif()

add_library(bz2
    blocksort.c
    bzlib.c
    compress.c
    crctable.c
    decompress.c
    huffman.c
    randtable.c
)
if(FPIC)
    message(WARNING "ENABLED FPIC")
    set_target_properties(bz2 PROPERTIES COMPILE_FLAGS "-fPIC")
endif()

add_executable(bzip2 bzip2.c)
target_link_libraries(bzip2 bz2)
