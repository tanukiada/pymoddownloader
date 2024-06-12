from bs4 import BeautifulSoup
from dotenv import load_dotenv
import re, os, subprocess, time, requests

load_dotenv()

USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
SOURCE_DIR = "C:/arma/steamapps/workshop/content/107410/"
MOD_DIR = "C:/ArmA 3/Arma 3 Server/"



def ModDownloadAndRename(modId, modName):
	failCounter = 0
	if os.path.isdir(MOD_DIR + "@" + modName):
		print("mod exists.. skipping")
	else:
		while not os.path.isdir(SOURCE_DIR + modId or not os.path.isdir(MOD_DIR + "@" + modName)):
			subprocess.run(f'C:/steamcmd/steamcmd.exe +login {USER_NAME} {PASSWORD} +bVerifyAllDownloads 1 +workshop_download_item 107410 {item[1]} +quit')
			failCounter+=1
			time.sleep(10)
			if failCounter == 3:
				failCounter = 0
				with open('failed.txt', 'a') as f:
					f.write(modName + " | " + modId + "\n")
				break
		if os.path.isdir(SOURCE_DIR + modId) and not os.path.isdir(MOD_DIR + "@" + modName):
			os.rename(SOURCE_DIR + modId, MOD_DIR + "@" + modName)


# need to figure out
# def ModDownloadAndRename(modId, modName):
# 	response = requests.post(f"https://api.steampowered.com/IPublishedFileService/Subscribe/v1/?key={API_KEY}&appid=107410&modid={modId}&include_dependencies=true")

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