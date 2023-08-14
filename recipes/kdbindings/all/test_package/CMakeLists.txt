cmake_minimum_required(VERSION 3.8)
project(test_package LANGUAGES CXX)

find_package(KDBindings QUIET CONFIG)
add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE KDAB::KDBindings)

target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_17)
set_target_properties(${PROJECT_NAME} PROPERTIES CMAKE_INCLUDE_CURRENT_DIRS ON)
