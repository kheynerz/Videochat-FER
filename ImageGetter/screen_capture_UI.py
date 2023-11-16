import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget
import time
import mss
import sys

from Config.app_settings import AppSettings

class ScreenCaptureApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Screen Capture')
        self.setGeometry(100, 100, 400, 200)

        self.screen_label = QLabel(self)
        self.screen_label.setAlignment(Qt.AlignCenter)

        self.screen_combo = QComboBox(self)
        self.screen_combo.currentIndexChanged.connect(self.update_screen)

        self.capture_button = QPushButton('Capture', self)
        self.capture_button.clicked.connect(self.capture_screen)

        layout = QVBoxLayout()
        layout.addWidget(self.screen_label)
        layout.addWidget(self.screen_combo)
        layout.setAlignment(self.screen_combo, Qt.AlignTop)
        layout.addWidget(self.capture_button, alignment=Qt.AlignBottom)

        self.setLayout(layout)

        self.update_screen_list()

    def update_screen_list(self):
        screens = QDesktopWidget().screenCount()
        for i in range(screens):
            self.screen_combo.addItem(f"Screen {i + 1}")

    def update_screen(self):
        screen_number = self.screen_combo.currentIndex() + 1
        self.current_screen_number = screen_number

    def capture_screen(self):
        screen_number = self.screen_combo.currentIndex() + 1
        self.capture_full_screen(screen_number)

    def capture_full_screen(self, screen_number):
        with mss.mss() as sct:
            for i, _ in enumerate(sct.monitors):
                if i + 1 == screen_number:
                    sct.shot(output=f"images/Screen_{screen_number}.png", mon=i)

        #Load settings
        settings = AppSettings()
        settings.load_settings()
        delay = int(settings.get_app_setting('screenshotRate'))
        time.sleep(delay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScreenCaptureApp()
    ex.show()
    sys.exit(app.exec_())