#from progress.bar import Bar
#import time

#bar = Bar('Processing', max=20)
#for i in range(20):
    #time.sleep(1)
    #bar.next()
#bar.finish()
#import emoji
#print(emoji.emojize('Python is :thumbs_up:'))

#print(emoji.emojize('Python is :thumbsup:', language='alias'))

#print(emoji.demojize('Python is 👍'))

#print(emoji.emojize("Python is fun :red_heart:"))

##print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))

#print(emoji.is_emoji("👍"))
#import matplotlib.pyplot as plt
#import numpy as np

#list = [1,2,3,2,7]
#plt.plot(list)

#plt.show()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("sum", sum_command))
app.run_polling()