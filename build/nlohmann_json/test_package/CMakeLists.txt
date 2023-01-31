cmake_minimum_required(VERSION 3.24)

#####################################################################################
# find nlomann_json packages                                                        #
#####################################################################################
# list(APPEND CMAKE_PREFIX_PATH ${CMAKE_CURRENT_LIST_DIR}/../../../nlohmann_json-3.11.2)
find_package(nlohmann_json 3.11.2 EXACT CONFIG REQUIRED COMPONENTS nlohmann_json)

#####################################################################################
# debug lines, for more info, not affect build precudure                            #
#####################################################################################
# packages found                                                                    #
get_property(_packages_found GLOBAL PROPERTY PACKAGES_FOUND)                        #
message(STATUS "@@@ PACKAGES_FOUND: ${_packages_found}")                            #
# imported targtets (from cmake 3.21)                                               #
get_property(_targets DIRECTORY ${CMAKE_SOURCE_DIR} PROPERTY IMPORTED_TARGETS)      #
message(STATUS "@@@ IMPORTED_TARGETS: ${_targets}")                                 #
foreach(_t ${_targets})                                                             #
    message(STATUS "    ${_t}")                                                     #
    foreach(_p                                                                      #
        IMPORTED_IMPLIB_RELEASE                                                     #
        IMPORTED_IMPLIB_DEBUG                                                       #
        IMPORTED_LOCATION_RELEASE                                                   #
        IMPORTED_LOCATION_DEBUG                                                     #
        INTERFACE_INCLUDE_DIRECTORIES                                               #
        INTERFACE_COMPILE_DEFINITIONS                                               #
    )                                                                               #
        get_target_property(_v ${_t} ${_p})                                         #
        message(STATUS "        ${_p} = ${_v}")                                     #
    endforeach()                                                                    #
endforeach()                                                                        #
#####################################################################################
# debug lines, for more info, not affect build precudure                            #
#####################################################################################


add_executable(test_package main.cpp)
target_link_libraries(test_package
    PRIVATE
        nlohmann_json::nlohmann_json
)
