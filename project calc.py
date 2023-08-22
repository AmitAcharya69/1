from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random


class PasswordGeneratorApp(App):
    def build(self):
        self.title = 'Password Generator'

        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.length_label = Label(text='Enter the length of your password:')
        self.layout.add_widget(self.length_label)

        self.length_input = TextInput(multiline=False)
        self.layout.add_widget(self.length_input)

        self.generate_button = Button(text='Generate Password')
        self.generate_button.bind(on_press=self.generate_password)
        self.layout.add_widget(self.generate_button)

        self.password_label = Label(text='')
        self.layout.add_widget(self.password_label)

        return self.layout


    def generate_password(self, instance):
        upper = "QWERTYUIOPASDFGHZXCVBJNKML"
        lower = "qwertyuiopalskdjfhgmznxbcv"
        number = "0123456789"
        symbol = "£$%^&*<|"
        string = lower + upper + number + symbol

        length_text = self.length_input.text.strip()

        if not length_text:
            self.password_label.text = 'Please enter a password length below.'
            return

        try:
            length = int(length_text)
        except ValueError:
            self.password_label.text = 'Invalid input. Please enter a valid number.'
            return

        if length <= 0:
            self.password_label.text = 'Password length must be greater than 0.'
        else:
            password = "".join(random.sample(string, length))
            self.password_label.text = 'Your password is: ' + password


if __name__ == '__main__':
    PasswordGeneratorApp().run()
