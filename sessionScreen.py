from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QListWidgetItem, QLabel
from PyQt5.QtCore import QSize
from datetime import datetime
from config import ConfigMenu

class SessionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.session_name = QLineEdit()
        self.session_name.setPlaceholderText('Session name')
        self.session_name.setStyleSheet('font-size: 13px; border-radius: 10px; padding: 10px;')

        self.start_button = QPushButton('New session')
        self.start_button.clicked.connect(self.start_session)
        self.start_button.setStyleSheet('background-color: #4CAF50; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')

        self.top_layout = QHBoxLayout()
        self.top_layout.addWidget(self.session_name)
        self.top_layout.addWidget(self.start_button)

        self.list_title = QLabel("Previous sessions")
        self.list_title.setStyleSheet('font-size: 16px;')

        self.session_list = QListWidget()
        self.session_list.itemSelectionChanged.connect(self.enable_view_button)
        self.session_list.setStyleSheet('font-size: 12px; border-radius: 10px;')

        for i in range(self.session_list.count()):
            item = self.session_list.item(i)
            item.setSizeHint(QSize(item.sizeHint().width(), 50))

        self.view_button = QPushButton('View session')
        self.view_button.clicked.connect(self.view_session)
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
        session_name = self.session_name.text()
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        session_item = QListWidgetItem(f'Session: {session_name}, Time: {start_time}')
        self.session_list.addItem(session_item)

    def enable_view_button(self):
        if len(self.session_list.selectedItems()) > 0:
            self.view_button.setEnabled(True)
        else:
            self.view_button.setEnabled(False)

    def view_session(self):
        print('activated')
        pass

    def open_config(self):
        self.config_window = ConfigMenu()
        self.config_window.show()

if __name__ == '__main__':
    app = QApplication([])
    window = SessionApp()
    window.show()
    app.exec_()






