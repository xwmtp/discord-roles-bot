from Bot import Bot
from Config import validate_config

if validate_config():
    bot = Bot()
    bot.run_bot()








