from pathlib import Path
from typing import AnyStr, Callable

from build_system.compiler.version import CompilerVersion
from utils.cmd_integrity import cmd_exists


def assure_path_integrity(compiler_path: Path) -> None:
    """Assures the integrity of the supplied :param:`compiler_path`

    :param compiler_path: The path to the compiler executable file. It must not be a directory.
    """
    if not cmd_exists(str(compiler_path)):
        raise FileNotFoundError('Compiler at the supplied path does not exist or requires ungranted permissions')


def interpret_fetched_version(compiler_version_str: AnyStr) -> CompilerVersion:
    return CompilerVersion.create_from_str(compiler_version_str.strip())


def fetch(compiler: Path, fetch_compiler_version_func: Callable[[Path], AnyStr]) -> CompilerVersion:
    compiler_version_str: AnyStr = fetch_compiler_version_func(compiler)
    return interpret_fetched_version(compiler_version_str)
