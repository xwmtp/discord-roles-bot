import discord

# Returns the actual emote as a string if it's available in the server, otherwise just plain 'Kappa' text
def get_kappa(guild):
    try:
        return str(discord.utils.get(guild.emojis, name='Kappa'))
    except Exception:
        return 'Kappa'

def find_string_match(item, lst):
    for elem in lst:
        if str(item).lower() == str(elem).lower():
            return elem


def get_roles(bot, guild, availible):
    bot_role = get_bot_role(bot, guild)
    if availible:
        return [role for role in guild.roles if role <  bot_role and str(role) != '@everyone']
    else:
        return [role for role in guild.roles if role >= bot_role]

def get_bot_role(bot, guild):
    return guild.get_member(bot.user.id).top_role

def extract_command(message):
    return message.split(' ')[0]