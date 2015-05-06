@echo off

REM  Realizado por @rjotac

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f

ipconfig /flushdns

ipconfig /release

ipconfig /renew

netsh interface ipv4 set address name="ethernet" static 172.22.20.33 255.255.255.192 172.22.20.60 store=persistent

netsh interface ipv4 set dnsservers name="ethernet"  source=static address="172.22.20.60" validate=no

mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' ); sh.Popup( 'Cambios Realizados Con Éxito!', 10, 'Servicios Computacionales', 64 );close()"

exit