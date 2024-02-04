from aiogram import types

from keyboards.default.menu_btn import menu
from loader import dp, bot
from aiogram.dispatcher import FSMContext

from keyboards.default.check import check_btn
from states.kursga_yozilish import kursgaYozilish

@dp.message_handler(text="®️ Buyurtma berish")
async def kursga_yozilish(message: types.message):
    await message.answer("Familiya Ism Sharif?\n\n(Masalan: Ali Valiyev G\'ani o\'g\'li)")
    await kursgaYozilish.fullName.set()

@dp.message_handler(state=kursgaYozilish.fullName)
async def fullName(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({"Name": fullname})

    await message.answer("Yoshingiz?\n\n(Masalan : (22) yosh)")
    await kursgaYozilish.next()

@dp.message_handler(state=kursgaYozilish.yosh)
async def yosh(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data({"Yosh": yosh})

    await message.answer("Qaysi xizmatlarimiz bo'yicha ma'lumot olmoqchisiz?\n\n🎓 Xizmatlarimiz :\n\n❇️  ISTALGAN TURDAGI DASTURLAR\n\n❇️  WEB DASTURLASH  (FRONT END,  BECK END)\n\n❇️  C# .NET FREMWORK, PHYTON DGANGO, PHP LARAVEL, JAVA SPRINGBOOT PROEKTLAR(KURS ISHLAR)\n\n❇️  GRAFIK DIZAYN\n\n❇️  TELEGRAM BOT HIZMATLARI\n\n❇️  PHOTOSHOP\n\n❇️  KURS ISHI \n\n❇️ MUSTAQIL ISH \n\n❇️  SUNIY INTELEKT MASALALARI\n\n❇️  LOYIHALASH ISHLARI\n\n Yuqoridagilardan birortasini tanlab bizga yozib qoldiring!.")
    await kursgaYozilish.next()

@dp.message_handler(state=kursgaYozilish.kurs)
async def kurs(message: types.message, state: FSMContext):
    kurs = message.text
    await state.update_data({"Xizmat": kurs})

    await message.answer("Tanlagan xizmatingiz bo\'yicha bilim darajangiz qanday?\n\n(Masalan : Umuman yo'q, Oz-moz bilaman, To'liq bilaman)")
    await kursgaYozilish.next()

@dp.message_handler(state=kursgaYozilish.bilim)
async def bilim(message: types.Message, state: FSMContext):
    bilim = message.text
    await state.update_data({"Bilim": bilim})

    await message.answer("Telefon raqamingizni kiriting?\n\n(Masalan : +99891 0256525)")
    await kursgaYozilish.next()

@dp.message_handler(state=kursgaYozilish.nomer)
async def nomer(message: types.Message, state: FSMContext):
    nomer = message.text
    await state.update_data({"Nomer": nomer})

    data = await state.get_data()
    fullname = data.get("Name")
    yosh = data.get("Yosh")
    kurs = data.get("Kurs")
    bilim = data.get("Bilim")
    nomer = data.get("Nomer")

    msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
    msg += f"🎓 Mijoz: - {fullname}\n"
    msg += f"🌐 Yosh: - {yosh}\n"
    msg += f"🎓 Kurs: - {kurs}\n"
    msg += f"👨🏻‍💻 Daraja: - {bilim}\n"
    msg += f"📞 Aloqa: - {nomer}"
    await message.answer(msg)
    await message.answer("Barcha ma\'lumotlar to\'g\'rimi?", reply_markup=check_btn)
    await kursgaYozilish.next()


@dp.message_handler(state=kursgaYozilish.check)
async def chesk(message: types.Message, state: FSMContext):
    if message.text.lower() == "ha":
        data = await state.get_data()
        fullname = data.get("Name")
        yosh = data.get("Yosh")
        kurs = data.get("Kurs")
        bilim = data.get("Bilim")
        nomer = data.get("Nomer")

        msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
        msg += f"🎓 Mijoz: - {fullname}\n"
        msg += f"🌐 Yosh: - {yosh}\n"
        msg += f"🎓 Kurs: - {kurs}\n"
        msg += f"👨🏻‍💻 Daraja: - {bilim}\n"
        msg += f"📞 Aloqa: - {nomer}"
        await message.answer(msg)
        await message.answer("Barcha ma\'lumotlar to\'g\'rimi?", reply_markup=check_btn)
        await bot.send_message(chat_id=6053584538, text=msg)
        # await bot.send_message(chat_id=912653144, text=msg)
        # await bot.send_message(chat_id=1405814595, text=msg)
        await message.answer("Barcha ma\`lumotlar adminga yuborildi. Tez orada siz bilan bog\`lanadi")
        await message.answer("Bosh menyu!", reply_markup=menu)
        await state.finish()
    else:
        await message.answer("Qabul qilinmadi", reply_markup=menu)
        await state.finish()
