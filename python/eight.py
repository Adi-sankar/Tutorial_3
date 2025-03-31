from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Guess the Number Game")
        
        self.setSize(400, 200)

        self.targetNumber = random.randint(1, 100)
        self.attempts = 0

        self.addLabel(text="Enter your guess (1-100):", row=0, column=0)
        self.inputField = self.addIntegerField(value="", row=0, column=1, width=10)

        self.resultLabel = self.addLabel(text="", row=1, column=0, columnspan=2)

        self.addButton(text="Guess", row=2, column=0, columnspan=2, command=self.checkGuess)

    def checkGuess(self):
        
        guess = self.inputField.getNumber()
        self.attempts += 1

        if guess < self.targetNumber:
            self.resultLabel["text"] = "Too small, try again."
        elif guess > self.targetNumber:
            self.resultLabel["text"] = "Too large, try again."
        else:
            self.resultLabel["text"] = f"Correct! You guessed it in {self.attempts} tries."
            self.inputField["state"] = "disabled"
            
if __name__ == "__main__":
    GuessingGame().mainloop()
