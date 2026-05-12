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

import asyncio
import threading
from flask import Flask, jsonify
from telegram import Bot
from telegram.ext import Application
import os

# إعداد Flask لصفحة الصحة
app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({"status": "alive", "service": "telegram-bot"}), 200

@app.route('/')
def home():
    return jsonify({"message": "Telegram Transfer Bot is running!"}), 200

def run_flask():
    # تشغيل Flask على المنفذ 10000 (المنفذ الافتراضي في Render)
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# دالة تشغيل البوت الرئيسية
async def run_bot():
    # إعدادات البوت الخاصة بك
    token = os.environ.get('BOT_TOKEN')
    
    # إنشاء تطبيق البوت
    application = Application.builder().token(token).build()
    
    # أضف معالجات الأوامر الخاصة بك هنا
    # مثال:
    # from telegram.ext import CommandHandler
    # async def start(update, context):
    #     await update.message.reply_text('مرحباً!')
    # application.add_handler(CommandHandler('start', start))
    
    # بدء البوت
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    # الانتظار إلى أجل غير مسمى
    await asyncio.Event().wait()

if __name__ == '__main__':
    # تشغيل Flask في خيط منفصل
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    # تشغيل البوت
    asyncio.run(run_bot())
