$desktop = [Environment]::GetFolderPath('Desktop')
$ws = New-Object -ComObject WScript.Shell
$root = 'F:\interview helper\interview-copilot'

$lnk = $ws.CreateShortcut("$desktop\Interview Copilot.lnk")
$lnk.TargetPath = "$root\.venv\Scripts\pythonw.exe"
$lnk.Arguments = 'server.py'
$lnk.WorkingDirectory = $root
$lnk.IconLocation = "$root\assets\icon.ico"
$lnk.Description = '面试实时提词助手'
$lnk.Save()

$lnk2 = $ws.CreateShortcut("$desktop\Interview Copilot 停止.lnk")
$lnk2.TargetPath = "$root\停止.bat"
$lnk2.WorkingDirectory = $root
$lnk2.IconLocation = "$root\assets\icon.ico"
$lnk2.Description = '停止面试提词助手服务'
$lnk2.Save()

Write-Output "created at $desktop"
