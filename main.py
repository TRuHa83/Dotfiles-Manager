import os
import sys
import json
import sqlite3
import logging as log

from engine import search
from version import __version__
from widgets.task_widget import Ui_Form
from ui.main_window import Ui_MainWindow
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QDateTime, QSize, Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QFileDialog, QWidget, QMenu

# folders
work_folder = os.path.abspath(os.path.dirname(sys.argv[0]))
config_folder = os.path.join(work_folder, 'config')


# Configuracion logs
def configure_logging(level=log.INFO):
    log.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S',
        level=level,
        handlers=[
            log.StreamHandler()
        ]
    )


def check_esencials_files():
    if not os.path.isdir(config_folder):
        log.error("No se encuentra la carpeta de configuración")
        return False

    if not os.path.isfile(f"{config_folder}/config.json"):
        log.error("No se encuentra el archivo config.json")
        return False

    if not os.path.isfile(f"{config_folder}/tasks.json"):
        log.error("No se encuentra el archivo tasks.json")
        return False

    return True


def get_db_version():
    try:
        conn = sqlite3.connect(f"{config_folder}/dotfiles.db")
        cursor = conn.cursor()
        cursor.execute("SELECT version FROM db_version ORDER BY id DESC LIMIT 1")
        version = cursor.fetchone()[0]

    except sqlite3.Error as e:
        log.error(f"Error al conectar con la base de datos: {e}")
        version = None

    finally:
        if conn:
            conn.close()

    log.info(f"Versión de la base de datos: {version}")
    return version


def get_last_update():
    try:
        with open(f'{config_folder}/config.json', 'r') as f:
            data = json.load(f)
        return data["last_update"]

    except (FileNotFoundError, json.JSONDecodeError) as e:
        log.error(f"Error al manejar el archivo config.json: {e}")
        return None


def get_last_update_db():
    try:
        with open(f'{config_folder}/config.json', 'r') as f:
            data = json.load(f)
        return data["last_update_db"]

    except (FileNotFoundError, json.JSONDecodeError) as e:
        log.error(f"Error al manejar el archivo config.json: {e}")
        return None


def check_new_version():
    time_now = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm")
    try:
        with open(f'{config_folder}/config.json', 'r') as f:
            data = json.load(f)

        # Comprueba en Github si hay una nueva versión

        data["last_update"] = time_now
        with open(f'{config_folder}/config.json', 'w') as f:
            f.write(json.dumps(data, indent=2))

        log.debug(f"Última actualización: {time_now}")
        return time_now

    except (FileNotFoundError, json.JSONDecodeError) as e:
        log.error(f"Error al manejar el archivo config.json: {e}")
        return None


