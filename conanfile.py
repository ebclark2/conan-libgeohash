from conans import ConanFile, CMake
from conans.errors import ConanException


class LibgeohashConan(ConanFile):
    name = "Libgeohash"
    version = "0.1"
    license = "https://github.com/simplegeo/libgeohash/blob/master/LICENSE"
    url = "https://github.com/ebclark2/conan-libgeohash.git"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=False"
    exports = ["CMakeLists.txt", "Geohash.cmake", "FindLibgeohash.cmake"]
    generators = "cmake"

    INSTALL_DIR = "_install"

    def configure(self):
        del self.settings.compiler.libcxx
        if self.settings.os == "Windows":
            raise ConanException("Windows not supported")

    def source(self):
        self.run("git clone https://github.com/simplegeo/libgeohash.git")

    def build(self):
        cmake = CMake(self)
        self.run("mkdir _build")
        cd_build = "cd _build"
        CMAKE_OPTIONALS = ""
        if self.options.fPIC:
            c_flags.append("-fPIC")
        self.run("%s && cmake .. -DCMAKE_INSTALL_PREFIX=../%s %s %s" % (cd_build, self.INSTALL_DIR, cmake.command_line, CMAKE_OPTIONALS))
        self.run("%s && cmake --build . %s" % (cd_build, cmake.build_config))
        self.run("%s && cmake --build . --target install %s" % (cd_build, cmake.build_config))

    def package(self):
        self.copy("license*", dst="licenses",  ignore_case=True, keep_path=False)
        self.copy("*.h", dst="include", src="hello")
        self.copy("*geohash.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["geohash"]
