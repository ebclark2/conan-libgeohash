from conans import ConanFile, CMake


class LibgeohashConan(ConanFile):
    name = "Libgeohash"
    version = "2469d3c"
    license = "BSD-3"
    homepage = "https://github.com/simplegeo/libgeohash"
    url = "https://github.com/ebclark2/conan-libgeohash.git"
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False]}
    default_options = "fPIC=False"
    exports = "CMakeLists.txt", "Geohash.cmake", "FindLibgeohash.cmake"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        self.run("git clone https://github.com/simplegeo/libgeohash.git")
        self.run("cd libgeohash && git checkout -q %s" % self.version)

    def build(self):
        cmake = CMake(self)
        if self.options.fPIC and self.settings.os != "Windows":
            cmake.definitions["CONAN_CXX_FLAGS"] = "-fPIC"
            cmake.definitions["CONAN_C_FLAGS"] = "-fPIC"
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("license*", dst="licenses", ignore_case=True, keep_path=False)
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*geohash.lib", dst="lib", keep_path=False)

        # Library is only building in static but keeping it in case it's added shared is added later
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["geohash"]
