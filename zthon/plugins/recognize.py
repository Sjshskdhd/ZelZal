# credits: @Mr_Hops
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from zthon import zedub
from zthon.core.managers import edit_or_reply

plugin_category = "utils"


@zedub.zed_cmd(
    pattern="حلل ?([\s\S]*)",
    command=("حلل", plugin_category),
    info={
        "header": "To recognize a image",
        "description": "Get information about an image using AWS Rekognition. Find out information including detected labels, faces. text and moderation tags",
        "usage": "{tr}recognize",
    },
)
async def _(event):
    "To recognize a image."
    if not event.reply_to_msg_id:
        return await edit_or_reply(event, "برجاء الرد علي صوره.")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await edit_or_reply(event, "برجاء الرد علي صوره.")
    chat = "@Rekognition_Bot"
    if reply_message.sender.bot:
        return await event.edit("اعمل ريب علي اي رساله.")
    cat = await edit_or_reply(event, "بحلل الصوره اهو ويت")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await cat.edit("unblock @Rekognition_Bot and try again")
            return
        if response.text.startswith("See next message."):
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            response = await response
            msg = response.message.message
            await cat.edit(msg)
        else:
            await cat.edit("مش لاقي تحليل")
        await event.client.send_read_acknowledge(conv.chat_id)
