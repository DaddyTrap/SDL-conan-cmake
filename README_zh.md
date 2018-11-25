# SDL-conan-cmake

如仓库所述，这是一个使用了 conan 和 cmake 来构建的简单的 SDL 框架。本仓库的意图是让配置 SDL 更加简单。

## 配置

### 前置软件

+ [conan](https://docs.conan.io/en/latest/introduction.html) 如果你已经安装 `pip`，那么只要简单地 `pip install conan`
	+ conan 是 python 的一个模块，因此你必须先安装 [python](https://www.python.org/)
+ [cmake](https://cmake.org/)
+ 构建工具，如 `Visual Studio`、`g++` 等等

### 使用 `sdl-cli` 来生成项目

```
python /path/to/sdl-cli.py -p new_proj /path/to/output_dir
```

"new_proj" 可以替换为项目名

"/path/to/output_dir" 可以替换为合适的路径

此外，你可以用 `-e` 参数来指定入口程序名 (默认为 `'entrypoint'`) 和 `-std` 参数指定 C++ 的标准 (默认为 `'c++14'`)

### 项目生成后

`cd` 到已生成项目目录，然后

```
mkdir build && cd build
conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
conan install ..
cmake ..
```

在某些情况下，你可能需要修改上面的指令。

+ Windows 上
	+ 推荐使用 Visual Studio 来构建本项目，因为 conan 可以找到对应 Visual Studio 的已构建好的包 (而 MinGW 没有)。如果你使用的正是 Visual Studio，那么你可以：
		+ `conan install -s compiler="Visual Studio" -s compiler.version=15 ..`
		+ 这会指定编译器为 Visual Studio。取决于 Visual Studio 的版本，你可能需要修改 `compiler.version`。如果你使用的是 Visual Studio 2017，那么版本号就是 `15`，或者如果你使用的是 VS 2015，版本号是 `14`。(这些应该是 Visual C++ 的版本号……)
		+ 如果你发现 `cmake` 生成了一个 x86 的解决方案，而你想要生成 x64 的解决方案，你可以删除 build 目录然后将 `cmake ..` 改为 `cmake -G "Visual Studio 15 2017 Win64" ..` 重复上述步骤

`conan install ..` 可能会花一些时间。(而且可能需要科学上网)

在 `cmake` 之后：

+ Windows 上，你可以使用 `MSBuild` 来在 `build/` 目录下构建项目，或者直接用 Visual Studio 打开 `SDL_CONAN_CMAKE.sln` 并进行生成。
+ 在 Linux / MacOS 上，你可以使用 `make` 来构建项目。

> `hello.cpp` 是一个用于验证你现在是否能正常使用 SDL 和 SDL_image 的简单测试程序。它会展示 3 秒 SDL 的 logo
> 如果窗口闪退，别慌！这很可能是因为它找不到 `SDL_logo.png`
> 将它复制到你的工作目录 (你运行已构建项目的地方) 然后它就能用了

### 然后呢？

或许你现在可以开始你的项目了……Enjoy
