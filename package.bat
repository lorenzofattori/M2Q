python -m unittest discover -s .\test\ && ^
pyinstaller m2q.py --onefile --icon=m2q.ico --add-data "m2q.ico;." --add-data "m2q-logo-v2.png;." --add-data "m2q-logo-v2-text.png;."