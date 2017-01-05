'''
Created on 16 Oct 2015

@author: Alanna
'''
from State import State
import time
import random

class StateDefault(State):
    def __init__(self,owner):
        State.__init__(self, owner, "Default")
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(0.0)
    def execute(self):
        State.execute(self)

        if self.duration < 5:
            return
        
        if self.owner.facesSeen:
            self.owner.changeState(self.owner.states['hello'])
            return

        if self.duration > 25:
            self.owner.changeState(self.owner.states['default'])
            return
            
    def exit(self):
        State.exit(self)

class StateHello(State):
    def __init__(self, owner):
        State.__init__(self, owner, "Hello")
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(33.5)
    def execute(self):
        State.execute(self)

        if self.duration < 2:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return

        #user did not speak    
        if self.owner.facesSeen:
            self.owner.changeState(self.owner.states['howareyou'])
            return
        else:
            self.owner.changeState(self.owner.states['default'])
            return
            
    def exit(self):
        State.exit(self)

class StateHowAreYou(State):
    def __init__(self, owner ):
        State.__init__(self, owner, "HowAreYou")
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(46.5)
    def execute(self):
        State.execute(self)
        
        if self.duration < 2:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return

        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.changeState(self.owner.states['howareyoufeeling'])
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])
            
    def exit(self):
        State.exit(self)

class StateHowAreYouFeeling(State):
    def __init__(self, owner ):
        State.__init__(self, owner, "HowAreYouFeeling")
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(57.0)
    def execute(self):
        State.execute(self)

        if self.duration < 2:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.changeState(self.owner.states['whydoyouthinkthatis'])
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])
        
    def exit(self):
        State.exit(self)

class StateWhyDoYouThinkThatIs(State):
    def __init__(self, owner):
        State.__init__(self, owner, "WhyDoYouThinkThatIs")    
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(121.0)
    def execute(self):
        State.execute(self)

        if self.duration < 4:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.changeState(self.owner.states['howdoesthatmakeyoufeel'])
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])
                                
    def exit(self):
        State.exit(self)
        
class StateHowDoesThatMakeYouFeel(State):
    def __init__(self, owner):
        State.__init__(self, owner, "HowDoesThatMakeYouFeel")
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(108.5)
    def execute(self):
        State.execute(self)

        if self.duration < 4:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.changeState(self.owner.states['canyouexplainwhyyoufeelthatway'])
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])
        
    def exit(self):
        State.exit(self)

class StateCanYouExplainWhyYouFeelThatWay(State):
    def __init__(self, owner):
        State.__init__(self, owner, "CanYouExplainWhyYouFeelThatWay")
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(94.0)
    def execute(self):
        State.execute(self)

        if self.duration < 4:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.changeState(self.owner.states['doyouliketofeelthatway'])
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])
        
    def exit(self):
        State.exit(self)
        
class StateDoYouLikeToFeelThatWay(State):
    def __init__(self, owner):
        State.__init__(self, owner, "DoYouLikeToFeelThatWay")   
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(83.0)
    def execute(self):
        State.execute(self)

        if self.duration < 2:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.changeState(self.owner.states['tellmemoreaboutthat'])
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])  
        
    def exit(self):
        State.exit(self)

class StateTellMeMoreAboutThat(State):
    def __init__(self, owner):
        State.__init__(self, owner, "TellMeMoreAboutThat") 
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(72.5)
    def execute(self):
        State.execute(self)

        if self.duration < 4:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.pickRandomStatement()
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])  
        
    def exit(self):
        State.exit(self)
                          
class StateYouSeemAngry(State):
    def __init__(self, owner):
        State.__init__(self, owner, "YouSeemAngry")   
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(135)
    def execute(self):
        State.execute(self)

        if self.duration < 2:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.pickRandomQuestion()
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])  

        
    def exit(self):
        State.exit(self)
                       
class StateYouSeemDissappointed(State):
    def __init__(self, owner):
        State.__init__(self, owner, "YouSeemDissappointed")
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(148)
    def execute(self):
        State.execute(self)

        if self.duration < 2:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.pickRandomQuestion()
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])
        
    def exit(self):
        State.exit(self)
                       
class StateYouSeemHappy(State):
    def __init__(self, owner):
        State.__init__(self, owner, "YouSeemHappy")
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(159.0)
    def execute(self):
        State.execute(self)

        if self.duration < 2:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.pickRandomQuestion()
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])
        
    def exit(self):
        State.exit(self)
                       
class StateYouSeemSad(State):
    def __init__(self, owner):
        State.__init__(self, owner, "YouSeemSad")
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(171)
    def execute(self):
        State.execute(self)

        if self.duration < 2:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.pickRandomQuestion()
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])
        
    def exit(self):
        State.exit(self)

class StateYouSeemUpset(State):
    def __init__(self, owner):
        State.__init__(self, owner, "YouSeemUpset")
    def enter(self):
        State.enter(self)
        self.owner.player.set_position(181)
    def execute(self):
        State.execute(self)

        if self.duration < 3:
            return

        if self.duration < 8 and (not self.owner.isSoundDetected()):
            return
        
        #user response
        if self.owner.facesSeen and self.owner.isSoundDetected():
            self.owner.pickRandomQuestion()
            return

        #user does not speak
        if self.owner.facesSeen:
            self.owner.pickRandomStatement()
            return

        #nobody there
        self.owner.changeState(self.owner.states['default'])
    def exit(self):
        State.exit(self)

    def exit(self):
        State.exit(self)    
        
