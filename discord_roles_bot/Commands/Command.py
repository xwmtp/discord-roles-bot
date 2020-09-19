from Config import config
from Helpers import extract_command

class Command:

    def __init__(self, name, triggers):
        self.name = name
        self.triggers = triggers
        try:
            self.channel = config()['commands'][self.name.lower()]['channel']
        except KeyError:
            self.channel = None

    def trigger(self, message):
        potential_command = extract_command(message.content.lower())
        if any([potential_command == trigger.lower() for trigger in self.triggers]):
            if self.channel:
                if str(message.channel) == self.channel:
                    print(f"Triggered command '{self.name}' in channel #{self.channel}")
                    return True
                else:
                    print(f"Command '{self.name}' only triggers in channel #{self.channel}")
                    return False
            else:
                return True
