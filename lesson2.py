from kivymd.app import MDApp
from kivy.lang import Builder
from helpers2 import *
from kivymd.uix.list import MDList,OneLineListItem,TwoLineIconListItem,IconLeftWidget




class Lesson2App(MDApp):
	def build(self):
		screen = Builder.load_string(newlist)

		return screen
	def on_start(self):

		notes = ['Juma','John','Jackson','Egidius','Karol']

		for i in notes:
			icon = IconLeftWidget(icon="language-python")

			items = TwoLineIconListItem(text="My name is " + str(i), secondary_text="Python programmer")
			items.add_widget(icon)
			self.root.ids.space.add_widget(items)
		


		


		















if __name__ == '__main__':
	Lesson2App().run()