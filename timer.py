# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timer.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(354, 340)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 90, 91, 16))
        self.Clock_ed = QLineEdit(self.centralwidget)
        self.Clock_ed.setObjectName(u"Clock_ed")
        self.Clock_ed.setGeometry(QRect(120, 90, 151, 22))
        self.Clock_ed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 90, 48, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 130, 91, 16))
        self.Prescal_ed = QLineEdit(self.centralwidget)
        self.Prescal_ed.setObjectName(u"Prescal_ed")
        self.Prescal_ed.setGeometry(QRect(120, 130, 151, 22))
        self.Prescal_ed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 40, 301, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 170, 48, 16))
        self.Period_ed = QLineEdit(self.centralwidget)
        self.Period_ed.setObjectName(u"Period_ed")
        self.Period_ed.setGeometry(QRect(120, 170, 151, 22))
        self.Period_ed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Cal_btn = QPushButton(self.centralwidget)
        self.Cal_btn.setObjectName(u"Cal_btn")
        self.Cal_btn.setGeometry(QRect(30, 200, 241, 24))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 250, 81, 16))
        self.label_6.setFont(font)
        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(120, 250, 131, 16))
        self.result_label.setFont(font)
        self.result_label.setLayoutDirection(Qt.RightToLeft)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 250, 48, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 270, 81, 16))
        self.label_8.setFont(font)
        self.resultSeclabel = QLabel(self.centralwidget)
        self.resultSeclabel.setObjectName(u"resultSeclabel")
        self.resultSeclabel.setGeometry(QRect(120, 270, 131, 16))
        self.resultSeclabel.setFont(font)
        self.resultSeclabel.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 354, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        Def_Set = '{0:,}'.format(72000000)
        self.Clock_ed.setText(Def_Set)
        self.result_label.setText("0")
        self.resultSeclabel.setText("0")
        self.Cal_btn.clicked.connect(self.Cal_btnFnc)
        self.Clock_ed.textChanged.connect(self.clockTX_Chg_Fnc)

    def clockTX_Chg_Fnc(self):
        resut_tx = self.Clock_ed.text()
        try:
            number = int(resut_tx.replace(',', ''))
            formatted_str = '{:,}'.format(number)
            self.Clock_ed.setText(formatted_str)
        except ValueError:
            pass

        #resut_tx_ = '{0:,}'.format(int(resut_tx))
        #print(resut_tx)
        #print(resut_tx_)
        #self.Clock_ed.setText(result)

    
    def Cal_btnFnc(self):
        InternalClock_text = self.Clock_ed.text()
        Prescal_text = self.Prescal_ed.text()
        Period_text = self.Period_ed.text()
        InternalClock_int = float(InternalClock_text.replace(',', ''))
        Prescal_int = float(Prescal_text.replace(',', ''))
        Period_int = float(Period_text.replace(',', ''))

        f_result = (InternalClock_int) / ((Prescal_int + 1) *  (Period_int + 1))

        print(InternalClock_int)
        print(Prescal_int)
        print(Period_int)
        print(f_result)

        self.result_label.setText(str(float(f_result)))
        self.resultSeclabel.setText(str(float(1/f_result)))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Intermal Clock", None))
        self.Clock_ed.setText(QCoreApplication.translate("MainWindow", u"20000", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Prescaler", None))
        self.Prescal_ed.setText(QCoreApplication.translate("MainWindow", u"99", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"F = ((Internal Clock) / (Prescaler+1)) / Period", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Period", None))
        self.Period_ed.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.Cal_btn.setText(QCoreApplication.translate("MainWindow", u"Calcultor", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"frequency :", None))
        self.result_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"mSec        :", None))
        self.resultSeclabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi
################################################################################
app = QApplication([])
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
app.exec()