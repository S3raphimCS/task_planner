import sys
# from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtWidgets import QAction, qApp, QMenu, QSystemTrayIcon
from des import *
import sqlite3
import schedule
import datetime


DB_NAME = 'tasks.db'
STATIC_ROOT = 'static/'


def connect_db(db_name):
    try:
        db = sqlite3.connect(db_name)
        cursor = db.cursor()

        return db, cursor
    except Exception as excp:
        print(f"В connect_db возникла ошибка - {excp}")


def close_db(db):
    db.commit()
    if db:
        db.close()
    else:
        print('Возникла ошибка в close_db')


def check_db():
    db, cursor = connect_db(DB_NAME)
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id        INTEGER PRIMARY KEY Autoincrement,
    task      STRING  NOT NULL,
    completed BOOLEAN NOT NULL,
    date      DATE    NOT NULL
);''')


# Поток для отправки уведомлений в фоновом режиме
class NotificationThread(QThread):
    def __init__(self, mainwindow=None, parent=None):
        super().__init__(parent)
        self.mainwindow = mainwindow

    # Получение количества задач на день из БД
    @staticmethod
    def get_number_of_tasks():
        db, cursor = connect_db(DB_NAME)
        date = datetime.date.today()
        query = "SELECT COUNT(*) FROM tasks WHERE date = ? AND completed = 'No'"
        params = (date,)
        cursor.execute(query, params)
        number_of_tasks = cursor.fetchall()[0][0]
        close_db(db)
        return number_of_tasks

    # Логика отправки уведомлений
    def schedule_work(self):
        number_of_tasks = self.get_number_of_tasks()
        if number_of_tasks >= 1:
            self.mainwindow.tray_icon.showMessage(
                "Планировщик задач",
                f"На сегодня у вас осталось невыполненных задач - {number_of_tasks} . Нажмите, чтобы просмотреть их",
                QIcon(STATIC_ROOT + "icon.png"),
                3000
            )

    def run(self):
        schedule.every().hour.do(self.schedule_work)

        while True:
            schedule.run_pending()


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Название окна
        self.setWindowTitle("Планировщик задач")
        self.setWindowIcon(QIcon(STATIC_ROOT + "icon.png"))

        # Настройка трея
        self.notification_sended = False
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(STATIC_ROOT + 'icon.png'))
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.activated.connect(self.open_window_dc)
        self.tray_icon.messageClicked.connect(self.message_clicked)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Подключение функций к кнопкам
        self.calendar_change(init=True)
        self.ui.calendarWidget.selectionChanged.connect(self.calendar_change)
        self.ui.save_changes_button.clicked.connect(self.save_changes)
        self.ui.add_new_button.clicked.connect(self.add_task)
        self.ui.action.triggered.connect(self.about)

        # Запуск потока уведомлений и отправка первого уведомления
        self.notification_thread = NotificationThread(mainwindow=self)
        self.notification_thread.start()
        self.start_notification()

    # Переопределение закрытия приложения в трей
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        event.ignore()
        self.hide()
        if not self.notification_sended:
            self.tray_icon.showMessage(
                "Планировщик задач",
                "Программа была убрана в трей",
                QIcon(STATIC_ROOT + "icon.png"),
                2000,
            )
            self.notification_sended = True

# Нажатие кнопки About
    def about(self):
        QtWidgets.QMessageBox.about(
            self,
            'О программе',
            ' Эта программа предназначена для планирования дел на день с возможностью редактирования задач.\n '
            'Связь с разработчиком - vk.com/s3raphimCS',
        )

# Открытие приложения из трея по двойному нажатию
    def open_window_dc(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show()

# Открытие приложения из нажатия по уведомлению
    def message_clicked(self):
        self.show()
        self.calendar_change(date=datetime.date.today())

# Смена даты в календаре
    def calendar_change(self, init=False, date=None) -> None:
        selected_date = self.ui.calendarWidget.selectedDate().toPyDate()
        if date:
            selected_date = date
        self.update_tasks(selected_date, init=True)

# Начальное уведомление
    def start_notification(self) -> None:
        number = NotificationThread.get_number_of_tasks()
        self.tray_icon.showMessage(
            'Планировщик заданий',
            f'Количество запланированных целей на сегодня - {number}',
            QIcon(STATIC_ROOT + "icon.png"),
            2000,
        )

# Обновление задач в базе данных
    def update_tasks(self, date, init=False) -> None:
        self.ui.listWidget.clear()
        db, cursor = connect_db(DB_NAME)
        query = "SELECT task, completed FROM tasks WHERE date = ?"
        params = (date,)
        results = cursor.execute(query, params).fetchall()
        for row in results:
            item = QtWidgets.QListWidgetItem(row[0])
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            if row[1] == "Yes":
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
            self.ui.listWidget.addItem(item)
        close_db(db)
        if not init:
            self.ui.statusbar.showMessage('Изменения успешно сохранены.', 3000)

# Добавление задачи в БД
    def add_task(self) -> None:
        if self.ui.lineEdit.text():
            task = self.ui.lineEdit.text()
            db, cursor = connect_db(DB_NAME)
            date = self.ui.calendarWidget.selectedDate().toPyDate()
            query = "INSERT INTO tasks(task, completed, date) VALUES (?, ?, ?)"
            params = (task,
                      "No",
                      date,)
            cursor.execute(query, params)
            close_db(db)
        else:
            self.ui.statusbar.showMessage("Строка ввода задачи пуста.", 3000)
            return None
        self.calendar_change()
        self.ui.lineEdit.clear()
        self.ui.statusbar.showMessage("Задание успешно записано.", 3000)

# Обработка кнопки "Сохранить изменения"
    def save_changes(self) -> None:
        db, cursor = connect_db(DB_NAME)
        date = self.ui.calendarWidget.selectedDate().toPyDate()

        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            task = item.text()
            if item.checkState() == Qt.Checked:
                query = "UPDATE tasks SET completed = 'Yes' WHERE task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'No' WHERE task = ? AND date = ?"
            params = (task,
                      date,)
            cursor.execute(query, params)
        close_db(db)
        self.ui.statusbar.showMessage('Изменения успешно сохранены.', 3000)


if __name__ == '__main__':
    check_db()
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
