import asyncpg
import os
from datetime import datetime

DATABASE_URL = os.getenv('DATABASE_URL')

class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        """إنشاء مجموعة اتصالات بقاعدة البيانات"""
        self.pool = await asyncpg.create_pool(DATABASE_URL)
        await self.create_tables()
        print("✅ تم الاتصال بقاعدة البيانات")

    async def create_tables(self):
        """إنشاء الجداول المطلوبة"""
        async with self.pool.acquire() as conn:
            # جدول المستخدمين
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id BIGINT PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    transferred_at TIMESTAMP DEFAULT NOW(),
                    source_group TEXT,
                    target_group TEXT
                )
            ''')
            
            # جدول سجل العمليات
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS transfer_logs (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT,
                    action TEXT,
                    status TEXT,
                    created_at TIMESTAMP DEFAULT NOW()
                )
            ''')

    async def add_user(self, user_id: int, username: str, first_name: str):
        """إضافة مستخدم إلى قاعدة البيانات"""
        async with self.pool.acquire() as conn:
            await conn.execute('''
                INSERT INTO users (user_id, username, first_name)
                VALUES ($1, $2, $3)
                ON CONFLICT (user_id) DO NOTHING
            ''', user_id, username, first_name)

    async def log_transfer(self, user_id: int, action: str, status: str):
        """تسجيل عملية نقل"""
        async with self.pool.acquire() as conn:
            await conn.execute('''
                INSERT INTO transfer_logs (user_id, action, status)
                VALUES ($1, $2, $3)
            ''', user_id, action, status)

    async def get_stats(self):
        """إحصائيات عن عمليات النقل"""
        async with self.pool.acquire() as conn:
            total = await conn.fetchval('SELECT COUNT(*) FROM users')
            today = await conn.fetchval('''
                SELECT COUNT(*) FROM users 
                WHERE DATE(transferred_at) = CURRENT_DATE
            ''')
            return {'total': total, 'today': today}

# إنشاء كائن واحد للاستخدام في جميع أنحاء البوت
db = Database()
