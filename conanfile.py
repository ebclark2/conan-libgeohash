from conans import ConanFile, CMake
from conans.errors import ConanException


class LibgeohashConan(ConanFile):
    name = "Libgeohash"
    version = "2469d3c"
    license = "BSD-3"
    homepage = "https://github.com/simplegeo/libgeohash"
    url = "https://github.com/ebclark2/conan-libgeohash.git"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False",
    exports = "CMakeLists.txt", "Geohash.cmake", "FindLibgeohash.cmake"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        self.run("git clone https://github.com/simplegeo/libgeohash.git")
        self.run("cd libgeohash && git checkout -q %s" % self.version)

    def build(self):
        cmake = CMake(self)
        if self.options.shared and self.settings.os != "Windows":
            cmake.definitions["CONAN_CXX_FLAGS"] = "-fPIC"
            cmake.definitions["CONAN_C_FLAGS"] = "-fPIC"
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("license*", dst="licenses", ignore_case=True, keep_path=False)
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*geohash.lib", dst="lib", keep_path=False)

        if self.options.shared:
            self.copy("*.dll", dst="bin", keep_path=False)
            self.copy("*.so", dst="lib", keep_path=False)
            self.copy("*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["geohash"]
