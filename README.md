# Loading-Screen-Bloxstrap

Requirements:
- Windows 10/11
- [Python V3.x for the installer](https://www.python.org/downloads/)
**only if you gona use the installer**
- [VLC Media Player](https://www.videolan.org/vlc/)
- [Bloxstrap (obviously)](https://github.com/pizzaboxer/bloxstrap)
---
<details>
<summary>Loader Screen Python Installer - User Guide</summary>

Steps to use installer.py

1. **Preparation**
   - Make sure you have the `installer.py` file on your computer.
   - Have a video file ready that you want to use as a loading screen.

2. **Running the script**
   - Open a terminal or command prompt.
   - Navigate to the directory where `installer.py` is located.
   - Run the script with the command:
     ```
     python installer.py
     ```

3. **Using the graphical interface**
   - A window titled "Loader Screen Installer" will open.
   - You'll see three main options:
     - Install/Change
     - Uninstall
     - Cancel

4. **Installing or changing the loading screen**
   - Click on "Install/Change".
   - Select the video file you want to use as a loading screen.
   - If VLC is not installed, you'll be given the option to install it or manually select its location.

5. **Uninstalling the loading screen**
   - If you want to remove the custom loading screen, click on "Uninstall".

6. **Canceling the operation**
   - If you decide not to perform any action, you can click on "Cancel" or close the window.

7. **Reviewing the logs**
   - After each operation, a window with the installation logs will be displayed.
   - Review this information to ensure everything has been done correctly.

8. **Finishing**
   - Close the log window to end the process.

## Additional notes

- The script will automatically detect your system language and display the interface in English or Spanish accordingly.
- If you encounter any issues, check the logs for more information about what might have gone wrong.
- Any error that the console presents, you can report in the repository
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
