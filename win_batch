::stay alive batch 
::author bn.
@ECHO OFF
::ipaddress = destination host
set IP=0.0.0.0
::interval = time in seconds
set INTERVAL=10
:MAIN
	ping -n 1 %IP% | find "TTL=" > nul
	if errorlevel 1 echo %date%;%time% >> log.csv
	timeout %INTERVAL%
GOTO MAIN
