# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)
import ui.recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet(u"QStatusBar{\n"
"	background-color: #28292a\n"
"}")
        self.window = QWidget(MainWindow)
        self.window.setObjectName(u"window")
        self.horizontalLayout = QHBoxLayout(self.window)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QWidget(self.window)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"QWidget{\n"
"	background-color: #2d2f31\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: #f1f3f4;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #f1f3f4;\n"
"	color: #3c3d40;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.menu_button = QPushButton(self.menu)
        self.menu_button.setObjectName(u"menu_button")
        icon = QIcon()
        icon.addFile(u":/icons/assets/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_button.setIcon(icon)
        self.menu_button.setIconSize(QSize(24, 24))
        self.menu_button.setChecked(False)
        self.menu_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.menu_button)

        self.menu_line_up = QFrame(self.menu)
        self.menu_line_up.setObjectName(u"menu_line_up")
        self.menu_line_up.setFrameShape(QFrame.Shape.HLine)
        self.menu_line_up.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.menu_line_up)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.menu_layout_up = QVBoxLayout()
        self.menu_layout_up.setSpacing(15)
        self.menu_layout_up.setObjectName(u"menu_layout_up")
        self.menu_layout_up.setContentsMargins(-1, -1, 0, -1)
        self.button_home = QPushButton(self.menu)
        self.button_home.setObjectName(u"button_home")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/assets/home_on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_home.setIcon(icon1)
        self.button_home.setIconSize(QSize(24, 24))
        self.button_home.setCheckable(True)
        self.button_home.setChecked(True)
        self.button_home.setAutoExclusive(True)

        self.menu_layout_up.addWidget(self.button_home)

        self.button_backup = QPushButton(self.menu)
        self.button_backup.setObjectName(u"button_backup")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/build_circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/assets/build_circle_on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_backup.setIcon(icon2)
        self.button_backup.setIconSize(QSize(24, 24))
        self.button_backup.setCheckable(True)
        self.button_backup.setAutoExclusive(True)

        self.menu_layout_up.addWidget(self.button_backup)

        self.button_reports = QPushButton(self.menu)
        self.button_reports.setObjectName(u"button_reports")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/list_alt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/assets/list_alt_on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_reports.setIcon(icon3)
        self.button_reports.setIconSize(QSize(24, 24))
        self.button_reports.setCheckable(True)
        self.button_reports.setAutoExclusive(True)

        self.menu_layout_up.addWidget(self.button_reports)

        self.button_settings = QPushButton(self.menu)
        self.button_settings.setObjectName(u"button_settings")
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/assets/settings_on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_settings.setIcon(icon4)
        self.button_settings.setIconSize(QSize(24, 24))
        self.button_settings.setCheckable(True)
        self.button_settings.setAutoExclusive(True)

        self.menu_layout_up.addWidget(self.button_settings)


        self.verticalLayout_4.addLayout(self.menu_layout_up)

        self.menu_spacer = QSpacerItem(20, 151, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.menu_spacer)

        self.menu_layout_down = QVBoxLayout()
        self.menu_layout_down.setSpacing(15)
        self.menu_layout_down.setObjectName(u"menu_layout_down")
        self.menu_layout_down.setContentsMargins(-1, -1, 0, -1)
        self.menu_line_down = QFrame(self.menu)
        self.menu_line_down.setObjectName(u"menu_line_down")
        self.menu_line_down.setFrameShape(QFrame.Shape.HLine)
        self.menu_line_down.setFrameShadow(QFrame.Shadow.Sunken)

        self.menu_layout_down.addWidget(self.menu_line_down)

        self.button_about = QPushButton(self.menu)
        self.button_about.setObjectName(u"button_about")
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/assets/info_on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_about.setIcon(icon5)
        self.button_about.setIconSize(QSize(24, 24))
        self.button_about.setCheckable(True)
        self.button_about.setAutoExclusive(True)
        self.button_about.setFlat(False)

        self.menu_layout_down.addWidget(self.button_about)


        self.verticalLayout_4.addLayout(self.menu_layout_down)


        self.horizontalLayout.addWidget(self.menu)

        self.menu_full = QWidget(self.window)
        self.menu_full.setObjectName(u"menu_full")
        self.menu_full.setEnabled(True)
        self.menu_full.setStyleSheet(u"QWidget{\n"
"	background-color: #2d2f31\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: #f1f3f4;\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	padding-left: 2px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #f1f3f4;\n"
"	color: #3c3d40;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.menu_full)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.menu_full_button = QPushButton(self.menu_full)
        self.menu_full_button.setObjectName(u"menu_full_button")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.menu_full_button.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/menu_open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_full_button.setIcon(icon6)
        self.menu_full_button.setIconSize(QSize(24, 24))
        self.menu_full_button.setFlat(False)

        self.verticalLayout.addWidget(self.menu_full_button)

        self.menu_full_line_up = QFrame(self.menu_full)
        self.menu_full_line_up.setObjectName(u"menu_full_line_up")
        self.menu_full_line_up.setFrameShape(QFrame.Shape.HLine)
        self.menu_full_line_up.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.menu_full_line_up)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.menu_full_layout_up = QVBoxLayout()
        self.menu_full_layout_up.setSpacing(15)
        self.menu_full_layout_up.setObjectName(u"menu_full_layout_up")
        self.button_full_home = QPushButton(self.menu_full)
        self.button_full_home.setObjectName(u"button_full_home")
        self.button_full_home.setIcon(icon1)
        self.button_full_home.setIconSize(QSize(24, 24))
        self.button_full_home.setCheckable(True)
        self.button_full_home.setChecked(True)
        self.button_full_home.setAutoExclusive(True)

        self.menu_full_layout_up.addWidget(self.button_full_home)

        self.button_full_backup = QPushButton(self.menu_full)
        self.button_full_backup.setObjectName(u"button_full_backup")
        self.button_full_backup.setIcon(icon2)
        self.button_full_backup.setIconSize(QSize(24, 24))
        self.button_full_backup.setCheckable(True)
        self.button_full_backup.setAutoExclusive(True)

        self.menu_full_layout_up.addWidget(self.button_full_backup)

        self.button_full_reports = QPushButton(self.menu_full)
        self.button_full_reports.setObjectName(u"button_full_reports")
        self.button_full_reports.setIcon(icon3)
        self.button_full_reports.setIconSize(QSize(24, 24))
        self.button_full_reports.setCheckable(True)
        self.button_full_reports.setAutoExclusive(True)

        self.menu_full_layout_up.addWidget(self.button_full_reports)

        self.button_full_settings = QPushButton(self.menu_full)
        self.button_full_settings.setObjectName(u"button_full_settings")
        self.button_full_settings.setIcon(icon4)
        self.button_full_settings.setIconSize(QSize(24, 24))
        self.button_full_settings.setCheckable(True)
        self.button_full_settings.setAutoExclusive(True)

        self.menu_full_layout_up.addWidget(self.button_full_settings)


        self.verticalLayout_2.addLayout(self.menu_full_layout_up)

        self.menu_full_spacer = QSpacerItem(20, 202, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.menu_full_spacer)

        self.menu_full_layout_down = QVBoxLayout()
        self.menu_full_layout_down.setSpacing(15)
        self.menu_full_layout_down.setObjectName(u"menu_full_layout_down")
        self.menu_full_line_down = QFrame(self.menu_full)
        self.menu_full_line_down.setObjectName(u"menu_full_line_down")
        self.menu_full_line_down.setFrameShape(QFrame.Shape.HLine)
        self.menu_full_line_down.setFrameShadow(QFrame.Shadow.Sunken)

        self.menu_full_layout_down.addWidget(self.menu_full_line_down)

        self.button_full_about = QPushButton(self.menu_full)
        self.button_full_about.setObjectName(u"button_full_about")
        self.button_full_about.setIcon(icon5)
        self.button_full_about.setIconSize(QSize(24, 24))
        self.button_full_about.setCheckable(True)
        self.button_full_about.setAutoExclusive(True)
        self.button_full_about.setFlat(False)

        self.menu_full_layout_down.addWidget(self.button_full_about)


        self.verticalLayout_2.addLayout(self.menu_full_layout_down)


        self.horizontalLayout.addWidget(self.menu_full)

        self.main = QWidget(self.window)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"QWidget{\n"
