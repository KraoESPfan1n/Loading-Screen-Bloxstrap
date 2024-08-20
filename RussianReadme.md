<p align="center">
    <img src="https://i.ibb.co/bgsKbPF/image.png" width="640" height="360">
</p>

[![Лицензия](https://img.shields.io/badge/License-MIT-lime)](./LICENSE)
[![Версия](https://img.shields.io/badge/Version-1.0-purple)](https://github.com/KraoESPfan1n/Loading-Screen-Bloxstrap/releases/tag/Release)
[![Кража интеллектуальной собственности](https://img.shields.io/badge/Based_on-Bloxstrap-591ac7)](https://github.com/pizzaboxer/bloxstrap)
[![Discord](https://img.shields.io/badge/Discord-Original_thread-blue)](https://discord.com/channels/1099468797410283540/1260503953234329662)
[![Автор](https://img.shields.io/badge/Author-Krao-darkblue)](https://github.com/KraoESPfan1n)
[![Участник](https://img.shields.io/badge/Contributor-HxLL-darkred)](https://github.com/hxll-f)
[![Дополнительно](https://img.shields.io/badge/I_am-_very_tired-black)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

# Loading-Screen-Bloxstrap

Требования:
- Windows 10/11
- [PowerShell](https://docs.microsoft.com/en-us/powershell/) (обычно поставляется по умолчанию на Windows)
- [Python V3.x для установщика](https://www.python.org/downloads/)
- [VLC Media Player](https://www.videolan.org/vlc/)
- [Bloxstrap (очевидно)](https://github.com/pizzaboxer/bloxstrap)


[![Windows 11](https://img.shields.io/badge/Windows-11-blue)](https://www.microsoft.com/en-us/software-download/windows10)
[![Windows 10](https://img.shields.io/badge/Windows-10-blue)](https://www.microsoft.com/software-download/windows11)
[![PowerShell](https://img.shields.io/badge/PowerShell-latest-blue)](https://docs.microsoft.com/en-us/powershell/)
[![Python](https://img.shields.io/badge/Python-latest-Yellow)](https://www.python.org/downloads/)
[![VLC](https://img.shields.io/badge/VLC-latest-orange)](https://www.videolan.org/vlc/index.html)
[![Bloxstrap](https://img.shields.io/badge/Bloxtrap-latest-591ac7)](https://github.com/pizzaboxer/bloxstrap)
---
> [!WARNING]
> Кнопка удаления НЕ удалит Python, VLC, PowerShell, Bloxstrap, она только удалит мод.
<details>
<summary>Руководство пользователя установщика Python</summary>
    
## Необходимые библиотеки

Перед запуском скрипта убедитесь, что у вас установлены необходимые библиотеки. Используйте следующую команду для их установки, если они ещё не установлены:


```
pip install pillow
```

[![Pillow](https://img.shields.io/badge/Pillow-latest-Yellow)](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)

## Шаги для использования `installer.py`

### Подготовка

- Убедитесь, что у вас есть файл [![Installer](https://img.shields.io/badge/installer.py-e6c912)](https://github.com/KraoESPfan1n/Loading-Screen-Bloxstrap/releases/tag/Release) на вашем компьютере.
- Подготовьте видеофайл, который вы хотите использовать в качестве экрана загрузки.

### Запуск скрипта

1. Откройте терминал или командную строку.
2. Перейдите в каталог, где находится `installer.py`.
3. Запустите скрипт командой:
    ```bash
    python installer.py
    ```

### Установка или изменение экрана загрузки

1. Нажмите на **Установить/Изменить**.
2. Выберите видеофайл, который вы хотите использовать в качестве экрана загрузки.
3. Если VLC не найден, вам будет предложено установить его или вручную выбрать его расположение.

### Просмотр журналов

1. После каждой операции будет отображаться окно с журналами установки.
2. Ознакомьтесь с этой информацией, чтобы убедиться, что всё выполнено правильно.

## Дополнительные примечания

- Скрипт в настоящее время поддерживает английский, испанский и немецкий языки.
- Если вы столкнулись с какими-либо проблемами, проверьте журналы для получения дополнительной информации о возможных причинах.
- Любую ошибку, которую вы видите в консоли, можно сообщить в репозиторий.

</details>

---
<!-- Руководство по ручной установке -->
<details>
<summary>Руководство по ручной установке</summary>
Для тех, кто предпочитает делать всё по-своему...

# Настройка скрипта
1. Скачайте файл [![intro](https://img.shields.io/badge/intro.ps1-7b36c9)](https://github.com/KraoESPfan1n/Loading-Screen-Bloxstrap/releases/tag/Release)
2. Откройте его в текстовом редакторе по вашему выбору
3. Вверху замените [INSERT VIDEO PATH] на путь к вашему видеофайлу
4. Если ваш VLC Media Player находится в (x86), добавьте его в переменную $vlcPath
5. Сохраните файл

# Руководство по настройке интеграции
1. Откройте меню Bloxstrap
2. Прокрутите вниз до "Пользовательские интеграции"
3. Нажмите "Новое"
4. Установите это как расположение приложения: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`
5. В аргументы запуска добавьте следующее: `powershell -ExecutionPolicy Bypass -File ` и добавьте путь к .ps1 файлу после этого
6. Нажмите "Сохранить"
</details>

---
<details>
<summary>Принудительное отключение OSD / субтитров</summary>

# Шаги по настройке VLC:
1. Откройте VLC Media Player.
2. Перейдите в меню "Инструменты" наверху и выберите "Настройки".
3. В окне настроек нажмите на вкладку "Субтитры / OSD".
4. Снимите галочку с опции "Показывать название медиа на старте видео".
5. Нажмите "Сохранить" для применения изменений.
</details>

---

<!-- Конец README -->

После завершения установки протестируйте и наслаждайтесь!

Если у вас возникли вопросы, создайте новый [![Issue](https://img.shields.io/badge/issue-ff0000)](https://github.com/KraoESPfan1n/Loading-Screen-Bloxstrap/issues) наверху.

В вашем вопросе, пожалуйста, объясните, что происходит / какая проблема возникла.

В метках для вашего вопроса выберите метод установки, а также операционную систему.
