'''
Created on 17 Oct 2015

@author: Alanna
'''
from StateMachine import StateMachine
from omxplayer import OMXPlayer
from EmpathyMachineStates import StateDefault, StateDoYouLikeToFeelThatWay, StateHello, StateHowAreYou, StateCanYouExplainWhyYouFeelThatWay, StateHowAreYouFeeling, StateHowDoesThatMakeYouFeel, StateTellMeMoreAboutThat, StateWhyDoYouThinkThatIs, StateYouSeemAngry, StateYouSeemDissappointed, StateYouSeemSad, StateYouSeemUpset 
from FaceRecognizer import FaceRecognizer
import alsaaudio as aa
import audioop
import time
import random
import cv2

SOUND_DET_THRESHOLD = 4000
AUDIO_THRESHOLD = 0.15
NORMALIZE = 1.0 / 32768.0

class EmpathyMachine(StateMachine):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        StateMachine.__init__(self)
        self.running = True
        self.player = OMXPlayer('./videos/strip-1366x768/empathy-machine-strip.mp4',args=['--loop','--no-osd','--alpha=128'])
        self.faceRecognizer = FaceRecognizer()
        self.facesSeen = 0
        self.states = {
            'default':StateDefault(self),
            'hello':StateHello(self),
            'howareyou':StateHowAreYou(self),
            'howareyoufeeling':StateHowAreYouFeeling(self),
            'tellmemoreaboutthat':StateTellMeMoreAboutThat(self),            
            'doyouliketofeelthatway':StateDoYouLikeToFeelThatWay(self),
            'canyouexplainwhyyoufeelthatway':StateCanYouExplainWhyYouFeelThatWay(self),
            'howdoesthatmakeyoufeel':StateHowDoesThatMakeYouFeel(self),
            'whydoyouthinkthatis':StateWhyDoYouThinkThatIs(self),
            'youseemangry':StateYouSeemAngry(self),
            'youseemdisappointed':StateYouSeemDissappointed(self),
            'youseemhappy':StateYouSeemSad(self),
            'youseemsad':StateYouSeemUpset(self),
            'youseemupset':StateYouSeemUpset(self)
            }

        self.possibleRandomStatement = [
            self.states['youseemangry'],
            self.states['youseemdisappointed'],
            self.states['youseemhappy'],
            self.states['youseemsad'],
            self.states['youseemupset'],
            self.states['howareyoufeeling'],
            self.states['howareyou']
            ]

        self.possibleRandomQuestion = [
            self.states['howareyoufeeling'],
            self.states['tellmemoreaboutthat'],
            self.states['doyouliketofeelthatway'],
            self.states['canyouexplainwhyyoufeelthatway'],
            self.states['howdoesthatmakeyoufeel'],
            self.states['whydoyouthinkthatis']
            ]

        self.faceRecognizer.subscribe( self )        
        self.faceRecognizer.start()
        self.data_in = aa.PCM(aa.PCM_CAPTURE, aa.PCM_NONBLOCK,device="default:CARD=Set")
        self.data_in.setchannels(2)
        self.data_in.setrate(8000)
        self.data_in.setformat(aa.PCM_FORMAT_S16_LE)
        self.data_in.setperiodsize(1024)
        self.soundLevel = 0
        self.soundDetected = 0
        self.facesSeen = False

        self.changeState( self.states['default'] )
        self.player.play()

        #img = cv2.imread("~/test.jpg")
        #cv2.imshow("test",img)

    def isSoundDetected(self):
        return (self.soundDetected > SOUND_DET_THRESHOLD)

    def pickRandomStatement(self):
        print "Picking a random statement."
        randStatement = self.state
        while randStatement == self.state:
            randStatement = random.choice(self.possibleRandomStatement)
            
        self.changeState(randStatement)

    def pickRandomQuestion(self):
        print "Picking a random question."
        randQ = self.state
        while randQ == self.state:
            randQ = random.choice(self.possibleRandomQuestion)
            
        self.changeState(randQ)
        

    def changeState(self,state):
        print "self.soundDetected = ", self.soundDetected
        self.soundDetected = 0
        StateMachine.changeState(self,state)
      
    def updateSound(self):
        l,data = self.data_in.read()
        if l:
            try:
                self.soundLevel = audioop.max(data,2) * NORMALIZE
            except audioop.error, e:
                if e.message !="not a whole number of frames":
                    raise e

    def reportFaces( self, faces ):
        #print self.uptime, "I see ", faces, " faces."
        if faces > 0:
            #print "I see someone"
            self.facesSeen = True
        else:
            self.facesSeen = False
                 
    def update(self):
        StateMachine.update(self)
        self.updateSound()
        if self.soundLevel > AUDIO_THRESHOLD:
            #print "I hear something: ", self.soundLevel
            self.soundDetected += 1
                
    def shutdown(self):
        if self.player:
            self.player.quit()
        if self.faceRecognizer:
            self.faceRecognizer.shutdown()
     
            
        
            
        
            
        
