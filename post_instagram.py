from instabot import Bot
#!/usr/bin/python
import os
import sys
import shutil
from PIL import Image

bot = Bot()
bot.login(username = "calistoantonino", password = "************")
bot.small_delay()
im = Image.open("testando_bot.jpg")  
newsize = (1080, 1080) 
im1 = im.resize(newsize) 
im1.save('resized_testando_bot.jpg')
bot.upload_photo("resized_testando_bot.jpg",
                 caption = "Testando bot de publicacao de feed!")
#bot.delay(10)
#bot.comment()
print("Tempo delay")

print("Terminou Tempo delay")

  

mydir = '/Users/macbook/Documents/Antonino/Pessoal/Github/post_instagram/config'
try:
    shutil.rmtree(mydir)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

#bot.like()
#bot.send_messages()
#bot.logout()