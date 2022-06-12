import os
import argparse
import glob
from pathlib import Path
from colorama import Fore, init
from pycodestyle import StyleGuide
from typing import Union


def test_file_exists(base_path: Path, filename: str):
    """
    Checks that a file exists. The return scheme is reversed: this allows us
    to count the ERRORS.

    :param {Path} base_path - The base path.
    :param {str} filename - The filename to check for.
    :param {bool} status - True if the file does NOT exist.
    """
    if not os.path.exists(base_path / filename):
        print(Fore.RED + 'File missing: ' + filename)
        return True
    return False


def test_string_exists(base_path: Path, filename: str, string: Union[str, list], beginning: bool):
    """
    Tests whether a file contains a specific string, optionally at the beginning of a line. As with
    test_file_exists, returns True if the string does NOT exist.

    :param {Path} base_path - The base path
    :param {str} filename - The file to test
    :param {Union[str, list]} string - The string to test. If a list, checks if ANY of the strings exist
    :param {bool} beginning - Whether the string should be at the beginning of the file.
    :return {bool} status - True if the string does NOT exist.
    """
    with open(base_path / filename, 'r') as f:
        text = f.read()

    pattern = ''  # Pattern to test for
    if beginning:
        pattern += '\n'

    if isinstance(string, str):
        pattern += string
        if pattern not in text:
            print(Fore.RED + f'Missing text in {filename}: {string}')
            return True
    else:
        pattern_reset = pattern  # Keep a backup
        for item in string:
            pattern += item
            if pattern in text:
                return False  # We don't need to check anymore
            pattern = pattern_reset  # Reset `pattern`
        return True
    return False


def _main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='Checks compliance with the RAISE code template.')
    parser.add_argument('path', type=str, help='Root directory')
    parser.add_argument('--max_line_length', default=120)
    args = parser.parse_args()

    # Extract root directory
    base_path = Path(args.path)

    # Initialize colorama
    init()

    # Perform pycodestyle checks
    print(Fore.BLUE + '[Running code style checks]')
    print(Fore.RED)
    checker = StyleGuide(max_line_length=args.max_line_length)
    report = checker.check_files(paths=glob.glob(
        f'{base_path}/**/*.py', recursive=True))
    report.print_statistics()

    if report.get_count() == 0:
        print(Fore.GREEN + 'No issues found.')
    print()

    # Perform file checks
    print(Fore.BLUE + '[Checking directory structure]\n')
    error_count = 0
    file_list = [
        'README.md',
        'src/',
        'data/',
        '.gitignore',
        'LICENSE',
        'requirements.txt',
        'main.py',
        'src/__init__.py'
    ]

    for file in file_list:
        error_count += test_file_exists(base_path, file)

    if error_count == 0:
        print(Fore.GREEN + 'No issues found.')
    print()

    print(Fore.BLUE + '[Checking README]\n')
    error_count = 0
    lines_list = [
        '## Data',
        '## Reference',
        ['## Instructions', '## Setup']
    ]

    for line in lines_list:
        error_count += test_string_exists(base_path, 'README.md', line, True)

    if error_count == 0:
        print(Fore.GREEN + 'No issues found.')


if __name__ == '__main__':
    _main()
