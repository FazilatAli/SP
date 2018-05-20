import requests
import os
import urllib
from PIL import Image
from bs4 import BeautifulSoup
from StringIO import StringIO
from datetime import datetime


def getMp3(URL):

	req = requests.get(URL,stream =True)
	mp3 = []
	if req.status_code == 200:
		parserObj = BeautifulSoup(req.content, "html.parser")
		href_tag_list = parserObj.find_all("a")
		for href_tag in href_tag_list[1:]:
			mp3.append(href_tag['href'])
	return mp3

def downloadMp3(url_list):
	count = 0
	mypath = "/home/fazilatali/SP/Assignments/Assignment2/Task1/"
	for mp3_url in url_list:
		URL = "https://download.quranicaudio.com/quran/"+mp3_url
		mp3 = getMp3(URL)
		mp3 = mp3[-26:]
		direc = mypath+mp3_url[:-1]
		os.mkdir(direc)
		os.chdir(direc)

		f = open(direc+"/logFile", "a+")
		f.write("%s Total Qari %d\n"%(date().strip("\n"),len(url_list)))
		count = count + 1
		f.write("%s Processing %d out %d\n" %(date().strip("\n"),count,len(url_list)))
		f.write("%s "%(date().strip("\n")))
		f.write(u'{0}'.format(mp3_url[:-1]))		
		for i in mp3:
			f.write("%s "%(date().strip("\n")))
			f.write(u'{0}'.format(mp3_url[:-1]))
			f.write(" %s START\n"%(i)) 
			os.system('wget -c "{}" '.format("https://download.quranicaudio.com/quran/"+mp3_url+i))
			f.write("%s "%(date().strip("\n")))
			f.write(u'{0}'.format(mp3_url[:-1]))
			f.write(" %s END\n"%(i))  
		f.write("%s Merging the files of "%(date().strip("\n")))
		f.write(u'{0}'.format(mp3_url[:-1]))
		f.write(" START\n")
		os.system('mp3wrap second_Half.mp3 *.mp3')
		f.write("%s Merging the files of "%(date().strip("\n")))
		f.write(u'{0}'.format(mp3_url[:-1]))
		f.write(" END\n")
		f.close()		
		os.chdir(mypath)


def date():
	return os.popen('date').read()		

def main():
	URL = "https://download.quranicaudio.com/quran/"
	url_list = getMp3(URL)
	downloadMp3(url_list)

if __name__ == "__main__":
	main()