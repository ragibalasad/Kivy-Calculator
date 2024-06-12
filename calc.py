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
        # Create variable that contains whatever was in the textbox already
        prior = self.ids.calc_input.text

        # Determine if 0 is sitting there
        if prior == "0" or prior == "Error":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"

    # Create function to remove ast charecter
    def remove(self):
        prior = self.ids.calc_input.text

        if not prior == "0":
            # Remove the last item in the textbox
            prior = prior[:-1]
            # Output back to the textbox
            self.ids.calc_input.text = prior

            # Put a 0 to the textbox if empty
            if len(prior) == 0:
                self.ids.calc_input.text = "0"

    # Create function to make the number positive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text

        # Check if there's already a negative sign
        if "-" in prior:
            self.ids.calc_input.text = f"{prior.replace('-','')}"
        else:
            self.ids.calc_input.text = f"-{prior}"

    # Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        # Split out textbox by +
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            # Add a period to the end of the text
            prior = f"{prior}."
            # Output back to the textbox
            self.ids.calc_input.text = prior

        elif not "." in prior:
            # Add a period to the end of the text
            prior = f"{prior}."
            # Output back to the textbox
            self.ids.calc_input.text = prior

    # Create addition function
    def math_sign(self, sign):
        # Create variable that contains whatever was in the textbox already
        prior = self.ids.calc_input.text
        # Slap a plus sign to the textinput
        self.ids.calc_input.text = f"{prior}{sign}"

    # Create equas to function
    def equals(self):
        prior = self.ids.calc_input.text
        try:
            # Replace symbols with actual math operators
            prior = prior.replace("÷", "/").replace("×", "*")
            # Evaluate math from the textbox
            answer = eval(prior)
            # Print the answer in the textinput
            self.ids.calc_input.text = str(answer)
        except Exception:
            self.ids.calc_input.text = "Error"

        """
        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            # Loop thru our list
            for number in num_list:
                answer += float(number)

            # Print the answer in the textinput
            self.ids.calc_input.text = str(answer)
        """


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()
