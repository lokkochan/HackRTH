"""
Code to change 2022
RTHbuddy sponsoredbyRTH
"""
import refresh_user_menu as rum

time = 6
days_passed = 0

#refresh menu
if time != 6:
    #wait 1 hour
    time += 1
    if time == 24:
        time = 0
        days_passed += 1
else:
    rum.print_menu()
    #wait 1 hour
    time += 1 

class users:
    def __init__(self, points, task_history):
        self.points=points
        self.task_history=task_history

    def checkpoints(self):
        print('The current point is : '+self.point+'.')


    def checkhist(self):

        






def main():







main()