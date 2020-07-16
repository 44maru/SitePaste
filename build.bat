@echo off

call .venv\Scripts\activate
rem pkg_resources.py2_warn をhidden importに追加したspecファイルでbuild
pyInstaller site-paste.spec

pause
