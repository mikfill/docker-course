from datetime import datetime as dt
from zoneinfo import ZoneInfo
from aiogram import Bot, Dispatcher, types
from bot.src.settings import BOT_TOKEN
from bot.src.database.create_table import execute_query


# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    time_now = dt.now(tz=ZoneInfo("UTC")).isoformat(" ")
    insert_q = (
        f"INSERT INTO messages (message, user_id, message_time) "
        f"VALUES ('START-> [{message.text}]', {message.from_user['id']}, '{time_now}')"
    )
    execute_query(insert_q)
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    time_now = dt.now(tz=ZoneInfo("UTC")).isoformat(" ")
    insert_q = (
        f"INSERT INTO messages (message, user_id, message_time) "
        f"VALUES ('ECHO -> [{message.text}]', {message.from_user['id']}, '{time_now}')"
    )
    execute_query(insert_q)
    await message.answer(message.text)
