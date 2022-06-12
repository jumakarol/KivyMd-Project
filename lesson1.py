from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

from kivymd.uix.screen import Screen
from kivy.lang import Builder
from helpers1 import *
from kivymd.uix.button import MDRectangleFlatButton






class Lesson1App(MDApp):
	def build(self):

		screen = Screen()
		#var = Builder.load_string(header)
		self.var2 = Builder.load_string(lesson1)
		#var3 = Builder.load_string(lesson1btn)
		var4 = MDRectangleFlatButton(text="Submit", pos_hint={'center_x': 0.5,'center_y':0.4}, on_release=self.show_data)
		#screen.add_widget(var)
		screen.add_widget(self.var2)

		screen.add_widget(var4)
		return screen


	def show_data(self, obj):
		self.btn_close = MDRectangleFlatButton(text="Close", on_release=self.close_action)
		btn_dashboard = MDRectangleFlatButton(text="Dashboard", on_release=self.dashboard_action)
		self.popup = MDDialog(title="Pop Up",text=self.var2.text, size_hint=(0.7,1), buttons=[self.btn_close, btn_dashboard])
		self.popup.open()


	def close_action(self,obj):
		self.popup.dismiss()
		self.popup2.dismiss()


	def dashboard_action(self,obj):
		btn_close = MDRectangleFlatButton(text="Close", on_release=self.close_action)
		self.popup.dismiss()
		self.popup2 = MDDialog(title="More Info",text="I love coding so much ", size_hint=(0.7,1),buttons=[btn_close])
		self.popup2 .open()



if __name__ == '__main__':
	Lesson1App().run()