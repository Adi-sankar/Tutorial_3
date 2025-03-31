from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")

        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel(text="Celsius", row=0, column=1)

        self.fahrenheitField = self.addFloatField(value=32.0, row=1, column=0, width=10)
        self.celsiusField = self.addFloatField(value=0.0, row=1, column=1, width=10)

        self.addButton(text=">>>>", row=2, column=0, command=self.convertToCelsius)
        self.addButton(text="<<<<", row=2, column=1, command=self.convertToFahrenheit)

    def convertToCelsius(self):
        fahrenheit = self.fahrenheitField.getNumber()
        celsius = (fahrenheit - 32) * 5 / 9
        self.celsiusField.setNumber(round(celsius, 2))

    def convertToFahrenheit(self):
        celsius = self.celsiusField.getNumber()
        fahrenheit = (celsius * 9 / 5) + 32
        self.fahrenheitField.setNumber(round(fahrenheit, 2))

if __name__ == "__main__":
    TemperatureConverter().mainloop()
