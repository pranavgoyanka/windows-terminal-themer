import json
import pprint
import os
pp = pprint.PrettyPrinter(4)

# profiles.json path
l = os.getenv('localappdata')
a = '\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json'
pathProfile = l+a

fileJson = open(pathProfile, 'r')
profiles = json.load(fileJson)
fileJson.close()
# Defaults
defaultFallback = {
    'acrylicOpacity': 0.65,
    'background': '#024557',
    'closeOnExit': True,
    'colorScheme': 'Campbell',
    'commandline': 'powershell.exe',
    'cursorColor': '#FFFFFF',
    'cursorShape': 'vintage',
    'fontFace': 'Consolas',
    'fontSize': 11,
    'guid': '{61c54bbd-c2c6-5271-96e7-009a87ff44bf}',
    'historySize': 9001,
    'icon': 'ms-appx:///ProfileIcons/{61c54bbd-c2c6-5271-96e7-009a87ff44bf}.png',
    'name': 'Windows PowerShell',
    'padding': '0, 0, 0, 0',
    'snapOnInput': True,
    'startingDirectory': '%USERPROFILE%',
    'useAcrylic': True}

# currentProfName = "WLinux"
def getProfname():
    return input('Enter the name of terminal who\'s profile you want to change: ') or 'Windows PowerShell'
    
allProfs = []
def displayAvailableProfiles():
    # print(profiles['profiles']['list'])
    for prof in profiles['profiles']['list']:
        allProfs.append(prof['name'])
        # print(prof['name'])

def findProfile():
    for x in profiles['profiles']['list']:
        if x['name'] == currentProfName:
            return x

def writeProfile(currentProf):
    with open(pathProfile, 'r+') as f:
        data = json.load(f)
        # print(data)
        for p in range(len(data['profiles']['list'])):
            if data['profiles']['list'][p]['name'] == currentProfName:
                data['profiles']['list'][p] = currentProf
        # seek to the begining, write and remove everything else
        f.seek(0) 
        json.dump(data, f, indent=4)
        f.truncate()
            

# print('Available Windows Terminal Profiles:')
displayAvailableProfiles()
# currentProfName = getProfname()
currentProfName = allProfs[0]
currentProf = findProfile()
# print('Current Profile:')
# pp.pprint(currentProf)



