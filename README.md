# SDL-conan-cmake

As the repo name says, this is a simple framework of SDL with using conan and cmake. The purpose of this repo is to make it easier to setup a SDL environment.

## Setup

### Prerequisites

+ [conan](https://docs.conan.io/en/latest/introduction.html) (Simply execute `pip install conan` if you have `pip`)
+ [cmake](https://cmake.org/)

### Commands

```
mkdir build && cd build
conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan # Add bincrafters's packages
conan install .. # This may take a few minutes
cmake ..
```

After `cmake`:

+ On Windows, you may use `MSBuild` to build the project in `build/` or just directly open `SDL_CONAN_CMAKE.sln` with Visual Studio and build.
+ On Linux / MacOS, you may use `make` to build.

> `hello.cpp` is a simple test to make sure that you can now use SDL and also SDL_image. It shows the SDL logo for about 3 seconds.
> If the window just flashes and disappears, don't panic! It's probably that it didn't find the file `SDL_logo.png`.
> Copy it to your working directory (where you run the built project) and it can work.

## Then?

Then you may delete the unnecessary files in the directory, like `.git/`, `SDL_logo.png` and `hello.cpp` and add your own files. Don't forget to modify `CMakeLists.txt` to suit your needs.
