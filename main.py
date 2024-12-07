import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ApplicationUI.MainWindow import Ui_MainWindow  # Import the auto-generated UI class

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the button to the external file dialog handler
        self.ui.pushButton_ChooseFile.clicked.connect(self.handleFileDialog)

    def handleFileDialog(self):
        # Implement the file dialog logic here
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*);;Text Files (*.txt)")
        if file_path:  # If a file was selected
            self.ui.lineEdit_FilePath.setText(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
