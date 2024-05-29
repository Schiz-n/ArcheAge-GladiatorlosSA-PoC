# File: tail-log.ps1
$path = "C:\Users\<name>\Documents\ArcheRage\Combat.log"
Get-Content -Path $path -Tail 10 -Wait
