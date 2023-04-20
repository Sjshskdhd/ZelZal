""" 
# 𓏺الهكر زين 
# حقزق الهقر زين

"""

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from zthon import zedub

from ..core.managers import edit_or_reply


@zedub.zed_cmd(pattern="حساب العمر(?:\s|$)([\s\S]*)")
async def song2(event):
    card = event.pattern_match.group(1)
    chat = "@xbank1_bot"
    await reply_id(event)
    zed = await edit_or_reply(event, "**- جـارِ معرفت عمرك بالتفصيل...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zedub(unblock("xbank1_bot"))
            await conv.send_message(card)
        await asyncio.sleep(3)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


@zedub.zed_cmd(pattern="اسال(?:\s|$)([\s\S]*)")
async def song2(event):
    card = event.pattern_match.group(1)
    chat = "@ChatAi5Bot"
    await reply_id(event)
    zed = await edit_or_reply(event, "**- جـارِ الحصول علي اجابه ...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zedub(unblock("@ChatAi5Bot"))
            await conv.send_message(card)
        await asyncio.sleep(15)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()
