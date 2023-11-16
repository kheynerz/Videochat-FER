import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QCheckBox

class ConfigMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.alerts_label = QLabel("Alerts")
        self.alerts_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(self.alerts_label)

        config = self.read_config()

        self.add_alert_section("angry", main_layout, config["user"].get("angry", ""))
        self.add_alert_section("disgust", main_layout, config["user"].get("disgust", ""))
        self.add_alert_section("fear", main_layout, config["user"].get("fear", ""))
        self.add_alert_section("happy", main_layout, config["user"].get("happy", ""))
        self.add_alert_section("sad", main_layout, config["user"].get("sad", ""))
        self.add_alert_section("surprise", main_layout, config["user"].get("surprise", ""))
        self.add_alert_section("neutral", main_layout, config["user"].get("neutral", ""))

        alert_rate_layout = QHBoxLayout()
        main_layout.addLayout(alert_rate_layout)

        self.alert_rate_label = QLabel("Alert rate:")
        alert_rate_layout.addWidget(self.alert_rate_label)

        self.alert_rate_input = QLineEdit()
        self.alert_rate_input.setText(config["user"].get("alertRate", ""))
        self.alert_rate_input.setPlaceholderText("300")
        alert_rate_layout.addWidget(self.alert_rate_input)

        self.silence_alerts_checkbox = QCheckBox("Silence alerts", self)
        self.silence_alerts_checkbox.setChecked(config["user"].get("silentAlerts", False))
        main_layout.addWidget(self.silence_alerts_checkbox)

        self.fire_emergency_checkbox = QCheckBox("Fire Emergency Alert", self)
        self.fire_emergency_checkbox.setChecked(config["user"].get("fireEmergencyAlerts", False))
        main_layout.addWidget(self.fire_emergency_checkbox)

        self.save_button = QPushButton('Guardar')
        self.save_button.setStyleSheet('background-color: #0000FF; font-size: 14px; color: white; border-radius: 10px; padding: 10px;')
        main_layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_config)  

    def add_alert_section(self, alert_type, layout, value):
        alert_layout = QHBoxLayout()
        layout.addLayout(alert_layout)

        alert_label = QLabel(alert_type + ":")
        alert_layout.addWidget(alert_label)

        alert_input = QLineEdit()
        alert_input.setText(str(value))
        alert_input.setPlaceholderText("100")
        alert_input.setMaximumWidth(50)
        alert_layout.addWidget(alert_input)

        setattr(self, alert_type.lower() + '_input', alert_input)

    def save_config(self):
        config = self.read_config()  
        config["user"] = {  
            "alertRate" : self.alert_rate_input.text(),
            "silentAlerts" : self.silence_alerts_checkbox.isChecked(),
            "fireEmergencyAlerts" : self.fire_emergency_checkbox.isChecked(),
            "angry": int(self.angry_input.text()) if self.angry_input.text() else 0,
            "disgust": int(self.disgust_input.text()) if self.disgust_input.text() else 0,
            "fear": int(self.fear_input.text()) if self.fear_input.text() else 0,
            "happy": int(self.happy_input.text()) if self.happy_input.text() else 0,
            "sad": int(self.sad_input.text()) if self.sad_input.text() else 0,
            "surprise": int(self.surprise_input.text()) if self.surprise_input.text() else 0,
            "neutral": int(self.neutral_input.text()) if self.neutral_input.text() else 0
        }
        with open('settings.json', 'w') as f:
            json.dump(config, f) 

    def read_config(self):
        with open('settings.json', 'r') as f:
            config = json.load(f)
        return config

def main(): 
    app = QApplication(sys.argv)
    ex = ConfigMenu()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
