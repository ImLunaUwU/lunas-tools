taskkill /im "Spotify.exe" /f
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe "iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 | iex"
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe "iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-marketplace/main/resources/install.ps1 | iex"
start "" "%appdata%\Spotify\Spotify.exe"
exit