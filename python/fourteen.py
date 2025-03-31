from breezypythongui import EasyFrame
import math

class SquareRootCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Square Root Calculator")
        
        self.setSize(400, 200)

        self.addLabel(text="Enter an Integer:", row=0, column=0)
        self.inputField = self.addIntegerField(value="", row=0, column=1, width=10)

        self.addLabel(text="Square Root:", row=1, column=0)
        self.outputField = self.addFloatField(value=0.0, row=1, column=1, width=10, state="readonly")

        self.addButton(text="Calculate", row=2, column=0, columnspan=2, command=self.computeSqrt)

    def computeSqrt(self):
        
        try:
            number = self.inputField.getNumber()
            if number < 0:
                raise ValueError 

            result = math.sqrt(number)  
            self.outputField.setNumber(result)  

        except ValueError:
            self.messageBox(title="ERROR", message="Input must be an integer >= 0") 

if __name__ == "__main__":
    SquareRootCalculator().mainloop()
