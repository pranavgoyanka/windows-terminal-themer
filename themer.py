import json
import pprint

pp = pprint.PrettyPrinter(4)

# profiles.json path
pathProfile = 'C:/Users/Pranav Goyanka/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/profiles.json'

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
            # print(x)
            # currentProf = x
            # print(currentProf)

print('Available Windows Terminal Profiles:')
displayAvailableProfiles()
currentProfName = getProfname()
currentProf = findProfile()
print('Current Profile:')
pp.pprint(currentProf)

