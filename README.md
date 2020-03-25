# Windows Terminal Themer
A GUI based theme manager for the new Windows Terminal

## Usage

Clone this repo

```
git clone https://github.com/pranavgoyanka/windows-terminal-themer.git
```
### Install Dependancies
```
pip install tkcolorpicker
```

### Or 
Download it manually and save it to your computer

### Method 1 (Adding the scripts to PATH)

```
[Environment]::SetEnvironmentVariable("Path", "$env:Path;<PATH_TO_REPO_DIRECTORY>")
```
Where, <PATH_TO_REPO_DIRECTORY> is the location of the downloaded/cloned files

Example

```
[Environment]::SetEnvironmentVariable("Path", "$env:Path;E:\code\windows-terminal-themer\")
```

Now run

```
themergui.py
```

Select the shell from the CLI (GUI will be added for this in the future) and hit enter to change the settings

### Method 2 

Change directory of PowerShell to the location where you have the files downloaded/cloned

```
cd <PATH_TO_REPO_DIRECTORY>
```

Now run

```
themergui.py
```

Select the shell from the CLI (GUI will be added for this in the future) and hit enter to change the settings

## Using the Custom Color Scheme
1) Open Windows Terminal and press ``` ctrl + ,```

2) Copy the contents of customColorScheme.json to schemes section of profiles.json

3) Edit the value of colorScheme under your profile name in profiles.json

4) Save and close profiles.json

## Screenshots

#### The GUI
![](https://github.com/pranavgoyanka/windows-terminal-themer/blob/master/screenshots/gui.PNG)

#### The working 
![](https://github.com/pranavgoyanka/windows-terminal-themer/blob/master/screenshots/working.gif)

#### To Do:
Improve what the GUI looks like


