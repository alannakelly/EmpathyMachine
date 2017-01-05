'''
Created on 16 Oct 2015

@author: Alanna
'''
from EmpathyMachine import EmpathyMachine

import curses

if __name__ == '__main__':
    empathyMachine = EmpathyMachine()
    try:
        while True:
            empathyMachine.update()
    except (KeyboardInterrupt, SystemExit):
        empathyMachine.shutdown()        
    pass






