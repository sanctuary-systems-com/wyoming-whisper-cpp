set(TARGET whisper-wyoming)
add_executable(${TARGET} wyoming.cpp)

# Include directories for whisper.cpp examples
target_include_directories(${TARGET} PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/../whisper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/../whisper.cpp/examples
)

# Link with the necessary libraries
target_link_libraries(${TARGET} PRIVATE whisper common ${FFMPEG_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT})

# Install the binary to the correct location for scikit-build
install(TARGETS ${TARGET} RUNTIME DESTINATION bin)