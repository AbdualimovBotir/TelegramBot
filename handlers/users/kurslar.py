from aiogram import types
from keyboards.default.menu_btn import menu
from loader import dp
from keyboards.default.kurslar import kurslar
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
channel_link_button = InlineKeyboardButton(
    "🔗 Telegram kanalimiz",
    url="https://t.me/m_service998"
)

# Create an inline keyboard markup and add the button to it
channel_inline_keyboard = InlineKeyboardMarkup().add(channel_link_button)

youtube_link_button = InlineKeyboardButton(
    "🔗 YouTube kanalimiz",
    url="https://youtube.com/@M-Service-bs4eu"
)

# Create an inline keyboard markup and add the button to it
youtube_inline_keyboard = InlineKeyboardMarkup().add(youtube_link_button)
@dp.message_handler(text="🎓 Xizmatlar")
async def habar(message: types.message):
    await message.answer("<b>Aynan qaysi yo\'nalishdagi xizmatlarimiz haqida ma\'lumot kerak?</b>", reply_markup=kurslar)

@dp.message_handler(text="🖥 ISTALGAN TURDAGI DASTURLAR")
async def komp(message: types.message):
    await message.answer("<b>🎓 Xizmat: Kompyuter ishlari!\n\n📚 Texnologiyalar : Kompyuter ishlari , Word, Excel, Powerpoint, PDF hujjatlar, Ta'lim saytlari bilan ishlash, Rangli va rangsiz Printerlar bilan ishlash. Undan tashqari 10 lab dasturlash tillarida muqobil kod yozish. Web app, Android app, Desktop applarni mukammal darajada yaratish hamda dasturlar loyihlarni ishlab chiqish. Bizda istalgan turdagi hizmatlar mavjud. Xususan texnik xizmat ko\'rsatishlargacha.</b>\n\n👨🏻‍💻 Jarayon: Admin tomonidan belgilanadi. Hoziroq bizga buyurtma bering!. Buyurtma berish uchun menyudagi \"buyurtma berish\" bo'limini tanlang.")

@dp.message_handler(text="🌐 WEB DASTURLASH(FRONT END,  BECK END)")
async def web(message: types.message):
    # await message.answer("<b>🎓 Xizmat:  Web dasturlash!\n\n Bu xizmatlarimiz Frontend va Backend qismlarga bo'linadi.\n\n📚 Frontend : Bunda siz web saytlarning dizayn qismilari muammo yechimlari va real loyihalarni olasiz!</b>\n\n📚 Texnologiyalar: \n\n👨🏻‍💻 FrondEnd:HTML5, CSS3, Bootstrap4, SASS, Javascript, Vue.js, etc.. \n\n👨🏻‍💻 Backend: Java Core, Java OOP, Java Collections, Spring boot, Spring Security OAuth, WebSocket, Mikroservice, JHipster backend, Sql darslari, Fullstack Spring+Vueda, etc..\n\n<b>👨🏻‍💻 Jarayon: Umumiy xizmatlarda siz eng sodda web sayt maketlaridan tortib eng murakkablarigacha olasiz. Bundan tashqari bir qancha real online magazinlar dizayni ham mavjud. Hoziroq bizga buyurtma bering!.")
    await message.answer(
        "<b>🎓 Xizmat:  Web dasturlash!\n\n Bu xizmatlarimiz Frontend va Backend qismlarga bo'linadi.\n\n📚 Frontend : Bunda siz web saytlarning dizayn qismilari muammo yechimlari va real loyihalarni olasiz!\n\n📚 Texnologiyalar: \n\n👨🏻‍💻 FrondEnd:HTML5, CSS3, Bootstrap4, SASS, Javascript, Vue.js, etc.. \n\n👨🏻‍💻 Backend: Java Core, Java OOP, Java Collections, Spring boot, Spring Security OAuth, WebSocket, Mikroservice, JHipster backend, Sql darslari, Fullstack Spring+Vueda, etc..</b>\n\n<b>👨🏻‍💻 Jarayon: Umumiy xizmatlarda siz eng sodda web sayt maketlaridan tortib eng murakkablarigacha olasiz. Bundan tashqari bir qancha real online magazinlar dizayni ham mavjud. Hoziroq bizga buyurtma bering! Buyurtma berish uchun menyudagi \"buyurtma berish\" bo'limini tanlang.</b>")



@dp.message_handler(text="🌄 Grafik dizayner")
async def grafik(message: types.message):
    await message.answer(
        "<b>🎓 Xizmat: Grafik dizayner!\n\n Bu xizmatlarimiz siz grafik dizayn bo'yicha loyihalar bilan yechimlarini taqdim qiladi!\n\n📚 Texnologiyalar : Photoshop, CorelDRAW, Adobe illustrator, Logo, Reklama </b>\n\n👨🏻‍💻 Jarayon: Admin tomonidan belgilangan bo'lib siz Grafik dizany bo'yicha barcha ishlarni bizga ikkilanmasdan aytishingiz mumkin. Hoziroq bizga buyurtma bering!. Buyurtma berish uchun menyudagi \"buyurtma berish\" bo'limini tanlang.")


