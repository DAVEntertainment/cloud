cmake_minimum_required(VERSION 3.24)

#####################################################################################
# debug lines, for more info, not affect build precudure                            #
#####################################################################################
set(Boost_DEBUG 1)                                                                  #
set(Boost_VERBOSE 1)                                                                #
# set(Boost_NO_BOOST_CMAKE 1)                                                       #
#####################################################################################
# debug lines, for more info, not affect build precudure                            #
#####################################################################################


#####################################################################################
# boost configurations (default ones)                                               #
#####################################################################################
# set(Boost_USE_STATIC_LIBS ON) # use static libs or shared libs
# set(Boost_USE_STATIC_RUNTIME OFF) # use static runtime
# set(Boost_USE_DEBUG_RUNTIME OFF) # use debug runtime
# set(Boost_USE_MULTITHREADED ON) # use multi-threaded libs
# set(Boost_USE_DEBUG_LIBS OFF) # use debug libs


#####################################################################################
# find boost packages                                                               #
#####################################################################################
# we should find boost packages with find_package(boost_<lib-name> [...])
# find_package(Boost [...]) will not find each library, only following targets found:
#   Boost::headers      Boost::boost    Boost::diagnostic_definitions
#   Boost::disable_autolinking          Boost::dynamic_linking
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_CURRENT_LIST_DIR}/../../../boost-1.80.0)
# find_package(Boost 1.80.0 EXACT CONFIG REQUIRED)
find_package(boost_headers 1.80.0 EXACT CONFIG REQUIRED)
find_package(boost_date_time 1.80.0 EXACT CONFIG REQUIRED)



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
        Boost::headers
        Boost::date_time
)
