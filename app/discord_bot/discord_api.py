from dotenv import load_dotenv
import discord 
import os
from app.chatgpt_ai.openai import chatgpt_response

#totalMessages=[]
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as ", self.user)
        
    
    async def on_message(self, message):
        
        print(message.content)
        global totalMessages
        if message.author == self.user:
            return
        command, user_message=None, None
        if message.content.startswith("!clear"):
            #totalMessages.clear()
            await message.channel.send("Memory wiped")
        for text in '!bot':
            if message.content.startswith(text):
                
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                #user_message = str(message.author) + ": "+user_message+"\n"
                #totalMessages.append(user_message)
                print(command, user_message)
                #print(totalMessages)
        if command == '!bot':
            
            #memory_message = ''
            # for x in totalMessages:
            #     memory_message += x
            # if len(totalMessages) > 20:
            #     totalMessages.clear()
            #     totalMessages.append(user_message)
            bot_response = chatgpt_response(prompt=user_message)
            # print("gave " + memory_message)

            # totalMessages.append((bot_response+"\n"))
            # if len(totalMessages) > 10:
            #     totalMessages.clear
            #     totalMessages.append(user_message)
            await message.channel.send(f"{bot_response}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)