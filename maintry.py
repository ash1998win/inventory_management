# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maintry.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mplwidget import MplWidget

import store_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1520, 944)
        MainWindow.setMinimumSize(QSize(800, 0))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(43, 31, 91);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 50))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tittle_container = QFrame(self.header_frame)
        self.tittle_container.setObjectName(u"tittle_container")
        self.tittle_container.setFrameShape(QFrame.StyledPanel)
        self.tittle_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.tittle_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_toggle_frame = QFrame(self.tittle_container)
        self.left_toggle_frame.setObjectName(u"left_toggle_frame")
        self.left_toggle_frame.setMinimumSize(QSize(50, 0))
        self.left_toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.left_toggle_frame.setStyleSheet(u"QFrame{\n"
"background-color:#000;\n"
"}\n"
"QPushButton{\n"
"packing:5px 10px;\n"
"border:none;\n"
"border-radius:5px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushBUtton:hover\n"
"background-color: rgb(0, 92, 157);")
        self.left_toggle_frame.setFrameShape(QFrame.NoFrame)
        self.left_toggle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_toggle_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_toggle_button = QPushButton(self.left_toggle_frame)
        self.left_toggle_button.setObjectName(u"left_toggle_button")
        self.left_toggle_button.setMinimumSize(QSize(0, 45))
        self.left_toggle_button.setMaximumSize(QSize(50, 16777215))
        self.left_toggle_button.setStyleSheet(u"QPushButton{\n"
"border radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_toggle_button.setIcon(icon)
        self.left_toggle_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.left_toggle_button)


        self.horizontalLayout_5.addWidget(self.left_toggle_frame)

        self.tittle_bar = QFrame(self.tittle_container)
        self.tittle_bar.setObjectName(u"tittle_bar")
        self.tittle_bar.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.tittle_bar.setFrameShape(QFrame.NoFrame)
        self.tittle_bar.setFrameShadow(QFrame.Raised)
        self.username_label = QLabel(self.tittle_bar)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(980, 10, 141, 16))
        self.username_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_toggle_button = QPushButton(self.tittle_bar)
        self.setting_toggle_button.setObjectName(u"setting_toggle_button")
        self.setting_toggle_button.setGeometry(QRect(30, 10, 93, 28))
        self.setting_toggle_button.setStyleSheet(u"QFrame{\n"
"background-color:#000;\n"
"}\n"
"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"")
        self.barcode_toggle_button = QPushButton(self.tittle_bar)
        self.barcode_toggle_button.setObjectName(u"barcode_toggle_button")
        self.barcode_toggle_button.setGeometry(QRect(170, 10, 93, 28))
        self.barcode_toggle_button.setStyleSheet(u"QFrame{\n"
"background-color:#000;\n"
"}\n"
"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"")
        self.label_35 = QLabel(self.tittle_bar)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(870, 10, 55, 16))
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.tittle_bar)


        self.horizontalLayout_2.addWidget(self.tittle_container)

        self.top_right_buttons = QFrame(self.header_frame)
        self.top_right_buttons.setObjectName(u"top_right_buttons")
        self.top_right_buttons.setMaximumSize(QSize(100, 16777215))
        self.top_right_buttons.setStyleSheet(u"QPushButton{\n"
"border radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"}\n"
"QFrame{\n"
"background-color:#000000;\n"
"}")
        self.top_right_buttons.setFrameShape(QFrame.StyledPanel)
        self.top_right_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_buttons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.top_right_buttons)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.minimize_button)

        self.restore_button = QPushButton(self.top_right_buttons)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon2)
        self.restore_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restore_button)

        self.closebutton = QPushButton(self.top_right_buttons)
        self.closebutton.setObjectName(u"closebutton")
        self.closebutton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closebutton.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.closebutton)


        self.horizontalLayout_2.addWidget(self.top_right_buttons)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_main_frame = QFrame(self.main_frame)
        self.left_main_frame.setObjectName(u"left_main_frame")
        self.left_main_frame.setMinimumSize(QSize(0, 0))
        self.left_main_frame.setMaximumSize(QSize(50, 16777215))
        self.left_main_frame.setStyleSheet(u"QFrame{\n"
"background-color:#000;\n"
"}\n"
"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"")
        self.left_main_frame.setFrameShape(QFrame.Box)
        self.left_main_frame.setFrameShadow(QFrame.Raised)
        self.left_main_frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.left_main_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(7, 0, 0, 0)
        self.inventory_toggle_button = QPushButton(self.left_main_frame)
        self.inventory_toggle_button.setObjectName(u"inventory_toggle_button")
        self.inventory_toggle_button.setMinimumSize(QSize(150, 0))
        self.inventory_toggle_button.setMaximumSize(QSize(16777215, 16777215))
        self.inventory_toggle_button.setFocusPolicy(Qt.NoFocus)
        self.inventory_toggle_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-truck.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left\n"
"")
        self.inventory_toggle_button.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.inventory_toggle_button)

        self.billing_toggle_button = QPushButton(self.left_main_frame)
        self.billing_toggle_button.setObjectName(u"billing_toggle_button")
        self.billing_toggle_button.setMinimumSize(QSize(150, 0))
        self.billing_toggle_button.setFocusPolicy(Qt.NoFocus)
        self.billing_toggle_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-dialpad.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.billing_toggle_button)

        self.services_toggle_button = QPushButton(self.left_main_frame)
        self.services_toggle_button.setObjectName(u"services_toggle_button")
        self.services_toggle_button.setMinimumSize(QSize(150, 50))
        self.services_toggle_button.setFocusPolicy(Qt.NoFocus)
        self.services_toggle_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-people.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left\n"
"")

        self.verticalLayout_2.addWidget(self.services_toggle_button)

        self.sales_toggle_button = QPushButton(self.left_main_frame)
        self.sales_toggle_button.setObjectName(u"sales_toggle_button")
        self.sales_toggle_button.setMinimumSize(QSize(150, 0))
        self.sales_toggle_button.setFocusPolicy(Qt.NoFocus)
        self.sales_toggle_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-chart-line.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.sales_toggle_button)

        self.logs_toggle_button = QPushButton(self.left_main_frame)
        self.logs_toggle_button.setObjectName(u"logs_toggle_button")
        self.logs_toggle_button.setMinimumSize(QSize(150, 0))
        self.logs_toggle_button.setMaximumSize(QSize(150, 16777215))
        self.logs_toggle_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-description.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left\n"
