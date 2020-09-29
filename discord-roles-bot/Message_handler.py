from Commands.Roles import Roles
from Commands.Help import Help
from Commands.Info import Info
from Config import config

class Message_handler:

    def __init__(self):
        self.commands = [
            Roles(),
            Help(),
            Info()
        ]


    async def get_response(self, message, bot):
        """Looks for commands in message and returns a response if a command is triggered"""
        settings = config(message.guild.id)

        for command in self.commands:
            if command.trigger(settings, message, bot):
                response = await command.get_response(settings, message, bot)
                if response and response != []:
                    return response




