project(SDL_CONAN_CMAKE)
cmake_minimum_required(VERSION 3.5)
add_definitions("-std=c++14")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(hello hello.cpp)
target_link_libraries(hello ${CONAN_LIBS})
