from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicWidgetsExampleApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.library = {"Harry Potter": "JK Rowling", "Book One": "Me", "Book Two": "Also Me"}

    def build(self):
        self.title = "Dynamic Widgets Example"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for book in self.library:
            temp_label = Label(text=book, id=book)
            self.root.ids.books_box.add_widget(temp_label)

    def clear_books(self):
        self.root.ids.books_box.clear_widgets()


DynamicWidgetsExampleApp().run()
