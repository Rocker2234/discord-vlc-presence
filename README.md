[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)
# discord-vlc-presence
* * *
This is a small python script that sets your locally running discord's Rich Presence to whatever you are playing on your VLC media player. And optionally if you are running Windows you can install pywinauto for displaying what you are playing too.

### Things to set up before you start using this
* Make sure you have Python3 installed.
  * Install the package pypresence  
  `pip install pypresence`  
  * Install the package psutil  
  `pip install psutil`
  * Optionally install the package pywinauto for video title(filename of current video)  
  `pip install pywinauto`  


### Set up the service on your PC
#### Hide execution window on Windows
You will see a file named silent.vbs. This is used to run the script without any window and everything is done in the background. 

#### Automatic Startup on Windows
If you wish to start the script directly after system startup, first create a shortcut for vbs file and then put it in startmenu's startup folder, that is either -  
* `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`
* `C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`