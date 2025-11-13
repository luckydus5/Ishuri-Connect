# Run Ishuri Connect (PowerShell)
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir
& .\ishuri\Scripts\python.exe main.py
