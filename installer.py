import os
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import subprocess
import locale
import webbrowser
import urllib.request

# Función para obtener el idioma del sistema
def get_system_language():
    try:
        return locale.getdefaultlocale()[0]
    except:
        return 'en_US'

# Función para verificar si se necesita el argumento "powershell"
def check_powershell_execution():
    command = 'Get-ExecutionPolicy'
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        return result.returncode == 0 and result.stdout.strip()
    except subprocess.SubprocessError:
        return False

# Diccionario de traducciones
translations = {
    "en_US": {
        "title": "Loader Screen Installer",
        "welcome": "Welcome to Loader Screen Installer",
        "choose": "What would you like to do?",
        "install": "Install/Change",
        "uninstall": "Uninstall",
        "cancel": "Cancel",
        "select_video": "Select video file",
        "select_vlc": "Select VLC location",
        "install_vlc": "VLC not found. Would you like to select the VLC location or install VLC?",
        "select_or_install_vlc": "Select or Install VLC",
        "select": "Select",
        "install": "Install",
        "no_video": "No video file selected.",
        "invalid_format": "The selected video file is not in a valid format.",
        "no_vlc": "VLC not found. Please select the VLC location.",
        "installation_complete": "Installation/Change completed.",
        "uninstallation_complete": "Uninstallation completed.",
        "log_title": "Change Log",
        "bloxstrap_not_found": "Bloxstrap not found. Please install Bloxstrap.",
        "install_bloxstrap": "Install Bloxstrap"
    },
    "es_ES": {
        "title": "Instalador de Loader Screen ",
        "welcome": "Bienvenido al instalador de Loader Screen ",
        "choose": "¿Qué deseas hacer?",
        "install": "Instalar/Cambiar",
        "uninstall": "Desinstalar",
        "cancel": "Cancelar",
        "select_video": "Seleccionar archivo de video",
        "select_vlc": "Seleccionar ubicación de VLC",
        "install_vlc": "No se encontró VLC. ¿Te gustaría seleccionar la ubicación de VLC o instalar VLC?",
        "select_or_install_vlc": "Seleccionar o Instalar VLC",
        "select": "Seleccionar",
        "install": "Instalar",
        "no_video": "No se seleccionó ningún archivo de video.",
        "invalid_format": "El archivo de video seleccionado no está en un formato válido.",
        "no_vlc": "No se encontró VLC. Por favor, selecciona la ubicación de VLC.",
        "installation_complete": "Instalación/Cambio completado.",
        "uninstallation_complete": "Desinstalación completada.",
        "log_title": "Registro de Cambios",
        "bloxstrap_not_found": "No se encontró Bloxstrap. Por favor, instala Bloxstrap.",
        "install_bloxstrap": "Instalar Bloxstrap"
    }
}

# Obtener el idioma del sistema y seleccionar las traducciones
system_language = get_system_language()
if system_language.startswith("es"):
    lang = translations["es_ES"]
else:
    lang = translations["en_US"]

# Función para verificar si Bloxstrap está instalado
def verificar_bloxstrap_instalado():
    return os.path.exists(os.path.expanduser("~/AppData/Local/Bloxstrap"))

# Función para seleccionar un archivo de video
def seleccionar_video():
    return filedialog.askopenfilename(title=lang["select_video"],
                                      filetypes=[("Video files",
                                                  "*.mp4;*.avi;*.mkv;*.mov;*.wmv;*.flv;*.mpeg;*.mpg")])

# Función para encontrar la ubicación de VLC
def encontrar_vlc(log_file):
    program_files = os.environ.get("ProgramFiles")
    program_files_x86 = os.environ.get("ProgramFiles(x86)")
    
    vlc_path = os.path.join(program_files_x86, "VideoLAN", "VLC", "vlc.exe")
    if os.path.exists(vlc_path):
        log_file.write(f"[{datetime.now()}] VLC found at {vlc_path}\n")
        return vlc_path
    
    vlc_path = os.path.join(program_files, "VideoLAN", "VLC", "vlc.exe")
    if os.path.exists(vlc_path):
        log_file.write(f"[{datetime.now()}] VLC found at {vlc_path}\n")
        return vlc_path
    
    log_file.write(f"[{datetime.now()}] VLC not found\n")
    return None

# Función para seleccionar la ubicación de VLC
def seleccionar_vlc():
    return filedialog.askopenfilename(title=lang["select_vlc"])

# Función para instalar VLC usando winget
def instalar_vlc():
    command = 'winget install -e --id VideoLAN.VLC'
    try:
        subprocess.run(command, shell=True)
        messagebox.showinfo("Information", "VLC installed successfully.")
    except subprocess.SubprocessError:
        messagebox.showerror("Error", "Failed to install VLC.")

