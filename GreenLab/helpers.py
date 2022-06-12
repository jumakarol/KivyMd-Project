screen_helper ="""
Screen:
	BoxLayout:
		orientation:'vertical'
		MDToolbar:
			title: 'Green Lab'
			left_action_items: [["menu", lambda x: app.navigation_draw()]]
			right_action_items: [["cog", lambda x: app.navigation_setting()]]
			elevation: 8
		MDLabel:
			text: "Make Money Online"
			halign: 'center'
		MDBottomAppBar:
			MDToolbar:
				title: 'Help'
				left_action_items: [["coffee", lambda x: app.navigation_help()]]
				mode:'end'
				type: 'bottom'
				icon: 'folder-open-outline'
				on_action_button: app.navigation_explore()
				
				
			


	




"""
