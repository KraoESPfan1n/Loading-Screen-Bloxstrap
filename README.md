<p align="center">
    <img src="https://i.ibb.co/bgsKbPF/image.png" width="640" height="360">
</p>

[![License](https://img.shields.io/badge/License-MIT-lime)](./LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0-purple)](https://github.com/KraoESPfan1n/Loading-Screen-Bloxstrap/releases/tag/Release)
[![Stealing Intellectual Property](https://img.shields.io/badge/Based_on-Bloxstrap-591ac7)](https://github.com/pizzaboxer/bloxstrap)
[![Discord](https://img.shields.io/badge/Discord-Original_thread-blue)](https://discord.com/channels/1099468797410283540/1260503953234329662)
[![Author](https://img.shields.io/badge/Author-Krao-darkblue)](https://github.com/KraoESPfan1n)
[![Contributor](https://img.shields.io/badge/Contributor-HxLL-darkred)](https://github.com/hxll-f)
[![Extra](https://img.shields.io/badge/I_am-_very_tired-black)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

# Loading-Screen-Bloxstrap

Requirements:
- Windows 10/11
- [PowerShell](https://docs.microsoft.com/en-us/powershell/) (usually comes by default on windows)
- [Python V3.x for the installer](https://www.python.org/downloads/)
- [VLC Media Player](https://www.videolan.org/vlc/)
- [Bloxstrap (obviously)](https://github.com/pizzaboxer/bloxstrap)


[![Windows 11](https://img.shields.io/badge/Windows-11-blue)](https://www.microsoft.com/en-us/software-download/windows10)
[![Windows 10](https://img.shields.io/badge/Windows-10-blue)](https://www.microsoft.com/software-download/windows11)
[![PowerShell](https://img.shields.io/badge/PowerShell-latest-blue)](https://docs.microsoft.com/en-us/powershell/)
[![Python](https://img.shields.io/badge/Python-latest-Yellow)](https://www.python.org/downloads/)
[![VLC](https://img.shields.io/badge/VLC-latest-orange)](https://www.videolan.org/vlc/index.html)
[![Bloxstrap](https://img.shields.io/badge/Bloxtrap-latest-591ac7)](https://github.com/pizzaboxer/bloxstrap)
---
> [!WARNING]
> The uninstall button will NOT uninstall python, VLC, PowerShell, Bloxstrap, it will only uninstall the mod.
<details>
<summary>Python Installer User Guide</summary>
    
## Required Libraries

Before running the script, ensure you have the necessary libraries installed. Use the following command to install them if they are not already available:


```
pip install pillow
```

[![Pillow](https://img.shields.io/badge/Pillow-latest-Yellow)](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)

## Steps to use `installer.py`

### Preparation

- Ensure you have the [![Installer](https://img.shields.io/badge/installer.py-e6c912)](https://github.com/KraoESPfan1n/Loading-Screen-Bloxstrap/releases/tag/Release) file on your computer.
- Have a video file ready that you want to use as a loading screen.

### Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory where `installer.py` is located.
3. Run the script with the command:
    ```bash
    python installer.py
    ```

### Installing or Changing the Loading Screen

1. Click on **Install/Change**.
2. Select the video file you want to use as a loading screen.
3. If VLC is not found, you will be given the option to install it or manually select its location.

### Reviewing the Logs

1. After each operation, a window with the installation logs will be displayed.
2. Review this information to ensure everything has been done correctly.

## Additional Notes

- The script currents supports English, Spanish and German.
- If you encounter any issues, check the logs for more information about what might have gone wrong.
- Any error that the console presents can be reported in the repository.

</details>

---
<!-- Manual installation guide -->
<details>
<summary>Manual installation guide</summary>
For the people that just don't like it the easy way...

# Script Setup
1. Download the [![intro](https://img.shields.io/badge/intro.ps1-7b36c9)](https://github.com/KraoESPfan1n/Loading-Screen-Bloxstrap/releases/tag/Release) file
2. Open it in the text editor of your choice
3. At the top, replace [INSERT VIDEO PATH] with the file path to your video
4. If your VLC Media Player is in (x86) then add it into the $vlcPath vairable
5. Save the file

# Integration Setup Guide
1. Open Bloxstrap Menu
2. Scroll down to "Custom Integrations"
3. Click "New"
4. Set this as the Application Location: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`
5. In the Launch Arguments, add this: `powershell -ExecutionPolicy Bypass -File ` and add the Path to the .ps1 file after it
6. Click "Save"
</details>

---
<details>
<summary>Force disable OSD / Subtitle</summary>

# Configuration Steps for VLC:
1. Open VLC Media Player.
2. Go to the Tools menu at the top and select Preferences.
3. In the Preferences window, click on the Subtitles / OSD tab.
4. Uncheck the option that says Show media title on video start.
5. Click Save to apply the changes.
</details>

---

<!-- End of README -->

Once you're done with the installation, test it out and enjoy!

For any questions, please create a new [![Issue](https://img.shields.io/badge/issue-ff0000)](https://github.com/KraoESPfan1n/Loading-Screen-Bloxstrap/issues) at the top.

In the issue please explain what's happening / the issue that you're experiencing.

In the labels for your issue, please choose installation method aswell as operating system.
