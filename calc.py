import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 400)
Builder.load_file("calc.kv")


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    # Create button pressing function
    def button_press(self, button):
        # Create variable that contains whatever was in the textboc already
        prior = self.ids.calc_input.text

        # Determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"

    # Create addition function
    def add(self):
        # Create variable that contains whatever was in the textboc already
        prior = self.ids.calc_input.text
        # Slap a plus sign to the textinput
        self.ids.calc_input.text = f"{prior}+"

    # Create subtraction function
    def subtract(self):
        # Create variable that contains whatever was in the textboc already
        prior = self.ids.calc_input.text
        # Slap a minus sign to the textinput
        self.ids.calc_input.text = f"{prior}-"

    # Create multiplication function
    def multiply(self):
        # Create variable that contains whatever was in the textboc already
        prior = self.ids.calc_input.text
        # Slap a cross sign to the textinput
        self.ids.calc_input.text = f"{prior}×"

    # Create divisoin function
    def divide(self):
        # Create variable that contains whatever was in the textboc already
        prior = self.ids.calc_input.text
        # Slap a divided by sign to the textinput
        self.ids.calc_input.text = f"{prior}÷"

    # Create equas to function
    def equals(self):
        prior = self.ids.calc_input.text

        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            # Loop thru our list
            for number in num_list:
                answer += int(number)

            # Print the answer in the textinput
            self.ids.calc_input.text = str(answer)


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()
