find_path(Libgeohash_INCLUDE_DIR NAMES shapefil.h
	PATHS ${CONAN_INCLUDE_DIRS_SHAPELIB}
	NO_DEFAULT_PATH)

find_library(Libgeohash_LIBRARY NAMES ${CONAN_LIBS_SHAPELIB}
	PATHS ${CONAN_LIB_DIRS_SHAPELIB}
	NO_DEFAULT_PATH)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Libgeohash
	REQUIRED_VARS Libgeohash_LIBRARY Libgeohash_INCLUDE_DIR
	FOUND_VAR Libgeohash_FOUND
)

set(Libgeohash_INCLUDE_DIRS ${Libgeohash_INCLUDE_DIR})
set(Libgeohash_LIBRARIES ${Libgeohash_LIBRARY})

mark_as_advanced(Libgeohash_INCLUDE_DIR Libgeohash_LIBRARY)

