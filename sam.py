import telepot
bot=telepot.Bot("5701983985:AAFj9sN8dUMulVe3fBShjJYpDYcjO8pNxNs")
bot.sendMessage("1102951994",str("hello"))
bot.sendPhoto("1102951994",photo=open("msg.jpg",'rb'))