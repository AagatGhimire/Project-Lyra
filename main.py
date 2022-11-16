from kivy.app import App
from kivy.uix.label import Label


class BasicApp(App):
    def build(self):
        label=Label(text="Project Started")
        return label

app = BasicApp()
app.run()
