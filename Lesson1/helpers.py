screen_helper ="""
Screen:
	BoxLayout:
		orientation:'vertical'
		MDToolbar:
			title: 'Green Lab'
			left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
			right_action_items: [["cog", lambda x: app.navigation_setting()]]
			elevation: 8
		MDLabel:
			text: "Make Money Online"
			halign: 'center'
		Image:
			id: avatar
			size_hint: (1,1)
			source: "prod.png"

		MDList:
            OneLineIconListItem:
                text: "Profile"
                            
                IconLeftWidget:
                    icon: "face-profile"

            OneLineIconListItem:
                text: "Upload"
                            
                IconLeftWidget:
                    icon: "upload"	
													
		MDBottomAppBar:
			MDToolbar:
				title: 'Help'
				left_action_items: [["coffee", lambda x: app.navigation_help()]]
				mode:'end'
				type: 'bottom'
				icon: 'language-ruby'
				on_action_button: app.navigation_explore()
	   

				
													
				
			


	




"""
