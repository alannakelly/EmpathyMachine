'''
Created on 17 Oct 2015

@author: Alanna
'''
import StateMachine
import time

class State(object):    
    def __init__(self, owner, name ):
        if not isinstance( owner, StateMachine.StateMachine ):
            raise TypeError
        self.owner = owner
        self.name = name
        self.startTime = 0
        self.duration = 0
    def enter(self):
        print "Entering State: %s." % self.name
        self.startTime = time.time()
    def execute(self):
        self.duration = time.time() - self.startTime        
    def exit(self):
        self.duration = time.time() - self.startTime
        print "Exit State: ", self.name, " after ", self.duration, " seconds."

