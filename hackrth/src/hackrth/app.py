"""
Try to create an Andriod app
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from . import refresh_user_menu as rum
# import qr_gen as qrg


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

    def main_view(self, widget):
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

        # path_label = toga.Label(str(toga.app().paths))
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
        # self.main_window.content = new_box

        # Store file in application storage (android)


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
