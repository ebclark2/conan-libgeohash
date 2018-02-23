from conans import ConanFile, CMake


class LibgeohashConan(ConanFile):
    name = "Libgeohash"
    version = "2469d3c"
    license = "BSD-3"
    homepage = "https://github.com/simplegeo/libgeohash"
    url = "https://github.com/ebclark2/conan-libgeohash.git"
    description = "A pure C implementation of the Geohash algorithm. http://geohash.org"
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False]}
    default_options = "fPIC=True"
    exports = "CMakeLists.txt", "Geohash.cmake", "FindLibgeohash.cmake"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/simplegeo/libgeohash.git")
        self.run("cd libgeohash && git checkout -q %s" % self.version)

    def build(self):
        cmake = CMake(self)
        if self.settings.os != "Windows":
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("FindLibgeohash.cmake", ".", ".")
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
