from kivymd.app import MDApp
from practicalhelper import *
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton


class PracticalApp(MDApp):
	def build(self):
		screen = Screen()
		heading = Builder.load_string(header)
		screen.add_widget(heading)
		fields = Builder.load_string(inputfields)
		screen.add_widget(fields)
		field2  = Builder.load_string(instagram)
		screen.add_widget(field2)
		field3  = Builder.load_string(twitter)
		screen.add_widget(field3)
		field4  = Builder.load_string(github)
		screen.add_widget(field4)
		field5  = Builder.load_string(tokenurl)
		screen.add_widget(field5)
		btn = MDRectangleFlatButton(text="Login", pos_hint = {'center_x':0.5,'center_y': 0.2}, on_release = self.access_granted)
		screen.add_widget(btn)




		return screen


	def access_granted(self,obj):
		print("Access granted")




if __name__ == '__main__':
	PracticalApp().run()


