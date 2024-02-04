from loader import dp
from aiogram import types

@dp.message_handler(text="📞 Aloqa")
async def aloqa(message: types.Message):
    await message.answer("🗣 M-Service bilan bog\'lanish\n\nSizga o'z hizmatlarimizni taklif qilganimizdan minnatdormiz!. M-Servise 24 soat sizning hizmatingizda. Siz bilan ishchi gruhlarimiz aloqaga chiqishgunicha biroz vaqt olishi mumkin!."
                         "\n\nBiz bilan bog\'lanish: \n\n📞 Tel.: +998(91) 025 65 25, +998(90) 181 77 80, +998(99) 779 62 02 \n\n📧 E-mail: sm7382148@gmail.com \n\nYou tube: https://youtube.com/@M-Service-bs4eu \n\nIjtimoiy tarmoqlar:\n\nTelegram: https://t.me/mservice_robot \n\nTelegram guruh: https://t.me/m_service999 \n\nTelegram kanal: https://t.me/m_service998")
