import os
import sys
import json
import sqlite3
import logging as log

import requests

from engine import search
from version import __version__
from widgets.task_widget import Ui_Form
from ui.main_window import Ui_MainWindow

from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QDateTime, QSize, Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QFileDialog
from PySide6.QtWidgets import QWidget, QMenu, QHeaderView, QTableWidgetItem, QMessageBox

# folders
work_folder = os.path.abspath(os.path.dirname(sys.argv[0]))
config_folder = os.path.join(work_folder, 'config')


def check_essential_files():
    if not os.path.isdir(config_folder):
        log.error("Configuration folder not found")
        return False

    if not os.path.isfile(f'{config_folder}/config.json'):
        log.error("The config.json file cannot be found")

        with open(f'{config_folder}/config.json', 'w') as f:
            data = {
                "last_update": None,
                "last_update_db": None
            }
            f.write(json.dumps(data, indent=2))

        log.info("The config.json file has been created")

    if not os.path.isfile(f'{config_folder}/tasks.json'):
        log.error("The tasks.json file cannot be found")

        with open(f'{config_folder}/tasks.json', 'w') as f:
            data = {}
            f.write(json.dumps(data, indent=2))

        log.info("The tasks.json file has been created")

    return True


def get_db_version():
    global conn
    try:
        conn = sqlite3.connect(f"{config_folder}/dotfiles.db")
        cursor = conn.cursor()
        cursor.execute("SELECT version FROM db_version ORDER BY id DESC LIMIT 1")
        version = cursor.fetchone()[0]

    except sqlite3.Error as e:
        log.error(f"Error connecting to database: {e}")
        version = None

    finally:
        if conn:
            conn.close()

    log.info(f"Current db version: {version}")
    return version


def get_data_config(value):
    try:
        with open(f'{config_folder}/config.json', 'r') as f:
            data = json.load(f)

        return data[value]

    except (FileNotFoundError, json.JSONDecodeError) as e:
        log.error(f"Error handling config.json file: {e}")
        return None


def save_data_config(value, data):
    try:
        with open(f'{config_folder}/config.json', 'r') as f:
            config = json.load(f)

        config[value] = data
        with open(f'{config_folder}/config.json', 'w') as f:
            f.write(json.dumps(config, indent=2))

    except (FileNotFoundError, json.JSONDecodeError) as e:
        log.error(f"Error handling config.json file: {e}")


def load_task_file():
    try:
        with open(f'{config_folder}/tasks.json', 'r') as file:
            tasks = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        log.error(f"Error handling tasks.json file: {e}")
        tasks = {}

    return tasks


def save_task_file(task):
    try:
        with open(f'{config_folder}/tasks.json', 'w') as file:
            json.dump(task, file, indent=2)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        log.error(f"Error handling tasks.json file: {e}")


def check_new_version():
    time_now = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm")

    # Comprueba en Github si hay una nueva versión

    save_data_config("last_update", time_now)
    log.debug(f"Last update: {time_now}")

    return time_now


def check_db_new_version():
    time_now = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm")

    url = f"https://api.github.com/repos/TRuHa83/Dotfiles-Manager/releases"
    response = requests.get(url)

    tag = None
    if response.status_code == 200:
        releases = response.json()
        for release in releases:
            tag = release["tag_name"]

    save_data_config("last_update_db", time_now)
    log.debug(f"Last database update: {time_now}")

    return tag, time_now


class ReportInject(log.Handler):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


