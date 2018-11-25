# coding: utf-8

from argparse import ArgumentParser, Namespace
import sys
import os
from shutil import copy as shcopy
from copy import copy
try:
    # This is only for typing check
    from typing import List, Tuple, Union
except ImportError:
    pass

# *tuple* means copy from *tuple[0]*(old name) to *tuple[1]*(new name)
# *str* means keep the original name
FILES_TO_COPY = [
    '.gitignore', 'conanfile.txt',
    ('hello.cpp', 'main.cpp'),
]  # type: List[Union[Tuple[str, str], str]]

if sys.platform == 'win32' or sys.platform == 'cygwin':
    PATH_SLASH = '\\'
else:
    PATH_SLASH = '/'


def parse_args(args):
    # type: (List[str]) -> Namespace
    parser = ArgumentParser(description='Simple SDL project generate')
    parser.add_argument(
        'output_dir', help='The directory path where the files generated', default='.')
    parser.add_argument('-p', '--project-name',
                        help='The project name', required=True)
    parser.add_argument('-e', '--entrypoint-name',
                        help='The entrypoint/executable name', default='entrypoint')
    parser.add_argument(
        '-std', help='Specify the standard of C++', default='c++14')

    return parser.parse_args(args)


def generate_cmakelists(parse_res):
    # type: (Namespace) -> str
    res_template = '''# This is generatede by sdl-cli, you may modify this to suit your need
project({project_name})
cmake_minimum_required(VERSION 3.5)
add_definitions("-std={std}")

include(${{CMAKE_BINARY_DIR}}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable({entrypoint_name} main.cpp)
target_link_libraries({entrypoint_name} ${{CONAN_LIBS}})
'''
    return res_template.format(project_name=parse_res.project_name,
                               std=parse_res.std,
                               entrypoint_name=parse_res.entrypoint_name)


def _copy_files(file_list):
    # type: (List[Union[Tuple[str, str]]]) -> None
    for f in file_list:
        shcopy(f[0], f[1])


def _file_list_to_abs(file_list, cli_dir, new_dir):
    # type: (List[Union[str, Tuple[str, str]]], str, str) -> List[Tuple[str, str]]
    new_file_list = []  # type: List[Tuple[str, str]]
    for f in file_list:
        if isinstance(f, tuple):
            assert len(f) == 2
            abs_0 = cli_dir + PATH_SLASH + f[0]
            abs_1 = new_dir + PATH_SLASH + f[1]
            new_file_list.append((abs_0, abs_1))
        elif isinstance(f, str):
            abs_0 = cli_dir + PATH_SLASH + f
            abs_1 = new_dir + PATH_SLASH + f
            new_file_list.append((abs_0, abs_1))
    return new_file_list


def copy_and_rename_files(cli_dir, new_dir):
    # type: (str, str) -> None
    print('Trying to make new dir: ' + new_dir + '\n')
    overwrite = False
    if os.path.isdir(new_dir):
        print('Directory {} already exists. Overwrite? (y/n) '.format(new_dir), end='')
        choice = input()  # type: str
        if choice.lower() == 'y':
            overwrite = True
        else:
            return
    try:
        os.makedirs(new_dir)
    except OSError:
        if not overwrite:
            print('Directory {} creating failed!'.format(new_dir))
            return

    file_list = _file_list_to_abs(FILES_TO_COPY, cli_dir, new_dir)
    try:
        _copy_files(file_list)
    except OSError:
        print('OSError happened when copying files')
        return


def build_project(parse_res):
    # type: (Namespace) -> None
    cmakelists_str = generate_cmakelists(parse_res)
    cli_dir = os.path.dirname(os.path.abspath(__file__))
    new_dir = ('{}' + PATH_SLASH +
               '{}').format(os.path.abspath(parse_res.output_dir), parse_res.project_name)
    copy_and_rename_files(cli_dir, new_dir)
    # write CMakeLists.txt
    with open('{}{}{}'.format(new_dir, PATH_SLASH, 'CMakeLists.txt'), 'wb') as f:
        f.write(cmakelists_str.encode('utf-8'))

    print('Generate finished!')

def main():
    args = sys.argv[1:]
    parse_res = parse_args(args)
    build_project(parse_res)

if __name__ == '__main__':
    main()
