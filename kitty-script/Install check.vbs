Option Explicit
Dim fso 
Set fso = CreateObject("Scripting.FileSystemObject")
If fso.FileExists("C:\Users\HP\AppData\Local\Programs\Python\Python310\python.exe") Then 
wscript.echo "you have python installed so you can run the code!"
Else
wscript.echo "Sorry you can't run the code yet you need to install python visit python.org to download"
End If