"	background-color: #1d1e20\n"
"}")
        self.gridLayout_2 = QGridLayout(self.main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setLineWidth(1)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"QGroupBox{\n"
"	background-color: #28292a\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: #28292a\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.page_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox = QGroupBox(self.page_home)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"	color: #5985E1;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	color: #5985E1;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: #5985E1;\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"QLabel {\n"
"	color: #5985E1;\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.page_home)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"QLabel {\n"
"	color: #5985E1;\n"
"}")

        self.verticalLayout_18.addWidget(self.label_21)

        self.list_tasks = QListView(self.groupBox_2)
        self.list_tasks.setObjectName(u"list_tasks")

        self.verticalLayout_18.addWidget(self.list_tasks)


        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.page_home)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"QLabel {\n"
"	color: #5985E1;\n"
"}")

        self.verticalLayout_11.addWidget(self.label_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_last_version = QLabel(self.groupBox_3)
        self.label_last_version.setObjectName(u"label_last_version")
        self.label_last_version.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_last_version, 1, 0, 1, 1)

        self.version = QLabel(self.groupBox_3)
        self.version.setObjectName(u"version")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.version.setFont(font3)
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.version, 0, 1, 1, 1)

        self.last_version = QLabel(self.groupBox_3)
        self.last_version.setObjectName(u"last_version")
        self.last_version.setFont(font3)
        self.last_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.last_version, 1, 1, 1, 1)

        self.label_version = QLabel(self.groupBox_3)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_version, 0, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.line_6 = QFrame(self.groupBox_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.check_version = QPushButton(self.groupBox_3)
        self.check_version.setObjectName(u"check_version")
        self.check_version.setSizeIncrement(QSize(0, 0))
        self.check_version.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(10)
        self.check_version.setFont(font4)
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.check_version.setIcon(icon7)
        self.check_version.setIconSize(QSize(16, 16))
        self.check_version.setFlat(True)

        self.horizontalLayout_4.addWidget(self.check_version)

        self.label_version_last_update = QLabel(self.groupBox_3)
        self.label_version_last_update.setObjectName(u"label_version_last_update")

        self.horizontalLayout_4.addWidget(self.label_version_last_update)

        self.last_update_version = QLabel(self.groupBox_3)
        self.last_update_version.setObjectName(u"last_update_version")

        self.horizontalLayout_4.addWidget(self.last_update_version)

        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_4)


        self.gridLayout_7.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.page_home)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_22 = QLabel(self.groupBox_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"QLabel {\n"
"	color: #5985E1;\n"
"}")

        self.verticalLayout_17.addWidget(self.label_22)

        self.list_backups = QListView(self.groupBox_4)
        self.list_backups.setObjectName(u"list_backups")

        self.verticalLayout_17.addWidget(self.list_backups)


        self.gridLayout_7.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.page_home)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"QLabel {\n"
