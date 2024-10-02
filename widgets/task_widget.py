# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import ui.recursos_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(539, 132)
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
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_widget = QPushButton(self.groupBox)
        self.icon_widget.setObjectName(u"icon_widget")
        icon = QIcon()
        icon.addFile(u":/icons/assets/icon24x24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_widget.setIcon(icon)
        self.icon_widget.setIconSize(QSize(48, 48))
        self.icon_widget.setFlat(True)

        self.horizontalLayout_3.addWidget(self.icon_widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.groupBox)
        self.label_name.setObjectName(u"label_name")
        font = QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.label_name.setFont(font)
        self.label_name.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout.addWidget(self.label)

        self.label_create = QLabel(self.groupBox)
        self.label_create.setObjectName(u"label_create")
        self.label_create.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.label_create)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


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
        self.button_start_backup.setText(QCoreApplication.translate("Form", u"Backup", None))
        self.button_retore.setText(QCoreApplication.translate("Form", u"Restore", None))
        self.button_options.setText(QCoreApplication.translate("Form", u"Options", None))
    # retranslateUi

