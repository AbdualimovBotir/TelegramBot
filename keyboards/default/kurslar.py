from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kurslar = ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton("🖥 ISTALGAN TURDAGI DASTURLAR"),
        ],
        [
            KeyboardButton("🌄 Grafik dizayner"),
            KeyboardButton("🐍 Python")
        ],
        [
            KeyboardButton("🌐 WEB DASTURLASH(FRONT END,  BECK END)")
        ],
        [
            KeyboardButton("⚙️ PHP Laravel fremwork(Web app)"),
            KeyboardButton("🤖 Python telegram bot"),
        ],
[
            KeyboardButton("🛠 C# .Net fremwork(Loyihalar)")
        ],
        [
            KeyboardButton("💼 Office ishlari"),
            KeyboardButton("®️ Buyurtma berish")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish")
        ]
    ], resize_keyboard=True
)
