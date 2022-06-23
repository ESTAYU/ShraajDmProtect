#REMEMBER THAT THIS SCRIPT IS SAFE BCOX THIS IS NOT WORKING WITH STRING SESSION....
#I MEAN TO SAY THAT IF YOUR ACCOUNT OR ANY PROBLEMS HAPPEN WITH YOU IS YOUR PROBLEMS, I DON'T TAKE ANY RESPONSE FOR THIS

#THIS PLUG-IN IS SEPREATED FOR USING ANYWHERE WITH ANY BOT SO U CAN TURN OFF BY TURNING OFF VPS SERVER...
#MADE BY - ZEUS @ZEUSESTAYU_1 & Join @LIFE_CODES For Supporting Me For This Awesome Idea

#importing modules
from pyrogram import Client, filters
import asyncio


in_app_id = input("Please Input Your APP_ID : ")
in_app_hash = input("Please Input Your APP_HASH : ")

prot = Client(session_name="ShraajDmProtect", api_id=int(in_app_id), api_hash=str(in_app_hash))


@prot.on_message(filters.text & filters.private)
async def echo(client, message):
	await message.reply_text("Hey Stop 🛑\nDon't Message To Me Otherwise You Will Be Blocked From Bot ❌\n\nGo To @ESBOT_HELP & Ask For Any Help You Want\n\n\nYour Message Is Forwarded To @ESBOT_HELP !! Go & Find Your Answer There\n\nClick 👉 @ESBOT_HELP", quote=True)
	await message.forward(chat_id=-1001265426244)

prot.run() 

#THIS IS A USER SCRIPT FOR INFORMING USERS OF BOTS WHO DISTURB ASSISTANT BOT
#PLEASE DO NOT SHARE THIS SCRIPT BCOX THIS IS PRIVATE & CONTAINING API_ID & API_HASH
