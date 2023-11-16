import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from Config.session_storage import SessionStorage
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

        self.labels = {
            'angry': QLabel(self),
            'disgust': QLabel(self),
            'fear': QLabel(self),
            'happy': QLabel(self),
            'sad' :  QLabel(self),
            'surprise' :  QLabel(self),
            'neutral' :  QLabel(self)
        }

        for name, label in self.labels.items():
            hbox = QHBoxLayout()
            
            pixmap = QPixmap(f"{name}.jpg")
            image_label = QLabel()
            image_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            
            hbox.addWidget(image_label)
            hbox.addWidget(label)
            
            self.layout.addLayout(hbox)

        """
            self.milestone_button = QPushButton('Milestones', self)
            self.milestone_button.setStyleSheet('background-color: #808080; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')
            self.milestone_button.clicked.connect(self.close)
            self.layout.addWidget(self.milestone_button)   
        """  

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.setStyleSheet('background-color: #FF0000; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')
        self.exit_button.clicked.connect(self.open_main_window)
        self.layout.addWidget(self.exit_button)

    def open_main_window(self):
        self.mainWindow.show()
        self.hide()

    def set_values(self, values):
        for name, value in values.items():
            label = self.labels[name]
            label.setText(f'{name}: {value}%')
            label.setStyleSheet("font-size: 24px; padding: 10px;")
            label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)

    window = EmotionWindow()
    window.show()

    #storage = SessionStorage()
    #print(storage.getEmotions())

    window.set_values({
        'angry':60,
        'disgust': 23,
        'fear': 33,
        'happy': 65,
        'sad' :56, 
        'surprise':34, 
        'neutral':10
    })
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