"	color: #5985E1;\n"
"}")

        self.verticalLayout_12.addWidget(self.label_10)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_db_version = QLabel(self.groupBox_5)
        self.label_db_version.setObjectName(u"label_db_version")
        self.label_db_version.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_db_version, 0, 0, 1, 1)

        self.label_db_last_version = QLabel(self.groupBox_5)
        self.label_db_last_version.setObjectName(u"label_db_last_version")
        self.label_db_last_version.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_db_last_version, 1, 0, 1, 1)

        self.db_last_version = QLabel(self.groupBox_5)
        self.db_last_version.setObjectName(u"db_last_version")
        self.db_last_version.setFont(font3)
        self.db_last_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.db_last_version, 1, 1, 1, 1)

        self.db_version = QLabel(self.groupBox_5)
        self.db_version.setObjectName(u"db_version")
        self.db_version.setFont(font3)
        self.db_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.db_version, 0, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.line_8 = QFrame(self.groupBox_5)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.check_db_version = QPushButton(self.groupBox_5)
        self.check_db_version.setObjectName(u"check_db_version")
        self.check_db_version.setIcon(icon7)
        self.check_db_version.setFlat(True)

        self.horizontalLayout_5.addWidget(self.check_db_version)

        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_5.addWidget(self.label_20)

        self.last_update_version_db = QLabel(self.groupBox_5)
        self.last_update_version_db.setObjectName(u"last_update_version_db")

        self.horizontalLayout_5.addWidget(self.last_update_version_db)

        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_5)


        self.gridLayout_7.addWidget(self.groupBox_5, 1, 1, 1, 1)

        self.gridLayout_7.setColumnStretch(0, 3)
        self.gridLayout_7.setColumnStretch(1, 2)

        self.verticalLayout_9.addLayout(self.gridLayout_7)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 4)
        self.stackedWidget.addWidget(self.page_home)
        self.page_backup = QWidget()
        self.page_backup.setObjectName(u"page_backup")
        self.page_backup.setStyleSheet(u"QGroupBox{\n"
"	background-color: #28292a\n"
"}\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.page_backup)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.buttons_backups = QGroupBox(self.page_backup)
        self.buttons_backups.setObjectName(u"buttons_backups")
        self.buttons_backups.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.buttons_backups)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.new_task = QPushButton(self.buttons_backups)
        self.new_task.setObjectName(u"new_task")
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/add_circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.new_task.setIcon(icon8)
        self.new_task.setIconSize(QSize(24, 24))
        self.new_task.setFlat(True)

        self.horizontalLayout_2.addWidget(self.new_task)

        self.horizontalSpacer = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.line_5 = QFrame(self.buttons_backups)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_5)

        self.run_all = QPushButton(self.buttons_backups)
        self.run_all.setObjectName(u"run_all")
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/play_circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.run_all.setIcon(icon9)
        self.run_all.setIconSize(QSize(24, 24))
        self.run_all.setFlat(True)

        self.horizontalLayout_2.addWidget(self.run_all)

        self.stop_all = QPushButton(self.buttons_backups)
        self.stop_all.setObjectName(u"stop_all")
        self.stop_all.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/stop_circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_all.setIcon(icon10)
        self.stop_all.setIconSize(QSize(24, 24))
        self.stop_all.setFlat(True)

        self.horizontalLayout_2.addWidget(self.stop_all)


        self.verticalLayout_10.addWidget(self.buttons_backups)

        self.task_area = QScrollArea(self.page_backup)
        self.task_area.setObjectName(u"task_area")
        self.task_area.setEnabled(True)
        self.task_area.setFrameShape(QFrame.NoFrame)
        self.task_area.setWidgetResizable(True)
        self.task_scrollarea = QWidget()
        self.task_scrollarea.setObjectName(u"task_scrollarea")
        self.task_scrollarea.setGeometry(QRect(0, 0, 556, 391))
        self.verticalLayout_19 = QVBoxLayout(self.task_scrollarea)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 3, 0)
        self.task_area.setWidget(self.task_scrollarea)

        self.verticalLayout_10.addWidget(self.task_area)

        self.stackedWidget.addWidget(self.page_backup)
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.gridLayout_4 = QGridLayout(self.page_report)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.report = QLabel(self.page_report)
        self.report.setObjectName(u"report")
        self.report.setTextFormat(Qt.AutoText)
        self.report.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.report, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_report)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setStyleSheet(u"QGroupBox{\n"
"	background-color: #28292a\n"
"}\n"
"\n"
"QTabWidget {\n"
"	background-color: #28292a\n"
"}\n"
"")
        self.verticalLayout_13 = QVBoxLayout(self.page_settings)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.buttons_backups_2 = QGroupBox(self.page_settings)
        self.buttons_backups_2.setObjectName(u"buttons_backups_2")
        self.buttons_backups_2.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.buttons_backups_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.button_reload = QPushButton(self.buttons_backups_2)
        self.button_reload.setObjectName(u"button_reload")
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_reload.setIcon(icon11)
        self.button_reload.setIconSize(QSize(24, 24))
        self.button_reload.setFlat(True)

        self.horizontalLayout_7.addWidget(self.button_reload)

        self.horizontalSpacer_2 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.line_4 = QFrame(self.buttons_backups_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_4)

        self.button_save = QPushButton(self.buttons_backups_2)
        self.button_save.setObjectName(u"button_save")
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_save.setIcon(icon12)
        self.button_save.setIconSize(QSize(24, 24))
        self.button_save.setFlat(True)

        self.horizontalLayout_7.addWidget(self.button_save)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_13.addWidget(self.buttons_backups_2)

        self.tabWidget = QTabWidget(self.page_settings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.tab_general.setAutoFillBackground(False)
        self.tabWidget.addTab(self.tab_general, "")
        self.tab_git = QWidget()
        self.tab_git.setObjectName(u"tab_git")
        self.tabWidget.addTab(self.tab_git, "")
        self.tab_ai = QWidget()
        self.tab_ai.setObjectName(u"tab_ai")
        self.tabWidget.addTab(self.tab_ai, "")
        self.tab_notify = QWidget()
        self.tab_notify.setObjectName(u"tab_notify")
        self.tabWidget.addTab(self.tab_notify, "")

        self.verticalLayout_13.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_settings)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.gridLayout_6 = QGridLayout(self.page_about)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.about = QLabel(self.page_about)
        self.about.setObjectName(u"about")
        self.about.setTextFormat(Qt.AutoText)
        self.about.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.about, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_about)
        self.page_addtask = QWidget()
        self.page_addtask.setObjectName(u"page_addtask")
        self.page_addtask.setStyleSheet(u"QGroupBox {\n"
"	background-color: #28292a;\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: #28292a;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #28292a;\n"
"}\n"
"\n"
"QListWidget {\n"
"	background-color: #28292a;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	background-color: #28292a;\n"
"}\n"
"")
        self.verticalLayout_15 = QVBoxLayout(self.page_addtask)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.buttons_backups_3 = QGroupBox(self.page_addtask)
        self.buttons_backups_3.setObjectName(u"buttons_backups_3")
        self.buttons_backups_3.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.buttons_backups_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.title = QLabel(self.buttons_backups_3)
        self.title.setObjectName(u"title")
        font5 = QFont()
        font5.setPointSize(14)
        self.title.setFont(font5)

        self.horizontalLayout_6.addWidget(self.title)

        self.horizontalSpacer_3 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.line_7 = QFrame(self.buttons_backups_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_7)

        self.button_cancel = QPushButton(self.buttons_backups_3)
        self.button_cancel.setObjectName(u"button_cancel")
        icon13 = QIcon()
        icon13.addFile(u":/icons/assets/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_cancel.setIcon(icon13)
        self.button_cancel.setIconSize(QSize(24, 24))
        self.button_cancel.setFlat(True)

        self.horizontalLayout_6.addWidget(self.button_cancel)

        self.button_add = QPushButton(self.buttons_backups_3)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setIcon(icon12)
        self.button_add.setIconSize(QSize(24, 24))
        self.button_add.setFlat(True)

        self.horizontalLayout_6.addWidget(self.button_add)


        self.verticalLayout_15.addWidget(self.buttons_backups_3)

        self.groupBox_6 = QGroupBox(self.page_addtask)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font2)
        self.groupBox_6.setStyleSheet(u"QGroupBox {\n"
"	background-color: #28292a;\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: #28292a;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	background-color: #28292a;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #1d1e20;\n"
"}\n"
"\n"
"QListWidget {\n"
"	background-color: #1d1e20;\n"
"}\n"
"")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(16)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_16.addWidget(self.label_11)

        self.name_task = QLineEdit(self.groupBox_6)
        self.name_task.setObjectName(u"name_task")

        self.verticalLayout_16.addWidget(self.name_task)


        self.horizontalLayout_9.addLayout(self.verticalLayout_16)

        self.button_icon = QPushButton(self.groupBox_6)
        self.button_icon.setObjectName(u"button_icon")
        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/icon24x24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_icon.setIcon(icon14)
        self.button_icon.setIconSize(QSize(48, 48))
        self.button_icon.setFlat(True)

        self.horizontalLayout_9.addWidget(self.button_icon)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(3)
        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)

        self.folder_task = QLineEdit(self.groupBox_6)
        self.folder_task.setObjectName(u"folder_task")

        self.gridLayout_5.addWidget(self.folder_task, 1, 0, 1, 1)

        self.button_folder = QPushButton(self.groupBox_6)
        self.button_folder.setObjectName(u"button_folder")
        icon15 = QIcon()
        icon15.addFile(u":/icons/assets/folder_open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_folder.setIcon(icon15)
        self.button_folder.setIconSize(QSize(24, 24))
        self.button_folder.setFlat(True)

        self.gridLayout_5.addWidget(self.button_folder, 1, 1, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.backup_radio = QRadioButton(self.groupBox_6)
        self.backup_radio.setObjectName(u"backup_radio")
        self.backup_radio.setChecked(True)

        self.horizontalLayout_11.addWidget(self.backup_radio)

        self.git_radio = QRadioButton(self.groupBox_6)
        self.git_radio.setObjectName(u"git_radio")

        self.horizontalLayout_11.addWidget(self.git_radio)


        self.verticalLayout_14.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)


        self.horizontalLayout_12.addLayout(self.verticalLayout_14)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(12)
        self.gridLayout_9.setVerticalSpacing(6)
        self.label_13 = QLabel(self.groupBox_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFrameShape(QFrame.NoFrame)
        self.label_13.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_9.addWidget(self.label_13, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_10.addWidget(self.label_14)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")
        font6 = QFont()
        font6.setPointSize(8)
        self.label_17.setFont(font6)

        self.horizontalLayout_10.addWidget(self.label_17)

        self.level_spin = QSpinBox(self.groupBox_6)
        self.level_spin.setObjectName(u"level_spin")
        self.level_spin.setFont(font6)
        self.level_spin.setMaximum(5)

        self.horizontalLayout_10.addWidget(self.level_spin)


        self.gridLayout_9.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)

        self.dotfiles_list = QListWidget(self.groupBox_6)
        self.dotfiles_list.setObjectName(u"dotfiles_list")
        self.dotfiles_list.setFrameShape(QFrame.StyledPanel)
        self.dotfiles_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.dotfiles_list.setSelectionMode(QAbstractItemView.NoSelection)
        self.dotfiles_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dotfiles_list.setModelColumn(0)
        self.dotfiles_list.setSortingEnabled(True)

        self.gridLayout_9.addWidget(self.dotfiles_list, 2, 1, 1, 1)

        self.apps_list = QListWidget(self.groupBox_6)
        self.apps_list.setObjectName(u"apps_list")
        self.apps_list.setFrameShape(QFrame.StyledPanel)
        self.apps_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.apps_list.setSelectionMode(QAbstractItemView.NoSelection)
        self.apps_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.apps_list.setModelColumn(0)
        self.apps_list.setSortingEnabled(True)

        self.gridLayout_9.addWidget(self.apps_list, 2, 0, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_9)

        self.horizontalLayout_12.setStretch(0, 2)
        self.horizontalLayout_12.setStretch(1, 3)

        self.verticalLayout_15.addWidget(self.groupBox_6)

        self.verticalLayout_15.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_addtask)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.window)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.menu_button.clicked.connect(self.menu_full.show)
        self.menu_button.clicked.connect(self.menu.hide)
        self.menu_full_button.clicked.connect(self.menu.show)
        self.menu_full_button.clicked.connect(self.menu_full.hide)
        self.button_home.toggled.connect(self.button_full_home.setChecked)
        self.button_full_home.toggled.connect(self.button_home.setChecked)
        self.button_backup.toggled.connect(self.button_full_backup.setChecked)
        self.button_full_backup.toggled.connect(self.button_backup.setChecked)
        self.button_reports.toggled.connect(self.button_full_reports.setChecked)
        self.button_full_reports.toggled.connect(self.button_reports.setChecked)
        self.button_settings.toggled.connect(self.button_full_settings.setChecked)
        self.button_full_settings.toggled.connect(self.button_settings.setChecked)
        self.button_about.toggled.connect(self.button_full_about.setChecked)
        self.button_full_about.toggled.connect(self.button_about.setChecked)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.dotfiles_list.setCurrentRow(-1)
        self.apps_list.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menu_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.menu_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(statustip)
        self.menu_button.setText("")
