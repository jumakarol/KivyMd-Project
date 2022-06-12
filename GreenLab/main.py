from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, ThreeLineListItem,ThreeLineIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.list import ThreeLineAvatarListItem, ImageLeftWidget, OneLineListItem
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang import Builder
from helpers import *





class GreenLabApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette="Green"
		self.theme_cls.primary_hbue= "A700"
		self.theme_cls.theme_style="Light"
		screen = Builder.load_string(screen_helper)

		
		return screen

	def navigation_draw(self):
		print("Your click Navigation")

	def navigation_setting(self):
		print("You Click Setting")

	def navigation_help(self):
		print("You Click Help")

	def navigation_explore(self):
		print("You Clicked Explorer")


			




GreenLabApp().run()

