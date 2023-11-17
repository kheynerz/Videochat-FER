from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from desktop_notifier import DesktopNotifier
from Config.session_storage import SessionStorage
from Config.app_settings import AppSettings

class EmotionWindow(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        self.initUI()

    def getEmotionsData(self):
        storage = SessionStorage()
        self.set_values(storage.getEmotions())

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Session Statistics')
        self.setStyleSheet("background-color: white")

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

        self.labels = {emotion: QLabel(self) for emotion in AppSettings.get_app_setting('emotions')}

        for name, label in self.labels.items():
            hbox = QHBoxLayout()
            
            pixmap = QPixmap(f"{name}.jpg")
            image_label = QLabel()
            image_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            
            hbox.addWidget(image_label)
            hbox.addWidget(label)
            
            self.layout.addLayout(hbox)

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.setStyleSheet('background-color: #FF0000; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')
        self.exit_button.clicked.connect(self.open_main_window)
        self.layout.addWidget(self.exit_button)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.getEmotionsData)
        self.timer.start(1000)


        self.notifier = DesktopNotifier()

        self.notifier_timer = QTimer(self)
        self.notifier_timer.timeout.connect(self.notifications)
        self.notifier_timer.start(2000)


    def open_main_window(self):
        self.mainWindow.show()
        self.hide()

    def set_values(self, values):
        for name, value in values.items():
            label = self.labels[name]
            label.setText(f'{name}: {round(value,2)}%')
            label.setStyleSheet("font-size: 24px; padding: 10px;")
            label.setAlignment(Qt.AlignCenter)


    def notifications(self):
        storage = SessionStorage()
        emotions = storage.getEmotions()

        if not emotions: return
        for emotion in emotions:
            level = emotions[emotion]
            if level >= AppSettings.get_user_setting(emotion):
                print("ENTER")
                n = self.notifier.send(title=f"Alerta de {emotion.lower()}", message=f"El {level}% de la clase está {emotion.lower()}.")
                self.notifier.clear(n)

