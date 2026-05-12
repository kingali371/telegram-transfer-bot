# 🤖 Telegram Member Transfer Bot

بوت لنقل أعضاء تيليجرام بين المجموعات مع دعم حسابات متعددة وتجنب الحظر.

## ✨ الميزات

- ✅ دعم عدة حسابات (Round-robin)
- ✅ معالجة تلقائية لأخطاء FloodWaitError
- ✅ حد يومي لكل حساب
- ✅ تصفية المستخدمين غير النشطين
- ✅ واجهة سطر أوامر ملونة

## ⚠️ ملاحظات هامة

| الخاصية | الحالة |
|---------|--------|
| نقل الأعضاء الظاهرين | ✅ ممكن |
| نقل الأعضاء المخفيين | ❌ غير ممكن |

## 📥 التثبيت

```bash
# استنساخ المشروع
git clone https://github.com/username/telegram-transfer-bot.git
cd telegram-transfer-bot

# تثبيت المكتبات
pip install -r requirements.txt

# نسخ ملف البيئة
cp .env.example .env

# تعديل ملف .env بالبيانات الخاصة بك
nano .env

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Telegram](https://img.shields.io/badge/telegram-bot-blue.svg)