# Función para crear el script PowerShell
def crear_script_ps(video_path, vlc_path):
    video_path = video_path.replace("/", "\\")
    vlc_path = vlc_path.replace("/", "\\")
    script_content = f"""
# Path to the video you want to play
$videoPath = "{video_path}"
# Define the P/Invoke method to call user32.dll functions
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class User32 {{
    [DllImport("user32.dll")]
    public static extern IntPtr GetForegroundWindow();
    [DllImport("user32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
}}
"@
# Get the handle of the current PowerShell window
$hwnd = [User32]::GetForegroundWindow()
# Minimize the window
[User32]::ShowWindow($hwnd, 6)
# Variable to control full-screen playback
$fullscreen = $true
# VLC arguments
if ($fullscreen) {{
    $vlcArgs = "--fullscreen --play-and-exit `"$videoPath`""
}} else {{
    $vlcArgs = "--play-and-exit `"$videoPath`""
}}
# Function to check if Roblox is running
function Is-RobloxRunning {{
    $robloxProcesses = @("RobloxPlayerBeta", "RobloxStudioBeta")
    foreach ($process in $robloxProcesses) {{
        if (Get-Process -Name $process -ErrorAction SilentlyContinue) {{
            return $true
        }}
    }}
    return $false
}}
# Wait for Roblox to start
while (-not (Is-RobloxRunning)) {{
    Start-Sleep -Seconds 1
}}
# Wait a bit more to allow the window to appear
Start-Sleep -Seconds 5
# Start VLC and play the video
$vlcProcess = Start-Process -FilePath "{vlc_path}" -ArgumentList $vlcArgs -PassThru
# Wait for VLC to exit on its own (due to --play-and-exit)
$vlcProcess.WaitForExit()
# If for some reason VLC is still running, force it to close
if (Get-Process -Id $vlcProcess.Id -ErrorAction SilentlyContinue) {{
    Stop-Process -Id $vlcProcess.Id -Force
}}
"""
    return script_content

# Función para modificar el archivo Settings.json
def modificar_settings_json(video_path, log_file):
    settings_path = os.path.expanduser("~/AppData/Local/Bloxstrap/Settings.json")
    if not os.path.exists(settings_path):
        log_file.write(f"[{datetime.now()}] Settings.json not found at {settings_path}\n")
        return False
    
    powershell_arg = "powershell" if not check_powershell_execution() else ""
    
    custom_integration = {
        "Name": "Loading Screen",
        "Location": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
        "LaunchArgs": f"{powershell_arg} -ExecutionPolicy Bypass -File \"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Bloxstrap\\Modifications\\content\\launcher_roblox.ps1\"",
        "AutoClose": True
    }
    
    with open(settings_path, 'r+') as f:
        try:
            settings_data = json.load(f)
            log_file.write(f"[{datetime.now()}] Loaded Settings.json\n")
        except json.JSONDecodeError:
            settings_data = {}
            log_file.write(f"[{datetime.now()}] Settings.json is empty or corrupted, creating new structure\n")
        
        if "CustomIntegrations" in settings_data:
            # Eliminar la integración existente si la hay
            settings_data["CustomIntegrations"] = [intg for intg in settings_data["CustomIntegrations"] if intg["Name"] != "Loading Screen"]
            # Añadir la nueva integración
            settings_data["CustomIntegrations"].append(custom_integration)
        else:
            settings_data["CustomIntegrations"] = [custom_integration]
        
        f.seek(0)
        json.dump(settings_data, f, indent=4)
        f.truncate()
        
        log_file.write(f"[{datetime.now()}] Updated custom integration in Settings.json\n")
        return True

# Función para desinstalar
def desinstalar(log_file):
    script_ps_path = os.path.expanduser("~/AppData/Local/Bloxstrap/Modifications/content/launcher_roblox.ps1")
    settings_path = os.path.expanduser("~/AppData/Local/Bloxstrap/Settings.json")
    
    if os.path.exists(script_ps_path):
        os.remove(script_ps_path)
        log_file.write(f"[{datetime.now()}] Removed {script_ps_path}\n")
    else:
        log_file.write(f"[{datetime.now()}] {script_ps_path} not found\n")
    
    if os.path.exists(settings_path):
        with open(settings_path, 'r+') as f:
            settings_data = json.load(f)
            if "CustomIntegrations" in settings_data:
                settings_data["CustomIntegrations"] = []
                f.seek(0)
                json.dump(settings_data, f, indent=4)
                f.truncate()
                log_file.write(f"[{datetime.now()}] Removed CustomIntegrations from {settings_path}\n")
    else:
        log_file.write(f"[{datetime.now()}] {settings_path} not found\n")

# Función para instalar/cambiar
def instalar_cambiar(video_path, vlc_path, log_file):
    script_ps_path = os.path.expanduser("~/AppData/Local/Bloxstrap/Modifications/content/launcher_roblox.ps1")
    
    script_ps_content = crear_script_ps(video_path, vlc_path)
    with open(script_ps_path, 'w') as f:
        f.write(script_ps_content)
    log_file.write(f"[{datetime.now()}] Created {script_ps_path}\n")
    
    if modificar_settings_json(video_path, log_file):
        log_file.write(f"[{datetime.now()}] Modified Settings.json\n")
    else:
        log_file.write(f"[{datetime.now()}] Settings.json already contains the integration or couldn't be modified\n")