#if QT_CONFIG(statustip)
        self.button_home.setStatusTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(statustip)
        self.button_home.setText("")
#if QT_CONFIG(statustip)
        self.button_backup.setStatusTip(QCoreApplication.translate("MainWindow", u"Backups", None))
#endif // QT_CONFIG(statustip)
        self.button_backup.setText("")
#if QT_CONFIG(statustip)
        self.button_reports.setStatusTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(statustip)
        self.button_reports.setText("")
#if QT_CONFIG(statustip)
        self.button_settings.setStatusTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(statustip)
        self.button_settings.setText("")
#if QT_CONFIG(statustip)
        self.button_about.setStatusTip(QCoreApplication.translate("MainWindow", u"About", None))
#endif // QT_CONFIG(statustip)
        self.button_about.setText("")
#if QT_CONFIG(tooltip)
        self.menu_full_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.menu_full_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(statustip)
        self.menu_full_button.setText(QCoreApplication.translate("MainWindow", u"Dotfile Manager", None))
#if QT_CONFIG(statustip)
        self.button_full_home.setStatusTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(statustip)
        self.button_full_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(statustip)
        self.button_full_backup.setStatusTip(QCoreApplication.translate("MainWindow", u"Backups", None))
#endif // QT_CONFIG(statustip)
        self.button_full_backup.setText(QCoreApplication.translate("MainWindow", u"Backups", None))
