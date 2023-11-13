import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class EmotionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Session Statistics')
        self.setStyleSheet("background-color: white")

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

        self.labels = {
            'Happiness': QLabel(self),
            'Sadness': QLabel(self),
            'Seriousness': QLabel(self),
            'Anger': QLabel(self),
            'Otros' :  QLabel(self)
        }

        for name, label in self.labels.items():
            hbox = QHBoxLayout()
            
            pixmap = QPixmap(f"{name}.jpg")
            image_label = QLabel()
            image_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            
            hbox.addWidget(image_label)
            hbox.addWidget(label)
            
            self.layout.addLayout(hbox)

        self.milestone_button = QPushButton('Milestones', self)
        self.milestone_button.setStyleSheet('background-color: #808080; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')
        self.milestone_button.clicked.connect(self.close)
        self.layout.addWidget(self.milestone_button)    

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.setStyleSheet('background-color: #FF0000; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)


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

    window.set_values({
        'Happiness': 60,
        'Sadness': 20,
        'Seriousness': 10,
        'Anger': 5,
        'Otros':5
    })

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