# Descargar y guardar el logo de Bloxstrap
def descargar_logo(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
    except Exception as e:
        print(f"Error downloading logo: {e}")

# Clase para la interfaz gráfica
class InstallerGUI:
    def __init__(self, master):
        self.master = master
        master.title(lang["title"])
        master.geometry("400x300")

        # Descargar el logo de Bloxstrap
        logo_url = "https://raw.githubusercontent.com/pizzaboxer/bloxstrap/main/Images/Bloxstrap.png"
        logo_path = os.path.expanduser("~/AppData/Local/Bloxstrap/Bloxstrap.png")
        descargar_logo(logo_url, logo_path)
        
        try:
            master.iconphoto(True, tk.PhotoImage(file=logo_path))
        except Exception as e:
            print(f"Error setting icon: {e}")
        
        style = ttk.Style()
        style.theme_use('clam')
        
        self.label = ttk.Label(master, text=lang["welcome"], font=("Helvetica", 14))
        self.label.pack(pady=20)
        
        self.choose_label = ttk.Label(master, text=lang["choose"])
        self.choose_label.pack()
        
        self.install_button = ttk.Button(master, text=lang["install"], command=self.install)
        self.install_button.pack(pady=10)
        
        self.uninstall_button = ttk.Button(master, text=lang["uninstall"], command=self.uninstall)
        self.uninstall_button.pack(pady=10)
        
        self.cancel_button = ttk.Button(master, text=lang["cancel"], command=self.cancel)
        self.cancel_button.pack(pady=10)
        
        self.log_file_path = os.path.expanduser("~/AppData/Local/Bloxstrap/install_log.txt")
        
        # Limpiar el archivo de logs si ya existe
        with open(self.log_file_path, 'w') as log_file:
            log_file.write(f"[{datetime.now()}] Log file created/cleaned\n")
        
        self.log_file = open(self.log_file_path, 'a')
        
        if not verificar_bloxstrap_instalado():
            messagebox.showinfo("Information", lang["bloxstrap_not_found"])
            self.log_file.write(f"[{datetime.now()}] Bloxstrap not found\n")
            webbrowser.open("https://github.com/pizzaboxer/bloxstrap")
            return

    def install(self):
        self.log_file.write(f"[{datetime.now()}] Installation process started\n")
        video_path = seleccionar_video()
        if not video_path:
            self.log_file.write(f"[{datetime.now()}] No video file selected\n")
            messagebox.showerror("Error", lang["no_video"])
            return
        
        video_path = video_path.replace("/", "\\")
        self.log_file.write(f"[{datetime.now()}] Video file selected: {video_path}\n")
        
        allowed_formats = ["mp4", "avi", "mkv", "mov", "wmv", "flv", "mpeg", "mpg"]
        if not any(video_path.lower().endswith(fmt) for fmt in allowed_formats):
            self.log_file.write(f"[{datetime.now()}] Invalid video format\n")
            messagebox.showerror("Error", lang["invalid_format"])
            return
        
        vlc_path = encontrar_vlc(self.log_file)
        if not vlc_path:
            self.log_file.write(f"[{datetime.now()}] VLC not found automatically\n")
            if messagebox.askyesno(lang["select_or_install_vlc"], lang["install_vlc"]):
                self.log_file.write(f"[{datetime.now()}] User chose to install VLC\n")
                instalar_vlc()
                vlc_path = encontrar_vlc(self.log_file)
                if not vlc_path:
                    self.log_file.write(f"[{datetime.now()}] VLC installation failed\n")
                    messagebox.showerror("Error", lang["no_vlc"])
                    return
            else:
                vlc_path = seleccionar_vlc()
                if not vlc_path:
                    self.log_file.write(f"[{datetime.now()}] VLC not selected manually\n")
                    messagebox.showerror("Error", lang["no_vlc"])
                    return
        
        vlc_path = vlc_path.replace("/", "\\")
        self.log_file.write(f"[{datetime.now()}] VLC path: {vlc_path}\n")
        
        instalar_cambiar(video_path, vlc_path, self.log_file)
        messagebox.showinfo("Information", lang["installation_complete"])
        self.show_logs()
    
    def uninstall(self):
        self.log_file.write(f"[{datetime.now()}] Uninstallation process started\n")
        desinstalar(self.log_file)
        messagebox.showinfo("Information", lang["uninstallation_complete"])
        self.show_logs()
    
    def cancel(self):
        self.log_file.write(f"[{datetime.now()}] Operation cancelled\n")
        self.show_logs()
    
    def show_logs(self):
        self.log_file.close()
        with open(self.log_file_path, 'r') as log_file:
            log_content = log_file.read()
        
        log_window = tk.Toplevel(self.master)
        log_window.title(lang["log_title"])
        log_text = tk.Text(log_window, wrap=tk.WORD)
        log_text.insert(tk.END, log_content)
        log_text.pack(expand=True, fill=tk.BOTH)
        
        def on_closing():
            log_window.destroy()
            self.master.quit()
        
        log_window.protocol("WM_DELETE_WINDOW", on_closing)

def main():
    root = tk.Tk()
    app = InstallerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
