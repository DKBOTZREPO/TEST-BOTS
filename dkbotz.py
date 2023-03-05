from pyrogram import Client, filters


DKBOTZ = Client(
    "TEST-BOTZ",
    api_id= , api_hash='',
    bot_token=''
)

@DKBOTZ.on_message(filters.command('start'))
async def start_cmd(bot, message):
    await message.reply_text(f'Hello {message.from_user.first_name}\n\nHow Are You\n\nYour Account is Premium : {message.from_user.is_premium}')







DKBOTZ.run()
