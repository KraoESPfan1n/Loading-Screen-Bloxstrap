<blockquote class="imgur-embed-pub" lang="en" data-id="a/7YCKxBG" data-context="false" ><a href="//imgur.com/a/7YCKxBG"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
# Loading-Screen-Bloxstrap

Requirements:
- Windows 10/11
- [Python V3.x for the installer](https://www.python.org/downloads/)
- [VLC Media Player](https://www.videolan.org/vlc/)
- [Bloxstrap (obviously)](https://github.com/pizzaboxer/bloxstrap)
---
<details>
<summary>Python Installer User Guide</summary>

## Required Libraries

Before running the script, ensure you have the necessary libraries installed. Use the following command to install them if they are not already available:

```
pip install pillow
```

## Steps to use `installer.py`

### Preparation

- Ensure you have the `installer.py` file on your computer.- Have a video file ready that you want to use as a loading screen.

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
