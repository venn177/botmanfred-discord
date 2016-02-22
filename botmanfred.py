# coding=utf8

import discord
import sys
import random
import importlib
import os
import time
import os.path
import re
from datetime import datetime
from pymarkovchain import MarkovChain
from glob import glob
from random import randint

bot = discord.Client()
bot.login('USERNAME', 'PASSWORD')

# comment out the next 5 lines unless you have a markov database
importlib.import_module("plugins")
mc = MarkovChain()
with open(r'C:\\Python35\\discordbot\\logpruned.txt', 'r', encoding="utf8") as log:
	thelog = log.read()
mc.generateDatabase(thelog)

#for plugin in glob("C:/Python35/discordbot/plugins/[!_]*.py"):
#	module = 'plugins.' + plugin[31:-3]
#	print(module)
#	print(plugin)
#	try:
#		importlib.import_module(module)
#	except Exception as e:
#		print('Failed to import {0}: {1}'.format(plugin, e))

@bot.event
def on_message(message):
	currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
	print(currentTime + str(message.author) + ': ' + message.content)
	if message.author == bot.user:
		return
	with open("C:\Python35\discordbot\log.txt", "a", encoding="utf8") as myfile: # you need to make a blank log.txt file here, and obviously poitn the directory correctly
		myfile.write(currentTime + str(message.author) + ': ' + message.content + '\n')
	with open("C:\Python35\discordbot\logpruned.txt", "a", encoding="utf8") as myfile: # ditto this one
		myfile.write(message.content + ' ')
	messageCheck = message.content.lower()
	if "ayy lmao" in messageCheck:
		ayyrandom = random.choice(('http://i.imgur.com/DTZpeZw.jpg', 'http://i.imgur.com/A59LSFx.png', 'http://i.imgur.com/OMxngaL.gif', 'http://i.imgur.com/Q9FMeEq.gif', 'http://i.imgur.com/oTg6iX7.gif', 'http://i.imgur.com/JcOhXAp.gif', 'http://i.imgur.com/QJLAFJW.gif', 'http://i.imgur.com/Yg5cJrY.png', 'http://i.imgur.com/AcnGuxb.png', 'http://i.imgur.com/RFw4wKS.png', 'http://i.imgur.com/ndl6i6q.png', 'http://i.imgur.com/2onOSUg.png', 'http://i.imgur.com/6Toewfr.png', 'http://i.imgur.com/BWToRIa.png', 'http://i.imgur.com/K9K7Co2.png', 'http://i.imgur.com/BPVmCph.png', 'http://i.imgur.com/FG7oxbz.png', 'http://i.imgur.com/KzIJxxs.png', 'http://i.imgur.com/wT8NgZT.png'))
		bot.send_message(message.channel, ayyrandom)
	if "doot doot" in messageCheck:
		skeltalrandom = random.choice(('http://i.imgur.com/TyR727g.jpg', 'https://41.media.tumblr.com/fd40ee2298e9200ff0850c430fcb9197/tumblr_nihhr7F1ZJ1tlpu2to3_540.jpg', 'Watch out fuccboi! https://i.imgur.com/S9fEydK.gif', 'http://i.imgur.com/kSl51gS.jpg', 'http://i.imgur.com/5w26yNa.jpg', 'http://i.imgur.com/3KudVwC.gif', 'http://i.imgur.com/dBUcXxW.gif', 'http://i.imgur.com/YeBSRwv.png', 'http://i.imgur.com/sXSvQGp.jpg', 'UNACCEPTABLE: http://i.imgur.com/UtOPvpF.jpg', 'https://33.media.tumblr.com/6dfdbb8dc857d55f04ee9c50e32e1ecd/tumblr_nd69kiE8Gb1qiz7imo1_500.gif', 'I am doot. http://i.imgur.com/uTzeLBz.jpg', 'http://i.imgur.com/q1iFS6P.jpg', 'http://i.imgur.com/KsLo7yM.png', 'http://i.imgur.com/CaEnKGu.png', 'http://i.imgur.com/6uNAzI3.jpg', 'http://i.imgur.com/wwdKB6a.png', 'http://i.imgur.com/98CqQj2.gif', 'TFW No Calcium: https://i.imgur.com/B92ZjT3.gif', 'http://i.imgur.com/x29nKdO.jpg', 'http://i.imgur.com/9pPcILj.jpg', 'http://i.imgur.com/KpY8R92.jpg', 'http://i.imgur.com/9PMdnoL.jpg', 'http://i.imgur.com/rQOsadt.png', 'http://i.imgur.com/ujNM6Dp.jpg', 'http://i.imgur.com/735CLv5.jpg', 'http://i.imgur.com/Nm9hWOt.jpg', 'http://i.imgur.com/8wMO5cS.jpg', 'http://i.imgur.com/nN49tnJ.png', 'http://i.imgur.com/t8IyHAB.gif'))
		bot.send_message(message.channel, skeltalrandom)
	if "38 bucks" in messageCheck:
		_38var = random.choice(('http://i.imgur.com/EpJNnSb.jpg', 'http://i.imgur.com/dRFEB9y.png', 'http://i.imgur.com/58zYhxl.png', 'http://i.imgur.com/HywGed2.png'))
		bot.send_message(message.channel, _38var)
	if "fuck the emps" in messageCheck:
		empirefuck = random.choice(('DAE RBIs > OPS??', 'I make Harold Reynolds look like he knows what he\'s talking about!', 'Triple crown = auto MVP, who needs to think??', 'Jon Lester is shit because he didn\'t get the Athletics into the playoffs against the Royals. He might as well kill himself! Despite the OVERWHELMING evidence that he was more useful to the team down the stretch than Yoenis Cespedes, the Athletics completely gimped their future and playoff chances by acquiring a better player!'))
		bot.send_message(message.channel, empirefuck)
	# comment out lines 59 through 71 unless you have a text database to to generate a markov database from
	thenumber = randint(1,40)
	if "botmanfred" in messageCheck:
		thenumber = randint(1,2)
		if thenumber == 1:
			time.sleep(randint(2,4))
			bot.send_message(message.channel, mc.generateString())
			return
		else:
			return
	if thenumber < 4:
		print("Markov time!")
		time.sleep(randint(1,7))
		bot.send_message(message.channel, mc.generateString())
		
@bot.event
def on_ready():
	print('Logged in as ' + str(bot.user.name) + ' (' + bot.user.id + ')')

bot.run()
