#state machine traversal

from random import randint
import time

State = type ("State",(object,),{})# define State base class

class LightOn(State): # define class for LightOn with State
	def Execute(self): # define function for class variable.Execute()
		print ("Light is ON") # print the action 

class LightOff(State): # define class for LightOff with State
	def Execute(self): # define function in class
		print ("Light is OFF")

class Transition(object):# define class with object name 
	def __init__(self,toState):# define contructor class with 	
		self.toState=toState #equal to itself

	def Execute(self): #define method 
		print ("Transitioning...")

class SimpleFSM(object):
	def __init__(self,char): # obstructor to construct/intialize the other variables  
		self.char=char
		self.states = {}
		self.transitions = {}
		self.curState = None
		self.trans =None

	def SetState(self, stateName):# used for defining states 
		self.curState=self.states[stateName]

	def Transisition(self,transName):#used for defining states
		self.trans = self.transitions[transName]

	def Execute(self):
		if(self.trans):# if there is a transition stored within self.trans
			self.trans.Execute() #execute transition 
			self.SetState(self.trans.toState)# set current state to current state to 
			self.trans = None # reset transition state to None
		self.curState.Execute() # execute current state 

class Char(object): #instance of FSM machine above 
	def __init__(self):
		self.FSM=SimpleFSM(self)
		self.LightOn = True


if __name__ == "__main__":
	light=Char() # instance of the character 

	light.FSM.states["On"]=LightOn() # created instance of the LightOn state 
	#stored the state within the state dictionary inside the Finite State Machine 
	light.FSM.states["Off"]=LightOff()
	light.FSM.transitions["toOn"]=Transition("On")# created an instance of transition
	#stored it within the dicitionary of transitions 
	light.FSM.transitions["toOff"]=Transition("Off")
	
	light.FSM.SetState("On")

	...

	for i in range(20):
		startTime=time.perf_counter() # not clock 
		timeInterval=1
		while (startTime +timeInterval>time.perf_counter()):#not clock
			pass
		if(randint(0,2)):
			if(light.LightOn):
				light.FSM.transitions["toOff"]
				light.LightOn=False  
			else:
				light.FSM.transitions["toOn"]
				light.LightOn =True
		light.FSM.Execute()


#not transitioning between the on and the off states just stays on 