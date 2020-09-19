from Bot import Bot
from Config import check_configurations

if __name__ == '__main__':

    print("\n ____  _                       _   ____       _             ____        _    \
           \n|  _ \(_)___  ___ ___  _ __ __| | |  _ \ ___ | | ___  ___  | __ )  ___ | |_  \
           \n| | | | / __|/ __/ _ \| '__/ _` | | |_) / _ \| |/ _ \/ __| |  _ \ / _ \| __| \
           \n| |_| | \__ \ (_| (_) | | | (_| | |  _ < (_) | |  __/\__ \ | |_) | (_) | |_  \
           \n|____/|_|___/\___\___/|_|  \__,_| |_| \_\___/|_|\___||___/ |____/ \___/ \__| \
           \nby xwillmarktheplace. \
           \nPlease read the manual at https://github.com/xwmtp/xwillmarktheBot/blob/master/README.md for information/help. \
           \n-----------------------------------------\n")

    if check_configurations():
        bot = Bot()
        bot.run_bot()












