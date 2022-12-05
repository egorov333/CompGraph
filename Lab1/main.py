from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import matplotlib.pyplot as plt
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 360)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_x1 = QtWidgets.QLabel(self.centralwidget)
        self.label_x1.setGeometry(QtCore.QRect(20, 15, 20, 20))
        self.label_x1.setObjectName("label_x1")
        self.label_x2 = QtWidgets.QLabel(self.centralwidget)
        self.label_x2.setGeometry(QtCore.QRect(20, 65, 20, 20))
        self.label_x2.setObjectName("label_x2")
        self.label_x3 = QtWidgets.QLabel(self.centralwidget)
        self.label_x3.setGeometry(QtCore.QRect(20, 115, 20, 20))
        self.label_x3.setObjectName("label_x3")
        self.label_y1 = QtWidgets.QLabel(self.centralwidget)
        self.label_y1.setGeometry(QtCore.QRect(170, 15, 20, 20))
        self.label_y1.setObjectName("label_y1")
        self.label_y2 = QtWidgets.QLabel(self.centralwidget)
        self.label_y2.setGeometry(QtCore.QRect(170, 65, 20, 20))
        self.label_y2.setObjectName("label_y2")
        self.label_y3 = QtWidgets.QLabel(self.centralwidget)
        self.label_y3.setGeometry(QtCore.QRect(170, 115, 20, 20))
        self.label_y3.setObjectName("label_y3")
        self.label_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_axis.setGeometry(QtCore.QRect(20, 170, 40, 20))
        self.label_axis.setObjectName("label_axis")
        self.label_scale = QtWidgets.QLabel(self.centralwidget)
        self.label_scale.setGeometry(QtCore.QRect(20, 240, 190, 20))
        self.label_scale.setObjectName("label_scale")

        self.plainTextEdit_x1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_x1.setGeometry(QtCore.QRect(60, 10, 80, 30))
        self.plainTextEdit_x1.setObjectName("plainTextEdit_x1")
        self.plainTextEdit_x2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_x2.setGeometry(QtCore.QRect(60, 60, 80, 30))
        self.plainTextEdit_x2.setObjectName("plainTextEdit_x2")
        self.plainTextEdit_x3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_x3.setGeometry(QtCore.QRect(60, 110, 80, 30))
        self.plainTextEdit_x3.setObjectName("plainTextEdit_x3")
        self.plainTextEdit_y1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_y1.setGeometry(QtCore.QRect(210, 10, 80, 30))
        self.plainTextEdit_y1.setObjectName("plainTextEdit_y1")
        self.plainTextEdit_y2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_y2.setGeometry(QtCore.QRect(210, 60, 80, 30))
        self.plainTextEdit_y2.setObjectName("plainTextEdit_y2")
        self.plainTextEdit_y3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_y3.setGeometry(QtCore.QRect(210, 110, 80, 30))
        self.plainTextEdit_y3.setObjectName("plainTextEdit_y3")
        self.plainTextEdit_scale = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_scale.setGeometry(QtCore.QRect(210, 235, 80, 30))
        self.plainTextEdit_scale.setObjectName("plainTextEdit_scale")
        
        self.radioButton_x = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_x.setGeometry(QtCore.QRect(60, 160, 50, 16))
        self.radioButton_x.setObjectName("radioButton_x")
        self.radioButton_y = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_y.setGeometry(QtCore.QRect(60, 190, 50, 16))
        self.radioButton_y.setObjectName("radioButton_y")
        
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(20, 290, 120, 50))
        self.pushButton_start.setObjectName("pushButton_start")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_x1.setText(_translate("MainWindow", "X1"))
        self.label_y1.setText(_translate("MainWindow", "Y1"))
        self.label_x2.setText(_translate("MainWindow", "X2"))
        self.label_x3.setText(_translate("MainWindow", "X3"))
        self.label_y2.setText(_translate("MainWindow", "Y2"))
        self.label_y3.setText(_translate("MainWindow", "Y3"))
        self.label_axis.setText(_translate("MainWindow", "Ось"))
        self.label_scale.setText(_translate("MainWindow", "Коэф. масштабирования"))
        self.radioButton_x.setText(_translate("MainWindow", "X"))
        self.radioButton_y.setText(_translate("MainWindow", "Y"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton_start.clicked.connect(self.plot_graph)

    def plot_graph(self):
        plt.close()

        x1 = float(self.plainTextEdit_x1.toPlainText())
        x2 = float(self.plainTextEdit_x2.toPlainText())
        x3 = float(self.plainTextEdit_x3.toPlainText())
        y1 = float(self.plainTextEdit_y1.toPlainText())
        y2 = float(self.plainTextEdit_y2.toPlainText())
        y3 = float(self.plainTextEdit_y3.toPlainText())
        scale = float(self.plainTextEdit_scale.toPlainText())

        triangle_matrix = np.array([[x1, y1], [x2, y2], [x3, y3]])
        scale_matrix = np.array([[scale, 0], [0, scale]])

        if self.radioButton_x.isChecked():
            x_matrix = np.array([[1, 0], [0, -1]])
            temp_matrix = np.dot(triangle_matrix, x_matrix)
            res_matrix = np.dot(temp_matrix, scale_matrix)
        elif self.radioButton_y.isChecked():
            y_matrix = np.array([[-1, 0], [0, 1]])
            temp_matrix = np.dot(triangle_matrix, y_matrix)
            res_matrix = np.dot(temp_matrix, scale_matrix)

        fig, ax = plt.subplots(figsize = (8, 8))
        ax.clear()
        ax.set(xlabel='X', ylabel='Y', title='Yo')
        x_triangle = np.array([triangle_matrix[0, 0], triangle_matrix[1, 0], triangle_matrix[2, 0], triangle_matrix[0, 0]])
        y_triangle = np.array([triangle_matrix[0, 1], triangle_matrix[1, 1], triangle_matrix[2, 1], triangle_matrix[0, 1]])
        x_res = np.array([res_matrix[0, 0], res_matrix[1, 0], res_matrix[2, 0], res_matrix[0, 0]])
        y_res = np.array([res_matrix[0, 1], res_matrix[1, 1], res_matrix[2, 1], res_matrix[0, 1]])
        ax.plot(x_triangle, y_triangle, color='blue')
        ax.plot(x_res, y_res, color='red')
        ax = plt.gca()
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid()
        plt.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
