"""
Code to change 2022
RTHbuddy sponsoredbyRTH
"""




class users:
    def __init__(self, points, task_history):
        self.points=points
        self.task_history=task_history

    def checkpoints(self):
        print('The current point is : '+self.point+'.')


    def checkhist(self):
        print("{:<10} {:<30} {:<12}".format('Date','Task', 'Difficulity'))
        for i in range(len(self.task_history)):
            print("{:<10} {:<30} {:<12}".format(self.task_history[i][0],self.task_history[i][1],self.task_history[i][2]))
        



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
    return


def main():







main()