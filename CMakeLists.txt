cmake_minimum_required(VERSION 3.12)
project(StackScopePlusPlus VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -fopenmp")

# Include directories
include_directories(${PROJECT_SOURCE_DIR}/include)

# Source files
set(EVALUATOR_SOURCES
    src/evaluator.cpp
)

set(MAIN_SOURCES
    src/main.cpp
    ${EVALUATOR_SOURCES}
)

# Main executable
add_executable(stackscope ${MAIN_SOURCES})
target_link_libraries(stackscope PRIVATE nlohmann_json::nlohmann_json)

# Enable testing
enable_testing()

# Google Test framework
include(FetchContent)
FetchContent_Declare(googletest
    URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
FetchContent_MakeAvailable(googletest)

# Unit tests
add_executable(stackscope_tests
    tests/test_evaluator.cpp
    ${EVALUATOR_SOURCES}
)
target_link_libraries(stackscope_tests PRIVATE GTest::gtest_main nlohmann_json::nlohmann_json)
add_test(NAME StackScopeTests COMMAND stackscope_tests)

# Installation
install(TARGETS stackscope DESTINATION bin)
install(FILES include/evaluator.h DESTINATION include)

# Print build info
message(STATUS "StackScope++ Build Configuration")
message(STATUS "CMAKE_BUILD_TYPE: ${CMAKE_BUILD_TYPE}")
message(STATUS "C++ Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Compiler: ${CMAKE_CXX_COMPILER}")
