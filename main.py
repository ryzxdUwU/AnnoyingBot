import discord
import pyautogui
import os

intents = discord.Intents.default()

intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# The commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!click'):
        pyautogui.click()
        await message.channel.send('Clicked')
    if message.content.startswith('!rickroll'):
        os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        await message.channel.send('Done!')
    if message.content.startswith('!cmd'):
        os.system("start")
        await message.channel.send('Opened cmd!')
    if message.content.startswith('!help'):
        await message.channel.send('!help - shows this message\n!click - clicks\n!rickroll - Opens rickroll\n!cmd - Opens command prompt!\n!win - clicks Windows button\n!taskmgr - Opens task manager\n!hello - Writes Hello world! and clicks enter\n!alttab - Alt tabs\n!virus - Opens "your computer has a virus" meme msg box')
    if message.content.startswith('!win'):
        pyautogui.press('win')
        await message.channel.send('Clicked that annoying windows button!')
    if message.content.startswith('!taskmgr'):
        pyautogui.hotkey('ctrl', 'shift', 'esc')
        await message.channel.send('Opened task manager!')
    if message.content.startswith('!hello'):
        pyautogui.write('Hello world!')
        pyautogui.press('enter')
        await message.channel.send('Wrote hello world!')
    if message.content.startswith('!alttab'):
        pyautogui.hotkey('alt', 'tab')
        await message.channel.send('Alt tabbed!')
    if message.content.startswith('!virus'):
        pyautogui.alert(text='Your computer has a virus!', title='Indian scammer', button='DESTROY THE SYSTEM')
        await message.channel.send('Opened it!')

client.run('yourTokenHere')
# Made with love by ryz