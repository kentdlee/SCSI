import random
import numpy as np

# np.dot
# np.sign
# np.c_ adds a column of 1's for bias

class Perceptron:
    def __init__(self, numInputs):
        # we add one to numInputs for the bias.
        self.w = np.array([random.random()*2-1 for x in range(numInputs+1)])
        
    def fit(self, xtrain, ytrain, falsePositivePct):
        
        done = False
        count = 0
        
        xv = np.c_[[1 for i in range(len(xtrain))],np.array(xtrain)]
        yv = np.array(ytrain)
        size = len(xtrain)
        falsePosRatio = falsePositivePct/100
        incorrectAnswers = ytrain
        print("before training", self.w)
        
        while len(incorrectAnswers) / size > falsePosRatio and not done and count < 1000:  

            count += 1
            incorrectAnswers = []
            for i in range(len(xtrain)):
                prediction = np.sign(np.dot(self.w,xv[i]))
                if prediction != ytrain[i]:
                    incorrectAnswers.append(i)
                    
            if len(incorrectAnswers) != 0:     
                chosenIndex = incorrectAnswers[random.randint(0,len(incorrectAnswers)-1)]     
                self.w = self.w + xv[chosenIndex] * yv[chosenIndex]
            else:
                done = True
                
        print("Training completed in", count, "iterations.")
        print("After training", self.w)
        
    def decisionFunction(self,x):
        # same as predict without calling sign so we can use it in the ROC curve score.
        pass 

                   
    def predict(self, x): 
        xv = np.array([1] + list(x)) 
        value = np.dot(self.w,xv)
        return np.sign(value)
        
def main():       
    pts = [(4,1),(4,10),(3,5),(4,4),(8,10),(6,9),(7,11),(5,7),(4,2),(2,3),(7,6)]
    y = [-1,1,-1,-1,1,1,1,1,-1,-1,1]
    
    percept = Perceptron(2)
    
    percept.fit(pts,y,1)
    
    for i in range(len(pts)):
        val = percept.predict(pts[i])
        if val == y[i]:
            print("correct at", pts[i])
        else:
            print("incorrect at", pts[i])
            
if __name__ == "__main__":
    main()