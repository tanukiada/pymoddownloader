from pysteamcmdwrapper import SteamCMD
from bs4 import BeautifulSoup
import re, os, sys

with open('mods.html') as f:
	read_data = f.read()

steam = SteamCMD("C:/steamcmd/")
steam.login("anonymous", "")

MOD_DIR = "C:/ArmA 3/Arma 3 Server"

soup = BeautifulSoup(read_data, 'html.parser')

for itemL in soup.find_all('a'):
	for modName in soup.find_all(attrs={"data-type" : "DisplayName"}):
		editedModName = re.sub(r"[=\s_+-\.,\[\]\(\)']", "", modName.string)

	for link in soup.find_all('a'):
		mod = re.split(r"=", link.get('href'))[1]

		steam.workshop_update(107410,mod, MOD_DIR, validate = True)
		os.rename(mods, editedModName)