# @dp.message_handler(text="❇️ Telegram bot")
# async def smm(message: types.message):
#     await message.answer("<b>🎓 Xizmat: Telegram botxizmatlari!\n\n Python dasturlash tilidan foydalangan holda Aiogram bot template shabloni orqali yaratilgan istalgan turdagi botlarni e'tiboringizga havola qilamiz!. Real loyihalar bilan ishlaymiz!\n\n👨🏻‍💻 Jarayon: Admin tomonidan belgilanadi. Hoziroq bizga buyurtma bering!. ")

@dp.message_handler(text="🐍 Python")
async def python(message: types.message):
    await message.answer(
        "<b>🎓 Xizmat: Python dasturlash tilida masalalar yechimlari asosan talabalar uchun hizmat qilamiz!. Python!\n\n📚 Texnologiya: Python!\n\nSiz Python bo'yicha barcha bilimlarga ega bo'lasiz va real loyiha bilan tanisha olasiz!</b>\n\n👨🏻‍💻 Jarayon: Admin tominidan belgilanadi. Hoziroq bizga buyurtma bering!. Buyurtma berish uchun menyudagi \"buyurtma berish\" bo'limini tanlang.")

@dp.message_handler(text="🛠 C# .Net fremwork(Loyihalar)")
async def csharp(message: types.message):
    await message.answer(
        "<b>🎓 Xizmat: C# dasturlash tilida masalalar yechimlari asosan talabalar uchun hizmat qilamiz!. Asosan kurs ishlari Desktop dasturlar, Mobil App, Web App. Biz sizning ishingizni yengillatib beramiz!\n\n📚 Texnologiya: C#!\n\nSiz C# bo'yicha barcha bilimlarga ega bo'lasiz va real loyiha bilan tanisha olasiz!</b>\n\n👨🏻‍💻 Jarayon: Admin tominidan belgilanadi. Hoziroq bizga buyurtma bering! Buyurtma berish uchun menyudagi \"buyurtma berish\" bo'limini tanlang.")

@dp.message_handler(text="⚙️ PHP Laravel fremwork(Web app)")
async def php(message: types.message):
    await message.answer(
        "<b>🎓 Xizmat: PHP Laravel dasturlash tilida masalalar yechimlari asosan talabalar uchun hizmat qilamiz!. Asosan kurs ishlari Mobil App, Web App. Biz sizning ishingizni yengillatib beramiz!\n\n📚 Texnologiya: PHP Laravel!\n\nSiz PHP Laravel bo'yicha barcha bilimlarga ega bo'lasiz va real loyiha bilan tanisha olasiz!</b>\n\n👨🏻‍💻 Jarayon: Admin tominidan belgilanadi. Hoziroq bizga buyurtma bering! Buyurtma berish uchun menyudagi \"buyurtma berish\" bo'limini tanlang.")

@dp.message_handler(text="🤖 Python telegram bot")
async def telegrambot(message: types.message):
    await message.answer("<b>🎓 Xizmat:  telegram bot  dasturlash tilida masalalar yechimlari asosan talabalar uchun hizmat qilamiz!. Asosan telegram bot Biz sizning ishingizni yengillatib beramiz!.  \n\n📚 Texnologiya:  Python Aiogram bot template shabloni orqali telegram bot !\n\nSiz Python telegram bot  bo'yicha barcha bilimlarga ega bo'lasiz va real loyiha bilan tanisha olasiz!</b>\n\n👨🏻‍💻 Jarayon: Admin tominidan belgilanadi. Hoziroq bizga buyurtma bering!. Buyurtma berish uchun menyudagi \"buyurtma berish\" bo'limini tanlang.")

@dp.message_handler(text="💼 Office ishlari")
async def office(message:types.message):
    await message.answer(
        "🎓 Xizmat: Office ilovalari bilan ishlash!\n\n Bu xizmat siz uchun istalgan turdagi office ilovalarida masofadan ishlaringizni bajarib berishni o\'z ichiga oladi!\n\n📚 Texnologiyalar : Micrasoft Office ilovalari(Word, Exel, PowerPoint, etc...) lardan foydalangan holda M-Service siznig ishlaringizni yengillashtirib beradi beradi. \n\n👨🏻‍💻 Jarayon: Admin tominidan belgilanadi. Hoziroq bizga buyurtma bering!")

@dp.message_handler(lambda message: message.text == "🔗 Havolalar")
async def channel_link_handler(message: types.Message):
    await message.answer(
        "👥 Bizning Telegram kanalimizga a'zo bo'ling va barcha yangiliklardan birinchi bo'lib xabardor bo'ling! 📢",
        reply_markup=channel_inline_keyboard)
    await message.answer(
        "🔔 Bizning YouTube kanalimizga obuna bo'ling va yangi videolardan birinchi bo'lib xabardor bo'ling! 🎬",
        reply_markup=youtube_inline_keyboard)
@dp.message_handler(text="🔙 Ortga qaytish")
async def orttga(message: types.Message):
    await message.answer("Sizga qanday yordam bera olishim mumkin?", reply_markup=menu)

