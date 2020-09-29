from Config import config
from Helpers import extract_command, get_bot_role
import logging
logger = logging.getLogger('roles_bot.command')

class Command:

    def __init__(self, name, triggers):
        self.name = name
        self.triggers = triggers

    def get_channel(self, settings):
        try:
            return settings['commands'][self.name]['channel'].replace(' ', '-')
        except KeyError:
            return None

    def trigger(self, settings, message, bot):
        trigger_command = self.check_triggered(settings, message, bot)
        if trigger_command:
            logger.info(f"Trigger message in #{message.channel} from {message.author}: {message.content}")
            return True


    def check_triggered(self, settings, message, bot):
        if self.contains_command_trigger(message):
            if not self.check_permission(message, settings, bot):
                logger.info(f"Author '{message.author}' does not have permission to use command '{self.name}'")
                return False
            channel = self.get_channel(settings)
            if channel:
                if str(message.channel) == channel:
                    logger.info(f"Triggered command '{self.name}' in channel #{channel}")
                    return True
                else:
                    logger.info(f"Command '{self.name}' only triggers in channel #{channel}")
                    return False
            else:
                logger.info(f"Triggered command '{self.name}'")
                return True

    def check_permission(self, message, settings, bot):
        try:
            permission = settings['commands'][self.name]['permission']
        except KeyError:
            return True
        highest_role = message.author.roles[-1]
        bot_role = get_bot_role(bot, message.guild)
        if permission == 'above':
            return highest_role > bot_role
        if permission == 'below':
            return highest_role < bot_role
        if permission == 'anyone':
            return True



    def contains_command_trigger(self, message):
        potential_command = extract_command(message.content.lower())
        return any([potential_command == trigger.lower() for trigger in self.triggers])
