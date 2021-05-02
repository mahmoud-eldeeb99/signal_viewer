from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import pyqtgraph.exporters   #for taking image then take an pdf
import numpy as np  #has method call genformatics to read data from feiil
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from pyqtgraph import PlotWidget ,PlotItem
import pyqtgraph as pg   #for css and row major
import os   #for remove and copy directory 
import shutil #for remove and copy directory 
import pathlib
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fftshift
from fpdf import FPDF
from PDF import PDF



class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(978, 683)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 10, 551, 43))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        font = QtGui.QFont()
        font.setPointSize(20)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("clear_left.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font = QtGui.QFont()
        font.setPointSize(20)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("p.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font = QtGui.QFont()
        font.setPointSize(20)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("t.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 75, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 100, 951, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView = PlotWidget(self.layoutWidget1)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.graphicsView.setFont(font)
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.graphicsView_4 = PlotWidget(self.layoutWidget1)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.graphicsView_4.setFont(font)
        self.graphicsView_4.setMouseTracking(False)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.horizontalLayout_2.addWidget(self.graphicsView_4)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 280, 951, 141))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graphicsView_2 = PlotWidget(self.layoutWidget2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_3.addWidget(self.graphicsView_2)
        self.graphicsView_5 = PlotWidget(self.layoutWidget2)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.graphicsView_5.setFont(font)
        self.graphicsView_5.setMouseTracking(False)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.horizontalLayout_3.addWidget(self.graphicsView_5)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 460, 951, 141))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graphicsView_3 = PlotWidget(self.layoutWidget3)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.graphicsView_3.setFont(font)
        self.graphicsView_3.setMouseTracking(False)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_4.addWidget(self.graphicsView_3)
        self.graphicsView_6 = PlotWidget(self.layoutWidget3)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.horizontalLayout_4.addWidget(self.graphicsView_6)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 250, 479, 28))
        self.widget.setObjectName("widget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.p1 = QtWidgets.QPushButton(self.widget)
        self.p1.setText("")
        self.p1.setIcon(icon1)
        self.p1.setObjectName("p1")
        self.horizontalLayout_5.addWidget(self.p1)
        self.r1 = QtWidgets.QPushButton(self.widget)
        self.r1.setText("")
        self.r1.setIcon(icon2)
        self.r1.setObjectName("r1")
        self.horizontalLayout_5.addWidget(self.r1)
        self.zz1 = QtWidgets.QPushButton(self.widget)
        self.zz1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("zz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zz1.setIcon(icon3)
        self.zz1.setObjectName("zz1")
        self.horizontalLayout_5.addWidget(self.zz1)
        self.z1 = QtWidgets.QPushButton(self.widget)
        self.z1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("z.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.z1.setIcon(icon4)
        self.z1.setObjectName("z1")
        self.horizontalLayout_5.addWidget(self.z1)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)
        self.print1 = QtWidgets.QPushButton(self.widget)
        self.print1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print1.setIcon(icon5)
        self.print1.setObjectName("print1")
        self.horizontalLayout_8.addWidget(self.print1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 430, 459, 28))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.p2 = QtWidgets.QPushButton(self.widget1)
        self.p2.setText("")
        self.p2.setIcon(icon1)
        self.p2.setObjectName("p2")
        self.horizontalLayout_6.addWidget(self.p2)
        self.r2 = QtWidgets.QPushButton(self.widget1)
        self.r2.setText("")
        self.r2.setIcon(icon2)
        self.r2.setObjectName("r2")
        self.horizontalLayout_6.addWidget(self.r2)
        self.zz2 = QtWidgets.QPushButton(self.widget1)
        self.zz2.setText("")
        self.zz2.setIcon(icon3)
        self.zz2.setObjectName("zz2")
        self.horizontalLayout_6.addWidget(self.zz2)
        self.z2 = QtWidgets.QPushButton(self.widget1)
        self.z2.setText("")
        self.z2.setIcon(icon4)
        self.z2.setObjectName("z2")
        self.horizontalLayout_6.addWidget(self.z2)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.print2 = QtWidgets.QPushButton(self.widget1)
        self.print2.setText("")
        self.print2.setIcon(icon5)
        self.print2.setObjectName("print2")
        self.horizontalLayout_9.addWidget(self.print2)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 610, 459, 28))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.p3 = QtWidgets.QPushButton(self.widget2)
        self.p3.setText("")
        self.p3.setIcon(icon1)
        self.p3.setObjectName("p3")
        self.horizontalLayout_7.addWidget(self.p3)
        self.r3 = QtWidgets.QPushButton(self.widget2)
        self.r3.setText("")
        self.r3.setIcon(icon2)
        self.r3.setObjectName("r3")
        self.horizontalLayout_7.addWidget(self.r3)
        self.zz3 = QtWidgets.QPushButton(self.widget2)
        self.zz3.setText("")
        self.zz3.setIcon(icon3)
        self.zz3.setObjectName("zz3")
        self.horizontalLayout_7.addWidget(self.zz3)
        self.z3 = QtWidgets.QPushButton(self.widget2)
        self.z3.setText("")
        self.z3.setIcon(icon4)
        self.z3.setObjectName("z3")
        self.horizontalLayout_7.addWidget(self.z3)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)
        self.print3 = QtWidgets.QPushButton(self.widget2)
        self.print3.setText("")
        self.print3.setIcon(icon5)
        self.print3.setObjectName("print3")
        self.horizontalLayout_10.addWidget(self.print3)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 21))
        self.menubar.setObjectName("menubar")
        self.menuchannel1 = QtWidgets.QMenu(self.menubar)
        self.menuchannel1.setObjectName("menuchannel1")
        self.menuchannel2 = QtWidgets.QMenu(self.menubar)
        self.menuchannel2.setObjectName("menuchannel2")
        self.menuchanell3 = QtWidgets.QMenu(self.menubar)
        self.menuchanell3.setObjectName("menuchanell3")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionadd_signal = QtWidgets.QAction(mainWindow)
        self.actionadd_signal.setObjectName("actionadd_signal")
        self.actionadd_signal_2 = QtWidgets.QAction(mainWindow)
        self.actionadd_signal_2.setObjectName("actionadd_signal_2")
        self.actionadd_signal_3 = QtWidgets.QAction(mainWindow)
        self.actionadd_signal_3.setObjectName("actionadd_signal_3")
        self.menuchannel1.addAction(self.actionadd_signal)
        self.menuchannel2.addAction(self.actionadd_signal_2)
        self.menuchanell3.addAction(self.actionadd_signal_3)
        self.menubar.addAction(self.menuchannel1.menuAction())
        self.menubar.addAction(self.menuchannel2.menuAction())
        self.menubar.addAction(self.menuchanell3.menuAction())




        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

 #<<<<<<<<<<<<<<<<     ### funcarions    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

        # creating timers
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timer3 = QtCore.QTimer()

        # actions
        self.actionadd_signal.triggered.connect(lambda: self.load_data_of_channel_1())
        self.actionadd_signal_2.triggered.connect(lambda: self.load_data_of_channel_2())
        self.actionadd_signal_3.triggered.connect(lambda: self.load_data_of_channel_3())
        self.p1.clicked.connect(lambda: self.pause_channel_1())
        self.r1.clicked.connect(lambda: self.resume_channel_1())
        self.p2.clicked.connect(lambda: self.pause_channel_2())
        self.r2.clicked.connect(lambda: self.resume_channel_2())
        self.p3.clicked.connect(lambda: self.pause_channel_3())
        self.r3.clicked.connect(lambda: self.resume_channel_3())
        self.zz1.clicked.connect(lambda: self.zoomin_channel_1())
        self.z1.clicked.connect(lambda: self.zoomout_channel_1())
        self.zz2.clicked.connect(lambda: self.resume_channel_2())
        self.z2.clicked.connect(lambda: self.zoomout_channel_2())
        self.zz3.clicked.connect(lambda: self.resume_channel_3())
        self.z3.clicked.connect(lambda: self.zoomout_channel_3())
        self.print1.clicked.connect(lambda: self.create_pdf_for_signal_1())
        self.print2.clicked.connect(lambda: self.create_pdf_for_signal_2())
        self.print3.clicked.connect(lambda: self.create_pdf_for_signal_3())

 #>>>>>>>>>>>>>>>>>>>>>>       ##### pausing



    def pause_channel_1(self):
        self.timer1.stop()

    def pause_channel_2(self):
        self.timer2.stop()

    def pause_channel_3(self):
        self.timer3.stop()

 #>>>>>>>>>>>>>>>       ##### reasuming



    def resume_channel_1(self):
        self.timer1.start()

    def resume_channel_2(self):
        self.timer2.start()

    def resume_channel_3(self):
        self.timer3.start()

 #>>>>>>>>>>>>>>>>       ######## zooming

    def zoomin_channel_1(self):
        self.graphicsView.plotItem.getViewBox().scaleBy((.5, .5))

    def zoomout_channel_1(self):
        self.graphicsView.plotItem.getViewBox().scaleBy((2, 2))

    def zoomin_channel_2(self):
        self.graphicsView_2.plotItem.getViewBox().scaleBy((.5, .5))

    def zoomout_channel_2(self):
        self.graphicsView_2.plotItem.getViewBox().scaleBy((2, 2))

    def zoomin_channel_3(self):
        self.graphicsView_3.plotItem.getViewBox().scaleBy((.5, .5))

    def zoomout_channel_3(self):
        self.graphicsView_3.plotItem.getViewBox().scaleBy((2, 2))

 #>>>>>>>>>>>>>>>>       #### clearing



 #>>>>>>>>>>>>>>>>       ##### reading files

    def read_file1(self):
        self.fname1 = QtGui.QFileDialog.getOpenFileName(None, 'Open only txt or CSV or xls', os.getenv('HOME'),
                                                        "csv(*.csv);; text(*.txt) ;; xls(*.xls)")
        path = self.fname1[0]
        # self.name1= self.fname1


        elif pathlib.Path(path).suffix == ".csv":
            self.data1 = np.genfromtxt(path, delimiter=',')
            self.time_of_signal_1 = self.data1[:, 0]
            self.amplitude_of_signal_1 = self.data1[:, 1]
            self.time_of_signal_1 = list(self.time_of_signal_1[:])
            self.amplitude_of_signal_1 = list(self.amplitude_of_signal_1[:])



    def read_file2(self):
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open only txt or CSV or xls', os.getenv('HOME'),
                                                  "csv(*.csv);; text(*.txt) ;; xls(*.xls)")
        path = fname[0]


        elif pathlib.Path(path).suffix == ".csv":
            self.data2 = np.genfromtxt(path, delimiter=',')
            self.time_of_signal_2 = self.data2[:, 0]
            self.amplitude_of_signal_2 = self.data2[:, 1]
            self.time_of_signal_2 = list(self.time_of_signal_2[:])
            self.amplitude_of_signal_2 = list(self.amplitude_of_signal_2[:])


    def read_file3(self):
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open only txt or CSV or xls', os.getenv('HOME'),
                                                  "csv(*.csv);; text(*.txt) ;; xls(*.xls)")
        path = fname[0]


        elif pathlib.Path(path).suffix == ".csv":
            self.data3 = np.genfromtxt(path, delimiter=',')
            self.time_of_signal_3 = self.data3[:, 0]
            self.amplitude_of_signal_3 = self.data3[:, 1]
            self.time_of_signal_3 = list(self.time_of_signal_3[:])
            self.amplitude_of_signal_3 = list(self.amplitude_of_signal_3[:])


