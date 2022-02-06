[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)
# discord-vlc-presence
This is a small python script that sets your locally running discord's Rich Presence to whatever you are playing on your VLC media player. And optionally if you are running Windows you can install pywinauto for displaying what you are playing too.

### Things to set up before you start using this
* Make sure you have Python3 installed.
  * Install the package pypresence  
  `pip install pypresence`  
  * Install the package psutil  
  `pip install psutil`
  * Optionally install the package pywinauto for video title(filename of current video) (Windows only)  
  `pip install pywinauto`  
 

### Set up the service on your PC
#### Settingup VLC for filename as title
For the title to Display currectly you will have to change the VLC media player's settings to display filename as your window title. To do this,  

`Open VLC -> Menu Tools -> Preferences (Show settings = ALL) -> Input/Codecs.`  

Then at the very bottom of the right panel set the option `"Change title according to current media"` to `"$u"`.  

Save, exit and restart VLC.

#### Running and Testing the Script
Clone or Download this repo as zip file then extract the contents, you can check and see if everything is working properly by running `main.py`.

#### Hide execution window on Windows
You will see a file named silent.vbs. This is used to run the script without any window and everything is done in the background.

#### Automatic Startup on Windows
If you wish to start the script directly after system startup, first create a shortcut for vbs file and then put it in startmenu's startup folder, that is either -  
* `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`
* `C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
