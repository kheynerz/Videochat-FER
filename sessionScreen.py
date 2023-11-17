from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QListWidgetItem, QLabel
from PyQt5.QtCore import QSize, QThreadPool, QRunnable
from datetime import datetime
from config import ConfigMenu
from Config.session_storage import SessionStorage
from emotionalScreen import EmotionWindow
from analyze import process_images
from ImageGetter.get_images import capture_full_screen

onSession = False
selectedMonitor = 1

class ImageCollector(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        global onSession
        while(onSession):
            capture_full_screen(selectedMonitor)

class ImageProcess(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        global onSession
        while(onSession):
            process_images()

class SessionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.emotionWindow = EmotionWindow(self)

        self.layout = QVBoxLayout()

        self.session_name = QLineEdit()
        self.session_name.setPlaceholderText('Session Name')
        self.session_name.setStyleSheet('font-size: 13px; border-radius: 10px; padding: 10px;')

        self.start_button = QPushButton('New Session')
        self.start_button.clicked.connect(self.start_session)
        self.start_button.setStyleSheet('background-color: #4CAF50; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')

        self.stop_button = QPushButton('Stop Session', self)
        self.stop_button.setStyleSheet('background-color: #FF0000; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')
        self.stop_button.clicked.connect(self.stop_session)
        self.stop_button.hide()

        self.top_layout = QHBoxLayout()
        self.top_layout.addWidget(self.session_name)
        self.top_layout.addWidget(self.start_button)
        self.top_layout.addWidget(self.stop_button)

        self.list_title = QLabel("Previous sessions")
        self.list_title.setStyleSheet('font-size: 16px;')

        self.session_list = QListWidget()
        self.session_list.itemSelectionChanged.connect(self.enable_view_button)
        self.session_list.setStyleSheet('font-size: 12px; border-radius: 10px;')

        for i in range(self.session_list.count()):
            item = self.session_list.item(i)
            item.setSizeHint(QSize(item.sizeHint().width(), 50))

        self.view_button = QPushButton('View session')
        self.view_button.clicked.connect(self.open_emotional_screen)
        self.view_button.setEnabled(False)  
        self.view_button.setStyleSheet('background-color: #008CBA; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')

        self.config_button = QPushButton('Alerts config')
        self.config_button.clicked.connect(self.open_config)
        self.config_button.setStyleSheet('background-color: #008CBA; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')

        self.layout.addLayout(self.top_layout)
        self.layout.addWidget(self.list_title)  
        self.layout.addWidget(self.session_list)
        self.layout.addWidget(self.view_button)  
        self.layout.addWidget(self.config_button)

        self.setLayout(self.layout)

    def start_session(self):
        global onSession
        storage = SessionStorage()

        self.stop_button.show()
        self.start_button.hide()
        self.session_name.hide()

        session_name = self.session_name.text()
        storage.init_session(session_name)
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        onSession = True
        self.runTasks()
        session_item = QListWidgetItem(f'Session: {session_name}, Time: {start_time}')
        self.session_list.addItem(session_item)
        self.open_emotional_screen()

    def stop_session(self):
        self.stop_button.hide()
        self.start_button.show()
        self.session_name.show()

        global onSession
        onSession = False

    def enable_view_button(self):
        if len(self.session_list.selectedItems()) > 0:
            self.view_button.setEnabled(True)
        else:
            self.view_button.setEnabled(False)

    def open_emotional_screen(self):
        self.hide()
        self.emotionWindow.getEmotionsData()
        self.emotionWindow.show()

    def open_config(self):
        self.config_window = ConfigMenu()
        self.config_window.show()

    def runTasks(self):
        threadCount = QThreadPool.globalInstance().maxThreadCount()
        pool = QThreadPool.globalInstance()
        #for i in range(2):
            # 2. Instantiate the subclass of QRunnable
        imageCollector = ImageCollector(1)
        imageProcessor = ImageProcess(2)
        
        # 3. Call start()
        pool.start(imageCollector)
        pool.start(imageProcessor)




