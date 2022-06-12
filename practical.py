from kivymd.app import MDApp
from kivy.lang import Builder
from phelpers import *
from kivymd.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList







class PracticalApp(MDApp):
	class ContentNavigationDrawer(BoxLayout):
		pass
	class DrawerList(ThemableBehavior, MDList):
		pass



	def build(self):
		self.theme_cls.primary_palette ="Indigo"
		screen = Builder.load_string(newscreen)
		return screen



	def search_now(self):
		print('Search action is clicked')




if __name__ == '__main__':
	PracticalApp().run()
			
