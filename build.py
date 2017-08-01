from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="ebclark2")
    builder.add_common_builds()
    builder.run()
