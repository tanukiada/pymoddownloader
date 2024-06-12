from bs4 import BeautifulSoup
import re, os, subprocess

SOURCE_DIR = "C:/arma/steamapps/workshop/content/107410/"
MOD_DIR = "C:/ArmA 3/Arma 3 Server/"

def ModDownloadAndRename(mod_id, mod_name):
	if os.path.isdir(MOD_DIR + "@" + mod_name):
		print("mod exists.. skipping")
	elif not os.path.isdir(SOURCE_DIR + mod_id):
		subprocess.run(f'C:/steamcmd/steamcmd.exe +force_install_dir ../ArmA 3/Arma 3 Server/ +login anonymous +workshop_download_item 107410 {item[1]} +quit')
		os.rename(SOURCE_DIR + mod_id, MOD_DIR + "@" + mod_name)
	else:
		ModDownloadAndRename(mod_id, mod_name)
		
with open('mods.html') as f:
	read_data = f.read()

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
	ModDownloadAndRename(item[1], item[0])