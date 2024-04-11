from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350, 600)

kv = '''
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    Image:
        source: "C:/Users/1/Desktop/PyWeatherKivy/assets/icon.png"
        size_hint: .1, .1
        pos_hint: {"center_x": .5, "center_y": .95}
'''


class WeatherApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    WeatherApp().run()