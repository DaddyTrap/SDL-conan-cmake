# SDL-conan-cmake

[中文README](./README_zh.md)

As the repo name says, this is a simple framework of SDL with using conan and cmake. The purpose of this repo is to make it easier to setup a SDL environment.

## Setup

### Prerequisites

+ [conan](https://docs.conan.io/en/latest/introduction.html) (Simply execute `pip install conan` if you have `pip`)
	+ conan is a module of python, so you have to install [python](https://www.python.org/) first.
+ [cmake](https://cmake.org/)
+ Build Tools, e.g., `Visual Studio`, `g++` and etc.

### Use `sdl-cli` to generate a project

```
python /path/to/sdl-cli.py -p new_proj /path/to/output_dir
```

"new_proj" may be replaced by your project name.

"/path/to/output_dir" may be replaced by another proper path.

Besides, you can use `-e` to specify the entrypoint name (default: `'entrypoint'`) and `-std` to specify the standard of C++ (default: `'c++14'`).

### When the project is generated

`cd` to the generated project's directory, and

```
mkdir build && cd build
conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
conan install ..
cmake ..
```

In some circumstances, you may modify the commands above.

+ On Windows
	+ It is recommended to use Visual Studio to build this project, because conan may find pre-built package for Visual Studio (but not for MinGW). If you use Visual Studio, you can:
		+ `conan install -s compiler="Visual Studio" -s compiler.version=15 ..`
		+ This specifys the compiler to be Visual Studio. Depending on your Visual Studio version, you may modify `compiler.version`. If you use Visual Studio 2017 then the version is `15`, or if you use VS 2015, the version is `14`. (These seem like the version of Visual C++ ...)
	+ If you find that `cmake` generated a x86 solution, but you want to generate a x64 solution, you can delete the build directory and repeat the commands above, except changing `cmake ..` to `cmake -G "Visual Studio 15 2017 Win64" ..`

`conan install ..` may take a few minutes.

After `cmake`:

+ On Windows, you may use `MSBuild` to build the project in `build/` or just directly open `SDL_CONAN_CMAKE.sln` with Visual Studio and build.
+ On Linux / MacOS, you may use `make` to build.

> `hello.cpp` is a simple test to make sure that you can now use SDL and also SDL_image. It shows the SDL logo for about 3 seconds.
> If the window just flashes and disappears, don't panic! It's probably that it didn't find the file `SDL_logo.png`.
> Copy it to your working directory (where you run the built project) and it can work.

### Then?

Maybe you can start your project now... Enjoy.
