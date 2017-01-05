'''
Created on 16 Oct 2015

@author: Alanna
'''
from State import State
import time

class StateMachine(object):
    
    def __init__(self):
        self.state = None
        self.previousState = None
        self.startTime = time.time()
        self.uptime = 0
            
    def update(self):
        self.uptime = time.time() - self.startTime
        self.state.execute()
        
    def changeState(self,state):        
        print "Changing State"
        if isinstance(state, State):
            if self.state:
                self.state.exit()
            self.previousState = self.state
            self.state = state
            self.state.enter()
        else:
            raise TypeError
