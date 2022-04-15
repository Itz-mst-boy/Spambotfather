from MukeshxSpam import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from MukeshxSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/aafe899afdbd00314a561.jpg"

Riz_Help = "__ᴄʟɪᴄᴋ  ᴏɴ  ʙᴇʟᴏᴡ  ʙᴜᴛᴛᴏɴs  ғᴏʀ ʜᴇʟᴘ__"


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
           [
            Button.inline("• Spam •", data="spam"),
            Button.inline("• Raid •", data="raid"),
           ],
           [
            Button.inline("• Extra •", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/mukhushi_official")
           ],
           ],
           )              

  
  
extra_msg = f"""
**ʜᴇʟᴘ  ᴇxᴛʀᴀ  ᴄᴍᴅs**

**Userbot**: Userbot Cmds
command:
i) {hl}ping 
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> : ᴏᴡɴᴇʀ ᴄᴍᴅ

**Echo**: ᴛᴏ  ᴀᴄᴛɪᴠᴇ  ᴇᴄʜᴏ  ᴏɴ ᴀɴʏ ᴜsᴇʀ
command:
i) {hl}addecho <reply to user>
ii) {hl}rmecho <reply to user>

**Leave**: ᴛᴏ ʟᴇᴀᴠᴇ  ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ
command:
i) {hl}leave <group/chat id>
ii) {hl}leave : ᴛʏᴘᴇ ɪɴ ᴛʜᴇ  ɢʀᴏᴜᴘ ʙᴏᴛ ᴡɪʟʟ  ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ

**Packspam**: sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ  sᴘᴀᴍ
i) {hl}packspam (replying to any sticker)

**© @itz_mst_boy**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**raid:** Activates raid on any individual user for given range.
command:
i) {hl}raid <count> <username
ii) {hl}raid <count> <reply to user>

**Delayraid**: ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴀɪᴅ  ᴏɴ  ᴀɴʏ  ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ  ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**replyraid:** ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ  ʀᴀɪᴅ  ᴏɴ  ᴛʜᴇ  ᴜsᴇʀ!!
command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>

**dreplyraid:** ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ  ʀᴀɪᴅ ᴏɴ  ᴛʜᴇ ᴜsᴇʀ!!
command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>


**© @itz_mst_boy**
"""

spam_msg = f"""
**Help Spam Cmds**

**spam**: sᴘᴀᴍs  ᴀ  ᴍᴇssᴀɢᴇ ғᴏʀ ɢɪᴠᴇɴ  ᴄᴏᴜɴᴛᴇʀ(<= 100).
command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**bigspam**: sᴘᴀᴍs ᴀ  ᴍᴇssᴀɢᴇ ғᴏʀ  ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.
command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**delayspam**: ᴅᴇʟᴀʏ  sᴘᴀᴍ ᴀ ᴛᴇxᴛ ғᴏʀ  ɢɪᴠᴇɴ  ᴄᴏᴜɴᴛᴇʀ ᴀғᴛᴇʀ ɢɪᴠᴇɴ ᴛɪᴍᴇ.
command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**pornspam**: ᴘᴏʀɴᴏɢʀᴀᴘʜʏ sᴘᴀᴍ.
command:
i) {hl}pornspam <count>

**hang**: sᴘᴀᴍs ʜᴀɴɢɪɴɢ ᴍᴇssᴀɢᴇ ғᴏʀ  ɢɪᴠᴇɴ  ᴄᴏᴜɴᴛᴇʀ.
command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @itz_mst_boy**
"""                     
           
           
@Riz.on(events.CallbackQuery(pattern=r"help_back"))
@Riz2.on(events.CallbackQuery(pattern=r"help_back"))
@Riz3.on(events.CallbackQuery(pattern=r"help_back"))
@Riz4.on(events.CallbackQuery(pattern=r"help_back"))
@Riz5.on(events.CallbackQuery(pattern=r"help_back"))
@Riz6.on(events.CallbackQuery(pattern=r"help_back"))
@Riz7.on(events.CallbackQuery(pattern=r"help_back"))
@Riz8.on(events.CallbackQuery(pattern=r"help_back"))
@Riz9.on(events.CallbackQuery(pattern=r"help_back"))
@Riz10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Riz_Help,
            buttons=[
                [
            Button.inline("Spam", data="spam"),
            Button.inline("Raid", data="raid"),
           ],
           [
            Button.inline("Extra cmds", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/mukhushi_official")
           ],
           ],
        )           
   else:
        Alert = (
                "ɴᴏᴏʙ !! ᴍᴀᴋᴇ  ʏᴏᴜʀ   ᴏᴡɴ ᴍᴜᴋᴇsʜ X sᴘᴀᴍ  ʙᴏᴛs  ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʀᴇᴘᴏ @itz_mst_boy !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Riz.on(events.CallbackQuery(pattern=r"spam"))
@Riz2.on(events.CallbackQuery(pattern=r"spam"))
@Riz3.on(events.CallbackQuery(pattern=r"spam"))
@Riz4.on(events.CallbackQuery(pattern=r"spam"))
@Riz5.on(events.CallbackQuery(pattern=r"spam"))
@Riz6.on(events.CallbackQuery(pattern=r"spam"))
@Riz7.on(events.CallbackQuery(pattern=r"spam"))
@Riz8.on(events.CallbackQuery(pattern=r"spam"))
@Riz9.on(events.CallbackQuery(pattern=r"spam"))
@Riz10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "ɴᴏᴏʙ !! ᴍᴀᴋᴇ ʏᴏᴜʀ  ᴏᴡɴ  ᴍᴜᴋᴇsʜ X sᴘᴀᴍ  ʙᴏᴛs  !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Riz.on(events.CallbackQuery(pattern=r"raid"))
@Riz2.on(events.CallbackQuery(pattern=r"raid"))
@Riz3.on(events.CallbackQuery(pattern=r"raid"))
@Riz4.on(events.CallbackQuery(pattern=r"raid"))
@Riz5.on(events.CallbackQuery(pattern=r"raid"))
@Riz6.on(events.CallbackQuery(pattern=r"raid"))
@Riz7.on(events.CallbackQuery(pattern=r"raid"))
@Riz8.on(events.CallbackQuery(pattern=r"raid"))
@Riz9.on(events.CallbackQuery(pattern=r"raid"))
@Riz10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "ɴᴏᴏʙ !! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ᴍᴜᴋᴇsʜ X sᴘᴀᴍ ʙᴏᴛs !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Riz.on(events.CallbackQuery(pattern=r"extra"))
@Riz2.on(events.CallbackQuery(pattern=r"extra"))
@Riz3.on(events.CallbackQuery(pattern=r"extra"))
@Riz4.on(events.CallbackQuery(pattern=r"extra"))
@Riz5.on(events.CallbackQuery(pattern=r"extra"))
@Riz6.on(events.CallbackQuery(pattern=r"extra"))
@Riz7.on(events.CallbackQuery(pattern=r"extra"))
@Riz8.on(events.CallbackQuery(pattern=r"extra"))
@Riz9.on(events.CallbackQuery(pattern=r"extra"))
@Riz10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "ɴᴏᴏʙ  !! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ᴍᴜᴋᴇsʜ X sᴘᴀᴍ ʙᴏᴛs !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)

