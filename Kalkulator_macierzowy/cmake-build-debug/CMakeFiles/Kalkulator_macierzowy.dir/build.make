# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "D:\Program Files (x86)\CLion\CLion 2019.3.4\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "D:\Program Files (x86)\CLion\CLion 2019.3.4\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\Clion_projekty\Kalkulator_macierzowy

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\Clion_projekty\Kalkulator_macierzowy\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/Kalkulator_macierzowy.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Kalkulator_macierzowy.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Kalkulator_macierzowy.dir/flags.make

CMakeFiles/Kalkulator_macierzowy.dir/main.cpp.obj: CMakeFiles/Kalkulator_macierzowy.dir/flags.make
CMakeFiles/Kalkulator_macierzowy.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Clion_projekty\Kalkulator_macierzowy\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Kalkulator_macierzowy.dir/main.cpp.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\Kalkulator_macierzowy.dir\main.cpp.obj -c D:\Clion_projekty\Kalkulator_macierzowy\main.cpp

CMakeFiles/Kalkulator_macierzowy.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Kalkulator_macierzowy.dir/main.cpp.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\Clion_projekty\Kalkulator_macierzowy\main.cpp > CMakeFiles\Kalkulator_macierzowy.dir\main.cpp.i

CMakeFiles/Kalkulator_macierzowy.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Kalkulator_macierzowy.dir/main.cpp.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S D:\Clion_projekty\Kalkulator_macierzowy\main.cpp -o CMakeFiles\Kalkulator_macierzowy.dir\main.cpp.s

# Object files for target Kalkulator_macierzowy
Kalkulator_macierzowy_OBJECTS = \
"CMakeFiles/Kalkulator_macierzowy.dir/main.cpp.obj"

# External object files for target Kalkulator_macierzowy
Kalkulator_macierzowy_EXTERNAL_OBJECTS =

Kalkulator_macierzowy.exe: CMakeFiles/Kalkulator_macierzowy.dir/main.cpp.obj
Kalkulator_macierzowy.exe: CMakeFiles/Kalkulator_macierzowy.dir/build.make
Kalkulator_macierzowy.exe: CMakeFiles/Kalkulator_macierzowy.dir/linklibs.rsp
Kalkulator_macierzowy.exe: CMakeFiles/Kalkulator_macierzowy.dir/objects1.rsp
Kalkulator_macierzowy.exe: CMakeFiles/Kalkulator_macierzowy.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Clion_projekty\Kalkulator_macierzowy\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Kalkulator_macierzowy.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\Kalkulator_macierzowy.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Kalkulator_macierzowy.dir/build: Kalkulator_macierzowy.exe

.PHONY : CMakeFiles/Kalkulator_macierzowy.dir/build

CMakeFiles/Kalkulator_macierzowy.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Kalkulator_macierzowy.dir\cmake_clean.cmake
.PHONY : CMakeFiles/Kalkulator_macierzowy.dir/clean

CMakeFiles/Kalkulator_macierzowy.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Clion_projekty\Kalkulator_macierzowy D:\Clion_projekty\Kalkulator_macierzowy D:\Clion_projekty\Kalkulator_macierzowy\cmake-build-debug D:\Clion_projekty\Kalkulator_macierzowy\cmake-build-debug D:\Clion_projekty\Kalkulator_macierzowy\cmake-build-debug\CMakeFiles\Kalkulator_macierzowy.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Kalkulator_macierzowy.dir/depend

