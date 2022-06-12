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





class MyApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette="Green"
		self.theme_cls.primary_hbue= "A700"
		self.theme_cls.theme_style="Light"
		screen = Screen()

		table = MDDataTable(pos_hint={'center_x':0.5,'center_y': 0.5},size_hint=(0.9,0.6),check=True,rows_num=10,column_data=[
				("No.", dp(18)),
				("Language", dp(20)),
				("Projects", dp(20)),
				("Publisher", dp(20))

			],
			row_data=[
				("01","python","35","Juma"),
				("02","Ruby","10","TronLite"),
				("03","HTML","12","Jax"),
				("04","python","35","Juma"),
				("05","Ruby","10","TronLite"),
				("06","HTML","12","Jax"),
				("07","python","35","Juma"),
				("08","Ruby","10","TronLite"),
				("09","HTML","12","Jax")


			])
		table.bind(on_check_press=self.check_press)
		table.bind(on_row_press=self.row_press)
		screen.add_widget(table)
		return screen

	def check_press(self, instance_table, current_row):
		print(instance_table, current_row)
	def row_press(self, instance_table, instance_row):
		print(instance_table, instance_row)




		










		




MyApp().run()

