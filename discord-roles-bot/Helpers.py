import discord
from Config import config

# Returns the actual emote as a string if it's available in the server, otherwise just plain 'Kappa' text
def get_kappa(guild):
    kappa = str(discord.utils.get(guild.emojis, name='Kappa'))
    if kappa and kappa != 'None':
        return kappa
    else:
        return 'Kappa'

def find_string_match(item, lst):
    for elem in lst:
        if str(item).lower() == str(elem).lower():
            return elem

def get_message_tag(incoming_message):
    server_id = incoming_message.guild.id
    settings = config()
    server_name = str(server_id)
    for name, server_settings in settings['servers'].items():
        if server_settings['id'] == server_id:
            server_name = name
    return f"[{server_name}-#{incoming_message.channel}]"

def get_roles(bot, guild, availible):
    bot_role = get_bot_role(bot, guild)
    if availible:
        return reversed([role for role in guild.roles if role <  bot_role and str(role) != '@everyone'])
    else:
        return reversed([role for role in guild.roles if role >= bot_role])

def get_bot_role(bot, guild):
    return guild.get_member(bot.user.id).top_role

def extract_command(message):
    return message.split(' ')[0]