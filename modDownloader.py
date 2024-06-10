from bs4 import BeautifulSoup
import re, os, sys

with open('mods.html') as f:
	read_data = f.read()

MOD_DIR = "C:/ArmA 3/Arma 3 Server/"

soup = BeautifulSoup(read_data, 'html.parser')

modListName = []
modListID = []
modDict = {}

for modName in soup.find_all(attrs={"data-type" : "DisplayName"}):
	editedModName = re.sub(r"[=\s_+-\.,\[\]\(\)']", "", modName.string)
	modListName.append(editedModName)


for link in soup.find_all('a'):
	mod = re.split(r"=", link.get('href'))[1]
	modListID.append(mod)

modDict = {key: value for key, value in zip(modListName, modListID)}

for item in modDict.items():
	os.system(f'C:/steamcmd/steamcmd.exe +force_install_dir C:/ArmA 3/Arma 3 Server +login anonymous +workshop_download_item 107410 {item[1]} +quit')
	os.rename(MOD_DIR + item[1], MOD_DIR + "@" + item[0])