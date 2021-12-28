:: install python
cd src
python-3.9.5-amd64.exe /passive InstallAllUsers=1 PrependPath=1 Include_test=0

:: install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
python -m pip install --upgrade pip

:: install youtube downloader
pip install youtube_dl pyqt5

:: install tkinter
pip install tk

:: run the program
python3 YouTubeDownloader/YouTubeDownloader.py