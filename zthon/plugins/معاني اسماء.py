# 𓏺الهكر زين 
# حقزق الهقر زين

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from zthon import zedub

from ..core.managers import edit_or_reply


@zedub.zed_cmd(pattern="معني ?(.*)")
async def zilzal(event):
    card = event.pattern_match.group(1)
    chat = "@ai1_12bot"
    await reply_id(event)
    zed = await edit_or_reply(event, "**جـارِ معرفه  معني الاسم 💞🧸...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zedub(unblock("ai1_12bot"))
            await conv.send_message(card)
        await asyncio.sleep(2)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()