"")

        self.verticalLayout_2.addWidget(self.logs_toggle_button)

        self.account_toggle_button = QPushButton(self.left_main_frame)
        self.account_toggle_button.setObjectName(u"account_toggle_button")
        self.account_toggle_button.setMinimumSize(QSize(150, 0))
        self.account_toggle_button.setFocusPolicy(Qt.NoFocus)
        self.account_toggle_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-user.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.account_toggle_button)

        self.settings_toggle_button = QPushButton(self.left_main_frame)
        self.settings_toggle_button.setObjectName(u"settings_toggle_button")
        self.settings_toggle_button.setMinimumSize(QSize(150, 0))
        self.settings_toggle_button.setMaximumSize(QSize(16777215, 16777215))
        self.settings_toggle_button.setFocusPolicy(Qt.NoFocus)
        self.settings_toggle_button.setStyleSheet(u"\n"
"background-image: url(:/icons/icons/cil-3d.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left\n"
"")

        self.verticalLayout_2.addWidget(self.settings_toggle_button)


        self.horizontalLayout.addWidget(self.left_main_frame)

        self.middle_main_frame = QFrame(self.main_frame)
        self.middle_main_frame.setObjectName(u"middle_main_frame")
        self.middle_main_frame.setFrameShape(QFrame.NoFrame)
        self.middle_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.middle_main_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.middle_main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(400, 0))
        self.stackedWidget.setStyleSheet(u"")
        self.inventory_page = QWidget()
        self.inventory_page.setObjectName(u"inventory_page")
        self.inventory_page.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.inventory_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.inventory_main_frame = QFrame(self.inventory_page)
        self.inventory_main_frame.setObjectName(u"inventory_main_frame")
        self.inventory_main_frame.setStyleSheet(u"")
        self.inventory_main_frame.setFrameShape(QFrame.StyledPanel)
        self.inventory_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.inventory_main_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(self.inventory_main_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.frame.setStyleSheet(u";")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 300))
        self.frame_3.setMaximumSize(QSize(476, 430))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.name_e = QLineEdit(self.frame_3)
        self.name_e.setObjectName(u"name_e")
        self.name_e.setMinimumSize(QSize(0, 30))
        self.name_e.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.name_e)

        self.clear_all_add_database = QPushButton(self.frame_3)
        self.clear_all_add_database.setObjectName(u"clear_all_add_database")
        self.clear_all_add_database.setStyleSheet(u"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.clear_all_add_database)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.stock_e = QLineEdit(self.frame_3)
        self.stock_e.setObjectName(u"stock_e")
        self.stock_e.setMinimumSize(QSize(0, 30))
        self.stock_e.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.stock_e)

        self.cp_e = QLineEdit(self.frame_3)
        self.cp_e.setObjectName(u"cp_e")
        self.cp_e.setMinimumSize(QSize(0, 30))
        self.cp_e.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.cp_e)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.sp_e = QLineEdit(self.frame_3)
        self.sp_e.setObjectName(u"sp_e")
        self.sp_e.setMinimumSize(QSize(0, 30))
        self.sp_e.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.sp_e)

        self.inventory_excel_button = QPushButton(self.frame_3)
        self.inventory_excel_button.setObjectName(u"inventory_excel_button")
        self.inventory_excel_button.setStyleSheet(u"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.inventory_excel_button)

        self.refres_button = QPushButton(self.frame_3)
        self.refres_button.setObjectName(u"refres_button")
        self.refres_button.setMaximumSize(QSize(100, 16777215))
        self.refres_button.setStyleSheet(u"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.refres_button)

        self.add_to_database_button = QPushButton(self.frame_3)
        self.add_to_database_button.setObjectName(u"add_to_database_button")
        self.add_to_database_button.setStyleSheet(u"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.add_to_database_button)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_6)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.ide_ud = QLineEdit(self.frame_6)
        self.ide_ud.setObjectName(u"ide_ud")
        self.ide_ud.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.ide_ud)

        self.find_ud = QPushButton(self.frame_6)
        self.find_ud.setObjectName(u"find_ud")
        self.find_ud.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.find_ud)

        self.ud_ud = QPushButton(self.frame_6)
        self.ud_ud.setObjectName(u"ud_ud")
        self.ud_ud.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.ud_ud)

        self.sp_ud = QLineEdit(self.frame_6)
        self.sp_ud.setObjectName(u"sp_ud")
        self.sp_ud.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.sp_ud)

        self.stock_ud = QLineEdit(self.frame_6)
        self.stock_ud.setObjectName(u"stock_ud")
        self.stock_ud.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.stock_ud)

        self.name_ud = QLineEdit(self.frame_6)
        self.name_ud.setObjectName(u"name_ud")
        self.name_ud.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.name_ud)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.cp_ud = QLineEdit(self.frame_6)
        self.cp_ud.setObjectName(u"cp_ud")
        self.cp_ud.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.cp_ud)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)


        self.gridLayout_2.addWidget(self.frame_6, 1, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.horizontalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.inventory_main_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table_database = QTableWidget(self.frame_2)
        if (self.table_database.columnCount() < 8):
            self.table_database.setColumnCount(8)
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.table_database.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font3);
        self.table_database.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.table_database.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.table_database.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.table_database.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.table_database.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.table_database.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.table_database.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.table_database.setObjectName(u"table_database")
        self.table_database.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.table_database, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_2)


        self.verticalLayout_6.addWidget(self.inventory_main_frame)

        self.stackedWidget.addWidget(self.inventory_page)
        self.barcode_page = QWidget()
        self.barcode_page.setObjectName(u"barcode_page")
        self.horizontalLayout_8 = QHBoxLayout(self.barcode_page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_16 = QFrame(self.barcode_page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(710, 30, 501, 721))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_17)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_36 = QLabel(self.frame_17)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.label_36, 0, 0, 1, 1)

        self.range_lineEdit = QLineEdit(self.frame_17)
        self.range_lineEdit.setObjectName(u"range_lineEdit")
        self.range_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.range_lineEdit, 0, 1, 1, 1)

        self.all_files_barcode = QPushButton(self.frame_17)
        self.all_files_barcode.setObjectName(u"all_files_barcode")
        self.all_files_barcode.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_14.addWidget(self.all_files_barcode, 0, 2, 1, 1)

        self.label_46 = QLabel(self.frame_17)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.label_46, 1, 0, 1, 1)

        self.bar_discount = QLineEdit(self.frame_17)
        self.bar_discount.setObjectName(u"bar_discount")
        self.bar_discount.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.bar_discount, 1, 1, 1, 1)

        self.label_34 = QLabel(self.frame_17)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.label_34, 2, 0, 1, 1)

        self.bar_product_name = QLineEdit(self.frame_17)
        self.bar_product_name.setObjectName(u"bar_product_name")
        self.bar_product_name.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.bar_product_name, 2, 1, 1, 1)

        self.bar_product_get = QPushButton(self.frame_17)
        self.bar_product_get.setObjectName(u"bar_product_get")
        self.bar_product_get.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_14.addWidget(self.bar_product_get, 2, 2, 1, 1)

        self.label_33 = QLabel(self.frame_17)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.label_33, 3, 0, 1, 1)

        self.barcode_lineEdit = QLineEdit(self.frame_17)
        self.barcode_lineEdit.setObjectName(u"barcode_lineEdit")
        self.barcode_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.barcode_lineEdit, 3, 1, 1, 1)

        self.idbarcode_button = QPushButton(self.frame_17)
        self.idbarcode_button.setObjectName(u"idbarcode_button")
        self.idbarcode_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_14.addWidget(self.idbarcode_button, 3, 2, 1, 1)

        self.barcode_add_to_database = QPushButton(self.frame_17)
        self.barcode_add_to_database.setObjectName(u"barcode_add_to_database")
        self.barcode_add_to_database.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_14.addWidget(self.barcode_add_to_database, 4, 1, 1, 1)

        self.gen_barcode_pdf = QPushButton(self.frame_17)
        self.gen_barcode_pdf.setObjectName(u"gen_barcode_pdf")
        self.gen_barcode_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 85, 0);\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
