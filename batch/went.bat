@echo off
title DHCP-Automatico / Desactivar-PROXY
::Programa Script para Desactivar proxy-> IE ; y restaura confoguracion de IPV4
REM  Realizado por @rjotac

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f

ipconfig /flushdns

ipconfig /release

ipconfig /renew

netsh interface ipv4 set address name="ethernet" source=dhcp

netsh interface ipv4 set dnsservers name="ethernet" source=dhcp

mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' ); sh.Popup( 'Cambios Realizados Con Éxito!', 10, 'Servicios Computacionales', 64 );close()"

exit
