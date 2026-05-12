import asyncio
import os
from telethon import TelegramClient, events
from database import db

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# إنشاء العميل
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('مرحباً! أنا بوت نقل الأعضاء')

@bot.on(events.NewMessage(pattern='/stats'))
async def stats(event):
    stats = await db.get_stats()
    await event.reply(f"""
📊 **إحصائيات البوت**
- إجمالي المنقولين: {stats['total']}
- اليوم: {stats['today']}
    """)

async def main():
    # الاتصال بقاعدة البيانات
    await db.connect()
    
    # بدء البوت
    await bot.start()
    print("✅ البوت يعمل...")
    await bot.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
