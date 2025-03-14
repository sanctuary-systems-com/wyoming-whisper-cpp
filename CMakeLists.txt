cmake_minimum_required(VERSION 3.16)
project(wyoming-whisper-cpp VERSION 0.1.0)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find dependencies
find_package(Threads REQUIRED)

# Build whisper.cpp with only what we need
set(BUILD_SHARED_LIBS OFF CACHE BOOL "Build shared libraries" FORCE)
set(WHISPER_BUILD_EXAMPLES OFF CACHE BOOL "Build examples" FORCE)
set(WHISPER_BUILD_TESTS OFF CACHE BOOL "Build tests" FORCE)
add_subdirectory(whisper.cpp)

# Add the common library from whisper.cpp examples
add_library(common STATIC
    whisper.cpp/examples/common.cpp
    whisper.cpp/examples/common-whisper.cpp
    whisper.cpp/examples/grammar-parser.cpp
)
target_include_directories(common PUBLIC 
    whisper.cpp/examples
    whisper.cpp
)
target_link_libraries(common PUBLIC whisper)

# Build Wyoming component
add_subdirectory(wyoming)