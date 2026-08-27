import sys
from PySide6 import QtCore, QtWidgets
from task_tracker.main_window import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.resize(800, 600)
    window.show()
    
    sys.exit(app.exec())