class TaskWidget(QWidget, Ui_Form):
    def __init__(self, parent=None, main_window=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

        self.main_window = main_window
        task = self.main_window.task

        # obtiene el primer key del dict data
        self.time = list(task.keys())[0]
        self.data = task[self.time]

        icon = QIcon()
        img = self.data["icon"]
        icon.addFile(img, QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.icon_widget.setIcon(icon)
        self.icon_widget.setIconSize(QSize(48, 48))

        self.label_name.setText(self.data["name"])

        timestamp = QDateTime.fromSecsSinceEpoch(int(self.time))
        self.label_create.setText(timestamp.toString("yyyy/MM/dd hh:mm"))

        self.menu = QMenu(self)

        option_edit = QAction("Edit", self)
        option_remove = QAction("Remove", self)

        option_edit.triggered.connect(self.edit)
        option_remove.triggered.connect(self.remove)

        self.menu.addAction(option_edit)
        self.menu.addAction(option_remove)

        self.button_options.setMenu(self.menu)

        self.button_start_backup.clicked.connect(self.start_backup)
        self.button_retore.clicked.connect(self.restore)

    def start_backup(self):
        print("Backup")

    def restore(self):
        print("Restore")

    @Slot()
    def edit(self):
        self.main_window.timestamp = self.time
        self.main_window.title.setText("Edit Task")
        self.main_window.name_task.setText(self.data["name"])
        self.main_window.folder_task.setText(self.data["folder"])

        icon = QIcon()
        img = self.data["icon"]
        icon.addFile(img, QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        if self.data["mode"] == "backup":
            self.main_window.backup_radio.setChecked(True)
        else:
            self.main_window.git_radio.setChecked(True)

        self.main_window.level_spin.setValue(self.data["level"])

        self.main_window.switch_taskPage()

        for i in range(self.main_window.apps_list.count()):
            item = self.main_window.apps_list.item(i)
            if item.text() in self.data["apps"]:
                item.setCheckState(Qt.Checked)

    @Slot()
    def remove(self):
        self.main_window.remove_task(self.time)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, level_log=log.INFO):
        super().__init__()
        self.applications = None
        self.default_icon = None
        self.timestamp = None
        self.task = None
        self.state_task = False
        self.state = 'home'
        self.level_log = level_log
        self.level_value = 0
        self.applications = {}
        self.user_files = []
        self.dotfiles = []
        self.widgets = []

        self.setupUi(self)

        self.setWindowTitle("Dotfile Manager")
        self.setFixedSize(800, 500)

        self.configure_logging()
        self.menu_full.setHidden(True)

        log.debug("Connecting signals")
        self.check_version.clicked.connect(self.new_version)
        self.check_db_version.clicked.connect(self.new_db_version)

        self.button_home.clicked.connect(self.switch_homePage)
        self.button_full_home.clicked.connect(self.switch_homePage)

        self.button_backup.clicked.connect(self.switch_backupPage)
        self.button_full_backup.clicked.connect(self.switch_backupPage)

        self.button_reports.clicked.connect(self.switch_reportPage)
        self.button_full_reports.clicked.connect(self.switch_reportPage)

        self.button_settings.clicked.connect(self.switch_settingsPage)
        self.button_full_settings.clicked.connect(self.switch_settingsPage)

        self.button_about.clicked.connect(self.switch_aboutPage)
        self.button_full_about.clicked.connect(self.switch_aboutPage)

        self.new_task.clicked.connect(self.switch_taskPage)

        self.apps_list.itemChanged.connect(self.list_dotfiles)
        self.level_spin.valueChanged.connect(self.change_level)

        self.button_folder.clicked.connect(self.select_folder)

        self.backup_radio.clicked.connect(self.select_backup_mode)
        self.git_radio.clicked.connect(self.select_git_mode)

        self.button_add.clicked.connect(self.save_task)
        self.button_cancel.clicked.connect(self.cancel_task)

        self.load_info()

    def configure_logging(self):
        self.looger = log.getLogger()
        self.looger.setLevel(self.level_log)

        handler = ReportInject(self.report)
        handler.setFormatter(log.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                            datefmt='%d-%m-%Y %H:%M:%S'))

        self.looger.addHandler(handler)

    def new_version(self):
        self.last_update_version.setText(check_new_version())

    def new_db_version(self):
        version, date = check_db_new_version()
        self.db_last_version.setText(version)
        self.last_update_version_db.setText(date)

    def switch_homePage(self):
        if self.state != 'home':
            self.state = 'home'
            log.debug("Home Page")

            self.load_info()

            self.stackedWidget.setCurrentIndex(0)

    def switch_backupPage(self):
        if self.state_task and self.state != 'task':
            self.state = 'task'
            self.stackedWidget.setCurrentIndex(5)

        elif not self.state_task and self.state != 'backup':
            self.state = 'backup'
            log.debug("Task page")

            self.stackedWidget.setCurrentIndex(1)
            self.update_widgets_task()

    def switch_reportPage(self):
        if self.state != 'report':
            self.state = 'report'
            log.debug("Report page")

            self.stackedWidget.setCurrentIndex(2)

    def switch_settingsPage(self):
        if self.state != 'settings':
            self.state = 'settings'
            log.debug("Settings page")

            self.stackedWidget.setCurrentIndex(3)

    def switch_aboutPage(self):
        if self.state != 'about':
            self.state = 'about'
            log.debug("About page")

            self.stackedWidget.setCurrentIndex(4)

    def switch_taskPage(self):
        log.debug("Creating task")
        self.stackedWidget.setCurrentIndex(5)
        self.state_task = True
        self.state = 'task'

        log.debug("Task status changes to %s", self.state_task)

        self.load_apps()

    def load_info(self):
        log.debug("Loading information home page")
        tasks = load_task_file()

        total_tasks = len(tasks)
        self.total_tasks.setText(str(total_tasks))

        backup_tasks = 0
        git_tasks = 0
        for task in tasks:
            if tasks[task]["mode"] == "backup":
                backup_tasks += 1
            else:
                git_tasks += 1

        self.count_backup_tasks.setText(str(backup_tasks))
        self.count_git_tasks.setText(str(git_tasks))

        git = self.git_tasks
        backup = self.backup_tasks
        widgets = [git, backup]

        for widget in widgets:
            for i in range(widget.rowCount()):
                widget.removeRow(0)

            widget.setHorizontalHeaderLabels(["Name", "Path", "Mode"])
            widget.horizontalHeader().setStretchLastSection(True)
            widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        def show_tasks(task, widget):
            data = {task: tasks[task]}

            name = data[task]["name"]
            path = data[task]["folder"]
            mode = data[task]["mode"]

            widget.insertRow(widget.rowCount())
            widget.setItem(widget.rowCount() - 1, 0, QTableWidgetItem(name))
            widget.setItem(widget.rowCount() - 1, 1, QTableWidgetItem(path))
            widget.setItem(widget.rowCount() - 1, 2, QTableWidgetItem(mode))

        for task in tasks:
            widget = backup
            if tasks[task]["mode"] == "git":
                widget = git

            show_tasks(task, widget)

        log.info("Current version: %s", __version__)
        self.version.setText(__version__)
        self.db_version.setText(get_db_version())

        last_get_update = get_data_config("last_update")
        last_get_db_update = get_data_config("last_update_db")

        self.last_update_version.setText(last_get_update)
        self.last_update_version_db.setText(last_get_db_update)

    def remove_widgets_task(self):
        if not self.task_scrollarea.layout().isEmpty():
            log.debug("Cleaning up tasks")
            for widget in self.widgets:
                self.task_scrollarea.layout().removeWidget(widget)
                widget.deleteLater()

            self.task_scrollarea.layout().removeItem(self.task_scrollarea.layout().itemAt(0))
            self.widgets.clear()

    def update_widgets_task(self):
        self.remove_widgets_task()

        log.debug("Loading tasks")
        tasks = load_task_file()

        if tasks:
            for task in tasks:
                data = {task: tasks[task]}
                self.add_task(data)

            self.task_scrollarea.layout().addStretch()

    def add_task(self, task):
        self.task = task
        log.debug("Adding task: %s", task)

        widget = TaskWidget(self, main_window=self)

        self.widgets.append(widget)
        self.task_scrollarea.layout().addWidget(widget)

        self.task.clear()

    def remove_task(self, task):
        log.warning(f'Delete task: {task}?')

        reply = QMessageBox.question(self, 'Confirm Deletion',
                                     f"Are you sure you want to delete the task?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            log.info("Task deleted")

            data = load_task_file()
            data.pop(task)
            save_task_file(data)

            self.update_widgets_task()

        else:
            log.info("Task deletion cancelled")

    def addAppsToList(self, apps):
        for app in apps:
            item = QListWidgetItem(app)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
            item.setCheckState(Qt.Unchecked)

            self.apps_list.addItem(item)

    def change_level(self, value):
        log.debug("Changing priority level to %s", value)
        app_newlevel = search.list_apps(self.user_files, self.level_spin.value())

        log.debug("Upgrading applications to a new level")
        items = {}
        for i in range(self.apps_list.count()):
            item = self.apps_list.item(i)
            items[item.text()] = item

        if value > self.level_value:
            appstoremove = self.applications.keys() - app_newlevel.keys()
            self.applications = app_newlevel

            for app in appstoremove:
                if app in items:
                    self.apps_list.takeItem(self.apps_list.row(items[app]))

        elif value < self.level_value:
            appstoadd = app_newlevel.keys() - self.applications.keys()
            self.applications = app_newlevel

            self.addAppsToList(appstoadd)

        self.list_dotfiles()
        self.level_value = value

    def load_apps(self):
        log.debug("Loading applications")
        self.apps_list.clear()

        self.user_files, self.user_folders, self.config_files, self.config_folders = search.dotfiles()
        self.applications = search.list_apps(self.user_files, self.level_spin.value())

        log.debug("Loaded applications: %s", self.applications.keys())
        self.addAppsToList(self.applications.keys())

    def list_dotfiles(self):
        log.debug("Listing configuration files")
        self.dotfiles_list.clear()
        self.dotfiles.clear()

        for i in range(self.apps_list.count()):
            item = self.apps_list.item(i)
            if item.checkState() == Qt.Checked:
                self.select_icon(item.text())
                for file in self.applications[item.text()]:
                    dotfile = QListWidgetItem(file["path"])
                    self.dotfiles_list.addItem(dotfile)
                    self.dotfiles.append(file["path"])

        log.debug("Selected configuration files: %s", self.dotfiles)

    def select_icon(self, application):
        icon = QIcon()

        log.debug("Looking for icon for %s", application)
        img = search.icons(application.lower())
        if img is None:
            log.debug("Icon not found, default icon set")
            img = work_folder + "/assets/icon24x24.png"

        self.default_icon = img
        icon.addFile(img, QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.button_icon.setIcon(icon)
        self.button_icon.setIconSize(QSize(48, 48))

    def select_folder(self):
        log.debug("Select folder")
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_task.setText(folder)
            log.debug("Selected folder: %s", folder)

    def select_backup_mode(self):
        log.debug("Select backup mode")

    def select_git_mode(self):
        log.debug("Select git mode")

    def clear_fields(self):
        log.debug("Clearing fields")
        self.timestamp = None
        self.state_task = False

        log.debug("Task status changes to %s", self.state_task)

        self.title.setText("New Task")

        self.name_task.clear()
        self.folder_task.clear()

        self.default_icon = None

        icon = QIcon()
        img = work_folder + "/assets/icon24x24.png"
        icon.addFile(img, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_icon.setIcon(icon)
        self.button_icon.setIconSize(QSize(48, 48))

        self.backup_radio.setChecked(True)

        self.apps_list.clear()
        self.dotfiles_list.clear()

    def cancel_task(self):
        log.info("Task cancelled")
        self.clear_fields()
        self.switch_backupPage()

    def save_task(self):
        log.info("Saving task")
        if self.timestamp is None:
            self.timestamp = QDateTime.currentDateTime().toSecsSinceEpoch()

        log.debug("Timestamp: %s", self.timestamp)
        log.debug("Collecting data")

        name = self.name_task.text()
        folder = self.folder_task.text()
        icon = self.default_icon
        mode = "backup" if self.backup_radio.isChecked() else "git"
        level = self.level_spin.value()
        files = self.dotfiles
        apps = []
        for i in range(self.apps_list.count()):
            item = self.apps_list.item(i)
            if item.checkState() == Qt.Checked:
                apps.append(item.text())

        task = {
            self.timestamp: {
                "name": name,
                "folder": folder,
                "icon": icon,
                "mode": mode,
                "level": level,
                "apps": apps,
                "files": files
            }
        }

        data = load_task_file()
        data.update(task)
        save_task_file(data)

        log.info("Task saved: %s", task[self.timestamp]["name"])

        self.clear_fields()
        self.switch_backupPage()


if __name__ == '__main__':
    level = log.INFO
    if "--debug" in sys.argv:
        level = log.DEBUG

    if check_essential_files():
        app = QApplication(sys.argv)

        window = MainWindow(level_log=level)
        window.show()

        app.exec()
