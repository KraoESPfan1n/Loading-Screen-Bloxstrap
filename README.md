# Loading-Screen-Bloxstrap

Requirements:
- Windows 10/11
- [VLC Media Player](https://www.videolan.org/vlc/)
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

And then test it out and enjoy!
For any questions, please create a new issue.
And please explain exactly what is happening / the issue that you're experiencing, aswell as your installation method.
(Providing screenshots of the output of the PowerShell helps massively; as long as it's not just saying "True")
