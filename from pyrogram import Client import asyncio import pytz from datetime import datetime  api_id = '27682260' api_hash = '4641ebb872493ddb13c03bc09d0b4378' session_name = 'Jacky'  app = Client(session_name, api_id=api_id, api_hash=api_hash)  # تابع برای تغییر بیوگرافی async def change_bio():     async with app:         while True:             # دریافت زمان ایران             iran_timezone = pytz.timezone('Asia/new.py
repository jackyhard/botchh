from pyrogram import Client
import asyncio
import pytz
from datetime import datetime

api_id = '27682260'
api_hash = '4641ebb872493ddb13c03bc09d0b4378'
session_name = 'Jacky'

app = Client(session_name, api_id=api_id, api_hash=api_hash)

# تابع برای تغییر بیوگرافی
async def change_bio():
    async with app:
        while True:
            # دریافت زمان ایران
            iran_timezone = pytz.timezone('Asia/Tehran')

# گرفتن زمان فعلی ایران
            iran_time = datetime.now(iran_timezone)
            current_time = iran_time.strftime('%H:%M')
            # تغییر بیوگرافی
            bio = f"|{current_time}|"
            await app.update_profile(last_name = bio,bio=bio)
            
            # منتظر ماندن برای یک دقیقه
            await asyncio.sleep(60)

# اجرای تابع
asyncio.get_event_loop().run_until_complete(change_bio())
