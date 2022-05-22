import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, ALIVE_PIC, OWNER_ID
from MukeshxSpam.plugins.help import *


RIZ_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/aafe899afdbd00314a561.jpg"

Riz_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/worldwide_friend_zone")
        ],
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]
               
RizX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/mukhushi_official"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/worldwide_friend_zone")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/Itz-mst-boy/Spambotfather")
        ]
        ]
        
        
#USERS 


@Riz.on(events.NewMessage(pattern="/start"))
@Riz2.on(events.NewMessage(pattern="/start"))
@Riz3.on(events.NewMessage(pattern="/start"))
@Riz4.on(events.NewMessage(pattern="/start"))
@Riz5.on(events.NewMessage(pattern="/start"))
@Riz6.on(events.NewMessage(pattern="/start"))
@Riz7.on(events.NewMessage(pattern="/start"))
@Riz7.on(events.NewMessage(pattern="/start"))
@Riz8.on(events.NewMessage(pattern="/start"))
@Riz9.on(events.NewMessage(pattern="/start"))
@Riz10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await event.client.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**ʜɪ ᴍᴀsᴛᴇʀ, ɪᴛs ᴍᴇ {bot_id}, ʏᴏᴜʀ sᴘᴀᴍ ʙᴏᴛ!! \n\n ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ғᴏʀ ʜᴇʟᴘ**"
       usermsg = f"**ʜᴇʟʟᴏ, {firstname} ! ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ, ᴡᴇʟʟ ɪ ᴀᴍ {bot_id}, ᴀɴ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍ ʙᴏᴛ.** \n\n**ɪғ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ sᴘᴀᴍ ʙᴏᴛs ʏᴏᴜ ᴄᴀɴ ᴅᴇᴘʟᴏʏ ғʀᴏᴍ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [ᴍɴᴏ](https://t.me/mastermind_network_official)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheRiZoeL,
                  RIZ_IMG,
                  caption=ownermsg, 
                  buttons=Riz_Button)
       else:
            await event.client.send_file(TheRiZoeL,
                  RIZ_IMG,
                  caption=usermsg, 
                  buttons=RizX_Button)
                

