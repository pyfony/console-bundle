from typing import List, Union
from consolebundle.ConsoleCommand import ConsoleCommand


class CommandManager:
    def __init__(self, commands: List[ConsoleCommand]):
        self.__commands = commands

    def get_commands(self):
        return self.__commands

    def log_commands(self, logger):
        print("\n[Available commands]:", flush=True)
        for existing_command in self.get_commands():
            logger.info(existing_command.get_command() + " - " + existing_command.get_description())

    def log_subcommands(self, command_name: list, logger):
        print("\n[Available space-separated commands]:", flush=True)
        command_prefix = ':'.join(command_name)
        for existing_command in self.get_commands():
            if existing_command.get_command().startswith(command_prefix):
                logger.info(
                    f"{' '.join(existing_command.get_command().split(':'))} - " + existing_command.get_description())

    def get_by_name(self, name: list) -> ConsoleCommand:
        desired_name = ':'.join(name)
        for command in self.__commands:
            if command.get_command() == desired_name:
                return command

        raise Exception('No command with name "{}" found'.format(name))

    def command_prefix_only(self, name: list) -> bool:
        desired_name = ':'.join(name)
        for command in self.__commands:
            if not command.get_command().startswith(desired_name):
                continue
            split_command = command.get_command().split(':')
            if len(name) < len(split_command):
                is_sublist = True
                for i in range(len(name)):
                    if name[i] != split_command[i]:
                        is_sublist = False
                        break
                if is_sublist:
                    return True
        return False

