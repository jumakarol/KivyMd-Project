newscreen="""

Screen:
	MDNavigationLayout:
		ScreenManager:
			id: screen_manager
			
			Screen:
				name:'homescreen'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar
						title: "Lesson 3"
						left_action_items: [["menu", lambda x:nav_drawer.set_state()]]
						right_action_items: [["magnify", lambda x:app.search_now()]]
						elevation: 8

					MDLabel:
						text: "Home Page"
						halign: 'center'
					MDBottomAppBar:
						MDToolbar
							
							left_action_items: [["cog", lambda x:app.navigation_draw()],["account", lambda x:app.search_now()]]
							mode: 'end'
							type: 'bottom'
							on_action_button: app.search_now()
							icon: 'github'






			Screen:
				name:'tutorial'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar
						title: "Lesson 3"
						left_action_items: [["menu", lambda x:nav_drawer.set_state()]]
						right_action_items: [["magnify", lambda x:app.search_now()]]
						elevation: 8

					MDLabel:
						text: "Tutorial Page"
						halign: 'center'
					MDBottomAppBar:
						MDToolbar
							
							left_action_items: [["cog", lambda x:app.navigation_draw()],["account", lambda x:app.search_now()]]
							mode: 'end'
							type: 'bottom'
							on_action_button: app.search_now()
							icon: 'github'

			Screen:
				name:'courses'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar
						title: "Lesson 3"
						left_action_items: [["menu", lambda x:nav_drawer.set_state()]]
						right_action_items: [["magnify", lambda x:app.search_now()]]
						elevation: 8

					MDLabel:
						text: "Courses  Page"
						halign: 'center'
					MDBottomAppBar:
						MDToolbar
							
							left_action_items: [["cog", lambda x:app.navigation_draw()],["account", lambda x:app.search_now()]]
							mode: 'end'
							type: 'bottom'
							on_action_button: app.search_now()
							icon: 'github'


			Screen:
				name:'services'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar
						title: "Lesson 3"
						left_action_items: [["menu", lambda x:nav_drawer.set_state()]]
						right_action_items: [["magnify", lambda x:app.search_now()]]
						elevation: 8

					MDLabel:
						text: "Services Page"
						halign: 'center'
					MDBottomAppBar:
						MDToolbar
							
							left_action_items: [["cog", lambda x:app.navigation_draw()],["account", lambda x:app.search_now()]]
							mode: 'end'
							type: 'bottom'
							on_action_button: app.search_now()
							icon: 'github'

			Screen:
				name:'shop'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar
						title: "Lesson 3"
						left_action_items: [["menu", lambda x:nav_drawer.set_state()]]
						right_action_items: [["magnify", lambda x:app.search_now()]]
						elevation: 8

					MDLabel:
						text: "Buy Our Products"
						halign: 'center'
					MDBottomAppBar:
						MDToolbar
							
							left_action_items: [["cog", lambda x:app.navigation_draw()],["account", lambda x:app.search_now()]]
							mode: 'end'
							type: 'bottom'
							on_action_button: app.search_now()
							icon: 'github'
							
			Screen:
				name:'hosting'
				BoxLayout:
					orientation: 'vertical'
					MDToolbar
						title: "Lesson 3"
						left_action_items: [["menu", lambda x:nav_drawer.set_state()]]
						right_action_items: [["magnify", lambda x:app.search_now()]]
						elevation: 8

					MDLabel:
						text: "Karol Hosting"
						halign: 'center'
					MDBottomAppBar:
						MDToolbar
							
							left_action_items: [["cog", lambda x:app.navigation_draw()],["account", lambda x:app.search_now()]]
							mode: 'end'
							type: 'bottom'
							on_action_button: app.search_now()
							icon: 'github'








				








				






















































		MDNavigationDrawer:
			id: nav_drawer


			ContentNavigationDrawer:
				orientation: 'vertical'
				padding: "8dp"
				spacing: "8dp"

				Image:
					id: avatar
					size_hint: (1,1)
					source: "tronlite.png"
				MDLabel:
					text: "TronLite"
					font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                	text: 'www.tronlitetechnology.com'
                	size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView
                	DrawerList:
                		id: md_list
                		MDList:
                			OneLineIconListItem:
                				text: "Home"

                				on_release:
                					root.ids.nav_drawer.set_state()
                					root.ids.screen_manager.current = 'homescreen'
                				
                				IconLeftWidget:
                					icon:'home'



                			OneLineIconListItem:
                				text: "Tutorial"
                				on_release:
                					root.ids.nav_drawer.set_state()
                					root.ids.screen_manager.current = 'tutorial'

                				IconLeftWidget:
                					icon:'video'

                			OneLineIconListItem:
                				text: "Courses"
                				on_release:
                					root.ids.nav_drawer.set_state()
                					root.ids.screen_manager.current = 'courses'

                				IconLeftWidget:
                					icon:'book'

                			OneLineIconListItem:
                				text: "Services"
                				on_release:
                					root.ids.nav_drawer.set_state()
                					root.ids.screen_manager.current = 'services'

                				IconLeftWidget:
                					icon:'folder'

                			OneLineIconListItem:
                				text: "Shop"
                				on_release:
                					root.ids.nav_drawer.set_state()
                					root.ids.screen_manager.current = 'shop'

                				IconLeftWidget:
                					icon:'shopping'

                			OneLineIconListItem:
                				text: "Hosting"
                				on_release:
                					root.ids.nav_drawer.set_state()
                					root.ids.screen_manager.current = 'hosting'

                				IconLeftWidget:
                					icon:'server'
				

				
				







"""