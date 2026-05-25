from PySide6.QtWidgets import QApplication, QLabel, QLayout, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QSlider, QProgressBar, QCheckBox, QRadioButton, QComboBox, QListWidget, QTableWidget, QComboBox, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit, QCalendarWidget, QLCDNumber, QDial, QScrollBar, QTabWidget, QToolBox, QStackedWidget
from PySide6.QtCore import Qt

def greet(name: str | None = None) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, world!"

class Model:
    def __init__(self) -> None:
        self._value: int = 1

    def increment_value(self) -> int:
        self._value += 1
        return self.get_value()
    
    def reset_value(self) -> int:
        self._value: int = 1
        return self.get_value()
    
    def get_value(self) -> int:
        return self._value

class MainWindow(QMainWindow):

    def __increment_button_clicked(self) -> None:
        self._label1.setText(greet(str(self.model.increment_value())))


    def __reset_button_clicked(self) -> None:
        self.model.reset_value()
        self._label1.setText(greet(str(self.model.get_value())))

    def __init__(self) -> None:
        super().__init__()
        self.model = Model()

        self.setWindowTitle("PySide6 Example")
        central_widget: QWidget = QWidget(self)
        self.setCentralWidget(central_widget)

        self._label1: QLabel = QLabel(greet(str(self.model.get_value())), self)
        self._label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        increment_button: QPushButton = QPushButton("Increment", self)
        increment_button.clicked.connect(lambda: self.__increment_button_clicked())
        reset_button: QPushButton = QPushButton("Reset", self)
        reset_button.clicked.connect(lambda: self.__reset_button_clicked())

        layout: QLayout = QVBoxLayout(central_widget)
        layout.addWidget(self._label1)
        layout.addWidget(increment_button)
        layout.addWidget(reset_button)


def main() -> None:
    app: QApplication = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
