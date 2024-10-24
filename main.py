from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

# Import your screens
from screens.home_screen import HomeScreen

# Import your custom widgets

# Load your .kv files
Builder.load_file("kv/home_screen.kv")

class TicTacToeApp(MDApp):
    def build(self):
        """
        This function is responsible for building the main application layout.

        Parameters:
        None

        Returns:
        screen_manager (MDScreenManager): The main screen manager that holds all the application screens.
        """
        # Set the theme
        self.theme_cls.theme_style = "Dark"

        # Create your screens
        self.home_screen = HomeScreen()

        # Add your screens to the screen manager
        self.screen_manager = MDScreenManager()
        self.screen_manager.add_widget(self.home_screen)

        return self.screen_manager


if __name__ == "__main__":
    TicTacToeApp().run()