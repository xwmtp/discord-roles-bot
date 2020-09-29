from Helpers import extract_command, get_bot_role, get_message_tag
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
            self.check_settings(settings, message)
            logger.info(f"{get_message_tag(message)} Triggered by {message.author}: {message.content}")
            return True


    def check_triggered(self, settings, message, bot):
        message_tag = get_message_tag(message)
        if self.contains_command_trigger(message):
            if not self.check_permission(message, settings, bot):
                logger.info(f"{message_tag} Author '{message.author}' does not have permission to use command '{self.name}'")
                return False
            channel = self.get_channel(settings)
            if channel:
                if str(message.channel) == channel:
                    logger.info(f"{message_tag} Triggered command '{self.name}' in channel #{channel}")
                    return True
                else:
                    logger.info(f"{message_tag} Command '{self.name}' only triggers in channel #{channel}")
                    return False
            else:
                logger.info(f"{message_tag} Triggered command '{self.name}'")
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

    # Give out a warning if default settings are used for the message that triggered the command.
    def check_settings(self, settings, message):
        try:
            if settings['default']:
                logger.info(f"{get_message_tag(message)} WARNING: no settings found for server with id {message.guild.id}, using default settings for this message.")
        except KeyError:
            pass

    def contains_command_trigger(self, message):
        potential_command = extract_command(message.content.lower())
        return any([potential_command == trigger.lower() for trigger in self.triggers])
