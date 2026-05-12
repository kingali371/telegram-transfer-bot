# بوت نقل أعضاء تيليجرام

أداة لنقل الأعضاء بين مجموعات تيليجرام مع دعم حسابات متعددة وتجنب الحظر.

## ✨ المميزات

- دعم عدة حسابات (round-robin) لزيادة السرعة
- تصفية المستخدمين النشطين فقط
- حد يومي لكل حساب (50-200 دعوة)
- معالجة تلقائية لأخطاء FloodWaitError
- واجهة أزرار مضمنة (إن وجدت)

## 🛠 المتطلبات

- Python 3.7+
- Telethon
- حساب تيليجرام مع api_id و api_hash من [my.telegram.org](https://my.telegram.org)

## 📥 التثبيت

```bash
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME
pip install -r requirements.txt