def check_db_new_version():
    time_now = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm")

    try:
        with open(f'{config_folder}/config.json', 'r') as f:
            data = json.load(f)

        # Comprueba en Github si hay una nueva versión

        data["last_update_db"] = time_now
        with open(f'{config_folder}/config.json', 'w') as f:
            f.write(json.dumps(data, indent=2))

        log.debug(f"Última actualización de la base de datos: {time_now}")
        return time_now

    except (FileNotFoundError, json.JSONDecodeError) as e:
        log.error(f"Error al manejar el archivo config.json: {e}")
        return None


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
    def __init__(self):
        super().__init__()
        log.info("Inicializando MainWindow")
        log.debug("Configurando variables iniciales")
        self.applications = None
        self.default_icon = None
        self.timestamp = None
        self.state_task = False
        self.state = 'home'
        self.level_value = 0
        self.applications = {}
        self.user_files = []
        self.dotfiles = []
        self.widgets = []

        log.debug("Configurando interfaz")
        self.setupUi(self)
        self.setWindowTitle("Dotfile Manager")
        self.setFixedSize(800, 500)

        self.menu_full.setHidden(True)

        log.info("Version actual: %s", __version__)
        self.version.setText(__version__)
        self.last_update_version.setText(get_last_update())
        self.db_version.setText(get_db_version())
        self.last_update_version_db.setText(get_last_update_db())

        log.debug("Conectando señales")
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

    def new_version(self):
        self.last_update_version.setText(check_new_version())

    def new_db_version(self):
        self.last_update_version_db.setText(check_db_new_version())

    def switch_homePage(self):
        log.debug("Página de inicio")
        self.stackedWidget.setCurrentIndex(0)

    def switch_backupPage(self):
        if self.state_task:
            self.stackedWidget.setCurrentIndex(5)

        else:
            log.debug("Página de tareas")
            self.stackedWidget.setCurrentIndex(1)

            if not self.task_scrollarea.layout().isEmpty():
                log.debug("Limpiando tareas")
                for widget in self.widgets:
                    self.task_scrollarea.layout().removeWidget(widget)
                    widget.deleteLater()

                self.task_scrollarea.layout().removeItem(self.task_scrollarea.layout().itemAt(0))
                self.widgets.clear()

            try:
                with open(f"{config_folder}/tasks.json", 'r') as file:
                    tasks = json.load(file)

            except (FileNotFoundError, json.JSONDecodeError) as e:
                log.error(f"Error al manejar el archivo tasks.json: {e}")
                tasks = {}

            log.debug("Cargando tareas")
            for task in tasks:
                data = {task: tasks[task]}
                self.add_task(data)

            self.task_scrollarea.layout().addStretch()

    def switch_reportPage(self):
        log.debug("Página de reportes")
        self.stackedWidget.setCurrentIndex(2)

    def switch_settingsPage(self):
        log.debug("Página de configuración")
        self.stackedWidget.setCurrentIndex(3)

    def switch_aboutPage(self):
        log.debug("Página acerca de...")
        self.stackedWidget.setCurrentIndex(4)

    def switch_taskPage(self):
        log.debug("Creando tarea")
        self.stackedWidget.setCurrentIndex(5)
        self.state_task = True
        log.debug("Estado de tarea pasa a %s", self.state_task)

        self.load_apps()

    def add_task(self, task):
        self.task = task
        log.debug("Añadiendo tarea: %s", task)

        widget = TaskWidget(self, main_window=self)
        self.widgets.append(widget)
        self.task_scrollarea.layout().addWidget(widget)

    def remove_task(self, task):
        log.info("Eliminando tarea: %s", task)

        try:
            with open(f'{config_folder}/tasks.json', 'r+') as file:
                data = json.load(file)
                data.pop(task)
                file.seek(0)
                json.dump(data, file, indent=2)
                file.truncate()

        except (FileNotFoundError, json.JSONDecodeError) as e:
            log.error(f"Error al manejar el archivo tasks.json: {e}")

        self.switch_backupPage()

    def addAppsToList(self, apps):
        for app in apps:
            item = QListWidgetItem(app)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
            item.setCheckState(Qt.Unchecked)

            self.apps_list.addItem(item)

    def change_level(self, value):
        log.debug("Cambiando nivel de prioridad a %s", value)
        app_newlevel = search.list_apps(self.user_files, self.level_spin.value())

        log.debug("Actualizando aplicaciones a nuevo nivel")
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
        log.debug("Cargando aplicaciones")
        self.apps_list.clear()

        self.user_files, self.user_folders, self.config_files, self.config_folders = search.dotfiles()
        self.applications = search.list_apps(self.user_files, self.level_spin.value())

        log.debug("Aplicaciones cargadas: %s", self.applications.keys())
        self.addAppsToList(self.applications.keys())

    def list_dotfiles(self):
        log.debug("Listando archivos de configuración")
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

        log.debug("Archivos de configuración seleccionados: %s", self.dotfiles)

    def select_icon(self, application):
        icon = QIcon()

        log.debug("Buscando icono para %s", application)
        img = search.icons(application.lower())
        if img is None:
            log.debug("Icono no encontrado, se establece icono por defecto")
            img = work_folder + "/assets/icon24x24.png"

        self.default_icon = img
        icon.addFile(img, QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.button_icon.setIcon(icon)
        self.button_icon.setIconSize(QSize(48, 48))

    def select_folder(self):
        log.debug("Seleccionar carpeta")
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta")
        if folder:
            self.folder_task.setText(folder)
            log.debug("Carpeta seleccionada: %s", folder)

    def select_backup_mode(self):
        log.debug("Seleccionar modo de backup")

    def select_git_mode(self):
        log.debug("Seleccionar modo de git")

    def clear_fields(self):
        log.debug("Limpiando campos")
        self.timestamp = None
        self.state_task = False

        log.debug("Estado de tarea pasa a %s", self.state_task)

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
        log.info("Tarea cancelada")
        self.clear_fields()
        self.switch_backupPage()

    def save_task(self):
        log.info("Guardando tarea")
        if self.timestamp is None:
            self.timestamp = QDateTime.currentDateTime().toSecsSinceEpoch()

        log.debug("Timestamp: %s", self.timestamp)
        log.debug("Recopilando datos")

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

        try:
            with open(f'{config_folder}/tasks.json', 'r+') as file:
                data = json.load(file)
                data.update(task)
                file.seek(0)
                json.dump(data, file, indent=2)
                file.truncate()

        except (FileNotFoundError, json.JSONDecodeError) as e:
            log.error(f"Error al manejar el archivo tasks.json: {e}")

        log.info("Tarea guardada")

        self.clear_fields()
        self.switch_backupPage()


if __name__ == '__main__':
    level = log.INFO
    if "--debug" in sys.argv:
        level = log.DEBUG

    configure_logging(level)

    if check_esencials_files():
        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()

        app.exec()
