import Tkinter as tk
import time

red ="""
 .----'  '----.
 |    .==.    |
 |   /####\   |
 |   \####/   |
 |    .==.    |
 |    .==.    |
 |    /  \    |
 |    \  /    |
 |    .==.    |
 |    .==.    |
 |    /  \    |
 |    \  /    |
 |    .==.    |
 '--.______.--'"""
yellow ="""
 .----'  '----.
 |    .==.    |
 |    /  \    |
 |    \  /    |
 |    .==.    |
 |    .==.    |
 |   /####\   |
 |   \####/   |
 |    .==.    |
 |    .==.    |
 |    /  \    |
 |    \  /    |
 |    .==.    |
 '--.______.--'"""
green = '''
 .----'  '----.
 |    .==.    |
 |    /  \    |
 |    \  /    |
 |    .==.    |
 |    .==.    |
 |    /  \    |
 |    \  /    |
 |    .==.    |
 |    .==.    |
 |   /####\   |
 |   \####/   |
 |    .==.    |
 '--.______.--'''

listOfColors = ["green","yellow", "red"]
listOfGraphics = [green,yellow,red]
listOfLights = []
currentLight = 2
counter = 0 
currentDuration = 0

class Light:
    lightColor = ""
    graphic = ""
    duration = 1
    def f(self):
        return 'I am a light'
class MainStopLight(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        
    def MakeLights(self):
        for a in range(0, len(listOfColors)):   
            x = Light()
            x.lightColor = listOfColors[a]
            x.graphic = listOfGraphics[a]
            listOfLights.append(x)
            
#Call this every time you want to switch lights
    def SelectLight(self):
        global currentLight
    #"red"
        if currentLight == 0:
            currentLight += 1
    #"yellow"
        elif currentLight == 1:
            currentLight += 1
    #"green"
        elif currentLight == 2:
            currentLight = 0

    def Exit(self):
        exitMessage = "Exiting Traffic Light Simulator"
        global root
        self.exitLabel.config(text = exitMessage)
        root.update()
        time.sleep(1)
        root.destroy()

    def Update(self, tick):
        def count():
            global counter
            global currentDuration
            counter += 1
            #Debug
            #tick.config(text=str(counter))
            tick.after(1000, count)
            #tick.grid(row = 5, column = 1)
            counterPlusDuration = int(counter) + int(currentDuration)
            if counterPlusDuration == counter:
                self.SelectLight()
                self.graphicDisplay.config(text = listOfLights[currentLight].graphic)
                currentDuration = listOfLights[currentLight].duration
            else:
                currentDuration -= 1
        count()
        
    def GetInput(self):
        try:
            redValue = int(self.redInput.get())
            listOfLights[2].duration = redValue
            print "red value is " + str(redValue)
        except ValueError:
            print "Please enter integer values"
        try:    
            yellowValue = int(self.yellowInput.get())
            print "yellow value is " + str(yellowValue)
            listOfLights[1].duration = yellowValue
        except ValueError:
            print "Please enter integer values"
        try:
            greenValue = int(self.greenInput.get())
            listOfLights[0].duration = greenValue
            print "green value is " + str(greenValue)
        except ValueError:
            print "Please enter integer values"
        #Debug
        self.Print()
    def Print(self):
        for x in range(0, len(listOfLights)):
            print str(listOfLights[x].duration)
    def DrawGui(self):
        self.redInput = tk.Entry(root,textvariable=tk.IntVar( value = 1))
        self.yellowInput = tk.Entry(root,textvariable=tk.IntVar(value = 1))
        self.greenInput = tk.Entry(root,textvariable=tk.IntVar(value = 1))
        self.redLabel = tk.Label(root, text="Red Light Duration")
        self.yellowLabel = tk.Label(root, text="Yellow Light Duration")
        self.greenLabel = tk.Label(root, text="Green Light Duration")
        self.submitButton = tk.Button(root, text='Submit',width=25, command=m.GetInput)
        self.button = tk.Button(root, text='Exit', width=25, command=m.Exit)
        self.exitLabel = tk.Label(root)
        self.graphicDisplay = tk.Label(root, text=None)
        
        self.graphicDisplay.grid(row=0, column = 0)
        self.redLabel.grid(row = 1, column = 0)
        self.yellowLabel.grid(row = 2, column = 0)
        self.greenLabel.grid(row = 3, column = 0)
        self.submitButton.grid(row=4,column = 0)
        self.exitLabel.grid(row =5, column = 0)
        self.redInput.grid(row = 1, column =1)
        self.yellowInput.grid(row = 2, column =1)
        self.greenInput.grid(row = 3, column =1)
        self.button.grid(row=4, column = 1)

if __name__ == "__main__":
    root = tk.Tk()
    m = MainStopLight(root)
    m.MakeLights()
    m.DrawGui()
    m.tick = tk.Label(root, fg="green")
    m.Update(m.tick)
    root.mainloop()
    




