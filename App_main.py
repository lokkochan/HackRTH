"""
Code to change 2022
RTHbuddy sponsoredbyRTH
"""

import refresh_user_menu as rum
import qr_gen as qrg

class users:
    def __init__(self, name, points, task_history):
        self.name=name
        self.points=points
        self.task_history=task_history

    def checkpoints(self):
        print('The current point is : '+self.points+'.')


    def checkhist(self):
        print("{:<10} {:<30}".format('Date','Task'))
        for i in range(len(self.task_history)):
            print("{:<10} {:<30}".format(self.task_history[i][0],self.task_history[i][1]))
        
    def new_task_done(self,new_task):
        self.task_history.append(new_task)




def verifytask_type1():
    """
    not sure on how to do that yet, so do other two verify
    """
    return True

def verifytask_type2():
    return True

def verifytask_type3():
    return True

def redeem():
    '''Will implant to generate a QR code for scanning to redeem the points'''
    qr_code = qrg.qr_gen()
    return qr_code

def task_menu():
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



def menu():
    print("1-View Task")
    print("2-View History")
    print("3-View Points")
    print("4-Quit")
    choice=int(input("Please select from above: "))
    return choice


def main():
    #read history of the user
    history_list=[]
    name=input("Please enter your name: ")
    user=users(name,history_list)
    new_task_done=[]
    choice=0
    while choice!=4:
        choice=menu()
        if choice ==1:
            task_list=task_menu()
            #function for menu for do, verify and record task
            
        elif choice==2:
            user.checkhist()

        elif choice==3:
            user.checkpoints()
            #function for menu for using points

        elif choice!=4:
            print("Invalid input")

        









main()