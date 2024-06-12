from bs4 import BeautifulSoup
import re, os, subprocess
from tenacity import retry, stop_after_attempt, wait_fixed

MOD_DIR = "C:/ArmA 3/Arma 3 Server/"

@retry(wait=wait_fixed(60))
def ModDownloadAndRename(mod_id, mod_name):
	try:
		subprocess.run(f'C:/steamcmd/steamcmd.exe +force_install_dir ../ArmA 3/Arma 3 Server/ +login anonymous +workshop_download_item 107410 {item[1]} +quit')
		if os.path.isfile(MOD_DIR + "@" + mod_name):
			pass
		else:
			os.rename(MOD_DIR + mod_id, MOD_DIR + "@" + mod_name)
		return 0
	except Exception as e:
		raise(e)

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