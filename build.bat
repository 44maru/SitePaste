@echo off

call .venv\Scripts\activate
pyInstaller --onefile --noconsole site-paste.py

pause
