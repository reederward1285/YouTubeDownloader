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

        self.retranslateUi(YouTubeDownloader)
        QtCore.QMetaObject.connectSlotsByName(YouTubeDownloader)

    def retranslateUi(self, YouTubeDownloader):
        _translate = QtCore.QCoreApplication.translate
        YouTubeDownloader.setWindowTitle(_translate("YouTubeDownloader", "YouTubeDownloader"))
        self.label.setText(_translate("YouTubeDownloader", "Put your youtube link here:"))
        self.pushButton.setText(_translate("YouTubeDownloader", "Download"))

        self.pushButton.adjustSize()
        self.pushButton.clicked.connect(self.downloadVideos)
        self.label.adjustSize()

    def downloadVideos(self):
        root = tk.Tk()
        root.withdraw()
        file = filedialog.askdirectory()
        youtube_link = self.textEdit.text()
        copy_file = "move *.mp4 " + file        
        copy_file = copy_file.replace("/", "\\")

        print(copy_file)

        commands = ["cd " + file, "youtube-dl.exe " + youtube_link, copy_file, "start " + file]
        
        for item in commands:
            print(item)
            os.system(item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YouTubeDownloader = QtWidgets.QWidget()
    ui = Ui_YouTubeDownloader()
    ui.setupUi(YouTubeDownloader)
    YouTubeDownloader.show()
    sys.exit(app.exec_())
