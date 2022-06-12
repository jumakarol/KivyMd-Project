navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Green Money'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation:5

                    Widget:

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
                    text: "Juma Karol"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "info@tronlitetechnology.com"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]

                ScrollView:

                    DrawerList:
                        id: md_list
                        
                        MDList:
                            OneLineIconListItem:
                                text: "Profile"
                            
                                IconLeftWidget:
                                    icon: "face-profile"
                                    
                           
                                    
                            OneLineIconListItem:
                                text: "portifolio"
                            
                                IconLeftWidget:
                                    icon: "file"
                                    
                           
                            OneLineIconListItem:
                                text: "Logout"
                            
                                IconLeftWidget:
                                    icon: "logout"
                                    
                           
                                
                            
                            

"""
