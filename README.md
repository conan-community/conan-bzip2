# conan-bzip2

Conan package for BZip2 library. http://www.bzip.org/

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/bzip2%3Aconan).


## Basic setup

    $ conan install bzip2/1.0.6@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    bzip2/1.0.6@conan/stable

    [options]
    bzip2:shared=true # false

    [generators]
    cmake
