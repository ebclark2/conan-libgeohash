from conans import ConanFile, CMake, tools


class LibgeohashConan(ConanFile):
    name = "Libgeohash"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/simplegeo/libgeohash.git")

    def build(self):
        self.run('make -C libgeohash')

    def package(self):
        self.copy("*.h", dst="include", src="libgeohash")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["geohash"]
