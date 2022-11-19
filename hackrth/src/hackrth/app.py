"""
Try to create an Andriod app
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from . import refresh_user_menu as rum
# import qr_gen as qrg
def task_menu():
    # time = 6
    # days_passed = 0

    # #refresh menu
    # if time != 6:
    #     #wait 1 hour
    #     time += 1
    #     if time == 24:
    #         time = 0
    #         days_passed += 1
    #     else:
    #         rum.print_menu()
    #         #wait 1 hour
    #         time += 1 
    return rum.print_menu()

class HackRTH(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
##create window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_view()
        self.main_window.show()

    def main_view(self, widget=None):
        ##split 2 into view and start up
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=2))
        view_options = [
            toga.Button('View Tasks', on_press=self.task_view, style=Pack(padding=3)),
            toga.Button('View History', on_press=self.history_view, style=Pack(padding=3)),
            toga.Button('View Points', on_press=self.points_view, style=Pack(padding=3)),
        ]
        for options in view_options:
            main_box.add(options)
        self.main_window.title = self.formal_name
        self.main_window.content = main_box

    def task_view(self, widget):
        new_box = toga.Box()
        self.main_window.title = 'View Tasks'
        new_box.add(toga.Button('Back', on_press=self.main_view, style=Pack(padding=3)))
        task_list=task_menu()
        view_options = [
            toga.Button(task_list[0], on_press=self.task_view, style=Pack(padding=3)),
            toga.Button(task_list[1], on_press=self.history_view, style=Pack(padding=3)),
            toga.Button(task_list[2], on_press=self.points_view, style=Pack(padding=3)),
        ]
        for options in view_options:
            new_box.add(options)
        self.main_window.content = new_box




    def history_view(self, widget):
        new_box = toga.Box()
        self.main_window.title = 'View History'
        new_box.add(toga.Button('Back', on_press=self.main_view, style=Pack(padding=3)))
        self.main_window.content = new_box

    def points_view(self, widget):
        new_box = toga.Box()
        self.main_window.title = 'View Points'
        new_box.add(toga.Button('Back', on_press=self.main_view, style=Pack(padding=3)))
        self.main_window.content = new_box


def main():
    return HackRTH()
