"""
Try to create an Andriod app
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HackRTH(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=2))
        view_options = [
            toga.Button('View Tasks', on_press=self.task_view, style=Pack(padding=3)),
            toga.Button('View History', on_press=self.history_view, style=Pack(padding=3)),
            toga.Button('View Points', on_press=self.points_view, style=Pack(padding=3)),
        ]
        for options in view_options:
            main_box.add(options)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def task_view(self, widget):
        new_box = toga.Box()
        self.main_window.title = 'View Tasks'
        path_label = toga.Label(str(dir(self.paths.Path())))
        new_box.add(path_label)
        self.main_window.content = new_box

    def history_view(self, widget):
        new_box = toga.Box()
        self.main_window.title = 'View History'
        self.main_window.content = new_box

    def points_view(self, widget):
        new_box = toga.Box()
        self.main_window.title = 'View Points'
        self.main_window.content = new_box


def main():
    return HackRTH()
