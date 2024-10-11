# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import ui.recursos_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(807, 173)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	background-color: #28292a\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: #28292a\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_widget = QPushButton(self.groupBox)
        self.icon_widget.setObjectName(u"icon_widget")
        icon = QIcon()
        icon.addFile(u":/icons/assets/icon24x24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_widget.setIcon(icon)
        self.icon_widget.setIconSize(QSize(48, 48))
        self.icon_widget.setFlat(True)

        self.horizontalLayout.addWidget(self.icon_widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.groupBox)
        self.label_name.setObjectName(u"label_name")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label_name.setFont(font)
        self.label_name.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_name)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(6)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_create = QLabel(self.groupBox)
        self.label_create.setObjectName(u"label_create")
        font1 = QFont()
        font1.setBold(True)
        self.label_create.setFont(font1)
        self.label_create.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_create)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_folder = QLabel(self.groupBox)
        self.label_folder.setObjectName(u"label_folder")
        self.label_folder.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_folder)


        self.verticalLayout.addLayout(self.formLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(38, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"	background-color: #1d1e20;\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: #1d1e20;\n"
"}\n"
"")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(10)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(8)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.label_status = QLabel(self.groupBox_2)
        self.label_status.setObjectName(u"label_status")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.label_status.setFont(font3)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_status)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_mode = QLabel(self.groupBox_2)
        self.label_mode.setObjectName(u"label_mode")
        self.label_mode.setFont(font3)
        self.label_mode.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_mode)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.label_last_run = QLabel(self.groupBox_2)
        self.label_last_run.setObjectName(u"label_last_run")
        self.label_last_run.setFont(font3)
        self.label_last_run.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_last_run)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(28, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.button_start_backup = QPushButton(self.groupBox)
        self.button_start_backup.setObjectName(u"button_start_backup")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_start_backup.setIcon(icon1)
        self.button_start_backup.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_start_backup)

        self.button_retore = QPushButton(self.groupBox)
        self.button_retore.setObjectName(u"button_retore")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/backup_restore.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_retore.setIcon(icon2)
        self.button_retore.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_retore)

        self.button_options = QPushButton(self.groupBox)
        self.button_options.setObjectName(u"button_options")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_options.setIcon(icon3)
        self.button_options.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_options)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.horizontalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.icon_widget.setText("")
        self.label_name.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label.setText(QCoreApplication.translate("Form", u"Created:", None))
        self.label_create.setText(QCoreApplication.translate("Form", u"yyyy/MM/DD hh:mm", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Folder:", None))
        self.label_folder.setText(QCoreApplication.translate("Form", u"path", None))
        self.groupBox_2.setTitle("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.label_status.setText(QCoreApplication.translate("Form", u"null", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"mode:", None))
        self.label_mode.setText(QCoreApplication.translate("Form", u"null", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Last run:", None))
        self.label_last_run.setText(QCoreApplication.translate("Form", u"null", None))
        self.button_start_backup.setText(QCoreApplication.translate("Form", u"Backup", None))
        self.button_retore.setText(QCoreApplication.translate("Form", u"Restore", None))
        self.button_options.setText(QCoreApplication.translate("Form", u"Actions", None))
    # retranslateUi

