from cli_fetch_compiler_version import cli_fetch_compiler_version_with_default_path
from data_model import Compiler
from fetch_gnu_compiler_version import fetch_gnu_compiler_version


def cli_fetch_gnu_compiler_version(compiler: Compiler):
    cli_fetch_compiler_version_with_default_path(compiler, fetch_gnu_compiler_version)
