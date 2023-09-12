import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from note_ui import Ui_Form
from save_for_ui import Ui_Form_save

directory_save = None
format_file = '.txt'
FORMATING_MAP = {
    0: '.txt',
    1: '.doc',
    2: '.py',
    3: '.html',
    4: '.cpp',
    5: '.c',
    6: '.css',
}


class Save:
    @staticmethod
    def show_save_form():
        Form_save.show()

    @staticmethod
    def set_format(index):
        global format_file
        format_file = FORMATING_MAP[index]

    @staticmethod
    def button_save_on_form():
        global directory_save
        directory_save = QFileDialog.getExistingDirectory()
        file = open(f'{directory_save}/{ui_save.lineEdit.text()}{format_file}', 'w+')
        file.write(ui.textEdit.toPlainText())
        file.close()
        Form_save.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app_save = QtWidgets.QApplication(sys.argv)
    Form_save = QtWidgets.QWidget()
    ui_save = Ui_Form_save()
    ui_save.setupUi(Form_save)
    ui_save.comboBox.addItem(FORMATING_MAP[0])
    ui_save.comboBox.addItem(FORMATING_MAP[1])
    ui_save.comboBox.addItem(FORMATING_MAP[2])
    ui_save.comboBox.addItem(FORMATING_MAP[3])
    ui_save.comboBox.addItem(FORMATING_MAP[4])
    ui_save.comboBox.addItem(FORMATING_MAP[5])
    ui_save.comboBox.addItem(FORMATING_MAP[6])
    ui.pushButton.clicked.connect(Save.show_save_form)
    ui_save.pushButton.clicked.connect(Save.button_save_on_form)
    ui_save.comboBox.currentIndexChanged.connect(Save.set_format)
    sys.exit(app.exec_())
