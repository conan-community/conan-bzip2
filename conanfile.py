import os
from conans import ConanFile, CMake, tools
from conans.tools import Version


class Bzip2Conan(ConanFile):
    name = "bzip2"
    version = "1.0.8"
    url = "https://github.com/conan-community/conan-bzip2"
    homepage = "http://www.bzip.org"
    author = "Conan Community"
    license = "bzip2-1.0.8"
    description = "bzip2 is a free and open-source file compression program that uses the Burrows–Wheeler algorithm."
    topics = ("conan", "bzip2", "data-compressor", "file-compression")
    settings = "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False], "build_executable": [True, False]}
    default_options = {"shared": False, "fPIC": True, "build_executable": True}
    exports = "LICENSE"
    exports_sources = "CMakeLists.txt"
    generators = "cmake"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        source_url = "https://sourceware.org/pub/bzip2/bzip2"
        folder_name = "%s-%s" % (self.name, self.version)
        sha256 = "ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269"
        tools.get("{}-{}.tar.gz".format(source_url, self.version), sha256=sha256)
        os.rename(folder_name, self._source_subfolder)

    def _configure_cmake(self):
        major = Version(self.version).major
        cmake = CMake(self)
        cmake.definitions["BZ2_VERSION_STRING"] = self.version
        cmake.definitions["BZ2_VERSION_MAJOR"] = major
        cmake.definitions["BZ2_BUILD_EXE"] = "ON" if self.options.build_executable else "OFF"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ['bz2']
