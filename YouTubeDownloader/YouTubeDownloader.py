from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import tkinter as tk
from tkinter import filedialog

class Ui_YouTubeDownloader(object):

    def setupUi(self, YouTubeDownloader):
        YouTubeDownloader.setObjectName("YouTubeDownloader")
        YouTubeDownloader.resize(800, 600)
        self.textEdit = QtWidgets.QLineEdit(YouTubeDownloader)
        self.textEdit.setGeometry(QtCore.QRect(50, 70, 500, 60))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(YouTubeDownloader)
        self.label.setGeometry(QtCore.QRect(50, 20, 261, 22))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(YouTubeDownloader)
        self.pushButton.setGeometry(QtCore.QRect(60, 250, 121, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton1 = QtWidgets.QPushButton(YouTubeDownloader)
        self.pushButton1.setGeometry(QtCore.QRect(200, 500, 400, 30))
        self.pushButton1.setObjectName("pushButton1")

        self.retranslateUi(YouTubeDownloader)
        QtCore.QMetaObject.connectSlotsByName(YouTubeDownloader)

    def retranslateUi(self, YouTubeDownloader):
        _translate = QtCore.QCoreApplication.translate
        YouTubeDownloader.setWindowTitle(_translate("YouTubeDownloader", "YouTubeDownloader"))
        self.label.setText(_translate("YouTubeDownloader", "Put your youtube link here:"))
        self.pushButton.setText(_translate("YouTubeDownloader", "Add"))
        self.pushButton1.setText(_translate("YouTubeDownloader", "Download"))

        self.pushButton.adjustSize()
        self.pushButton.clicked.connect(self.add)
        self.pushButton1.adjustSize()
        self.pushButton1.clicked.connect(self.downloadVideos)
        self.label.adjustSize()

    # add a new video/playlist to links and folders queue
    def add(self):
        # exit if no video link is there
        if (len(self.textEdit.text()) == 0):
            return

        root = tk.Tk()
        root.withdraw()

        # file dialog for dir to save video(s)
        destinationDir = filedialog.askdirectory()
        # fix the dir string so it can be used on command line later
        destinationDir = destinationDir.replace("/", "\\")

        # make cmd string for copying the video file(s) to dest dir
        copy_file = "move *.mp4 " + destinationDir

        # add commands for downloading the youtube video and copying
        # it to dest dir to links.txt file
        youTubeLinkFile = open("links.txt", "a")
        youTubeLinkFile.write("youtube-dl.exe " + self.textEdit.text() + "\n")
        youTubeLinkFile.write(copy_file + "\n")
        youTubeLinkFile.close()

        youTubeFolderFile = open("folders.txt", "a")
        youTubeFolderFile.write("start " + destinationDir + "\n")
        youTubeFolderFile.close()

        self.textEdit.clear()

    def downloadVideos(self):
        with open("links.txt") as file:
            commands = file.readlines()
            commands = [line.rstrip() for line in commands]
            for item in commands:
                print(item)
                os.system(item)
        with open("folders.txt") as file:
            commands = file.readlines()
            commands = [line.rstrip() for line in commands]
            for item in commands:
                print(item)
                os.system(item)

        os.remove("links.txt")
        os.remove("folders.txt")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YouTubeDownloader = QtWidgets.QWidget()
    ui = Ui_YouTubeDownloader()
    ui.setupUi(YouTubeDownloader)
    YouTubeDownloader.show()
    sys.exit(app.exec_())
