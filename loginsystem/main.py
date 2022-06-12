from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import *




class LoginSystemApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette="Green"
		self.theme_cls.primary_hbue= "A700"
		self.theme_cls.theme_style="Light"
		screen = Screen()
		
		login_btn = MDRectangleFlatButton(text="Login Now",pos_hint={'center_x': 0.5, 'center_y': 0.3},on_release= self.show_data)
		self.username = Builder.load_string(username_helper)
		self.password = Builder.load_string(password_helper)
		screen.add_widget(self.username)
		screen.add_widget(self.password)
		screen.add_widget(login_btn)

		return screen

	def show_data(self, obj):
		close_btn = MDRectangleFlatButton(text="close", on_release=self.close_data)
		dashboard_btn = MDRectangleFlatButton(text="Dashboard")
		if self.password.text == "password12":
			check_string = self.username.text
			
			
			self.dialog = MDDialog(title="Welcome",text=check_string, size_hint=(0.7,1), buttons=[close_btn, dashboard_btn])
			
		#print(self.username.text)
		#print(self.password.text)
		elif self.password.text is "":
			check_string = "Please Enter Password"
			self.dialog = MDDialog(title="Welcome",text=check_string, size_hint=(0.7,1), buttons=[close_btn])
		else:
			check_string = "Incorrect password"
			self.dialog = MDDialog(title="Welcome",text=check_string, size_hint=(0.7,1), buttons=[close_btn])
		self.dialog.open()

	def close_data(self, obj):
		self.dialog.dismiss()






LoginSystemApp().run()

