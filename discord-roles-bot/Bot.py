from Message_handler import Message_handler
from Config import config
from Helpers import get_message_tag
import discord
import logging
logger = logging.getLogger('roles_bot.bot')

class Bot(discord.Client):

    def __init__(self):
        super().__init__()
        self.message_handler = Message_handler()

    def run_bot(self):
        self.run(config()['bot']['token'])

    async def on_ready(self):
        logger.info(f'Logged on as Discord user {self.user}')

    async def send_message(self, outgoing_message, incoming_message):
        channel = incoming_message.channel
        await channel.send(outgoing_message)
        logger.info(f'{get_message_tag(incoming_message)} Sent response: ' + outgoing_message)


    async def on_message(self, message):
        # don't respond to self
        if message.author == self.user:
            return

        message_tag = get_message_tag(message)
        logger.debug(f'{message_tag} {message.author}: ' + message.content)

        try:
            response = await self.message_handler.get_response(message, self)
            if not response:
                return

            # multiple messages
            if isinstance(response, list):
                for msg in response:
                    await self.send_message(msg, message)
                return

            if response:
                return await self.send_message(response, message)

            if message.content == 'ping':
                return await self.send_message('pong', message)

        except Exception as e:
            print(f'ERROR while processing message {message.content}:\n{e}')
