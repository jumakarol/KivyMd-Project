lesson1="""

MDTextField:
	hint_text: "Enter Username"
	pos_hint: {'center_x': 0.5, 'center_y': 0.5}
	size_hint_x:None
	width: 300
	helper_text: "or click forgot password"
	helper_text_mode: "on_focus"
	icon_right: "facebook"





"""
lesson1btn="""

MDRectangleFlatButton:
	text: "Submit"
	pos_hint: {'center_x': 0.5, 'center_y': 0.4}
	on_release: self.show_data



"""
header = """
MDLabel:
	text: "My Lesson Ui"
	pos_hint: {'center_x': 0.5, 'center_y': 0.9}
	font_style: "H1"
	theme_color: "Custom"
	





"""