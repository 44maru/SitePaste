@echo off

call .venv\Scripts\activate
rem pkg_resources.py2_warn をhidden importに追加したspecファイルでbuild
pyInstaller --onefile --noconsole site-paste.spec

pause
