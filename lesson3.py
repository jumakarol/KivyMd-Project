from kivymd.app import MDApp
from kivy.lang import Builder
from helpers3 import *
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList




class Lesson3App(MDApp):
	class ContentNavigationDrawer(BoxLayout):
		pass
	class DrawerList(ThemableBehavior,MDList):
		pass
	def build(self):
		screen = Builder.load_string(newscreen)
		return screen



	def navigation_draw(self):
		print("This is navigation")
	def search_now(self):
		print("Search now")




if __name__ == '__main__':
	Lesson3App().run()