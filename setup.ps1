#Requires -RunAsAdministrator

Write-Output "Setting up VLC Presence"

# Check for Python 3
if (-not([bool] (Get-Command python3))) {
    Write-Output "Python 3 not found! Exiting!"
    Pause
    exit
}

# Install all required python packages

pip install pypresence
pip install psutil
pip install pywinauto

# Register Task for Auto Startup

$create_startup = $Host.UI.PromptForChoice("Startup", "Do you want to create a startup task?", ('&Yes', '&No'), 0)
if (-not($create_startup -eq 0)) {
    Write-Host "Skipping Autostart Task!"
    exit
}

$action = New-ScheduledTaskAction -Execute "silent.vbs" -WorkingDirectory $PSScriptRoot
$trigger = New-ScheduledTaskTrigger -AtLogOn
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1) -StartWhenAvailable -ExecutionTimeLimit 0

Register-ScheduledTask -TaskName "Start VLC Presence Hidden" -TaskPath "\Custom\" -Trigger $trigger -Action $action -Settings $settings
