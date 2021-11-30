import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.bot: # return message from bot
            return

        print(f'Message from {message.author}: {message.content}')

        if str(message.content).startswith("!pass"):
            args = str(message.content).split(" ")

            if len(args) == 1:
                await message.channel.send("!pass [length]")
                return

            length = args[1]
            if not str.isdecimal(length):
                await message.channel.send("整数を入力してください。")
                return

            if int(length) <= 0:
                await message.channel.send("1以上の数値を入力してください。")
                return

            if int(length) > 2000:
                await message.channel.send("2000以下の数値を入力してください。")
                return

            password = await generate_password(int(length))
            await message.channel.send(str(password))


async def generate_password(length):
    password = '' # generate empty string
    chars = list([chr(i) for i in range(97, 97+26)]) # abcde...
    chars.extend([chr(i) for i in range(65, 65+26)]) # ABCDE...
    chars.extend([chr(i) for i in range(48, 48+10)]) # 12345...

    for _ in range(length):
        password += random.choice(chars) # add char

    return password

client = MyClient()
client.run('your token here')
