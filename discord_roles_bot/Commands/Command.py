from Config import config

class Command:

    def __init__(self, name, triggers):
        self.name = name
        self.triggers = triggers
        try:
            self.channel = config()[self.name.lower()]['channel']
        except IndexError:
            self.channel = None


    def trigger(self, message):
        if not self.channel or message.channel == self.channel:
            return any([trigger.lower() in message.content.lower() for trigger in self.triggers])
