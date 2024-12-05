from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_test import Ui_MainWindow # Import the UI file converted from Qt Designer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the button to the file explorer functionality
        self.ui.pushButton.clicked.connect(self.open_file_explorer)

    def open_file_explorer(self):
        # Open a file dialog to select a file
        file_path, _ = QFileDialog.getOpenFileName(
            self,  # Parent widget
            "Select a File",  # Dialog title
            "",  # Initial directory
            "All Files (*.*);;Text Files (*.txt);;Images (*.png *.jpg *.jpeg)"  # File filters
        )

        # Display the selected file path in the label
        if file_path:
            self.ui.label.setText(f"Selected File: {file_path}")
        else:
            self.ui.label.setText("No file selected")


# Run the application
if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
