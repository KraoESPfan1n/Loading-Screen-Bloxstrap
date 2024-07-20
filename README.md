# Loading-Screen-Bloxstrap

Requirements:
- Windows 10/11
- [Python for the installer](https://www.python.org/downloads/)
**only if you are using the .py version instead of the .exe**
- [VLC Media Player](https://www.videolan.org/vlc/)
- [Bloxstrap (obviously)](https://github.com/pizzaboxer/bloxstrap)
---
<!-- Extra infos for people using the installer -->


---
<!-- Manual installation guide -->
<details>
<summary>Manual installation guide</summary>
For the people that just don't like it the easy way...

# Script Setup
1. Download the "Intro.ps1" file
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

<!-- End of README -->

Once you're done with the installation, test it out and enjoy!

For any questions, please create a new issue at the top.

In the issue please explain what's happening / the issue that you're experiencing.

In the labels for your issue, please choose installation method aswell as operating system.
