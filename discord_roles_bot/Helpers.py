import discord

# Returns the actual emote as a string if it's available in the server, otherwise just plain 'Kappa' text
def get_kappa(guild):
    try:
        return str(discord.utils.get(guild.emojis, name='Kappa'))
    except Exception:
        return 'Kappa'

def find_string_match(str, lst):
    for item in lst:
        if str.lower() == str(item).lower():
            return str


def get_roles(bot, guild, availible):
    bot_role = guild.get_member(bot.user.id).top_role
    if availible:
        return [role for role in guild.roles if role <  bot_role and str(role) != '@everyone']
    else:
        return [role for role in guild.roles if role >= bot_role]
