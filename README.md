# ArcheAge-GladiatorlosSA-PoC
A proof of concept implementation of WoW's GladiatorlosSA in Arche(R)age. It listens to the combat log and plays audio when certain skills appear. All hardcoded garbage right now but it's just a proof of concept to show this is possible without modding your gamefiles.

Install dependencies then run python combatlistener.py

tail_combatlog.ps1 functions as a "tails" implementation to view the combat log in powershell, to run this just do ./tail_combatlog.ps1 in powershell.