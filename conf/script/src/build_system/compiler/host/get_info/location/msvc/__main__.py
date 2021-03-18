#!/usr/bin/env python3

import build_system.compiler.host.get_info.location.msvc.cli
import utils.cli.main
from build_system.compiler.host.get_info import location


def main():
    location.msvc.cli.find()


utils.cli.main.wrap_main(main)
