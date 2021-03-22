import argparse
from typing import Final

import colorama

import build_system.cmd.hierarchy.find_build_dir
import utils.cli.arg
import utils.cli.arg_parsing
import utils.cli.try_cmd
from utils.more_typing import AnyPath

ROOT_DIR_ARG: Final[utils.cli.arg.CLIArg] = utils.cli.arg.CLIArg('rootdir')


def find_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Finds the project's '{colorama.Fore.LIGHTBLACK_EX}{build_system.cmd.hierarchy.find_build_dir.BUILD_DIR_NAME}{colorama.Style.RESET_ALL}' folder.")
    utils.cli.arg_parsing.add_optional_path_arg(arg_parser, ROOT_DIR_ARG, path_arg_help=f"The project's root directory")

    root_dir: AnyPath = utils.cli.arg_parsing.parse_optional_path_arg(arg_parser, ROOT_DIR_ARG)

    def cli_cmd():
        build_dir = build_system.cmd.hierarchy.find_build_dir.find_build_dir(root_dir)
        print(build_dir, end=str())

    utils.cli.try_cmd.try_cmd_except_managed_errors(cli_cmd, arg_parser)