";\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_14.addWidget(self.gen_barcode_pdf, 5, 1, 1, 1)

        self.clearfiles_barcode = QPushButton(self.frame_17)
        self.clearfiles_barcode.setObjectName(u"clearfiles_barcode")
        self.clearfiles_barcode.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_14.addWidget(self.clearfiles_barcode, 5, 2, 1, 1)

        self.clear_barcode_button = QPushButton(self.frame_17)
        self.clear_barcode_button.setObjectName(u"clear_barcode_button")
        self.clear_barcode_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 85, 0);\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
";\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_14.addWidget(self.clear_barcode_button, 6, 1, 1, 1)

        self.barcode_table = QTableWidget(self.frame_16)
        if (self.barcode_table.columnCount() < 4):
            self.barcode_table.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.barcode_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.barcode_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.barcode_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.barcode_table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.barcode_table.setObjectName(u"barcode_table")
        self.barcode_table.setGeometry(QRect(40, 50, 591, 700))
        self.barcode_table.setMinimumSize(QSize(0, 700))
        self.barcode_table.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_37 = QLabel(self.frame_16)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(90, 800, 551, 32))
        self.label_37.setFont(font1)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_38 = QLabel(self.frame_16)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(454, 810, 101, 20))
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.im_per_page = QLineEdit(self.frame_16)
        self.im_per_page.setObjectName(u"im_per_page")
        self.im_per_page.setGeometry(QRect(910, 810, 113, 22))
        self.im_per_page.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.label_39 = QLabel(self.frame_16)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(790, 810, 111, 16))
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.im_per_row = QLineEdit(self.frame_16)
        self.im_per_row.setObjectName(u"im_per_row")
        self.im_per_row.setGeometry(QRect(570, 810, 113, 22))
        self.im_per_row.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.barcode_page)
        self.services_page = QWidget()
        self.services_page.setObjectName(u"services_page")
        self.services_page.setStyleSheet(u"\n"
"background-color: rgb(43, 31, 91);")
        self.gridLayout_10 = QGridLayout(self.services_page)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.no_moving_table = QTableWidget(self.services_page)
        if (self.no_moving_table.columnCount() < 3):
            self.no_moving_table.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.no_moving_table.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.no_moving_table.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.no_moving_table.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.no_moving_table.setObjectName(u"no_moving_table")
        self.no_moving_table.setMinimumSize(QSize(300, 0))
        self.no_moving_table.setMaximumSize(QSize(400, 16777215))
        self.no_moving_table.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.no_moving_table, 0, 0, 2, 1)

        self.non_mover_button = QPushButton(self.services_page)
        self.non_mover_button.setObjectName(u"non_mover_button")
        self.non_mover_button.setMaximumSize(QSize(100, 16777215))
        self.non_mover_button.setStyleSheet(u"\n"
"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color: #000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_10.addWidget(self.non_mover_button, 0, 1, 1, 1)

        self.MplWidget = MplWidget(self.services_page)
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setMinimumSize(QSize(0, 800))

        self.gridLayout_10.addWidget(self.MplWidget, 0, 2, 2, 1)

        self.update_graph_button = QPushButton(self.services_page)
        self.update_graph_button.setObjectName(u"update_graph_button")
        self.update_graph_button.setMaximumSize(QSize(100, 16777215))
        self.update_graph_button.setStyleSheet(u"\n"
"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color: #000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_10.addWidget(self.update_graph_button, 1, 1, 1, 1)

        self.nonmovingreset = QPushButton(self.services_page)
        self.nonmovingreset.setObjectName(u"nonmovingreset")
        self.nonmovingreset.setStyleSheet(u"\n"
"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color: rgb(255, 170, 0);\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_10.addWidget(self.nonmovingreset, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.services_page)
        self.sales_page = QWidget()
        self.sales_page.setObjectName(u"sales_page")
        self.sales_page.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.sales_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_23 = QLabel(self.sales_page)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.gridLayout_9.addWidget(self.label_23, 0, 2, 1, 1)

        self.tableWidget = QTableWidget(self.sales_page)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem24)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.tableWidget, 2, 0, 1, 5)

        self.dateEdit_from = QDateEdit(self.sales_page)
        self.dateEdit_from.setObjectName(u"dateEdit_from")
        self.dateEdit_from.setFont(font1)
        self.dateEdit_from.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")
        self.dateEdit_from.setCalendarPopup(True)

        self.gridLayout_9.addWidget(self.dateEdit_from, 0, 1, 1, 1)

        self.dateEdit_to = QDateEdit(self.sales_page)
        self.dateEdit_to.setObjectName(u"dateEdit_to")
        self.dateEdit_to.setFont(font1)
        self.dateEdit_to.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")
        self.dateEdit_to.setCalendarPopup(True)

        self.gridLayout_9.addWidget(self.dateEdit_to, 0, 3, 1, 1)

        self.get_transaction = QPushButton(self.sales_page)
        self.get_transaction.setObjectName(u"get_transaction")
        self.get_transaction.setFont(font)
        self.get_transaction.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: #2b1f5b;\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.get_transaction, 0, 4, 1, 1)

        self.label_20 = QLabel(self.sales_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.gridLayout_9.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_29 = QLabel(self.sales_page)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(100, 0))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.gridLayout_9.addWidget(self.label_29, 1, 0, 1, 1)

        self.bill_identry = QLineEdit(self.sales_page)
        self.bill_identry.setObjectName(u"bill_identry")
        self.bill_identry.setMaximumSize(QSize(300, 16777215))
        self.bill_identry.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")

        self.gridLayout_9.addWidget(self.bill_identry, 1, 1, 1, 1)

        self.get_bill_number = QPushButton(self.sales_page)
        self.get_bill_number.setObjectName(u"get_bill_number")
        self.get_bill_number.setFont(font)
        self.get_bill_number.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: #2b1f5b;\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.get_bill_number, 1, 2, 1, 1)

        self.excelbutton = QPushButton(self.sales_page)
        self.excelbutton.setObjectName(u"excelbutton")
        self.excelbutton.setFont(font)
        self.excelbutton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: #2b1f5b;\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.excelbutton, 1, 4, 1, 1)

        self.stackedWidget.addWidget(self.sales_page)
        self.accounts_page = QWidget()
        self.accounts_page.setObjectName(u"accounts_page")
        self.accounts_page.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.accounts_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.login_form_frame = QFrame(self.accounts_page)
        self.login_form_frame.setObjectName(u"login_form_frame")
        self.login_form_frame.setFrameShape(QFrame.StyledPanel)
        self.login_form_frame.setFrameShadow(QFrame.Raised)
        self.input_login_frame = QFrame(self.login_form_frame)
        self.input_login_frame.setObjectName(u"input_login_frame")
        self.input_login_frame.setGeometry(QRect(380, 280, 501, 271))
        self.input_login_frame.setFont(font1)
        self.input_login_frame.setStyleSheet(u"\n"
"QLineEdit{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"background-color: rgb(34, 34, 34);\n"
"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"\n"
"\n"
"")
        self.input_login_frame.setFrameShape(QFrame.StyledPanel)
        self.input_login_frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.input_login_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.username_l = QLabel(self.input_login_frame)
        self.username_l.setObjectName(u"username_l")
        self.username_l.setMinimumSize(QSize(0, 40))
        self.username_l.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.username_l.setFont(font4)
        self.username_l.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")
        self.username_l.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.username_l)

        self.username_e = QLineEdit(self.input_login_frame)
        self.username_e.setObjectName(u"username_e")
        self.username_e.setMinimumSize(QSize(0, 40))
        self.username_e.setFont(font1)
        self.username_e.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")
        self.username_e.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.username_e)

        self.password_l = QLabel(self.input_login_frame)
        self.password_l.setObjectName(u"password_l")
        self.password_l.setFont(font4)
        self.password_l.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")
        self.password_l.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.password_l)

        self.password_e = QLineEdit(self.input_login_frame)
        self.password_e.setObjectName(u"password_e")
        self.password_e.setMinimumSize(QSize(0, 40))
        self.password_e.setFont(font1)
        self.password_e.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border radius:5px")
        self.password_e.setEchoMode(QLineEdit.Password)
        self.password_e.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.password_e)

        self.checkBox = QCheckBox(self.input_login_frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"\n"
"\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.checkBox)

        self.login_button = QPushButton(self.input_login_frame)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setStyleSheet(u"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.login_button)

        self.profile_icon_frame = QFrame(self.login_form_frame)
        self.profile_icon_frame.setObjectName(u"profile_icon_frame")
        self.profile_icon_frame.setGeometry(QRect(640, 170, 100, 100))
        self.profile_icon_frame.setMinimumSize(QSize(100, 100))
        self.profile_icon_frame.setMaximumSize(QSize(100, 100))
        self.profile_icon_frame.setStyleSheet(u"image: url(:/icons/icons/cil-user.png);\n"
"background-color: rgb(0, 0, 0);\n"
"border:3px solid rgb(43, 31, 91);\n"
"border-radius:50px;\n"
"border-color: rgb(104, 198, 200);")
        self.profile_icon_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_icon_frame.setFrameShadow(QFrame.Raised)
        self.logout_button = QPushButton(self.login_form_frame)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setGeometry(QRect(1030, 310, 93, 28))
        self.logout_button.setStyleSheet(u"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.login_form_frame)

        self.stackedWidget.addWidget(self.accounts_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"")
        self.gridLayout_12 = QGridLayout(self.settings_page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_13 = QFrame(self.settings_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.get_undertaken_details_button = QPushButton(self.frame_13)
        self.get_undertaken_details_button.setObjectName(u"get_undertaken_details_button")
        self.get_undertaken_details_button.setGeometry(QRect(10, 30, 100, 32))
        self.get_undertaken_details_button.setMinimumSize(QSize(100, 0))
        self.get_undertaken_details_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_12.addWidget(self.frame_13, 0, 0, 1, 1)

        self.undertaken_table = QTableWidget(self.settings_page)
        if (self.undertaken_table.columnCount() < 8):
            self.undertaken_table.setColumnCount(8)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.undertaken_table.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.undertaken_table.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.undertaken_table.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.undertaken_table.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.undertaken_table.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.undertaken_table.setHorizontalHeaderItem(5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.undertaken_table.setHorizontalHeaderItem(6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.undertaken_table.setHorizontalHeaderItem(7, __qtablewidgetitem32)
        self.undertaken_table.setObjectName(u"undertaken_table")
        self.undertaken_table.setMinimumSize(QSize(800, 0))
        self.undertaken_table.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.undertaken_table, 0, 1, 5, 1)

        self.frame_12 = QFrame(self.settings_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(300, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.frame_12)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.update_product_status_button = QPushButton(self.frame_12)
        self.update_product_status_button.setObjectName(u"update_product_status_button")
        self.update_product_status_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.update_product_status_button)

        self.delete_cusid_edit = QLineEdit(self.frame_12)
        self.delete_cusid_edit.setObjectName(u"delete_cusid_edit")
        self.delete_cusid_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.delete_cusid_edit)

        self.delete_cusid_button = QPushButton(self.frame_12)
        self.delete_cusid_button.setObjectName(u"delete_cusid_button")
        self.delete_cusid_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.delete_cusid_button)

        self.truncate_table_button = QPushButton(self.frame_12)
        self.truncate_table_button.setObjectName(u"truncate_table_button")
        self.truncate_table_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#ff5500;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.truncate_table_button)


        self.gridLayout_12.addWidget(self.frame_12, 2, 0, 1, 1)

        self.frame_14 = QFrame(self.settings_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_14, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.settings_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.horizontalLayout_9 = QHBoxLayout(self.setting_page)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_18 = QFrame(self.setting_page)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.inventory_clear_button = QPushButton(self.frame_18)
        self.inventory_clear_button.setObjectName(u"inventory_clear_button")
        self.inventory_clear_button.setGeometry(QRect(300, 420, 269, 32))
        self.inventory_clear_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#ff5500;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")
        self.transaction_truncate_button = QPushButton(self.frame_18)
        self.transaction_truncate_button.setObjectName(u"transaction_truncate_button")
        self.transaction_truncate_button.setGeometry(QRect(300, 340, 181, 28))
        self.transaction_truncate_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#ff5500;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")
        self.user_logs_clear_button = QPushButton(self.frame_18)
        self.user_logs_clear_button.setObjectName(u"user_logs_clear_button")
        self.user_logs_clear_button.setGeometry(QRect(300, 500, 131, 41))
        self.user_logs_clear_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#ff5500;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")
        self.user_table1 = QTableWidget(self.frame_18)
        if (self.user_table1.columnCount() < 2):
            self.user_table1.setColumnCount(2)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.user_table1.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.user_table1.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        self.user_table1.setObjectName(u"user_table1")
        self.user_table1.setGeometry(QRect(600, 110, 256, 192))
        self.user_table1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.username_create = QLineEdit(self.frame_18)
        self.username_create.setObjectName(u"username_create")
        self.username_create.setGeometry(QRect(810, 560, 113, 22))
        self.username_create.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.password_create = QLineEdit(self.frame_18)
        self.password_create.setObjectName(u"password_create")
        self.password_create.setGeometry(QRect(810, 610, 113, 22))
        self.password_create.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.register_admin = QPushButton(self.frame_18)
        self.register_admin.setObjectName(u"register_admin")
        self.register_admin.setGeometry(QRect(970, 560, 93, 28))
        self.register_admin.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")
        self.label_40 = QLabel(self.frame_18)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(700, 560, 71, 20))
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_41 = QLabel(self.frame_18)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(710, 615, 55, 21))
        self.label_41.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.register_employee = QPushButton(self.frame_18)
        self.register_employee.setObjectName(u"register_employee")
        self.register_employee.setGeometry(QRect(820, 660, 93, 28))
        self.register_employee.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")
        self.view_user = QPushButton(self.frame_18)
        self.view_user.setObjectName(u"view_user")
        self.view_user.setGeometry(QRect(920, 150, 93, 28))
        self.view_user.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")
        self.login_clear_button = QPushButton(self.frame_18)
        self.login_clear_button.setObjectName(u"login_clear_button")
        self.login_clear_button.setGeometry(QRect(300, 650, 161, 28))
        self.login_clear_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#ff5500;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")
        self.username_single = QLineEdit(self.frame_18)
        self.username_single.setObjectName(u"username_single")
        self.username_single.setGeometry(QRect(130, 90, 113, 22))
        self.username_single.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.single_user_remove_button = QPushButton(self.frame_18)
        self.single_user_remove_button.setObjectName(u"single_user_remove_button")
        self.single_user_remove_button.setGeometry(QRect(270, 80, 93, 28))
        self.single_user_remove_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")
        self.label_42 = QLabel(self.frame_18)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(30, 100, 91, 16))
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_43 = QLabel(self.frame_18)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(90, 520, 191, 20))
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_44 = QLabel(self.frame_18)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(90, 340, 191, 20))
        self.label_44.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_45 = QLabel(self.frame_18)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(60, 660, 211, 20))
        self.label_45.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.setting_page)
        self.billing_page = QWidget()
        self.billing_page.setObjectName(u"billing_page")
        self.billing_page.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.gridLayout_4 = QGridLayout(self.billing_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_9 = QFrame(self.billing_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(400, 16777215))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(True)
        font5.setWeight(75)
        self.frame_9.setFont(font5)
        self.frame_9.setFocusPolicy(Qt.StrongFocus)
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.final_price1 = QLabel(self.frame_9)
        self.final_price1.setObjectName(u"final_price1")
        self.final_price1.setFont(font4)
        self.final_price1.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_7.addWidget(self.final_price1, 7, 1, 1, 1)

        self.label_19 = QLabel(self.frame_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)

        self.gridLayout_7.addWidget(self.label_19, 0, 0, 1, 2)

        self.pprice_l = QLabel(self.frame_9)
        self.pprice_l.setObjectName(u"pprice_l")
        font6 = QFont()
        font6.setPointSize(12)
        self.pprice_l.setFont(font6)
        self.pprice_l.setStyleSheet(u"color: rgb(21, 95, 255);")

        self.gridLayout_7.addWidget(self.pprice_l, 3, 1, 1, 1)

        self.pplabel = QLabel(self.frame_9)
        self.pplabel.setObjectName(u"pplabel")
        self.pplabel.setFont(font6)
        self.pplabel.setStyleSheet(u"color: rgb(21, 95, 255);")

        self.gridLayout_7.addWidget(self.pplabel, 1, 1, 1, 1)

        self.add_to_cart = QPushButton(self.frame_9)
        self.add_to_cart.setObjectName(u"add_to_cart")
        self.add_to_cart.setFocusPolicy(Qt.StrongFocus)
        self.add_to_cart.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_7.addWidget(self.add_to_cart, 5, 1, 1, 1)

        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout_7.addWidget(self.label_21, 6, 0, 1, 1)

        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.gridLayout_7.addWidget(self.label_18, 4, 0, 1, 1)

        self.Quantity_lineedit = QLineEdit(self.frame_9)
        self.Quantity_lineedit.setObjectName(u"Quantity_lineedit")
        self.Quantity_lineedit.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout_7.addWidget(self.Quantity_lineedit, 4, 1, 1, 1)

        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)

        self.gridLayout_7.addWidget(self.label_22, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_9, 2, 0, 2, 1)

        self.frame_7 = QFrame(self.billing_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 70))
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.gridLayout_3.addWidget(self.label_13, 1, 4, 1, 1)

        self.bill_line_edit = QLineEdit(self.frame_7)
        self.bill_line_edit.setObjectName(u"bill_line_edit")
        self.bill_line_edit.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_3.addWidget(self.bill_line_edit, 1, 5, 1, 1)

        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.gridLayout_3.addWidget(self.label_25, 3, 2, 1, 1)

        self.dateEdit = QDateEdit(self.frame_7)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(2000, 1, 2), QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dateEdit, 0, 0, 1, 1)

        self.customer_name_e = QLineEdit(self.frame_7)
        self.customer_name_e.setObjectName(u"customer_name_e")

        self.gridLayout_3.addWidget(self.customer_name_e, 1, 1, 1, 1)

        self.phone_number_e = QLineEdit(self.frame_7)
        self.phone_number_e.setObjectName(u"phone_number_e")

        self.gridLayout_3.addWidget(self.phone_number_e, 1, 3, 1, 1)

        self.label_24 = QLabel(self.frame_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.gridLayout_3.addWidget(self.label_24, 3, 0, 1, 1)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.gridLayout_3.addWidget(self.label_12, 1, 2, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.frame_7)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setFocusPolicy(Qt.ClickFocus)
        self.dateTimeEdit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dateTimeEdit, 3, 1, 1, 1)

        self.dateTimeEdit_2 = QDateTimeEdit(self.frame_7)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setFocusPolicy(Qt.ClickFocus)
        self.dateTimeEdit_2.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dateTimeEdit_2, 3, 3, 1, 1)

        self.update_service_button = QPushButton(self.frame_7)
        self.update_service_button.setObjectName(u"update_service_button")
        self.update_service_button.setFocusPolicy(Qt.ClickFocus)
        self.update_service_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_3.addWidget(self.update_service_button, 3, 5, 1, 1)


        self.gridLayout_4.addWidget(self.frame_7, 0, 0, 1, 2)

        self.frame_5 = QFrame(self.billing_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.invoice_button = QPushButton(self.frame_5)
        self.invoice_button.setObjectName(u"invoice_button")
        self.invoice_button.setFont(font)
        self.invoice_button.setFocusPolicy(Qt.ClickFocus)
        self.invoice_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 0);\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#ffaa00;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.verticalLayout_8.addWidget(self.invoice_button)


        self.gridLayout_4.addWidget(self.frame_5, 4, 0, 1, 1)

        self.frame_10 = QFrame(self.billing_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFocusPolicy(Qt.NoFocus)
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.final_price = QLabel(self.frame_10)
        self.final_price.setObjectName(u"final_price")
        font7 = QFont()
        font7.setPointSize(15)
        self.final_price.setFont(font7)
        self.final_price.setStyleSheet(u"color: rgb(255, 0, 13);")
        self.final_price.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.final_price, 3, 6, 1, 1)

        self.billing_table_widget = QTableWidget(self.frame_10)
        if (self.billing_table_widget.columnCount() < 8):
            self.billing_table_widget.setColumnCount(8)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.billing_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.billing_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.billing_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.billing_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.billing_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.billing_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.billing_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.billing_table_widget.setHorizontalHeaderItem(7, __qtablewidgetitem42)
        self.billing_table_widget.setObjectName(u"billing_table_widget")
        self.billing_table_widget.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout_8.addWidget(self.billing_table_widget, 1, 0, 1, 7)

        self.change_button = QPushButton(self.frame_10)
        self.change_button.setObjectName(u"change_button")
        self.change_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_8.addWidget(self.change_button, 3, 2, 1, 1)

        self.label_30 = QLabel(self.frame_10)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font6)

        self.gridLayout_8.addWidget(self.label_30, 3, 0, 1, 1)

        self.label_28 = QLabel(self.frame_10)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font7)
        self.label_28.setAutoFillBackground(False)

        self.gridLayout_8.addWidget(self.label_28, 3, 5, 1, 1)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"border-color: rgb(255, 170, 0);\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_27 = QLabel(self.frame_11)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_6.addWidget(self.label_27, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_6.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.next_customer_button = QPushButton(self.frame_11)
        self.next_customer_button.setObjectName(u"next_customer_button")
        self.next_customer_button.setFont(font6)
        self.next_customer_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_6.addWidget(self.next_customer_button, 1, 0, 1, 1)

        self.clear_row_button = QPushButton(self.frame_11)
        self.clear_row_button.setObjectName(u"clear_row_button")
        self.clear_row_button.setMinimumSize(QSize(100, 0))
        self.clear_row_button.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_6.addWidget(self.clear_row_button, 1, 4, 1, 1)

        self.labour_price_entry = QLineEdit(self.frame_11)
        self.labour_price_entry.setObjectName(u"labour_price_entry")
        self.labour_price_entry.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_6.addWidget(self.labour_price_entry, 1, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame_11, 0, 0, 1, 7)

        self.cus_given_amount_line_edit = QLineEdit(self.frame_10)
        self.cus_given_amount_line_edit.setObjectName(u"cus_given_amount_line_edit")
        self.cus_given_amount_line_edit.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_8.addWidget(self.cus_given_amount_line_edit, 3, 1, 1, 1)

        self.change_indication_label = QLabel(self.frame_10)
        self.change_indication_label.setObjectName(u"change_indication_label")
        self.change_indication_label.setFont(font7)

        self.gridLayout_8.addWidget(self.change_indication_label, 3, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_10, 2, 1, 3, 1)

        self.frame_8 = QFrame(self.billing_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 100))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.product_name_search = QPushButton(self.frame_8)
        self.product_name_search.setObjectName(u"product_name_search")
        self.product_name_search.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_5.addWidget(self.product_name_search, 1, 2, 1, 1)

        self.search_billing = QPushButton(self.frame_8)
        self.search_billing.setObjectName(u"search_billing")
        self.search_billing.setFocusPolicy(Qt.StrongFocus)
        self.search_billing.setStyleSheet(u"QPushButton{\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")

        self.gridLayout_5.addWidget(self.search_billing, 0, 2, 1, 1)

        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)

        self.ide_billing_page = QLineEdit(self.frame_8)
        self.ide_billing_page.setObjectName(u"ide_billing_page")

        self.gridLayout_5.addWidget(self.ide_billing_page, 0, 1, 1, 1)

        self.discount_lineedit = QLineEdit(self.frame_8)
        self.discount_lineedit.setObjectName(u"discount_lineedit")
        self.discount_lineedit.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_5.addWidget(self.discount_lineedit, 3, 4, 1, 1)

        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 0, 3, 1, 1)

        self.service_e = QLineEdit(self.frame_8)
        self.service_e.setObjectName(u"service_e")

        self.gridLayout_5.addWidget(self.service_e, 1, 6, 1, 1)

        self.label_26 = QLabel(self.frame_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.gridLayout_5.addWidget(self.label_26, 1, 3, 1, 1)

        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 3, 3, 1, 1)

        self.service_edit = QLineEdit(self.frame_8)
        self.service_edit.setObjectName(u"service_edit")
        self.service_edit.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout_5.addWidget(self.service_edit, 0, 4, 1, 3)

        self.product_name_search_edit = QLineEdit(self.frame_8)
        self.product_name_search_edit.setObjectName(u"product_name_search_edit")

        self.gridLayout_5.addWidget(self.product_name_search_edit, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.frame_8)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_5.addWidget(self.comboBox, 1, 4, 1, 1)

        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.label_31 = QLabel(self.frame_8)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 1, 5, 1, 1)

        self.service_id_button = QPushButton(self.frame_8)
        self.service_id_button.setObjectName(u"service_id_button")

        self.gridLayout_5.addWidget(self.service_id_button, 3, 6, 1, 1)


        self.gridLayout_4.addWidget(self.frame_8, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.billing_page)
        self.log_page = QWidget()
        self.log_page.setObjectName(u"log_page")
        self.gridLayout_13 = QGridLayout(self.log_page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_15 = QFrame(self.log_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.main = QFrame(self.frame_15)
        self.main.setObjectName(u"main")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.main)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_32 = QLabel(self.main)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(40, 16777215))
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.label_32, 0, 0, 1, 1)

        self.dateEdit_log_to = QDateEdit(self.main)
        self.dateEdit_log_to.setObjectName(u"dateEdit_log_to")
        self.dateEdit_log_to.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.dateEdit_log_to.setCalendarPopup(True)

        self.gridLayout_11.addWidget(self.dateEdit_log_to, 0, 4, 1, 1)

        self.log_table_widget = QTableWidget(self.main)
        if (self.log_table_widget.columnCount() < 10):
            self.log_table_widget.setColumnCount(10)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.log_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.log_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.log_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.log_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.log_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.log_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.log_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.log_table_widget.setHorizontalHeaderItem(7, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.log_table_widget.setHorizontalHeaderItem(8, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.log_table_widget.setHorizontalHeaderItem(9, __qtablewidgetitem52)
        self.log_table_widget.setObjectName(u"log_table_widget")
        self.log_table_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.log_table_widget.horizontalHeader().setDefaultSectionSize(130)

        self.gridLayout_11.addWidget(self.log_table_widget, 1, 0, 1, 6)

        self.dateEdit_from_log = QDateEdit(self.main)
        self.dateEdit_from_log.setObjectName(u"dateEdit_from_log")
        self.dateEdit_from_log.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dateEdit_from_log.setCalendarPopup(True)

        self.gridLayout_11.addWidget(self.dateEdit_from_log, 0, 1, 1, 1)

        self.log_details_button = QPushButton(self.main)
        self.log_details_button.setObjectName(u"log_details_button")
        self.log_details_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: #2b1f5b;\n"
"padding:8px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.log_details_button, 0, 5, 1, 1)

        self.label_17 = QLabel(self.main)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(30, 16777215))
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.label_17, 0, 3, 1, 1)


        self.horizontalLayout_7.addWidget(self.main)


        self.gridLayout_13.addWidget(self.frame_15, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.log_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.middle_main_frame)

        self.right_main_frame = QFrame(self.main_frame)
        self.right_main_frame.setObjectName(u"right_main_frame")
        self.right_main_frame.setMaximumSize(QSize(50, 16777215))
        self.right_main_frame.setStyleSheet(u"QFrame{\n"
"background-color:#000;\n"
"}\n"
"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}\n"
"")
        self.right_main_frame.setFrameShape(QFrame.NoFrame)
        self.right_main_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.right_main_frame)


        self.verticalLayout.addWidget(self.main_frame)

        self.foot_frame = QFrame(self.centralwidget)
        self.foot_frame.setObjectName(u"foot_frame")
        self.foot_frame.setMaximumSize(QSize(16777215, 30))
        self.foot_frame.setFrameShape(QFrame.WinPanel)
        self.foot_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.foot_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_toggle_button.setText("")
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Guest", None))
        self.setting_toggle_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.barcode_toggle_button.setText(QCoreApplication.translate("MainWindow", u"Barcode", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.closebutton.setText("")
        self.inventory_toggle_button.setText(QCoreApplication.translate("MainWindow", u"INVENTORY", None))
        self.billing_toggle_button.setText(QCoreApplication.translate("MainWindow", u"BILLING", None))
        self.services_toggle_button.setText(QCoreApplication.translate("MainWindow", u"SERVICES", None))
        self.sales_toggle_button.setText(QCoreApplication.translate("MainWindow", u"SALES", None))
        self.logs_toggle_button.setText(QCoreApplication.translate("MainWindow", u"logs", None))
        self.account_toggle_button.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT", None))
        self.settings_toggle_button.setText(QCoreApplication.translate("MainWindow", u"WORK", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Product :", None))
        self.clear_all_add_database.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Stock :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cost Price :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Selling price:", None))
        self.inventory_excel_button.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.refres_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.add_to_database_button.setText(QCoreApplication.translate("MainWindow", u"Add To Database", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter Id", None))
        self.find_ud.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.ud_ud.setText(QCoreApplication.translate("MainWindow", u"Update Database", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Selling price", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cost Price", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem = self.table_database.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.table_database.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.table_database.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem3 = self.table_database.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cost_Price", None));
        ___qtablewidgetitem4 = self.table_database.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Selling_Price", None));
        ___qtablewidgetitem5 = self.table_database.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tcp", None));
        ___qtablewidgetitem6 = self.table_database.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tsp", None));
        ___qtablewidgetitem7 = self.table_database.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"profit", None));
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Number", None))
        self.all_files_barcode.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.bar_product_get.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.idbarcode_button.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.barcode_add_to_database.setText(QCoreApplication.translate("MainWindow", u"Enter Database", None))
        self.gen_barcode_pdf.setText(QCoreApplication.translate("MainWindow", u"Generate Pdf", None))
        self.clearfiles_barcode.setText(QCoreApplication.translate("MainWindow", u"clear files", None))
        self.clear_barcode_button.setText(QCoreApplication.translate("MainWindow", u"clear database", None))
        ___qtablewidgetitem8 = self.barcode_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem9 = self.barcode_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem10 = self.barcode_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Selling Price", None));
        ___qtablewidgetitem11 = self.barcode_table.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"discount", None));
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"If 'all' pressed donot click 'enter database'", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Images Per row", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"images per page", None))
        ___qtablewidgetitem12 = self.no_moving_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem13 = self.no_moving_table.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Movement", None));
        ___qtablewidgetitem14 = self.no_moving_table.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.non_mover_button.setText(QCoreApplication.translate("MainWindow", u"<-CHECK", None))
        self.update_graph_button.setText(QCoreApplication.translate("MainWindow", u"UPDATE->", None))
        self.nonmovingreset.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TO", None))
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Bill_id", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"customer_name", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"phone_number", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"date", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"product_name", None));
        ___qtablewidgetitem20 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"quantity", None));
        ___qtablewidgetitem21 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"selling_price", None));
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"labour_charge", None));
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"discount", None));
        ___qtablewidgetitem24 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"total", None));
        self.dateEdit_from.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.dateEdit_to.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.get_transaction.setText(QCoreApplication.translate("MainWindow", u"Get Details", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"FROM", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Enter Bill Number:", None))
        self.get_bill_number.setText(QCoreApplication.translate("MainWindow", u"GET", None))
        self.excelbutton.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.username_l.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.username_e.setText("")
        self.username_e.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_l.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.password_e.setText("")
        self.password_e.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Keep me logged in", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.logout_button.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.get_undertaken_details_button.setText(QCoreApplication.translate("MainWindow", u"get", None))
        ___qtablewidgetitem25 = self.undertaken_table.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Sno:", None));
        ___qtablewidgetitem26 = self.undertaken_table.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Branch", None));
        ___qtablewidgetitem27 = self.undertaken_table.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        ___qtablewidgetitem28 = self.undertaken_table.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"product status", None));
        ___qtablewidgetitem29 = self.undertaken_table.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"undertaken", None));
        ___qtablewidgetitem30 = self.undertaken_table.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Service", None));
        ___qtablewidgetitem31 = self.undertaken_table.horizontalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Completion Time", None));
        ___qtablewidgetitem32 = self.undertaken_table.horizontalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"phone", None));
        self.update_product_status_button.setText(QCoreApplication.translate("MainWindow", u"Update Product status", None))
        self.delete_cusid_button.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.truncate_table_button.setText(QCoreApplication.translate("MainWindow", u"delete all", None))
        self.inventory_clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear Inventory Database", None))
        self.transaction_truncate_button.setText(QCoreApplication.translate("MainWindow", u"Clear Transactions", None))
        self.user_logs_clear_button.setText(QCoreApplication.translate("MainWindow", u"user_logs_clear", None))
        ___qtablewidgetitem33 = self.user_table1.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"username", None));
        ___qtablewidgetitem34 = self.user_table1.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"admin_status", None));
        self.register_admin.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"username:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"password:", None))
        self.register_employee.setText(QCoreApplication.translate("MainWindow", u"Employee", None))
        self.view_user.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.login_clear_button.setText(QCoreApplication.translate("MainWindow", u"clear Login_database", None))
        self.username_single.setPlaceholderText(QCoreApplication.translate("MainWindow", u"username", None))
        self.single_user_remove_button.setText(QCoreApplication.translate("MainWindow", u"remove", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Remove user:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"clears user tracking details", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"clears  Transaction Database", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"clears all usernames except master:", None))
        self.final_price1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.pprice_l.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pplabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.add_to_cart.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Selling Price", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Bill No :", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Completion Time", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"work Undertaken Time", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Customer Name :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ph No :", None))
        self.update_service_button.setText(QCoreApplication.translate("MainWindow", u"update details for service", None))
        self.invoice_button.setText(QCoreApplication.translate("MainWindow", u"Generate Invoice", None))
        self.final_price.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem35 = self.billing_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"product Id", None));
        ___qtablewidgetitem36 = self.billing_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem37 = self.billing_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Selling Price", None));
        ___qtablewidgetitem38 = self.billing_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem39 = self.billing_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Labour Charge", None));
        ___qtablewidgetitem40 = self.billing_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Discount", None));
        ___qtablewidgetitem41 = self.billing_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.change_button.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Given Amount", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Price  :", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Service Charge", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.next_customer_button.setText(QCoreApplication.translate("MainWindow", u"Next customer", None))
        self.clear_row_button.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.change_indication_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.product_name_search.setText(QCoreApplication.translate("MainWindow", u"Get Product", None))
        self.search_billing.setText(QCoreApplication.translate("MainWindow", u"Get Product", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Get Id", None))
        self.discount_lineedit.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Service Provided", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Home", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"External", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Service Id", None))
        self.service_id_button.setText(QCoreApplication.translate("MainWindow", u"Get Details", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"FROM", None))
        self.dateEdit_log_to.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        ___qtablewidgetitem42 = self.log_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"sno", None));
        ___qtablewidgetitem43 = self.log_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"user", None));
        ___qtablewidgetitem44 = self.log_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"action", None));
        ___qtablewidgetitem45 = self.log_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"date", None));
        ___qtablewidgetitem46 = self.log_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"sold product", None));
        ___qtablewidgetitem47 = self.log_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"quantity", None));
        ___qtablewidgetitem48 = self.log_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"product", None));
        ___qtablewidgetitem49 = self.log_table_widget.horizontalHeaderItem(7)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"stock updated", None));
        ___qtablewidgetitem50 = self.log_table_widget.horizontalHeaderItem(8)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"cp updated", None));
        ___qtablewidgetitem51 = self.log_table_widget.horizontalHeaderItem(9)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"sp upadated", None));
        self.dateEdit_from_log.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.log_details_button.setText(QCoreApplication.translate("MainWindow", u"GET DETAILS", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TO", None))
    # retranslateUi

