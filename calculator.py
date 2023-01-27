from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config


class CalculatorApp(App):
    def build(self):
        self.st = StackLayout(size=(360, 800), orientation='lr-tb')
        self.result = TextInput(
            multiline=False, readonly=True, halign="right", font_size=32, size_hint=(1, .4)
        )
        self.st.add_widget(self.result)
        self.st.add_widget(
            Button(text="7", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="8", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="9", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="-", on_press=self.add_operation, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="4", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="5", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="6", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="+", on_press=self.add_operation, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="1", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="2", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="3", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="*", on_press=self.add_operation, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text=".", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="0", on_press=self.add_number, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="/", on_press=self.add_operation, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="C", on_press=self.clear, size_hint=(.25, .1)))
        self.st.add_widget(
            Button(text="=", on_press=self.calculate, size_hint=(1, .1)))
        return self.st

    def add_number(self, instance):
        if self.result.text == "Error":
            self.result.text = ""
        self.result.text += str(instance.text)

    def add_operation(self, instance):
        self.result.text += str(instance.text)

    def calculate(self, instance):
        try:
            self.result.text = str(eval(self.result.text))
        except:
            self.result.text = "Error"

    def clear(self, instance):
        self.result.text = ""


if __name__ == "__main__":
    Config.set("graphics", "resizable", 0)
    Config.set("graphics", "width", 360)
    Config.set("graphics", "height", 800)
    Config.write()
    CalculatorApp().run()
