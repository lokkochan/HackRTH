"""
Try to create an Andriod app
"""
import os
import random
import json
import urllib.request
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from . import refresh_user_menu as rum


class HackRTH(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        # create window
        self.main_window = toga.MainWindow(title=self.formal_name)
        # Read stored data
        data_dir = os.path.join(self.paths.data, 'data.json')
        self.data_dir = data_dir
        # Load data and show main view if data exists, else ask for name and create data

        if os.path.exists(data_dir):
            with open(data_dir) as f:
                self.data = json.load(f)
            self.main_view()
        else:
            self.data = {
                "points": 0,
                "history": []
            }
            self.ask_for_name_view()
        self.main_window.show()

    def main_view(self, widget=None):
        # split 2 into view and start up
        main_box = toga.Box(children=[
            toga.Label(f'Welcome, {self.data["name"]}', style=Pack(padding=3)),
            toga.Button('View Tasks', on_press=self.task_view, style=Pack(padding=3)),
            toga.Button('View History', on_press=self.history_view, style=Pack(padding=3)),
            toga.Button('View Points', on_press=self.points_view, style=Pack(padding=3)),
            toga.Button('Log out', on_press=self.ask_for_name_view, style=Pack(padding=3))
        ], style=Pack(direction=COLUMN, padding=2))
        self.main_window.title = self.formal_name
        self.main_window.content = main_box

    def ask_for_name_view(self, widget=None):
        self.main_window.title = 'Welcome to HackRTH'
        self.name_input = toga.TextInput(style=Pack(flex=1))
        self.main_window.content = toga.Box(
            children=[
                toga.Label('Please enter your name?'),
                self.name_input,
                toga.Button('Submit', on_press=self.name_set_view, style=Pack(padding=5))
            ],
            style=Pack(
                direction=COLUMN,
                padding=5
            )
        )

    def name_set_view(self, widget):
        self.data['name'] = self.name_input.value
        self.save_data()
        self.main_view()

    def task_view(self, widget):
        self.main_window.title = 'View Tasks'
        task_list = rum.print_menu()
        new_box = toga.Box(children=[
            toga.Button('Back', on_press=self.main_view, style=Pack(padding=3)),
            toga.Box(children=[toga.Button((task_list[0][0]), on_press=self.work_done_view, style=Pack(padding=3), id=f'{task_list[0][1]},{task_list[0][0]}'), toga.Label(f'{str(task_list[0][1])} points')], style=Pack(direction=ROW, padding=3, alignment='right')),
            toga.Box(children=[toga.Button((task_list[1][0]), on_press=self.work_done_view, style=Pack(padding=3), id=f'{task_list[1][1]},{task_list[1][0]}'), toga.Label(f'{str(task_list[1][1])} points')], style=Pack(direction=ROW, padding=3, alignment='right')),
            toga.Box(children=[toga.Button((task_list[2][0]), on_press=self.work_done_view, style=Pack(padding=3), id=f'{task_list[2][1]},{task_list[2][0]}'), toga.Label(f'{str(task_list[2][1])} points')], style=Pack(direction=ROW, padding=3, alignment='right'))
        ], style=Pack(direction=COLUMN, padding=3))
        self.main_window.content = new_box

    def work_done_view(self, widget):
        new_box = toga.Box(style=Pack(direction=COLUMN, padding=3))
        self.main_window.title = 'Work Done'
        points_gained, task_type = widget.id.split(',')
        new_box.add(toga.Label(f"Congrats!! you earn {points_gained} points~"))
        points_gained, task_type = int(points_gained), task_type
        new_box.add(toga.Button('Complete', on_press=self.main_view, style=Pack(padding=3)))
        self.data['points'] += points_gained
        self.data['history'].append([task_type, points_gained])
        self.save_data()
        self.main_window.content = new_box

    def history_view(self, widget):
        new_box = toga.Box(children=[
            toga.Button('Back', on_press=self.main_view, style=Pack(padding=3)),
            toga.Button('Clear History', on_press=self.clear_confirm_view, style=Pack(padding=3)),
            toga.ScrollContainer(content=toga.Box(children=[toga.Label(f'{task_type}: {points}') for task_type, points in self.data['history']], style=Pack(direction=COLUMN, padding=3)))
        ], style=Pack(direction=COLUMN, padding=3))
        self.main_window.title = 'View History'
        new_box.add()
        self.main_window.content = new_box

    def clear_confirm_view(self, widget):
        new_box = toga.Box(children=[
            toga.Label('Are you sure you want to clear your history?'),
            toga.Box(children=[
                toga.Button('Yes', on_press=self.clear_history_view, style=Pack(padding=3)),
                toga.Button('No', on_press=self.history_view, style=Pack(padding=3))
            ], style=Pack(direction=ROW, padding=2))
        ], style=Pack(direction=COLUMN, padding=3))
        self.main_window.title = 'Reset Points'
        self.main_window.content = new_box

    def clear_history_view(self, widget):
        new_box = toga.Box(style=Pack(direction=COLUMN, padding=3))
        self.main_window.title = 'Clear History'
        new_box.add(toga.Label("Your history has been cleared"))
        new_box.add(toga.Button('Complete', on_press=self.main_view, style=Pack(padding=3)))
        self.data['history'] = []
        self.save_data()
        self.main_window.content = new_box

    def points_view(self, widget):
        new_box = toga.Box(children=[
            toga.Button('Back', on_press=self.main_view, style=Pack(padding=3)),
            toga.Label(f"You have got {self.data['points']} points."),
        ], style=Pack(direction=COLUMN, padding=3))
        if self.data['points'] > 0:
            new_box.add(
                toga.Button('Redeem', on_press=self.redeem_selection_view, style=Pack(padding=3)),
                toga.Button('Reset', on_press=self.confirm_reset_view, style=Pack(padding=3))
            )
        self.main_window.title = 'View Points'
        self.main_window.content = new_box

    def redeem_selection_view(self, widget):
        self.custom_amount_of_points = toga.TextInput(style=Pack(flex=1))
        new_box = toga.Box(children=[
            toga.Button('Back', on_press=self.points_view, style=Pack(padding=3)),
            toga.Label('How much points do you want to redeem?')
            ], style=Pack(direction=COLUMN, padding=3))
        for i in (20, 100, 200, 500):
            if self.data['points'] >= i:
                new_box.add(toga.Button(f'{i} points', on_press=self.redeem_view, style=Pack(padding=3), id=str(i)))
        if self.data['points'] > 0:
            new_box.add(
                toga.Label('\nCustom amount: '),
                self.custom_amount_of_points,
                toga.Button('Redeem', on_press=self.redeem_view, style=Pack(padding=3), id='custom')
            )
        self.main_window.title = 'Redeem Points'
        self.main_window.content = new_box

    def redeem_view(self, widget):
        new_box = toga.Box(style=Pack(direction=COLUMN, padding=3))
        self.main_window.title = 'Redeem Points'
        code = random.randint(100000, 999999)
        if widget.id == 'custom':
            points_to_redeem = int(self.custom_amount_of_points.value)
            if points_to_redeem > self.data['points']:
                new_box.add(toga.Label(f'You do not have enough points!\n You have {self.data["points"]} points, but you want to redeem {points_to_redeem} points.'))
                new_box.add(toga.Button('Back', on_press=self.redeem_selection_view, style=Pack(padding=3)))
                self.main_window.content = new_box
                return
        else:
            points_to_redeem = int(widget.id)
        try:
            urllib.request.urlopen(f'http://101.132.227.6:3554/add_code?code={code}&points={points_to_redeem}')
        except:
            new_box.add(toga.Label('Failed to connect to server.'))
        new_box.add(toga.Button('Back', on_press=self.redeem_selection_view, style=Pack(padding=3)))
        new_box.add(toga.Label(f'You have redeemed {points_to_redeem} points.'))
        new_box.add(toga.Label(f'Your redeem code is {code}'))
        self.data['points'] -= points_to_redeem
        self.data['history'].append(['Redeem', -points_to_redeem])
        self.save_data()
        self.main_window.content = new_box

    def confirm_reset_view(self, widget):
        new_box = toga.Box(children=[
            toga.Label('Are you sure you want to reset your points?'),
            toga.Box(children=[
                toga.Button('Yes', on_press=self.reset_view, style=Pack(padding=3)),
                toga.Button('No', on_press=self.points_view, style=Pack(padding=3))
            ], style=Pack(direction=ROW, padding=2))
        ], style=Pack(direction=COLUMN, padding=3))
        self.main_window.title = 'Reset Points'
        self.main_window.content = new_box

    def reset_view(self, widget):
        new_box = toga.Box(style=Pack(direction=COLUMN, padding=3))
        self.main_window.title = 'Reset Points'
        new_box.add(toga.Label("Your point has been reset"))
        new_box.add(toga.Button('Complete', on_press=self.main_view, style=Pack(padding=3)))
        self.data['points'] = 0
        self.save_data()
        self.main_window.content = new_box

    def save_data(self):
        with open(self.data_dir, 'w') as f:
            json.dump(self.data, f)


def main():
    return HackRTH()
