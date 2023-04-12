import asyncio
import math

import heroku3
import requests
import urllib3

from joker import zedub

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY


@zedub.zed_cmd(pattern="ميوزك(?:\s|$)([\s\S]*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            event,
            "اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            event,
            "اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    input_str = event.pattern_match.group(1)
    heroku_var = app.config()
    zedub = await edit_or_reply(event, "** جارِ تغير وضع الميوزك ✅ . . .**")
    if input_str == "تفعيل":
        variable = "VCMODE"
        zinfo = "True"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zedub.edit("**⌔∮ تم بنجاح تغيير وضع الميوزك\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await zedub.edit("**⌔∮ تم بنجاح تغيير وضع الميوزك\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "تعطيل":
        variable = "VCMODE"
        zinfo = "False"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zedub.edit("**⌔∮ تم بنجاح تغيير وضع الميوزك\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await zedub.edit("**⌔∮ تم بنجاح تغيير وضع الميوزك\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo