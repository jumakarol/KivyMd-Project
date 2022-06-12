from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, ThreeLineListItem,ThreeLineIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.list import ThreeLineAvatarListItem, ImageLeftWidget, OneLineListItem
from kivy.lang import Builder
from helpers import *





class MyApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette="Green"
		self.theme_cls.primary_hbue= "A700"
		self.theme_cls.theme_style="Light"
		screen = Builder.load_string(list_helper)

		return screen


	def on_start(self):

		for i in range(20):
			img = ImageLeftWidget(source="prod.png")
			items = ThreeLineAvatarListItem(text="Item " + str(i), secondary_text="Check Out", tertiary_text="$.90")
		
			items.add_widget(img)
			self.root.ids.prodlist.add_widget(items)
			
		#screen.add_widget(scroll)

		







MyApp().run()

