import urllib2
import time
import os
import sys
import subprocess
import msvcrt

def getnews():
	newsfile = urllib2.urlopen("http://wsdownload.bbc.co.uk/worldservice/css/32mp3/latest/bbcnewssummary.mp3")
	output = open('news.mp3', 'wb')
	output.write(newsfile.read())
	output.close()

try:
	getnews()
	print "Downloading and playing BBC hourly bulletin.."
	print "Press 's' key on terminal window to stop playback and close media player."
	os.startfile('news.mp3')
except:
	print "No internet connection..\nPlease try again when connected to the internet.."
	time.sleep(2)
	sys.exit(0)

key = ''

for i in range(152):
	if msvcrt.kbhit():
		key = msvcrt.getch()
	else:
		pass
	if key == 's':
		break
	else:
		pass
	time.sleep(1)

subprocess.call(["taskkill", "-IM", "vlc.exe"])
sys.exit(0)