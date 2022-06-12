newscreen = """
Screen:
	MDNavigationLayout:
		ScreenManager:
			id: screen_manager
			Screen:
				name: 'homescreen'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar:
						title: 'Cool Design'
						left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
						right_action_items: [['magnify', lambda x: app.search_now()]]
						elevation: 8

					MDLabel:
						text: 'Cool Design'
						halign: 'center'
						font_style: 'H4'
					MDBottomAppBar
						MDToolbar:
							
							left_action_items: [['cog', lambda x: nav_drawer.set_state()],['account', lambda x: app.search_now()]]
							icon:'github'
							mode: 'end'
							type: 'bottom'
							on_action_button: nav_drawer.set_state()




			Screen:
				name: 'about'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar:
						title: 'Cool App'
						left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
						right_action_items: [['magnify', lambda x: app.search_now()]]
						elevation: 8

					MDLabel:
						text: 'About Me'
						halign: 'center'
						font_style: 'H4'
					MDBottomAppBar
						MDToolbar:
							
							left_action_items: [['cog', lambda x: nav_drawer.set_state()],['account', lambda x: app.search_now()]]
							icon:'github'
							mode: 'end'
							type: 'bottom'
							on_action_button: nav_drawer.set_state()

			Screen:
				name: 'about'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar:
						title: 'Cool Design'
						left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
						right_action_items: [['magnify', lambda x: app.search_now()]]
						elevation: 8

					MDLabel:
						text: 'About Me'
						halign: 'center'
						font_style: 'H4'
					MDBottomAppBar
						MDToolbar:
							
							left_action_items: [['cog', lambda x: nav_drawer.set_state()],['account', lambda x: app.search_now()]]
							icon:'github'
							mode: 'end'
							type: 'bottom'
							on_action_button: nav_drawer.set_state()

			Screen:
				name: 'portifolio'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar:
						title: 'Cool Design'
						left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
						right_action_items: [['magnify', lambda x: app.search_now()]]
						elevation: 8

					MDLabel:
						text: 'Portifolio'
						halign: 'center'
						font_style: 'H4'
					MDBottomAppBar
						MDToolbar:
							
							left_action_items: [['cog', lambda x: nav_drawer.set_state()],['account', lambda x: app.search_now()]]
							icon:'github'
							mode: 'end'
							type: 'bottom'
							on_action_button: nav_drawer.set_state()

			Screen:
				name: 'services'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar:
						title: 'Cool Design'
						left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
						right_action_items: [['magnify', lambda x: app.search_now()]]
						elevation: 8

					MDLabel:
						text: 'Services'
						halign: 'center'
						font_style: 'H4'
					MDBottomAppBar
						MDToolbar:
							
							left_action_items: [['cog', lambda x: nav_drawer.set_state()],['account', lambda x: app.search_now()]]
							icon:'github'
							mode: 'end'
							type: 'bottom'
							on_action_button: nav_drawer.set_state()

			Screen:
				name: 'skills'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar:
						title: 'Cool Design'
						left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
						right_action_items: [['magnify', lambda x: app.search_now()]]
						elevation: 8

					MDLabel:
						text: 'My Skills'
						halign: 'center'
						font_style: 'H4'
					MDBottomAppBar
						MDToolbar:
							
							left_action_items: [['cog', lambda x: nav_drawer.set_state()],['account', lambda x: app.search_now()]]
							icon:'github'
							mode: 'end'
							type: 'bottom'
							on_action_button: nav_drawer.set_state()























































		MDNavigationDrawer:
			id: nav_drawer

			ContentNavigationDrawer:
				orientation: 'vertical'
				padding: '8dp'
				spacing: '8dp'

				Image:
					id: avatar
					size_hint: (1,1)
					
					source: 'tronlite.png'



				MDLabel:
					text: 'Cool App'
					font_style: 'Subtitle1'
					size_hint_y: None
					height: self.texture_size[1]
				MDLabel:
					text: 'info@tronlitetechnology.com'
					font_style: 'Caption'
					size_hint_y: None
					height: self.texture_size[1]


				ScrollView:
					DrawerList:
						MDList:
							OneLineIconListItem:
								on_release:
									root.ids.nav_drawer.set_state()
									root.ids.screen_manager.current = 'homescreen'
								text: 'Home'
								IconLeftWidget:
									icon: 'home'

							OneLineIconListItem:
								on_release:
									root.ids.nav_drawer.set_state()
									root.ids.screen_manager.current = 'about'
								text: 'About'
								IconLeftWidget:
									icon: 'account'

							OneLineIconListItem:
								on_release:
									root.ids.nav_drawer.set_state()
									root.ids.screen_manager.current = 'portifolio'
								text: 'Portifolio'
								IconLeftWidget:
									icon: 'electron-framework'

							OneLineIconListItem:
								on_release:
									root.ids.nav_drawer.set_state()
									root.ids.screen_manager.current = 'services'
								text: 'Services'
								IconLeftWidget:
									icon: 'server'

							OneLineIconListItem:
								on_release:
									root.ids.nav_drawer.set_state()
									root.ids.screen_manager.current = 'skills'
								text: 'skills'
								IconLeftWidget:
									icon: 'desk'


							

						












"""