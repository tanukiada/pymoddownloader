from bs4 import BeautifulSoup
import re, os, sys, pysteamcmd

with open('mods.html') as f:
	read_data = f.read()

MOD_DIR = "C:/ArmA 3/Arma 3 Server/"

soup = BeautifulSoup(read_data, 'html.parser')

steam = pysteamcmd.Steamcmd("C:/ArmA 3/ArmA 3 Server/")

for itemL in soup.find_all('a'):
	for modName in soup.find_all(attrs={"data-type" : "DisplayName"}):
		editedModName = re.sub(r"[=\s_+-\.,\[\]\(\)']", "", modName.string)

	for link in soup.find_all('a'):
		mod = re.split(r"=", link.get('href'))[1]

	steamcmd.install_workshopfiles(107410, mod, MOD_DIR, user='anonymous' password=None)
	os.rename(MOD_DIR + mod, MOD_DIR + "@" + editedModName)
