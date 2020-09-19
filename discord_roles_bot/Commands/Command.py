from Config import config
from Helpers import extract_command, get_bot_role

class Command:

    def __init__(self, name, triggers):
        self.name = name
        self.triggers = triggers
        try:
            self.channel = config()['commands'][self.name]['channel']
        except KeyError:
            self.channel = None

    def trigger(self, message, bot):

        if self.contains_command_trigger(message):
            if not self.check_permission(message.author, message.guild, bot):
                print(f"Author '{message.author}' does not have permission to use command '{self.name}'")
                return False
            if self.channel:
                if str(message.channel) == self.channel:
                    print(f"Triggered command '{self.name}' in channel #{self.channel}")
                    return True
                else:
                    print(f"Command '{self.name}' only triggers in channel #{self.channel}")
                    return False
            else:
                print(f"Triggered command '{self.name}'")
                return True

    def check_permission(self, author, guild, bot):
        try:
            permission = config()['commands'][self.name]['permission']
        except KeyError:
            return True
        highest_role = author.roles[-1]
        bot_role = get_bot_role(bot, guild)
        if permission == 'above':
            return highest_role > bot_role
        if permission == 'below':
            return highest_role < bot_role
        if permission == 'anyone':
            return True



    def contains_command_trigger(self, message):
        potential_command = extract_command(message.content.lower())
        return any([potential_command == trigger.lower() for trigger in self.triggers])
