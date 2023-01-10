# from progress.bar import Bar
#
# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     bar.next()
# bar.finish()


# from isOdd import isOdd
#
#
# print(isOdd(0)) //=> false
# print(isOdd(4)) //=> false

# import emoji
#
# print(emoji.emojize('Python is :thumbs_up:'))
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))

# import matplotlib.pyplot as plt
# import numpy as np
#
# list =[1,2,3,2,7]
# plt.plot(list)
#
# plt.show()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
# встатвить нужный токен
app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('Server start')
app.run_polling()
