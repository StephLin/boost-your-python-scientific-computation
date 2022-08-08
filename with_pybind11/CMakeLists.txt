cmake_minimum_required(VERSION 3.0.0)
project(lib VERSION "0.0.1")

if(POLICY CMP0057)
    cmake_policy(SET CMP0057 NEW)
endif()

set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_FLAGS "-O3 -Wall -std=c++11")

find_package(Eigen3 REQUIRED)
find_package(OpenMP REQUIRED)
find_package(Python COMPONENTS Interpreter Development)

execute_process(
COMMAND "${PYTHON_EXECUTABLE}" -c
        "import pybind11; print(pybind11.get_cmake_dir())"
OUTPUT_VARIABLE _tmp_dir
OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")

# Now we can find pybind11
find_package(pybind11 CONFIG REQUIRED)

include_directories ( ${EIGEN3_INCLUDE_DIRS} )

pybind11_add_module(lib MODULE src/lib.cpp)
target_compile_definitions(lib PRIVATE VERSION_INFO=${PROJECT_VERSION})
target_link_libraries(lib PRIVATE OpenMP::OpenMP_CXX)
