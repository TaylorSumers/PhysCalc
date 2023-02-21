import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
Window.size = (450, 800)

# Layout
class MainWindow(Screen):
    pass


class MechanicsList(Screen):
    pass


class Speed(Screen):
    pass


class Efficiency(Screen):
    pass


class WindowManager(ScreenManager):
    pass

# Logic
class PhysicsCalculatorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('physicscalculator.kv')

    def callback(self, instance_action_top_appbar_button):
        self.root.current = "main"
        self.root.transition.direction = "right"

    def callbackmech(self, instance_action_top_appbar_button):
        self.root.current = "mech"
        self.root.transition.direction = "right"


PhysicsCalculatorApp().run()
