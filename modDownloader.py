from pysteamcmdwrapper import SteamCMD
from bs4 import BeautifulSoup
import re, os, sys

with open('mods.html') as f:
	read_data = f.read()

steam = SteamCMD("C:/steamcmd/")
steam.login("anonymous")

modsWithNames = {}

soup = BeautifulSoup(read_data, 'html.parser')

for itemL in soup.find_all('a'):
	for modName in soup.find_all(attrs={"data-type" : "DisplayName"}):
		editedModName = re.sub(r"[=\s_+-\.,\[\]\(\)']", "", modName.string)

	for link in soup.find_all('a'):
		mods = re.split(r"=", link.get('href'))[1]
	
