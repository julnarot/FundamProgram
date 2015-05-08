@echo off

REM  Realizado por @rjotac


reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f

set SUBKEY=Software\Microsoft\Windows\CurrentVersion\Internet Settings

reg delete "HKCU\%SUBKEY%\Connections" /f
reg add    "HKCU\%SUBKEY%" /f /v MigrateProxy /t REG_DWORD /d 0x1
reg add    "HKCU\%SUBKEY%" /f /v ProxyEnable /t REG_DWORD /d 0x0
reg delete "HKCU\%SUBKEY%" /f /v ProxyServer
reg delete "HKCU\%SUBKEY%" /f /v ProxyOverride


ipconfig /flushdns

ipconfig /release

ipconfig /renew

netsh interface ipv4 set address name="ethernet" source=dhcp

netsh interface ipv4 set dnsservers name="ethernet" source=dhcp

mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' ); sh.Popup( 'Cambios Realizados Con Exito!', 10, 'Servicios Computacionales', 64 );close()"

exit