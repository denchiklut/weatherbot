from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp
from states import Test


@dp.message_handler(Command('test'))
async def enter_test(message: types.Message):
    await message.reply('Вы начали тестирование\n'
                        'Вопрос 1.Укажите страну')
    await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    await state.update_data(answer1=message.text)
    await message.answer('Вопрос 2\n'
                          'Укажите город')
    await Test.next()


@dp.message_handler(state=Test.Q2 )
async def answer_q1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data['answer1']
    answer2 = message.text

    await message.answer('Спасибо за ответ!')
    await message.answer(f'Ответ 1! {answer1}')
    await message.answer(f'Ответ 2 ! {answer2}')

    await state.finish()
