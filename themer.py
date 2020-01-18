import json
import pprint

pp = pprint.PrettyPrinter(4)

# profiles.json path
pathProfile = 'C:/Users/Pranav Goyanka/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/profiles.json'
# pathProfile = 'E:/code/windows-terminal-themer/profiles.json'

fileJson = open(pathProfile, 'r')
profiles = json.load(fileJson)
fileJson.close()
# Defaults
# currentProfName = "WLinux"
def getProfname():
    return input('Enter the name of terminal who\'s profile you want to change: ') or 'Windows PowerShell'
    

def displayAvailableProfiles():
    for prof in profiles['profiles']:
        print(prof['name'])

def findProfile():
    for x in profiles['profiles']:
        if x['name'] == currentProfName:
            return x

def writeProfile(currentProf):
    with open(pathProfile, 'r+') as f:
        data = json.load(f)
        for p in range(len(data['profiles'])):
            if data['profiles'][p]['name'] == currentProfName:
                data['profiles'][p] = currentProf
        # seek to the begining, write and remove everything else
        f.seek(0) 
        json.dump(data, f, indent=4)
        f.truncate()
            

print('Available Windows Terminal Profiles:')
displayAvailableProfiles()
currentProfName = getProfname()
currentProf = findProfile()
print('Current Profile:')
pp.pprint(currentProf)



