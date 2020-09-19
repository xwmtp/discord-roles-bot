from Message_handler import Message_handler
from Config import config
import discord

class Bot(discord.Client):

    def __init__(self):
        super().__init__()
        self.message_handler = Message_handler()

    def run_bot(self):
        self.run(config()['bot']['token'])

    async def on_ready(self):
        print(f'Logged on as Discord user {self.user}')

    async def send_message(self, outgoing_message, channel):
        await channel.send(outgoing_message)
        print(f'Sent message to #{channel.name}: ' + outgoing_message)


    async def on_message(self, message):
        # don't respond to self
        if message.author == self.user:
            return

        print('Received message: ' + message.content)

        #try:

        response = await self.message_handler.get_response(message, self)
        if response:

            # multiple messages
            if isinstance(response, list):
                for msg in response:
                    await self.send_message(msg, message.channel)
                return

            if response:
                return await self.send_message(response, message.channel)

            if message.content == 'ping':
                return await self.send_message('pong', message.channel)

        #except Exception:
        #    print(f'Exception while processing message {message.content}')
