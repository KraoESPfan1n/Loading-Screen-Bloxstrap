# Path to the video you want to play
$videoPath = "[INSERT VIDEO PATH]"
$vlcPath = "C:\Program Files\VideoLAN\VLC\vlc.exe"

# Define the P/Invoke method to call user32.dll functions
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class User32 {
    [DllImport("user32.dll")]
    public static extern IntPtr GetForegroundWindow();

    [DllImport("user32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
}
"@

#  _______      _________      _____       ______     _
# / _____ \    |____ ____|    / ___ \     | ____ \   | |
#/ /     \_\       | |       / /   \ \    | |   \ \  | |
#| |               | |      / /     \ \   | |   | |  | |
#\ \______         | |      | |     | |   | |___/ /  | |
# \______ \        | |      | |     | |   |  ____/   | |
#        \ \       | |      | |     | |   | |        | |
# _      | |       | |      \ \     / /   | |        |_|
#\ \_____/ /       | |       \ \___/ /    | |         _
# \_______/        |_|        \_____/     |_|        |_|

# Stop!
# If someone instructed you to edit this code with another, it is not advisable to do so.
# Please do not edit the code unless you are certain of what you are doing. 
# If you need something in the code to be modified, please inform the creators.

# Get the handle of the current PowerShell window
$hwnd = [User32]::GetForegroundWindow()

# Minimize the window
[User32]::ShowWindow($hwnd, 6)

# Variable to control full-screen playback
$fullscreen = $true

# VLC arguments
if ($fullscreen) {
    $vlcArgs = "--fullscreen --play-and-exit --no-osd `"$videoPath`""
} else {
    $vlcArgs = "--play-and-exit --no-osd `"$videoPath`""
}

# Function to check if Roblox is running
function Is-RobloxRunning {
    $robloxProcesses = @("RobloxPlayerBeta", "RobloxStudioBeta")
    foreach ($process in $robloxProcesses) {
        if (Get-Process -Name $process -ErrorAction SilentlyContinue) {
            return $true
        }
    }
    return $false
}

# Wait for Roblox to start
while (-not (Is-RobloxRunning)) {
    Start-Sleep -Seconds 1
}

# Wait a bit more to allow the window to appear
Start-Sleep -Seconds 5

# Start VLC and play the video
$vlcProcess = Start-Process -FilePath $vlcPath -ArgumentList $vlcArgs -PassThru

# Wait for VLC to exit on its own (due to --play-and-exit)
$vlcProcess.WaitForExit()

# If for some reason VLC is still running, force it to close
if (Get-Process -Id $vlcProcess.Id -ErrorAction SilentlyContinue) {
    Stop-Process -Id $vlcProcess.Id -Force
}