#>>>>>>>>>>>>>>>>>>>>  ######## printing


    def create_pdf_for_signal_1(self): ##take pdf to to the gragh of chaneel 1

        PLOT_DIR = 'channel1_plots'
        PDF_DIR = 'channel1_pdf'

        try:
            shutil.rmtree(PDF_DIR)
            shutil.rmtree(PLOT_DIR)
            os.mkdir(PLOT_DIR)
            os.mkdir(PDF_DIR)
        except FileNotFoundError:
            os.mkdir(PDF_DIR)
            os.mkdir(PLOT_DIR)

        exporter = pg.exporters.ImageExporter(
                    self.graphicsView.scene())
        exporter.export(f'{PLOT_DIR}/0.jpg')
        exporter = pg.exporters.ImageExporter(
                    self.graphicsView_4.scene())
        exporter.export(f'{PLOT_DIR}/1.jpg')
        pdf = PDF()
        images = pdf.construct(PLOT_DIR)
        print (images[0:])
        pdf.print_page(images, PLOT_DIR)
        pdf.output(f'{PDF_DIR}/channel_01.pdf', 'F')



    def create_pdf_for_signal_2(self):   ##take pdf to spectrogram of chaneel 1
        PLOT_DIR = 'channel2_plots'
        PDF_DIR = 'channel2_pdf'

        try:
            shutil.rmtree(PDF_DIR)
            shutil.rmtree(PLOT_DIR)
            os.mkdir(PLOT_DIR)
            os.mkdir(PDF_DIR)
        except FileNotFoundError:
            os.mkdir(PDF_DIR)
            os.mkdir(PLOT_DIR)

        exporter = pg.exporters.ImageExporter(
                    self.graphicsView_2.scene())
        exporter.export(f'{PLOT_DIR}/0.jpg')
        exporter = pg.exporters.ImageExporter(
                    self.graphicsView_5.scene())
        exporter.export(f'{PLOT_DIR}/1.jpg')
        pdf = PDF()
        images = pdf.construct(PLOT_DIR)
        print (images[0:])
        pdf.print_page(images, PLOT_DIR)
        pdf.output(f'{PDF_DIR}/channel_02.pdf', 'F')


    def create_pdf_for_signal_3(self):
        PLOT_DIR = 'channel3_plots'
        PDF_DIR = 'channel3_pdf'

        try:
            shutil.rmtree(PDF_DIR)
            shutil.rmtree(PLOT_DIR)
            os.mkdir(PLOT_DIR)
            os.mkdir(PDF_DIR)
        except FileNotFoundError:
            os.mkdir(PDF_DIR)
            os.mkdir(PLOT_DIR)

        exporter = pg.exporters.ImageExporter(
                    self.graphicsView_3.scene())
        exporter.export(f'{PLOT_DIR}/0.jpg')
        exporter = pg.exporters.ImageExporter(
                    self.graphicsView_6.scene())
        exporter.export(f'{PLOT_DIR}/1.jpg')
        pdf = PDF()
        images = pdf.construct(PLOT_DIR)
        print (images[0:])
        pdf.print_page(images, PLOT_DIR)
        pdf.output(f'{PDF_DIR}/channel_03.pdf', 'F')
 


 #>>>>>>>>>>>>       ############## hiding

 #>>>>>>>>>>>>>>       ######3 loading files

     ## load 1111
    def load_data_of_channel_1(self):
        self.read_file1()
        self.pen = pg.mkPen(color=(255, 0, 0))
        self.data_line1 = self.graphicsView.plot(self.time_of_signal_1, self.amplitude_of_signal_1, pen=self.pen)
        self.graphicsView.plotItem.setLimits(xMin=0, xMax=12, yMin=min(self.amplitude_of_signal_1)-0.5, yMax=max(self.amplitude_of_signal_1)+0.5)
        self.sampling_of_signal_1 = 0
        self.timer1.setInterval(1)

        self.timer1.timeout.connect(self.update_plot_data1)
        self.timer1.start()

        self.draw_spectrogram_of_channel_1()

    def draw_spectrogram_of_channel_1(self):

        #spectrogram
        
        fs = 1 /(self.time_of_signal_1[1] - self.time_of_signal_1[0])
        array_of_sample = np.array(self.amplitude_of_signal_1)    
        f, t, Sxx = signal.spectrogram(array_of_sample, fs)
        pg.setConfigOptions(imageAxisOrder='row-major')
            
        win = self.graphicsView_4
        img = pg.ImageItem()
        win.addItem(img)
        hist = pg.HistogramLUTItem()
        hist.setImageItem(img)
        win.addItem(hist)
        hist.setLevels(np.min(Sxx), np.max(Sxx))
        hist.gradient.restoreState({
            'mode':
            'rgb',
            'ticks': [(0.5, (0, 182, 188, 255)), (1.0, (246, 111, 0, 255)),
                    (0.0, (75, 0, 113, 255))]
        })
        img.setImage(Sxx)
        img.scale(t[-1] / np.size(Sxx, axis=1), f[-1] / np.size(Sxx, axis=0))
        win.setLabel('bottom', "Time", units='s')
        win.setLabel('left', "Frequency", units='Hz')
        self.graphicsView_4.plotItem.setXRange(0, 4)
        self.graphicsView_4.plotItem.setYRange(0, 50)

    def load_data_of_channel_2(self):

        self.read_file2()
        self.pen = pg.mkPen(color=(0, 160, 0))
        self.data_line2 = self.graphicsView_2.plot(self.time_of_signal_2, self.amplitude_of_signal_2, pen=self.pen)
        self.graphicsView_2.plotItem.setLimits(xMin=0, xMax=12, yMin=min(self.amplitude_of_signal_1)-0.5, yMax=max(self.amplitude_of_signal_1)+0.5)


        self.sampling_of_signal_2 = 0
        self.timer2.setInterval(60)
        self.timer2.timeout.connect(self.update_plot_data2)
        self.timer2.start()
        self.draw_spectrogram_of_channel_2()

    def draw_spectrogram_of_channel_2(self):

        #spectrogram
        fs = 1 /(self.time_of_signal_1[1] - self.time_of_signal_1[0])
        array_of_sample = np.array(self.amplitude_of_signal_1)    
        f, t, Sxx = signal.spectrogram(array_of_sample, fs)
        pg.setConfigOptions(imageAxisOrder='row-major')
            
        win = self.graphicsView_5
        img = pg.ImageItem()
        win.addItem(img)
        hist = pg.HistogramLUTItem()
        hist.setImageItem(img)
        win.addItem(hist)
        hist.setLevels(np.min(Sxx), np.max(Sxx))
        hist.gradient.restoreState({
            'mode':
            'rgb',
            'ticks': [(0.5, (0, 182, 188, 255)), (1.0, (246, 111, 0, 255)),
                    (0.0, (75, 0, 113, 255))]
        })
        img.setImage(Sxx)
        img.scale(t[-1] / np.size(Sxx, axis=1), f[-1] / np.size(Sxx, axis=0))
        win.setLabel('bottom', "Time", units='s')
        win.setLabel('left', "Frequency", units='Hz')
        self.graphicsView_5.plotItem.setXRange(0, 4)
        self.graphicsView_5.plotItem.setYRange(0, 50)


    ##### load 3
    def load_data_of_channel_3(self):

        self.read_file3()
        self.pen = pg.mkPen(color=(255, 255, 0))
        self.data_line3 = self.graphicsView_3.plot(self.time_of_signal_3, self.amplitude_of_signal_3, pen=self.pen)
        self.graphicsView_3.plotItem.setLimits(xMin=0, xMax=12, yMin=min(self.amplitude_of_signal_1)-0.5, yMax=max(self.amplitude_of_signal_1)+0.5)


        self.sampling_of_signal_3 = 0
        self.timer3.setInterval(100)
        self.timer3.timeout.connect(self.update_plot_data3)
        self.timer3.start()
        self.draw_spectrogram_of_channel_3()


    def draw_spectrogram_of_channel_3(self):

        #spectrogram
        fs = 1 /(self.time_of_signal_1[1] - self.time_of_signal_1[0])
        array_of_sample = np.array(self.amplitude_of_signal_1)    
        f, t, Sxx = signal.spectrogram(array_of_sample, fs)
        pg.setConfigOptions(imageAxisOrder='row-major')
            
        win = self.graphicsView_6
        img = pg.ImageItem()
        win.addItem(img)
        hist = pg.HistogramLUTItem()
        hist.setImageItem(img)
        win.addItem(hist)
        hist.setLevels(np.min(Sxx), np.max(Sxx))
        hist.gradient.restoreState({
            'mode':
            'rgb',
            'ticks': [(0.5, (0, 182, 188, 255)), (1.0, (246, 111, 0, 255)),
                    (0.0, (75, 0, 113, 255))]
        })
        img.setImage(Sxx)
        img.scale(t[-1] / np.size(Sxx, axis=1), f[-1] / np.size(Sxx, axis=0))
        win.setLabel('bottom', "Time", units='s')
        win.setLabel('left', "Frequency", units='Hz')
        self.graphicsView_6.plotItem.setXRange(0, 4)
        self.graphicsView_6.plotItem.setYRange(0, 50)




 #>>>>>>>>>>>>>>>>>       ####### updating

    def update_plot_data1(self):
        time = self.time_of_signal_1[:self.sampling_of_signal_1]
        amplitude = self.amplitude_of_signal_1[:self.sampling_of_signal_1]
        self.sampling_of_signal_1 += 10                                       #take aampe of 10 readings then udata data 

        if self.sampling_of_signal_1 > len(self.time_of_signal_1):
            self.sampling_of_signal_1 = 0
            print("saeed")



        self.graphicsView.plotItem.setXRange(max(time, default=0) - 0.5, max(time, default=0))

        self.data_line1.setData(time, amplitude)

    def update_plot_data2(self):

        time = self.time_of_signal_2[:self.sampling_of_signal_2]
        amplitude = self.amplitude_of_signal_2[:self.sampling_of_signal_2]
        self.sampling_of_signal_2 += 10
        if self.sampling_of_signal_2 > len(self.time_of_signal_2):
            self.sampling_of_signal_2 = 0
     

        self.graphicsView_2.plotItem.setXRange(max(time, default=0) - 0.5, max(time, default=0))
        self.data_line2.setData(time, amplitude)  # Update the data.

    def update_plot_data3(self):

        time = self.time_of_signal_3[:self.sampling_of_signal_3]
        amplitude = self.amplitude_of_signal_3[:self.sampling_of_signal_3]
        self.data_line3.setData(time, amplitude)  # Update the data.
        self.sampling_of_signal_3 += 10
        if self.sampling_of_signal_3 > len(self.time_of_signal_3):
            self.sampling_of_signal_3 = 0
   
        self.graphicsView_3.plotItem.setXRange(max(time, default=0) - 0.5, max(time, default=0))
        self.data_line3.setData(time, amplitude)  # Update the data.


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "signal viewer"))
        self.label_2.setText(_translate("mainWindow", "signal"))
        self.label_3.setText(_translate("mainWindow", "spectrogram"))
        self.p1.setShortcut(_translate("mainWindow", "Ctrl+q"))
        self.r1.setShortcut(_translate("mainWindow", "Ctrl+w"))
        self.zz1.setShortcut(_translate("mainWindow", "Ctrl+e"))
        self.z1.setShortcut(_translate("mainWindow", "Ctrl+r"))
        self.print1.setShortcut(_translate("mainWindow", "Ctrl+t"))
        self.p2.setShortcut(_translate("mainWindow", "Ctrl+a"))
        self.r2.setShortcut(_translate("mainWindow", "Ctrl+s"))
        self.zz2.setShortcut(_translate("mainWindow", "Ctrl+d"))
        self.z2.setShortcut(_translate("mainWindow", "Ctrl+f"))
        self.print2.setShortcut(_translate("mainWindow", "Ctrl+g"))
        self.p3.setShortcut(_translate("mainWindow", "Ctrl+z"))
        self.r3.setShortcut(_translate("mainWindow", "Ctrl+x"))
        self.zz3.setShortcut(_translate("mainWindow", "Ctrl+c"))
        self.z3.setShortcut(_translate("mainWindow", "Ctrl+v"))
        self.print3.setShortcut(_translate("mainWindow", "Ctrl+b"))
        self.menuchannel1.setTitle(_translate("mainWindow", "channel1"))
        self.menuchannel2.setTitle(_translate("mainWindow", "channel2"))
        self.menuchanell3.setTitle(_translate("mainWindow", "channel3"))
        self.actionadd_signal.setText(_translate("mainWindow", "add signal"))
        self.actionadd_signal.setShortcut(_translate("mainWindow", "Ctrl+Shift+Z"))
        self.actionadd_signal_2.setText(_translate("mainWindow", "add signal"))
        self.actionadd_signal_2.setShortcut(_translate("mainWindow", "Ctrl+Shift+X"))
        self.actionadd_signal_3.setText(_translate("mainWindow", "add signal"))
        self.actionadd_signal_3.setShortcut(_translate("mainWindow", "Ctrl+Shift+C"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
