import telebot
from telebot import types

output = open('Base.txt', 'w');
 
yazik = "\U0001F60B";
mashinka = "\U0001F69A";
clever = "\U0001F340";
derevo="\U0001F332"
palecvverh ="\U0001F446"
meshoksdengami="\U0001F4B0"
deadsmile ="\U0001F635"
smilesdimom ="\U0001F624"
raketa = "\U0001F680"
palecvpravo ="\U0001F449"

bot = telebot.TeleBot('740263628:AAFCA_6e_b2MjkZQuMs2O5-A3iwZw4UkHPE')

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item1 = types.KeyboardButton('Жидкости с CBD '+derevo)
    item2 = types.KeyboardButton('Жидкости с THC'+yazik)
    item3 = types.KeyboardButton('Как заказать? '+mashinka)
    markup.add(item1, item2)
    markup.row(item3)
    bot.send_message(message.chat.id, clever + ' Привет, спасибо что заглянул, мы продаём жижки из Амстердама. ' + yazik, reply_markup=markup)
    output = open('Base.txt', 'a');
    output.write(str(message.chat.id)+"\n")
    output.close()

@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.text == 'Жидкости с CBD '+derevo:
        photo = open('cbd.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, palecvverh+' Данная жидкость без ТГК!\n'+ meshoksdengami+' 50/100/150 ml - 600Rub/900Rub/1200rub')

    if message.text == 'Жидкости с THC'+yazik:
        photo = open('thc1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, deadsmile+' [INDICA] Skywalker 79% THC\n'+meshoksdengami+'100/300/500 ml - 1000Rub/2000Rub/3200Rub\n')
        bot.send_message(message.chat.id, yazik+' [HYBRID] Gelato 83% THC\n'+ meshoksdengami+'100/300/500/1000 ml - 1100Rub/2100Rub/3250Rub/Нет в наличии\n')
        bot.send_message(message.chat.id, smilesdimom+' [Sativa] Jack Herer 77% THC\n'+meshoksdengami+'100/300/500 ml - 930Rub/Нет в наличии/3000Rub\n')


    if message.text == 'Как заказать? '+mashinka:
        bot.send_message(message.chat.id, raketa+' Доставка происходит путём закладок в вашем районе. Работаем по всему СНГ! '+palecvpravo+' Для покупки обращаться к @DarkVapeDealer с названием товара и местом!')
        


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

