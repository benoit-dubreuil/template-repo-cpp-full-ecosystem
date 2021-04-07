import contextlib
from typing import Final

import colorama

import build_system.build_target.build_target
import build_system.compiler.installed_instance


# TODO : Refactor
def print_target_info(compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                      target_build_dir: build_system.build_target.build_target.BuildTarget,
                      compiler_env_vars_manager: contextlib.AbstractContextManager) -> None:
    def print_indented_label_and_info(pre_label_indent: str = str(),
                                      post_label_indent: str = str(),
                                      label: str = str(),
                                      info: str = str(),
                                      color_label: bool = True,
                                      color_info: bool = False) -> None:
        if color_label:
            label_colored = colorama.Fore.CYAN + label + colorama.Style.RESET_ALL + ':'
        else:
            label_colored = label

        if color_info:
            info_colored = colorama.Fore.LIGHTBLACK_EX + info + colorama.Style.RESET_ALL
        else:
            info_colored = info

        label_formatted = pre_label_indent + label_colored + post_label_indent
        line = label_formatted + info_colored

        print(line)

    def print_post_header_labels_and_info(pre_label_indent: str = str(),
                                          post_label_indent: str = str()):
        label_compiler_family_label = r'Compiler family'
        label_compiler_family_info = compiler_instance.compiler_family.value

        label_compiler_version_label = r'Compiler version'
        label_compiler_version_info = str(compiler_instance.version)

        label_compiler_arch_label = r'Compiler architecture'
        label_compiler_arch_info = compiler_instance.arch.arch_to_bit_name()

        label_compiler_installation_path_label = r'Compiler installation path'
        label_compiler_installation_path_info = str(compiler_instance.installation_dir)

        label_build_type_label = r'Build type'
        label_build_type_info = target_build_dir.target_build_type.value

        label_env_vars_label = None
        label_env_vars_info = None

        # noinspection PyTypeChecker
        if not isinstance(compiler_env_vars_manager, contextlib.nullcontext):
            label_env_vars_label = r'Environment variables'

            # noinspection PyUnresolvedReferences
            compiler_env_vars: dict[str, list[str]] = compiler_env_vars_manager.get_env_vars()

            label_env_vars_info = str(compiler_env_vars)

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_compiler_family_label,
                                      info=label_compiler_family_info)

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_compiler_version_label,
                                      info=label_compiler_version_info)

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_compiler_arch_label,
                                      info=label_compiler_arch_info)

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_compiler_installation_path_label,
                                      info=label_compiler_installation_path_info,
                                      color_info=True)

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_build_type_label,
                                      info=label_build_type_info)

        # noinspection PyTypeChecker
        if not isinstance(compiler_env_vars_manager, contextlib.nullcontext):
            assert label_env_vars_label is not None
            assert label_env_vars_info is not None

            print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                          post_label_indent=post_label_indent,
                                          label=label_env_vars_label,
                                          info=label_env_vars_info,
                                          color_info=True)

    white_space: Final[str] = ' '

    header_label = r'Target'
    header_colored_label = colorama.Fore.LIGHTCYAN_EX + header_label + colorama.Style.RESET_ALL
    post_header_indent = white_space * 6
    header_total_indent = (white_space * len(header_label)) + post_header_indent

    post_label_indent = white_space * 3

    print_indented_label_and_info(post_label_indent=post_header_indent,
                                  label=header_colored_label,
                                  color_label=False)

    print_post_header_labels_and_info(pre_label_indent=header_total_indent,
                                      post_label_indent=post_label_indent)
