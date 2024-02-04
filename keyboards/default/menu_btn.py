from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton,InlineKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("ℹ Biz haqimizda")
        ],
        [
            KeyboardButton("🎓 Xizmatlar"),
            KeyboardButton("📞 Aloqa")
        ],
        [
            KeyboardButton("🔗 Havolalar"),
            KeyboardButton("®️ Buyurtma berish")
        ],
    ], resize_keyboard=True
)

