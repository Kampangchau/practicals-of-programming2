"""
CP1404 Practical
Kivy GUI program to square a number
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_of_name = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.list_of_name:
            # create a button for each data entry, specifying the text and id
            # (although text and id are the same in this case, you should see how this works)
            temp_button = Label(text=name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, name):
        name = name.id
        self.status_text = "The name if {}".format(self.name)



DynamicWidgetsApp().run()