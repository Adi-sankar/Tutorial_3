from breezypythongui import EasyFrame

class BouncyBall(EasyFrame):
    def __init__(self):
        
        EasyFrame.__init__(self, title="Bouncy Ball Calculator")
        self.setSize(400, 250)

       
        self.addLabel(text="Initial Height (meters):", row=0, column=0)
        self.heightField = self.addFloatField(value="", row=0, column=1, width=10)

        self.addLabel(text="Bounciness Index (0-1):", row=1, column=0)
        self.bouncinessField = self.addFloatField(value="", row=1, column=1, width=10)

        self.addLabel(text="Number of Bounces:", row=2, column=0)
        self.bouncesField = self.addIntegerField(value="", row=2, column=1, width=10)

        self.addButton(text="Compute Distance", row=3, column=0, columnspan=2, command=self.computeDistance)

        self.resultLabel = self.addLabel(text="Total Distance: 0.0 meters", row=4, column=0, columnspan=2)

    def computeDistance(self):
        
        try:
            height = self.heightField.getNumber()
            bounciness = self.bouncinessField.getNumber()
            bounces = self.bouncesField.getNumber()

            if height <= 0 or not (0 < bounciness < 1) or bounces < 0:
                raise ValueError

            total_distance = height 
            for _ in range(bounces):
                height *= bounciness
                total_distance += 2 * height
            
            self.resultLabel["text"] = f"Total Distance: {total_distance:.2f} meters"

        except ValueError:
            self.messageBox(title="ERROR", message="Invalid input! Please enter valid values.")


if __name__ == "__main__":
    BouncyBall().mainloop()
