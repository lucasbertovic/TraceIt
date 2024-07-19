from datetime import datetime
import threading
import http.server
import socketserver
from PySide2.QtCore import Signal, Qt, QRunnable
from PySide2 import QtCore, QtWidgets
from PySide2.QtWebEngineWidgets import QWebEnginePage
from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy, QLineEdit, QPushButton, QVBoxLayout
import copy
import pandas as pd
import pandasql as psql

class CustomDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(CustomDelegate, self).__init__(parent)

    def displayText(self, value, locale):
        if str(value) == 'nan':
            return '\x7f'
        if isinstance(value, (int, float)):
            return "{:,.2f}".format(int(value)) if value == int(value) else "{:,.2f}".format(value)
        return super(CustomDelegate, self).displayText(value, locale)

class LoggedPage(QWebEnginePage):
    newData = Signal(list)
    def javaScriptConsoleMessage(self, _, msg, line, source):
        l = msg.split(",")
        self.newData.emit(l)

class HTTPServerThread(threading.Thread):
    def __init__(self, port=8000):
        super().__init__()
        self.port = port
        self.server = None
        self._stop_event = threading.Event()

    def run(self):
        handler = http.server.SimpleHTTPRequestHandler
        self.server = socketserver.TCPServer(("", self.port), handler)
        while not self._stop_event.is_set():
            self.server.handle_request()

    def stop(self):
        if self.server:
            self._stop_event.set()
            self.server.shutdown()
            self.server.server_close()

class MyWebEnginePage(QWebEnginePage):
    pass

class TraceBannerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a horizontal layout
        layout = QHBoxLayout()

        # Create 5 QLabels with white text and different background colors
        self.label1 = QLabel("0 transactions loaded")
        self.label1.setStyleSheet("background-color:  #2c313c; color: #949494")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label2 = QLabel("0 transactions matched")
        self.label2.setStyleSheet("background-color: #2c313c; color: #949494")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label3 = QLabel("0 starting transactions selected")
        self.label3.setStyleSheet("background-color: #2c313c; color: #949494")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label4 = QLabel("No methodology selected")
        self.label4.setStyleSheet("background-color: #2c313c; color: #949494")
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label5 = QLabel("No trace selected")
        self.label5.setStyleSheet("background-color: #2c313c; color: #949494")
        self.label5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label6 = QLabel("No end points")
        self.label6.setStyleSheet("background-color: #2c313c; color: #949494")
        self.label6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the labels to the layout
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addWidget(self.label5)
        layout.addWidget(self.label6)

        # Set the layout on the widget
        self.setLayout(layout)

        # Set the minimum height of the widget to 45
        self.setMinimumHeight(35)

        # Set the size policy to expand horizontally
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.setContentsMargins(0, 0, 0, 0)

class MatchBannerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a horizontal layout
        layout = QHBoxLayout()

        # Create 5 QLabels with white text and different background colors
        self.label1 = QLabel("0 transactions loaded")
        self.label1.setStyleSheet("background-color:  #2c313c; color: #949494")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label2 = QLabel("0 manual matches")
        self.label2.setStyleSheet("background-color:  #2c313c; color: #949494")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label3 = QLabel("0 manual unmatches")
        self.label3.setStyleSheet("background-color:  #2c313c; color: #949494")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label4 = QLabel("0 party/entity search terms")
        self.label4.setStyleSheet("background-color:  #2c313c; color: #949494")
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label5 = QLabel("0 category search terms")
        self.label5.setStyleSheet("background-color: #2c313c; color: #949494")
        self.label5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label6 = QLabel("0 transactions matched")
        self.label6.setStyleSheet("background-color: #2c313c; color: #949494")
        self.label6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label7 = QLabel("0 transactions categorised")
        self.label7.setStyleSheet("background-color: #2c313c; color: #949494")
        self.label7.setAlignment(Qt.AlignmentFlag.AlignCenter)


        # Add the labels to the layout
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addWidget(self.label5)
        layout.addWidget(self.label6)
        layout.addWidget(self.label7)

        # Set the layout on the widget
        self.setLayout(layout)

        # Set the minimum height of the widget to 45
        self.setMinimumHeight(35)

        # Set the size policy to expand horizontally
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.setContentsMargins(0, 0, 0, 0)

        self.resizeEvent = self.updateFontSize

    def updateFontSize(self, event):
        frame_size = self.size()
        font_size = max(int(frame_size.width()  * 0.0055),9) 
        for label in self.findChildren(QLabel):
            label_font = label.font()
            label_font.setPointSize(font_size)
            label.setFont(label_font)

class MyRunnable(QRunnable):
    def __init__(self, function, *args, **kwargs):
        super(MyRunnable, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.function(*self.args, **self.kwargs)

class Transaction:
    def __init__(self, refID=None):
        self.refID = refID
        self.name = None
        self.account = None
        self.date = None
        self.narrative = None
        self.debit = None
        self.credit = None
        self.balance = None
        self.effectiveDebit = None
        self.taintedBalance = []
        self.taintedFundsUsed = None
        self.matchedTransactionID = None
        self.matchedTransaction = None
        self.transGroupID = None
        self.category = None
        self.previouslyTraced = False
        self.effectiveDebitLog = []

class SearchBar(QWidget):
    def __init__(self):
        super().__init__()
        self.searchEdit = QLineEdit()
        self.searchEdit.setPlaceholderText("Search...")

        self.searchButton = QPushButton("Search")

        layout = QHBoxLayout()
        layout.addWidget(self.searchEdit)
        layout.addWidget(self.searchButton)

        self.setLayout(layout)

        
    