#if QT_CONFIG(statustip)
        self.button_full_reports.setStatusTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(statustip)
        self.button_full_reports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
#if QT_CONFIG(statustip)
        self.button_full_settings.setStatusTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(statustip)
        self.button_full_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(statustip)
        self.button_full_about.setStatusTip(QCoreApplication.translate("MainWindow", u"About", None))
#endif // QT_CONFIG(statustip)
        self.button_full_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(statustip)
        self.groupBox.setStatusTip(QCoreApplication.translate("MainWindow", u"Resume", None))
#endif // QT_CONFIG(statustip)
        self.groupBox.setTitle("")
#if QT_CONFIG(statustip)
        self.label.setStatusTip(QCoreApplication.translate("MainWindow", u"Total Tasks", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(statustip)
        self.label_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Total Tasks", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Tasks", None))
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Enabled Tasks", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(statustip)
        self.label_4.setStatusTip(QCoreApplication.translate("MainWindow", u"Enabled Tasks", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enabled Tasks", None))
#if QT_CONFIG(statustip)
        self.label_5.setStatusTip(QCoreApplication.translate("MainWindow", u"Disabled Tasks", None))
#endif // QT_CONFIG(statustip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(statustip)
        self.label_6.setStatusTip(QCoreApplication.translate("MainWindow", u"Disabled Tasks", None))
#endif // QT_CONFIG(statustip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Disabled Tasks", None))
#if QT_CONFIG(statustip)
        self.label_7.setStatusTip(QCoreApplication.translate("MainWindow", u"Total Storage", None))
#endif // QT_CONFIG(statustip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(statustip)
        self.label_8.setStatusTip(QCoreApplication.translate("MainWindow", u"Total Storage", None))
#endif // QT_CONFIG(statustip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None))
#if QT_CONFIG(statustip)
        self.groupBox_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Tasks Info", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_2.setTitle("")
#if QT_CONFIG(statustip)
        self.label_21.setStatusTip(QCoreApplication.translate("MainWindow", u"Tasks Info", None))
#endif // QT_CONFIG(statustip)
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Tasks", None))
#if QT_CONFIG(statustip)
        self.groupBox_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Version Info", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_3.setTitle("")
#if QT_CONFIG(statustip)
        self.label_9.setStatusTip(QCoreApplication.translate("MainWindow", u"Version Info", None))
#endif // QT_CONFIG(statustip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_last_version.setText(QCoreApplication.translate("MainWindow", u"Latest Version", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"0.0.0", None))
        self.last_version.setText(QCoreApplication.translate("MainWindow", u"0.0.0", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Installed Version", None))
        self.check_version.setText("")
        self.label_version_last_update.setText(QCoreApplication.translate("MainWindow", u"Last update:", None))
        self.last_update_version.setText(QCoreApplication.translate("MainWindow", u"0 seg", None))
#if QT_CONFIG(statustip)
        self.groupBox_4.setStatusTip(QCoreApplication.translate("MainWindow", u"Backups Info", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_4.setTitle("")
#if QT_CONFIG(statustip)
        self.label_22.setStatusTip(QCoreApplication.translate("MainWindow", u"Backups Info", None))
#endif // QT_CONFIG(statustip)
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Backups", None))
#if QT_CONFIG(statustip)
        self.groupBox_5.setStatusTip(QCoreApplication.translate("MainWindow", u"Data Base Info", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_5.setTitle("")
#if QT_CONFIG(statustip)
        self.label_10.setStatusTip(QCoreApplication.translate("MainWindow", u"Data Base Info", None))
#endif // QT_CONFIG(statustip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Data Base", None))
        self.label_db_version.setText(QCoreApplication.translate("MainWindow", u"Installed Version", None))
        self.label_db_last_version.setText(QCoreApplication.translate("MainWindow", u"Latest Version", None))
        self.db_last_version.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.db_version.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.check_db_version.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Last update:", None))
        self.last_update_version_db.setText(QCoreApplication.translate("MainWindow", u"0 seg", None))
#if QT_CONFIG(statustip)
        self.new_task.setStatusTip(QCoreApplication.translate("MainWindow", u"New Task", None))
#endif // QT_CONFIG(statustip)
        self.new_task.setText(QCoreApplication.translate("MainWindow", u"New Task", None))
#if QT_CONFIG(statustip)
        self.run_all.setStatusTip(QCoreApplication.translate("MainWindow", u"Run All", None))
#endif // QT_CONFIG(statustip)
        self.run_all.setText(QCoreApplication.translate("MainWindow", u"Run All", None))
#if QT_CONFIG(statustip)
        self.stop_all.setStatusTip(QCoreApplication.translate("MainWindow", u"Stop All", None))
#endif // QT_CONFIG(statustip)
        self.stop_all.setText(QCoreApplication.translate("MainWindow", u"Stop All", None))
#if QT_CONFIG(statustip)
        self.task_area.setStatusTip(QCoreApplication.translate("MainWindow", u"Tasks List", None))
#endif // QT_CONFIG(statustip)
        self.report.setText(QCoreApplication.translate("MainWindow", u"Report", None))
#if QT_CONFIG(statustip)
        self.page_settings.setStatusTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(statustip)
        self.button_reload.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(statustip)
        self.tab_general.setStatusTip(QCoreApplication.translate("MainWindow", u"Settings - General", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QCoreApplication.translate("MainWindow", u"General", None))
#if QT_CONFIG(statustip)
        self.tab_git.setStatusTip(QCoreApplication.translate("MainWindow", u"Settings - Git", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_git), QCoreApplication.translate("MainWindow", u"Git", None))
#if QT_CONFIG(statustip)
        self.tab_ai.setStatusTip(QCoreApplication.translate("MainWindow", u"Settings - AI", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ai), QCoreApplication.translate("MainWindow", u"AI", None))
#if QT_CONFIG(statustip)
        self.tab_notify.setStatusTip(QCoreApplication.translate("MainWindow", u"Settings - Notify", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_notify), QCoreApplication.translate("MainWindow", u"Notify", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"New Task", None))
        self.button_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_6.setTitle("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.button_icon.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Folder", None))
        self.button_folder.setText("")
        self.backup_radio.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.git_radio.setText(QCoreApplication.translate("MainWindow", u"Git", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Aplicaciones", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Dotfiles", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
    # retranslateUi

