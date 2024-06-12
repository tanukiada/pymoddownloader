from bs4 import BeautifulSoup
import re, os, subprocess, time

SOURCE_DIR = "C:/arma/steamapps/workshop/content/107410/"
MOD_DIR = "C:/ArmA 3/Arma 3 Server/"

def ModDownloadAndRename(modId, modName):
	failCounter = 0
	if os.path.isdir(MOD_DIR + "@" + modName):
		print("mod exists.. skipping")
	else:
		while not os.path.isdir(SOURCE_DIR + modId or not os.path.isdir(MOD_DIR + "@" + modName)):
			subprocess.run(f'C:/steamcmd/steamcmd.exe +force_install_dir ../ArmA 3/Arma 3 Server/ +login anonymous +bVerifyAllDownloads 1 +workshop_download_item 107410 {item[1]} +quit')
			failCounter+=1
			time.sleep(10)
			if failCounter == 5:
				failCounter = 0
				break
		if os.path.isdir(SOURCE_DIR + modId) and not os.path.isdir(MOD_DIR + "@" + modName):
			os.rename(SOURCE_DIR + modId, MOD_DIR + "@" + modName)


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