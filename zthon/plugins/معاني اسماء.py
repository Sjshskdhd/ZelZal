# Zed-Thon - ZelZal
# Copyright (C) 2022 Zedthon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/main/LICENSE/>.
# الملــف محمــي بحقــوق النشـــر والملـكيـه
# تخمــط بــدون ذكــر المصــدر ابلــع حســابـك بانـــد
""" 
CC Checker & Generator for ZThon™ t.me/ZedThon
Write file by Zelzal t.me/zzzzl1l
hhh o ya beby

"""

import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from zthon import zedub

from ..core.managers import edit_or_reply

plugin_category = "البوت"


# code by t.me/zzzzl1l
@zedub.zed_cmd(pattern="معني(?:\s|$)([\s\S]*)")
async def song2(event):
    song = event.pattern_match.group(1)
    chat = "@ai1_12bot" # code by t.me/zzzzl1l
    reply_id_ = await reply_id(event)
    zed = await edit_or_reply(event, "**⎉╎جـارِ الحصول علي معني الاسم.**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "معني {}".format(song)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await zedub(unblock("ai1_12bot"))
            gool = "معني {}".format(song)
            await conv.send_message(gool)
        await asyncio.sleep(3)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await zed.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await zed.edit("**- خطـأ :**\n**أعد محاولة اكتب .معني +الاسم**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


