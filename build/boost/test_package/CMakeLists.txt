cmake_minimum_required(VERSION 3.24)

list(APPEND CMAKE_PREFIX_PATH ${CMAKE_CURRENT_LIST_DIR}/../../../boost-1.80.0)
find_package(Boost 1.80.0 CONFIG REQUIRED)

# packages found
get_property(_packages_found GLOBAL PROPERTY PACKAGES_FOUND)
message(STATUS "@@@ PACKAGES_FOUND: ${_packages_found}")
# imported targtets (from cmake 3.21)
get_property(_targets DIRECTORY ${CMAKE_SOURCE_DIR} PROPERTY IMPORTED_TARGETS)
message(STATUS "@@@ IMPORTED_TARGETS: ${_targets}")

add_executable(test_package main.cpp)
target_link_libraries(test_package Boost::headers Boost::dynamic_linking)
