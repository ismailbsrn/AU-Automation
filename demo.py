import sys
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QTextEdit, QComboBox, QFileDialog,
                            QHBoxLayout, QVBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 100
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.options = ('getOpenFileName()', 'getOpenFileNames()', 'getExistingDirectory()', 'getSaveFileName()')

        self.combo = QComboBox()
        self.combo.addItems(self.options)
        layout.addWidget(self.combo)

        btn = QPushButton('Launch')
        btn.clicked.connect(self.launchDialog)
        layout.addWidget(btn)

        self.textbox = QTextEdit()
        layout.addWidget(self.textbox)


    def launchDialog(self):
        option = self.options.index(self.combo.currentText())

        if option == 0:
            response = self.getFileName()
        elif option == 1:
            response = self.getFileNames()
        elif option == 2:
            response = self.getDirectory()
        elif option == 3:
            response = self.getSaveFileName()
        else:
            print('Got Nothing')

        # Eğer bir dosya seçilmişse işlem yapalım
        if response:
            self.processFile(response)


    def getFileName(self):
        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls);; Image File (*.png *.jpg)'
        response, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Excel File (*.xlsx *.xls *.csv)'
        )
        self.textbox.setText(str(response))
        return response

    def getFileNames(self):
        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls);; Image File (*.png *.jpg)'
        response, _ = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select file(s)',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Excel File (*.xlsx *.xls)'
        )
        self.textbox.setText(str(response))
        return response


    def getDirectory(self):
         response = QFileDialog.getExistingDirectory(
             self,
             caption='Select a folder'
         )
         self.textbox.setText(str(response))
         return response

    def getSaveFileName(self):
         file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
         response, _ = QFileDialog.getSaveFileName(
             parent=self,
             caption='Select a data file',
             directory='Data File.dat',
             filter=file_filter,
             initialFilter='Excel File (*.xlsx *.xls)'
         )
         self.textbox.setText(str(response))
         return response

    def processFile(self, file_path):
        """Seçilen dosyada işlem yap"""
        if not file_path:
            return

        # Örnek işlem: Dosya içeriğini okuma
        if os.path.isfile(file_path):  # Eğer bu bir dosyaysa
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.textbox.append("\n--- File Content ---\n")
                self.textbox.append(content)
            except Exception as e:
                self.textbox.append(f"\nHata: {e}")
        else:
            self.textbox.append("Bu bir dosya değil.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 20px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
