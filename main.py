from telegram import Bot
import asyncio
from datetime import datetime

TOKEN = "8539830765:AAEoB1zsN9hXAOJWXeuJgdV-m_78UeE4JYc"
CHANNEL_ID = "@ggmangg1"

bot = Bot(token=TOKEN)

target_date = datetime(2026, 5, 30, 21, 0, 0)

async def main():
    message = await bot.send_message(
        chat_id=CHANNEL_ID,
        text="⏳ بدء العد التنازلي..."
    )

    while True:
        now = datetime.now()
        remaining = target_date - now

        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        text = (
            f"🏆 نهائي دوري أبطال أوروبا\n\n"
            f"⏳ {days} يوم : {hours} ساعة : {minutes} دقيقة"
        )

        try:
            await bot.edit_message_text(
                chat_id=CHANNEL_ID,
                message_id=message.message_id,
                text=text
            )
        except:
            pass

        await asyncio.sleep(60)

asyncio.run(main())
