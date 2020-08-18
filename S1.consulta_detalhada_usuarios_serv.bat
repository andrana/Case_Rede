cd "%~dp0"
@echo on

cd /d C:
del *.txt
cd ..
for /F "eol=; skip=1 tokens=1 delims=," %%a in (nome_arquivo.txt) do net user %%a /domain |findstr "Nome ativa logon * Coment rio "> resultado\%%a.txt 
pause