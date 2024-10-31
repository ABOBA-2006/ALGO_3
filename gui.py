import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsBlurEffect, QLineEdit
import main


class SimpleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle('DATA BASE 3000')
        self.setGeometry(100, 100, 800, 800)
        self.setFixedSize(800, 800)
        self.setWindowFlags(QtCore.Qt.WindowMinMaxButtonsHint | QtCore.Qt.WindowCloseButtonHint)

        self.text_field = QLineEdit(self)
        self.text_field.setPlaceholderText("Enter index...")  # Optional placeholder text
        self.text_field.setAlignment(QtCore.Qt.AlignCenter)
        self.text_field.setGeometry(300, 350, 200, 100)
        self.text_field.hide()

        self.text_field2 = QLineEdit(self)
        self.text_field2.setPlaceholderText("Enter data...")  # Optional placeholder text
        self.text_field2.setAlignment(QtCore.Qt.AlignCenter)
        self.text_field2.setGeometry(300, 200, 200, 100)
        self.text_field2.hide()


        self.button_add = QtWidgets.QPushButton(self)
        self.button_add.setGeometry(300, 100, 200, 100)
        self.button_add.setText("ADD")
        self.button_add.setStyleSheet("""
                    QPushButton {
                        border-radius: 20px;
                        background-color: black;
                        font-size: 30px;
                        color: lightgray;
                        border: 2px solid #000;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color: lightgray;
                        color:black;
                    }
                """)
        self.button_add.clicked.connect(self.add_pressed)

        self.button_delete = QtWidgets.QPushButton(self)
        self.button_delete.setGeometry(300, 250, 200, 100)
        self.button_delete.setText("DELETE")
        self.button_delete.setStyleSheet("""
                    QPushButton {
                        border-radius: 20px;
                        background-color: black;
                        font-size: 30px;
                        color: lightgray;
                        border: 2px solid #000;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color: lightgray;
                        color:black;
                    }
                """)
        self.button_delete.clicked.connect(self.delete_pressed)

        self.button_edit = QtWidgets.QPushButton(self)
        self.button_edit.setGeometry(300, 400, 200, 100)
        self.button_edit.setText("EDIT")
        self.button_edit.setStyleSheet("""
                            QPushButton {
                                border-radius: 20px;
                                background-color: black;
                                font-size: 30px;
                                color: lightgray;
                                border: 2px solid #000;
                                padding: 10px;
                            }
                            QPushButton:hover {
                                background-color: lightgray;
                                color:black;
                            }
                        """)
        self.button_edit.clicked.connect(self.edit_pressed)

        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setGeometry(300, 500, 200, 100)
        self.back_button.setText("BACK")
        self.back_button.setStyleSheet("""
                                    QPushButton {
                                        border-radius: 20px;
                                        background-color: black;
                                        font-size: 30px;
                                        color: lightgray;
                                        border: 2px solid #000;
                                        padding: 10px;
                                    }
                                    QPushButton:hover {
                                        background-color: lightgray;
                                        color:black;
                                    }
                                """)
        self.back_button.hide()
        self.back_button.clicked.connect(self.back_pressed)

        self.send_button = QtWidgets.QPushButton(self)
        self.send_button.setGeometry(300, 50, 200, 100)
        self.send_button.setText("SEND")
        self.send_button.setStyleSheet("""
                                            QPushButton {
                                                border-radius: 20px;
                                                background-color: black;
                                                font-size: 30px;
                                                color: lightgray;
                                                border: 2px solid #000;
                                                padding: 10px;
                                            }
                                            QPushButton:hover {
                                                background-color: lightgray;
                                                color:black;
                                            }
                                        """)
        self.send_button.hide()

        self.button_find = QtWidgets.QPushButton(self)
        self.button_find.setGeometry(300, 550, 200, 100)
        self.button_find.setText("FIND")
        self.button_find.setStyleSheet("""
                                    QPushButton {
                                        border-radius: 20px;
                                        background-color: black;
                                        font-size: 30px;
                                        color: lightgray;
                                        border: 2px solid #000;
                                        padding: 10px;
                                    }
                                    QPushButton:hover {
                                        background-color: lightgray;
                                        color:black;
                                    }
                                """)
        self.button_find.clicked.connect(self.find_pressed)


    def send_pressed(self, task):
        index = self.text_field.text()
        if index == "":
            index = 0
        else:
            index = int(index)
        if task == 1:
            data = self.text_field2.text()
            rec1 = main.Record(0, index, data)
            main.add_record(rec1)
        if task == 2:
            main.delete_record(index)
        if task == 3:
            data = self.text_field2.text()
            main.edit_record(index, data)
        if task == 4:
            print(main.find_record(index))



    def add_pressed(self):
        self.button_add.hide()
        self.button_edit.hide()
        self.button_find.hide()
        self.button_delete.hide()
        self.text_field.show()
        self.text_field2.show()
        self.back_button.show()
        self.send_button.show()
        self.send_button.setGeometry(450, 500, 200, 100)
        self.back_button.setGeometry(150, 500, 200, 100)
        self.send_button.clicked.connect(lambda: self.send_pressed(1))

    def edit_pressed(self):
        self.button_add.hide()
        self.button_edit.hide()
        self.button_find.hide()
        self.button_delete.hide()
        self.text_field.show()
        self.text_field2.show()
        self.back_button.show()
        self.send_button.show()
        self.send_button.setGeometry(450, 500, 200, 100)
        self.back_button.setGeometry(150, 500, 200, 100)
        self.send_button.clicked.connect(lambda: self.send_pressed(3))

    def delete_pressed(self):
        self.button_add.hide()
        self.button_edit.hide()
        self.button_find.hide()
        self.button_delete.hide()
        self.text_field.show()
        self.back_button.show()
        self.send_button.show()
        self.send_button.setGeometry(300, 200, 200, 100)
        self.back_button.setGeometry(300, 500, 200, 100)
        self.send_button.clicked.connect(lambda: self.send_pressed(2))

    def find_pressed(self):
        self.button_add.hide()
        self.button_edit.hide()
        self.button_find.hide()
        self.button_delete.hide()
        self.text_field.show()
        self.back_button.show()
        self.send_button.show()
        self.send_button.setGeometry(300, 200, 200, 100)
        self.back_button.setGeometry(300, 500, 200, 100)
        self.send_button.clicked.connect(lambda: self.send_pressed(4))

    def back_pressed(self):
        self.button_add.show()
        self.button_edit.show()
        self.button_find.show()
        self.button_delete.show()
        self.text_field2.hide()
        self.text_field.hide()
        self.back_button.hide()
        self.send_button.hide()
        self.text_field.setText("")
        self.text_field2.setText("")
        self.send_button.clicked.disconnect()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec_())