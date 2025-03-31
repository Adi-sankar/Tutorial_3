from breezypythongui import EasyFrame

class UppercaseConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Uppercase Converter")

        self.addLabel(text="Enter Text:", row=0, column=0)
        self.inputField = self.addTextField(text="", row=0, column=1, width=20)

        self.addLabel(text="Uppercase Output:", row=1, column=0)
        self.outputField = self.addTextField(text="", row=1, column=1, width=20, state="readonly")

    
        self.addButton(text="Convert", row=2, column=0, columnspan=2, command=self.convertToUppercase)

    def convertToUppercase(self):
        input_text = self.inputField.getText()
        uppercase_text = input_text.upper()
        self.outputField.setText(uppercase_text)

if __name__ == "__main__":
    UppercaseConverter().mainloop()
