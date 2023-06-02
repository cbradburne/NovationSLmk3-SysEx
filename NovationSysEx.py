#macOS
# pip3 install https://github.com/kivy/kivy/archive/master.zip --no-cache-dir
# pip3 install https://github.com/kivymd/KivyMD/archive/master.zip --no-cache-dir
# pip3 install pyinstaller

# To create a standalone App
# python3 -m PyInstaller --onefile --name NovationSysEx --windowed NovationSysEx.py

#Windows
# python -m pip install https://github.com/kivy/kivy/archive/master.zip
# python -m pip install https://github.com/kivymd/KivyMD/archive/master.zip
# python -m pip install pyinstaller

# To create a standalone App
# python -m PyInstaller --onefile -name NovationSysEx --windowed NovationSysEx.py

from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix import screen
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.widget import Widget
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.filemanager import MDFileManager
import os
import json

#Config.set('graphics', 'width', '1600')
#Config.set('graphics', 'height', '900')
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'window_state', 'windowed')
Config.set('kivy', 'exit_on_escape', '0')
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.write()

class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class ThirdWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

header = b'\xf0\x00\x20\x29\x02\x0a\x01'
footer = b'\xf7'

setScreenProperties = b'\x02'
setLayoutProperties = b'\x01'
setLayoutToKnobs = b'\x01'

config = {}

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import NoTransition kivy.uix.screenmanager.NoTransition

WindowManager:
    transition: NoTransition()
    MainWindow:
    SecondWindow:
    ThirdWindow:

<MainWindow>:
    name: 'main'
    MDScreen:
        id: main

        MDRaisedButton:
            id: applyToTopBars
            md_bg_color: .3, .3, .3, 1
            pos_hint: {"center_x": .03, "center_y": .83}
            #size: 200, 30
            #size_hint: None, None
            text_color: 1, 1, 1, 1
            font_size: "12sp"
            text: 'Apply to Top'
            on_release: app.applyToTopBars()

        MDRaisedButton:
            id: applyToAllBars
            md_bg_color: .3, .3, .3, 1
            pos_hint: {"center_x": .03, "center_y": .7}
            #size: 200, 30
            #size_hint: None, None
            text_color: 1, 1, 1, 1
            font_size: "12sp"
            text: 'Apply to ALL'
            on_release: app.applyToAllBars()

        MDRaisedButton:
            id: applyToBotBars
            md_bg_color: .3, .3, .3, 1
            pos_hint: {"center_x": .03, "center_y": .18}
            #size: 200, 30
            #size_hint: None, None
            text_color: 1, 1, 1, 1
            font_size: "12sp"
            text: 'Apply to Bot'
            on_release: app.applyToBotBars()

            

        MDRaisedButton:
            id: applyToAllKnobs
            md_bg_color: .3, .3, .3, 1
            pos_hint: {"center_x": .03, "center_y": .5}
            #size: 200, 30
            #size_hint: None, None
            text_color: 1, 1, 1, 1
            font_size: "12sp"
            text: 'Apply to ALL'
            on_release: app.applyToAllKnobs()

        
        MDFlatButton:
            line_width: 2.4
            line_color: 0.4, 0.4, 0.4, 1
            pos_hint: {"center_x": .14, "center_y": .5}
            size: 490, 600
            size_hint: None, None
            disabled: True

        MDTextField:
            id: textInputBox11
            pos_hint: {"center_x": .1, "center_y": .8}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'Chorus'
        MDTextField:
            id: textInputBox12
            pos_hint: {"center_x": .1, "center_y": .73}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox13
            pos_hint: {"center_x": .1, "center_y": .3}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'Piano'
        MDTextField:
            id: textInputBox14
            pos_hint: {"center_x": .1, "center_y": .23}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''

    
        MDRaisedButton:
            id: panelBarTop01
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .1, "center_y": .85}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(17)

        MDRaisedButton:
            id: panelBarBot01
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .1, "center_y": .15}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(18)



        MDRoundFlatButton:
            id: panelKnob01
            line_width: 2.4
            line_color: 1, 1, 1, 1
            pos_hint: {"center_x": .1, "center_y": .5}
            size: 120, 120
            size_hint: None, None
            on_release: app.open_color_picker(33)







        MDTextField:
            id: textInputBox21
            pos_hint: {"center_x": .18, "center_y": .8}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'Tremolo'
        MDTextField:
            id: textInputBox22
            pos_hint: {"center_x": .18, "center_y": .73}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox23
            pos_hint: {"center_x": .18, "center_y": .3}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'E.Piano'
        MDTextField:
            id: textInputBox24
            pos_hint: {"center_x": .18, "center_y": .23}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''

        
        MDRaisedButton:
            id: panelBarTop02
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .18, "center_y": .85}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(19)

        MDRaisedButton:
            id: panelBarBot02
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .18, "center_y": .15}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(20)


        MDRoundFlatButton:
            id: panelKnob02
            line_width: 2.4
            line_color: 1, 1, 1, 1
            pos_hint: {"center_x": .18, "center_y": .5}
            size: 120, 120
            size_hint: None, None
            on_release: app.open_color_picker(34)

        
            



        MDFlatButton:
            line_width: 2.4
            line_color: 0.4, 0.4, 0.4, 1
            pos_hint: {"center_x": .3, "center_y": .5}
            size: 490, 600
            size_hint: None, None
            disabled: True

        MDTextField:
            id: textInputBox31
            pos_hint: {"center_x": .26, "center_y": .8}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox32
            pos_hint: {"center_x": .26, "center_y": .73}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox33
            pos_hint: {"center_x": .26, "center_y": .3}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'Clav'
        MDTextField:
            id: textInputBox34
            pos_hint: {"center_x": .26, "center_y": .23}
            size_hint_x: 0.06
            text_color_normal: "white"

        
        MDRaisedButton:
            id: panelBarTop03
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .26, "center_y": .85}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(21)

        MDRaisedButton:
            id: panelBarBot03
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .26, "center_y": .15}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(22)


        MDRoundFlatButton:
            id: panelKnob03
            line_width: 2.4
            line_color: 1, 1, 1, 1
            pos_hint: {"center_x": .26, "center_y": .5}
            size: 120, 120
            size_hint: None, None
            on_release: app.open_color_picker(35)
            




        MDTextField:
            id: textInputBox41
            pos_hint: {"center_x": .34, "center_y": .8}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox42
            pos_hint: {"center_x": .34, "center_y": .73}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox43
            pos_hint: {"center_x": .34, "center_y": .3}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'Strings'
        MDTextField:
            id: textInputBox44
            pos_hint: {"center_x": .34, "center_y": .23}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''

        
        MDRaisedButton:
            id: panelBarTop04
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .34, "center_y": .85}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(23)

        MDRaisedButton:
            id: panelBarBot04
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .34, "center_y": .15}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(24)


        MDRoundFlatButton:
            id: panelKnob04
            line_width: 2.4
            line_color: 1, 1, 1, 1
            pos_hint: {"center_x": .34, "center_y": .5}
            size: 120, 120
            size_hint: None, None
            on_release: app.open_color_picker(36)




            

        
        MDFlatButton:
            line_width: 2.4
            line_color: 0.4, 0.4, 0.4, 1
            pos_hint: {"center_x": .46, "center_y": .5}
            size: 490, 600
            size_hint: None, None
            disabled: True

        MDTextField:
            id: textInputBox51
            pos_hint: {"center_x": .42, "center_y": .8}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox52
            pos_hint: {"center_x": .42, "center_y": .73}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox53
            pos_hint: {"center_x": .42, "center_y": .3}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'Bells'
        MDTextField:
            id: textInputBox54
            pos_hint: {"center_x": .42, "center_y": .23}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'Organ 1'

        
        MDRaisedButton:
            id: panelBarTop05
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .42, "center_y": .85}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(25)

        MDRaisedButton:
            id: panelBarBot05
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .42, "center_y": .15}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(26)


        MDRoundFlatButton:
            id: panelKnob05
            line_width: 2.4
            line_color: 1, 1, 1, 1
            pos_hint: {"center_x": .42, "center_y": .5}
            size: 120, 120
            size_hint: None, None
            on_release: app.open_color_picker(37)



        MDTextField:
            id: textInputBox61
            pos_hint: {"center_x": .5, "center_y": .8}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox62
            pos_hint: {"center_x": .5, "center_y": .73}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox63
            pos_hint: {"center_x": .5, "center_y": .3}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox64
            pos_hint: {"center_x": .5, "center_y": .23}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'Organ 2'

        
        MDRaisedButton:
            id: panelBarTop06
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .5, "center_y": .85}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(27)

        MDRaisedButton:
            id: panelBarBot06
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .5, "center_y": .15}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(28)


        MDRoundFlatButton:
            id: panelKnob06
            line_width: 2.4
            line_color: 1, 1, 1, 1
            pos_hint: {"center_x": .5, "center_y": .5}
            size: 120, 120
            size_hint: None, None
            on_release: app.open_color_picker(38)




        
            

        MDFlatButton:
            line_width: 2.4
            line_color: 0.4, 0.4, 0.4, 1
            pos_hint: {"center_x": .62, "center_y": .5}
            size: 490, 600
            size_hint: None, None
            disabled: True

        MDTextField:
            id: textInputBox71
            pos_hint: {"center_x": .58, "center_y": .8}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox72
            pos_hint: {"center_x": .58, "center_y": .73}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox73
            pos_hint: {"center_x": .58, "center_y": .3}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox74
            pos_hint: {"center_x": .58, "center_y": .23}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'Organ 3'

        
        MDRaisedButton:
            id: panelBarTop07
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .58, "center_y": .85}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(29)

        MDRaisedButton:
            id: panelBarBot07
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .58, "center_y": .15}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(30)


        MDRoundFlatButton:
            id: panelKnob07
            line_width: 2.4
            line_color: 1, 1, 1, 1
            pos_hint: {"center_x": .58, "center_y": .5}
            size: 120, 120
            size_hint: None, None
            on_release: app.open_color_picker(39)






        MDTextField:
            id: textInputBox81
            pos_hint: {"center_x": .66, "center_y": .8}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox82
            pos_hint: {"center_x": .66, "center_y": .73}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox83
            pos_hint: {"center_x": .66, "center_y": .3}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox84
            pos_hint: {"center_x": .66, "center_y": .23}
            size_hint_x: 0.06
            text_color_normal: "white"
            text: 'Organ 4'

        
        MDRaisedButton:
            id: panelBarTop08
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .66, "center_y": .85}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(31)

        MDRaisedButton:
            id: panelBarBot08
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .66, "center_y": .15}
            size: 200, 20
            size_hint: None, None
            on_release: app.open_color_picker(32)


        MDRoundFlatButton:
            id: panelKnob08
            line_width: 2.4
            line_color: 1, 1, 1, 1
            pos_hint: {"center_x": .66, "center_y": .5}
            size: 120, 120
            size_hint: None, None
            on_release: app.open_color_picker(40)




            

        
        MDFlatButton:
            line_width: 2.4
            line_color: 0.4, 0.4, 0.4, 1
            pos_hint: {"center_x": .78, "center_y": .5}
            size: 490, 600
            size_hint: None, None
            disabled: True

        MDTextField:
            id: textInputBox91
            pos_hint: {"center_x": .74, "center_y": .75}
            size_hint_x: 0.05
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox92
            pos_hint: {"center_x": .74, "center_y": .66}
            size_hint_x: 0.05
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox93
            pos_hint: {"center_x": .82, "center_y": .785}
            size_hint_x: 0.05
            text_color_normal: "white"
            text: ''
        MDTextField:
            id: textInputBox94
            pos_hint: {"center_x": .82, "center_y": .63}
            size_hint_x: 0.05
            text_color_normal: "white"
            text: ''

            

        
        MDRaisedButton:
            id: panelBarLeft09
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .71, "center_y": .7}
            size: 20, 220
            size_hint: None, None
            on_release: app.open_color_picker(33)

        MDRaisedButton:
            id: panelBarRightTop09
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .85, "center_y": .775}
            size: 20, 100
            size_hint: None, None
            on_release: app.open_color_picker(34)

        MDRaisedButton:
            id: panelBarRightBot09
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .85, "center_y": .625}
            size: 20, 100
            size_hint: None, None
            on_release: app.open_color_picker(35)




        MDFlatButton:
            text: "Open config"
            text_color: 0, 0, 1, 1
            line_width: 2
            line_color: 0.7, 0.2, 0.2, 1
            pos_hint: {'center_x': .92, 'center_y': .8}
            size_hint_x: 0.1
            font_size: "18sp"
            on_release: app.openFileLoadScreen()
        
        MDTextField:
            id: textInputSave
            pos_hint: {"center_x": .92, "center_y": .65}
            size_hint_x: 0.1
            text_color_normal: "white"
            text: ''
        
        MDFlatButton:
            text: "Save config"
            text_color: 0, 0, 1, 1
            line_width: 2
            line_color: 0.7, 0.2, 0.2, 1
            pos_hint: {'center_x': .92, 'center_y': .54}
            size_hint_x: 0.1
            font_size: "18sp"
            on_release: app.pressSaveFile()




        MDTextField:
            id: textInputSaveSysEx
            pos_hint: {"center_x": .92, "center_y": .3}
            size_hint_x: 0.1
            text_color_normal: "white"
            text: 'NovationSysEx'

        MDFlatButton:
            id: createFileButton
            text: "Create File"
            text_color: 0, 0, 1, 1
            line_width: 2
            line_color: 0.7, 0.2, 0.2, 1
            pos_hint: {"center_x": .92, "center_y": .175}
            size_hint: (0.1), (0.02)
            font_size: "18sp"
            on_release: app.createFile()





<SecondWindow>:
    name: 'RGBPicker'
    MDScreen:
        id: RGBPicker
        GridLayout:
            id: colourPicker
            cols: 1
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: (0.4), (0.9)

<ThirdWindow>:
    name: 'loadFileWindow'
    MDScreen:
        id: fileWindow
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: (0.5), (0.9)
        BoxLayout:
            orientation: "vertical"
            FileChooserListView:
                id: fileChooserLoad

            BoxLayout:
                size_hint_y: None
                height: 60
                Button:
                    text: "Cancel"
                    on_release: app.cancelFile()

                Button:
                    text: "Load"
                    on_release: app.pressLoadFile(fileChooserLoad.selection)
'''

class MainApp(MDApp):
    def build(self):
        self.title = 'Novation SL Mk3 SysEx'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        Window.size = (1600, 400)
        return Builder.load_string(KV)
    
    def openFileLoadScreen(self):
        self.root.current = "loadFileWindow"
    
    def cancelFile(self):
        self.root.current = "main"

    def pressLoadFile(self, fileName):
        global config

        self.root.current = "main"

        try:
            with open(fileName[0], 'r') as f:
                config = json.load(f)

            head, tail = os.path.split(fileName[0])

            self.root.get_screen('main').ids.textInputSave.text = tail[:-5]
            self.root.get_screen('main').ids.textInputSaveSysEx.text = config['sysexfile']

            self.root.get_screen('main').ids.textInputBox11.text = config['textBox11']
            self.root.get_screen('main').ids.textInputBox12.text = config['textBox12']
            self.root.get_screen('main').ids.textInputBox13.text = config['textBox13']
            self.root.get_screen('main').ids.textInputBox14.text = config['textBox14']

            self.root.get_screen('main').ids.textInputBox21.text = config['textBox21']
            self.root.get_screen('main').ids.textInputBox22.text = config['textBox22']
            self.root.get_screen('main').ids.textInputBox23.text = config['textBox23']
            self.root.get_screen('main').ids.textInputBox24.text = config['textBox24']

            self.root.get_screen('main').ids.textInputBox31.text = config['textBox31']
            self.root.get_screen('main').ids.textInputBox32.text = config['textBox32']
            self.root.get_screen('main').ids.textInputBox33.text = config['textBox33']
            self.root.get_screen('main').ids.textInputBox34.text = config['textBox34']

            self.root.get_screen('main').ids.textInputBox41.text = config['textBox41']
            self.root.get_screen('main').ids.textInputBox42.text = config['textBox42']
            self.root.get_screen('main').ids.textInputBox43.text = config['textBox43']
            self.root.get_screen('main').ids.textInputBox44.text = config['textBox44']

            self.root.get_screen('main').ids.textInputBox51.text = config['textBox51']
            self.root.get_screen('main').ids.textInputBox52.text = config['textBox52']
            self.root.get_screen('main').ids.textInputBox53.text = config['textBox53']
            self.root.get_screen('main').ids.textInputBox54.text = config['textBox54']

            self.root.get_screen('main').ids.textInputBox61.text = config['textBox61']
            self.root.get_screen('main').ids.textInputBox62.text = config['textBox62']
            self.root.get_screen('main').ids.textInputBox63.text = config['textBox63']
            self.root.get_screen('main').ids.textInputBox64.text = config['textBox64']

            self.root.get_screen('main').ids.textInputBox71.text = config['textBox71']
            self.root.get_screen('main').ids.textInputBox72.text = config['textBox72']
            self.root.get_screen('main').ids.textInputBox73.text = config['textBox73']
            self.root.get_screen('main').ids.textInputBox74.text = config['textBox74']

            self.root.get_screen('main').ids.textInputBox81.text = config['textBox81']
            self.root.get_screen('main').ids.textInputBox82.text = config['textBox82']
            self.root.get_screen('main').ids.textInputBox83.text = config['textBox83']
            self.root.get_screen('main').ids.textInputBox84.text = config['textBox84']

            self.root.get_screen('main').ids.textInputBox91.text = config['textBox91']
            self.root.get_screen('main').ids.textInputBox92.text = config['textBox92']
            self.root.get_screen('main').ids.textInputBox93.text = config['textBox93']
            self.root.get_screen('main').ids.textInputBox94.text = config['textBox94']

            self.root.get_screen('main').ids.panelBarTop01.md_bg_color = config['panelBarTop01']
            self.root.get_screen('main').ids.panelBarTop02.md_bg_color = config['panelBarTop02']
            self.root.get_screen('main').ids.panelBarTop03.md_bg_color = config['panelBarTop03']
            self.root.get_screen('main').ids.panelBarTop04.md_bg_color = config['panelBarTop04']
            self.root.get_screen('main').ids.panelBarTop05.md_bg_color = config['panelBarTop05']
            self.root.get_screen('main').ids.panelBarTop06.md_bg_color = config['panelBarTop06']
            self.root.get_screen('main').ids.panelBarTop07.md_bg_color = config['panelBarTop07']
            self.root.get_screen('main').ids.panelBarTop08.md_bg_color = config['panelBarTop08']
            self.root.get_screen('main').ids.panelBarLeft09.md_bg_color = config['panelBarTop09']
            self.root.get_screen('main').ids.panelBarRightTop09.md_bg_color = config['panelBarTop10']

            self.root.get_screen('main').ids.panelBarBot01.md_bg_color = config['panelBarBot01']
            self.root.get_screen('main').ids.panelBarBot02.md_bg_color = config['panelBarBot02']
            self.root.get_screen('main').ids.panelBarBot03.md_bg_color = config['panelBarBot03']
            self.root.get_screen('main').ids.panelBarBot04.md_bg_color = config['panelBarBot04']
            self.root.get_screen('main').ids.panelBarBot05.md_bg_color = config['panelBarBot05']
            self.root.get_screen('main').ids.panelBarBot06.md_bg_color = config['panelBarBot06']
            self.root.get_screen('main').ids.panelBarBot07.md_bg_color = config['panelBarBot07']
            self.root.get_screen('main').ids.panelBarBot08.md_bg_color = config['panelBarBot08']
            self.root.get_screen('main').ids.panelBarRightBot09.md_bg_color = config['panelBarBot09']
            
            self.root.get_screen('main').ids.panelKnob01.line_color = config['panelKnob01']
            self.root.get_screen('main').ids.panelKnob02.line_color = config['panelKnob02']
            self.root.get_screen('main').ids.panelKnob03.line_color = config['panelKnob03']
            self.root.get_screen('main').ids.panelKnob04.line_color = config['panelKnob04']
            self.root.get_screen('main').ids.panelKnob05.line_color = config['panelKnob05']
            self.root.get_screen('main').ids.panelKnob06.line_color = config['panelKnob06']
            self.root.get_screen('main').ids.panelKnob07.line_color = config['panelKnob07']
            self.root.get_screen('main').ids.panelKnob08.line_color = config['panelKnob08']

        except:
            print("not json file")
            pass

    def pressSaveFile(self):
        global config

        filename = self.root.get_screen('main').ids.textInputSave.text
        config['sysexfile'] = self.root.get_screen('main').ids.textInputSaveSysEx.text

        config['textBox11'] = self.root.get_screen('main').ids.textInputBox11.text
        config['textBox12'] = self.root.get_screen('main').ids.textInputBox12.text
        config['textBox13'] = self.root.get_screen('main').ids.textInputBox13.text
        config['textBox14'] = self.root.get_screen('main').ids.textInputBox14.text

        config['textBox21'] = self.root.get_screen('main').ids.textInputBox21.text
        config['textBox22'] = self.root.get_screen('main').ids.textInputBox22.text
        config['textBox23'] = self.root.get_screen('main').ids.textInputBox23.text
        config['textBox24'] = self.root.get_screen('main').ids.textInputBox24.text

        config['textBox31'] = self.root.get_screen('main').ids.textInputBox31.text
        config['textBox32'] = self.root.get_screen('main').ids.textInputBox32.text
        config['textBox33'] = self.root.get_screen('main').ids.textInputBox33.text
        config['textBox34'] = self.root.get_screen('main').ids.textInputBox34.text

        config['textBox41'] = self.root.get_screen('main').ids.textInputBox41.text
        config['textBox42'] = self.root.get_screen('main').ids.textInputBox42.text
        config['textBox43'] = self.root.get_screen('main').ids.textInputBox43.text
        config['textBox44'] = self.root.get_screen('main').ids.textInputBox44.text

        config['textBox51'] = self.root.get_screen('main').ids.textInputBox51.text
        config['textBox52'] = self.root.get_screen('main').ids.textInputBox52.text
        config['textBox53'] = self.root.get_screen('main').ids.textInputBox53.text
        config['textBox54'] = self.root.get_screen('main').ids.textInputBox54.text

        config['textBox61'] = self.root.get_screen('main').ids.textInputBox61.text
        config['textBox62'] = self.root.get_screen('main').ids.textInputBox62.text
        config['textBox63'] = self.root.get_screen('main').ids.textInputBox63.text
        config['textBox64'] = self.root.get_screen('main').ids.textInputBox64.text

        config['textBox71'] = self.root.get_screen('main').ids.textInputBox71.text
        config['textBox72'] = self.root.get_screen('main').ids.textInputBox72.text
        config['textBox73'] = self.root.get_screen('main').ids.textInputBox73.text
        config['textBox74'] = self.root.get_screen('main').ids.textInputBox74.text

        config['textBox81'] = self.root.get_screen('main').ids.textInputBox81.text
        config['textBox82'] = self.root.get_screen('main').ids.textInputBox82.text
        config['textBox83'] = self.root.get_screen('main').ids.textInputBox83.text
        config['textBox84'] = self.root.get_screen('main').ids.textInputBox84.text

        config['textBox91'] = self.root.get_screen('main').ids.textInputBox91.text
        config['textBox92'] = self.root.get_screen('main').ids.textInputBox92.text
        config['textBox93'] = self.root.get_screen('main').ids.textInputBox93.text
        config['textBox94'] = self.root.get_screen('main').ids.textInputBox94.text

        config['panelBarTop01'] = self.root.get_screen('main').ids.panelBarTop01.md_bg_color
        config['panelBarTop02'] = self.root.get_screen('main').ids.panelBarTop02.md_bg_color
        config['panelBarTop03'] = self.root.get_screen('main').ids.panelBarTop03.md_bg_color
        config['panelBarTop04'] = self.root.get_screen('main').ids.panelBarTop04.md_bg_color
        config['panelBarTop05'] = self.root.get_screen('main').ids.panelBarTop05.md_bg_color
        config['panelBarTop06'] = self.root.get_screen('main').ids.panelBarTop06.md_bg_color
        config['panelBarTop07'] = self.root.get_screen('main').ids.panelBarTop07.md_bg_color
        config['panelBarTop08'] = self.root.get_screen('main').ids.panelBarTop08.md_bg_color
        config['panelBarTop09'] = self.root.get_screen('main').ids.panelBarLeft09.md_bg_color
        config['panelBarTop10'] = self.root.get_screen('main').ids.panelBarRightTop09.md_bg_color

        config['panelBarBot01'] = self.root.get_screen('main').ids.panelBarBot01.md_bg_color
        config['panelBarBot02'] = self.root.get_screen('main').ids.panelBarBot02.md_bg_color
        config['panelBarBot03'] = self.root.get_screen('main').ids.panelBarBot03.md_bg_color
        config['panelBarBot04'] = self.root.get_screen('main').ids.panelBarBot04.md_bg_color
        config['panelBarBot05'] = self.root.get_screen('main').ids.panelBarBot05.md_bg_color
        config['panelBarBot06'] = self.root.get_screen('main').ids.panelBarBot06.md_bg_color
        config['panelBarBot07'] = self.root.get_screen('main').ids.panelBarBot07.md_bg_color
        config['panelBarBot08'] = self.root.get_screen('main').ids.panelBarBot08.md_bg_color
        config['panelBarBot09'] = self.root.get_screen('main').ids.panelBarRightBot09.md_bg_color
        
        config['panelKnob01'] = self.root.get_screen('main').ids.panelKnob01.line_color
        config['panelKnob02'] = self.root.get_screen('main').ids.panelKnob02.line_color
        config['panelKnob03'] = self.root.get_screen('main').ids.panelKnob03.line_color
        config['panelKnob04'] = self.root.get_screen('main').ids.panelKnob04.line_color
        config['panelKnob05'] = self.root.get_screen('main').ids.panelKnob05.line_color
        config['panelKnob06'] = self.root.get_screen('main').ids.panelKnob06.line_color
        config['panelKnob07'] = self.root.get_screen('main').ids.panelKnob07.line_color
        config['panelKnob08'] = self.root.get_screen('main').ids.panelKnob08.line_color

        if filename != "":
            filename += ".json"
            with open(filename, 'w') as f:
                json.dump(config, f)

    def textStringToBytes(self, sentString):
        sentStringBytes = (r'\x' + (r'\x').join([(sentString.encode().hex())[i:i+2] for i in range(0, len((sentString.encode().hex())), 2)])).encode().decode('unicode_escape').encode("raw_unicode_escape")
        sentStringBytes += b'\x00'
        return sentStringBytes
    
    def panelBarColours(self):

        tb1 = b'\x00\x04\x00'
        tb2 = b'\x01\x04\x00'
        tb3 = b'\x02\x04\x00'
        tb4 = b'\x03\x04\x00'
        tb5 = b'\x04\x04\x00'
        tb6 = b'\x05\x04\x00'
        tb7 = b'\x06\x04\x00'
        tb8 = b'\x07\x04\x00'
        tb9 = b'\x08\x04\x00'
        tb10 = b'\x08\x04\x01'

        bb1 = b'\x00\x04\x02'
        bb2 = b'\x01\x04\x02'
        bb3 = b'\x02\x04\x02'
        bb4 = b'\x03\x04\x02'
        bb5 = b'\x04\x04\x02'
        bb6 = b'\x05\x04\x02'
        bb7 = b'\x06\x04\x02'
        bb8 = b'\x07\x04\x02'
        bb9 = b'\x08\x04\x02'

        num1 = int(self.root.get_screen('main').ids.panelBarTop01.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarTop01.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarTop01.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        tbc1 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelBarTop02.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarTop02.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarTop02.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        tbc2 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")
        
        num1 = int(self.root.get_screen('main').ids.panelBarTop03.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarTop03.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarTop03.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        tbc3 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")
        
        num1 = int(self.root.get_screen('main').ids.panelBarTop04.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarTop04.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarTop04.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        tbc4 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")
        
        num1 = int(self.root.get_screen('main').ids.panelBarTop05.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarTop05.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarTop05.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        tbc5 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")
        
        num1 = int(self.root.get_screen('main').ids.panelBarTop06.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarTop06.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarTop06.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        tbc6 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")
        
        num1 = int(self.root.get_screen('main').ids.panelBarTop07.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarTop07.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarTop07.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        tbc7 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")
        
        num1 = int(self.root.get_screen('main').ids.panelBarTop08.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarTop08.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarTop08.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        tbc8 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")
        
        num1 = int(self.root.get_screen('main').ids.panelBarLeft09.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarLeft09.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarLeft09.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        tbc9 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")
        
        num1 = int(self.root.get_screen('main').ids.panelBarRightTop09.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarRightTop09.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarRightTop09.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        tbc10 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")


        num1 = int(self.root.get_screen('main').ids.panelBarBot01.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarBot01.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarBot01.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        bbc1 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelBarBot02.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarBot02.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarBot02.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        bbc2 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelBarBot03.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarBot03.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarBot03.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        bbc3 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelBarBot04.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarBot04.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarBot04.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        bbc4 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelBarBot05.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarBot05.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarBot05.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        bbc5 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelBarBot06.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarBot06.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarBot06.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        bbc6 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelBarBot07.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarBot07.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarBot07.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        bbc7 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelBarBot08.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarBot08.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarBot08.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        bbc8 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelBarRightBot09.md_bg_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelBarRightBot09.md_bg_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelBarRightBot09.md_bg_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        bbc9 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        panelBarColours = tb1 + tbc1 + bb1 + bbc1 + tb2 + tbc2 + bb2 + bbc2 + tb3 + tbc3 + bb3 + bbc3 + tb4 + tbc4 + bb4 + bbc4 + tb5 + tbc5 + bb5 + bbc5 + tb6 + tbc6 + bb6 + bbc6 + tb7 + tbc7 + bb7 + bbc7 + tb8 + tbc8 + bb8 + bbc8 + tb9 + tbc9 + bb9 + bbc9 + tb10 + tbc10

        return panelBarColours
    
    def panelText(self):
        panelTextID11 = b'\x00\x01\x00'
        panelTextID12 = b'\x00\x01\x01'
        panelTextID13 = b'\x00\x01\x02'
        panelTextID14 = b'\x00\x01\x03'

        panelTextID21 = b'\x01\x01\x00'
        panelTextID22 = b'\x01\x01\x01'
        panelTextID23 = b'\x01\x01\x02'
        panelTextID24 = b'\x01\x01\x03'

        panelTextID31 = b'\x02\x01\x00'
        panelTextID32 = b'\x02\x01\x01'
        panelTextID33 = b'\x02\x01\x02'
        panelTextID34 = b'\x02\x01\x03'

        panelTextID41 = b'\x03\x01\x00'
        panelTextID42 = b'\x03\x01\x01'
        panelTextID43 = b'\x03\x01\x02'
        panelTextID44 = b'\x03\x01\x03'

        panelTextID51 = b'\x04\x01\x00'
        panelTextID52 = b'\x04\x01\x01'
        panelTextID53 = b'\x04\x01\x02'
        panelTextID54 = b'\x04\x01\x03'

        panelTextID61 = b'\x05\x01\x00'
        panelTextID62 = b'\x05\x01\x01'
        panelTextID63 = b'\x05\x01\x02'
        panelTextID64 = b'\x05\x01\x03'

        panelTextID71 = b'\x06\x01\x00'
        panelTextID72 = b'\x06\x01\x01'
        panelTextID73 = b'\x06\x01\x02'
        panelTextID74 = b'\x06\x01\x03'

        panelTextID81 = b'\x07\x01\x00'
        panelTextID82 = b'\x07\x01\x01'
        panelTextID83 = b'\x07\x01\x02'
        panelTextID84 = b'\x07\x01\x03'

        panelTextID91 = b'\x08\x01\x00'
        panelTextID92 = b'\x08\x01\x01'
        panelTextID93 = b'\x08\x01\x02'
        panelTextID94 = b'\x08\x01\x03'

        textBoxString = b''
        eol = b'\x00'
        
        textBox11 = self.root.get_screen('main').ids.textInputBox11.text
        textBox12 = self.root.get_screen('main').ids.textInputBox12.text
        textBox13 = self.root.get_screen('main').ids.textInputBox13.text
        textBox14 = self.root.get_screen('main').ids.textInputBox14.text

        textBox21 = self.root.get_screen('main').ids.textInputBox21.text
        textBox22 = self.root.get_screen('main').ids.textInputBox22.text
        textBox23 = self.root.get_screen('main').ids.textInputBox23.text
        textBox24 = self.root.get_screen('main').ids.textInputBox24.text

        textBox31 = self.root.get_screen('main').ids.textInputBox31.text
        textBox32 = self.root.get_screen('main').ids.textInputBox32.text
        textBox33 = self.root.get_screen('main').ids.textInputBox33.text
        textBox34 = self.root.get_screen('main').ids.textInputBox34.text

        textBox41 = self.root.get_screen('main').ids.textInputBox41.text
        textBox42 = self.root.get_screen('main').ids.textInputBox42.text
        textBox43 = self.root.get_screen('main').ids.textInputBox43.text
        textBox44 = self.root.get_screen('main').ids.textInputBox44.text

        textBox51 = self.root.get_screen('main').ids.textInputBox51.text
        textBox52 = self.root.get_screen('main').ids.textInputBox52.text
        textBox53 = self.root.get_screen('main').ids.textInputBox53.text
        textBox54 = self.root.get_screen('main').ids.textInputBox54.text

        textBox61 = self.root.get_screen('main').ids.textInputBox61.text
        textBox62 = self.root.get_screen('main').ids.textInputBox62.text
        textBox63 = self.root.get_screen('main').ids.textInputBox63.text
        textBox64 = self.root.get_screen('main').ids.textInputBox64.text

        textBox71 = self.root.get_screen('main').ids.textInputBox71.text
        textBox72 = self.root.get_screen('main').ids.textInputBox72.text
        textBox73 = self.root.get_screen('main').ids.textInputBox73.text
        textBox74 = self.root.get_screen('main').ids.textInputBox74.text

        textBox81 = self.root.get_screen('main').ids.textInputBox81.text
        textBox82 = self.root.get_screen('main').ids.textInputBox82.text
        textBox83 = self.root.get_screen('main').ids.textInputBox83.text
        textBox84 = self.root.get_screen('main').ids.textInputBox84.text

        textBox91 = self.root.get_screen('main').ids.textInputBox91.text
        textBox92 = self.root.get_screen('main').ids.textInputBox92.text
        textBox93 = self.root.get_screen('main').ids.textInputBox93.text
        textBox94 = self.root.get_screen('main').ids.textInputBox94.text

        if textBox11 != "":
            textBoxString += panelTextID11 + self.textStringToBytes(textBox11)
        else:
            textBoxString += panelTextID11 + eol
        if textBox12 != "":
            textBoxString += panelTextID12 + self.textStringToBytes(textBox12)
        else:
            textBoxString += panelTextID12 + eol
        if textBox13 != "":
            textBoxString += panelTextID13 + self.textStringToBytes(textBox13)
        else:
            textBoxString += panelTextID13 + eol
        if textBox14 != "":
            textBoxString += panelTextID14 + self.textStringToBytes(textBox14)
        else:
            textBoxString += panelTextID14 + eol
        
        if textBox21 != "":
            textBoxString += panelTextID21 + self.textStringToBytes(textBox21)
        else:
            textBoxString += panelTextID21 + eol
        if textBox22 != "":
            textBoxString += panelTextID22 + self.textStringToBytes(textBox22)
        else:
            textBoxString += panelTextID22 + eol
        if textBox23 != "":
            textBoxString += panelTextID23 + self.textStringToBytes(textBox23)
        else:
            textBoxString += panelTextID23 + eol
        if textBox24 != "":
            textBoxString += panelTextID24 + self.textStringToBytes(textBox24)
        else:
            textBoxString += panelTextID24 + eol

        if textBox31 != "":
            textBoxString += panelTextID31 + self.textStringToBytes(textBox31)
        else:
            textBoxString += panelTextID31 + eol
        if textBox32 != "":
            textBoxString += panelTextID32 + self.textStringToBytes(textBox32)
        else:
            textBoxString += panelTextID32 + eol
        if textBox33 != "":
            textBoxString += panelTextID33 + self.textStringToBytes(textBox33)
        else:
            textBoxString += panelTextID33 + eol
        if textBox34 != "":
            textBoxString += panelTextID34 + self.textStringToBytes(textBox34)
        else:
            textBoxString += panelTextID34 + eol

        if textBox41 != "":
            textBoxString += panelTextID41 + self.textStringToBytes(textBox41)
        else:
            textBoxString += panelTextID41 + eol
        if textBox42 != "":
            textBoxString += panelTextID42 + self.textStringToBytes(textBox42)
        else:
            textBoxString += panelTextID42 + eol
        if textBox43 != "":
            textBoxString += panelTextID43 + self.textStringToBytes(textBox43)
        else:
            textBoxString += panelTextID43 + eol
        if textBox44 != "":
            textBoxString += panelTextID44 + self.textStringToBytes(textBox44)
        else:
            textBoxString += panelTextID44 + eol

        if textBox51 != "":
            textBoxString += panelTextID51 + self.textStringToBytes(textBox51)
        else:
            textBoxString += panelTextID51 + eol
        if textBox52 != "":
            textBoxString += panelTextID52 + self.textStringToBytes(textBox52)
        else:
            textBoxString += panelTextID52 + eol
        if textBox53 != "":
            textBoxString += panelTextID53 + self.textStringToBytes(textBox53)
        else:
            textBoxString += panelTextID53 + eol
        if textBox54 != "":
            textBoxString += panelTextID54 + self.textStringToBytes(textBox54)
        else:
            textBoxString += panelTextID54 + eol

        if textBox61 != "":
            textBoxString += panelTextID61 + self.textStringToBytes(textBox61)
        else:
            textBoxString += panelTextID61 + eol
        if textBox62 != "":
            textBoxString += panelTextID62 + self.textStringToBytes(textBox62)
        else:
            textBoxString += panelTextID62 + eol
        if textBox63 != "":
            textBoxString += panelTextID63 + self.textStringToBytes(textBox63)
        else:
            textBoxString += panelTextID63 + eol
        if textBox64 != "":
            textBoxString += panelTextID64 + self.textStringToBytes(textBox64)
        else:
            textBoxString += panelTextID64 + eol
        
        if textBox71 != "":
            textBoxString += panelTextID71 + self.textStringToBytes(textBox71)
        else:
            textBoxString += panelTextID71 + eol
        if textBox72 != "":
            textBoxString += panelTextID72 + self.textStringToBytes(textBox72)
        else:
            textBoxString += panelTextID72 + eol
        if textBox73 != "":
            textBoxString += panelTextID73 + self.textStringToBytes(textBox73)
        else:
            textBoxString += panelTextID73 + eol
        if textBox74 != "":
            textBoxString += panelTextID74 + self.textStringToBytes(textBox74)
        else:
            textBoxString += panelTextID74 + eol
        
        if textBox81 != "":
            textBoxString += panelTextID81 + self.textStringToBytes(textBox81)
        else:
            textBoxString += panelTextID81 + eol
        if textBox82 != "":
            textBoxString += panelTextID82 + self.textStringToBytes(textBox82)
        else:
            textBoxString += panelTextID82 + eol
        if textBox83 != "":
            textBoxString += panelTextID83 + self.textStringToBytes(textBox83)
        else:
            textBoxString += panelTextID83 + eol
        if textBox84 != "":
            textBoxString += panelTextID84 + self.textStringToBytes(textBox84)
        else:
            textBoxString += panelTextID84 + eol
        
        if textBox91 != "":
            textBoxString += panelTextID91 + self.textStringToBytes(textBox91)
        else:
            textBoxString += panelTextID91 + eol
        if textBox92 != "":
            textBoxString += panelTextID92 + self.textStringToBytes(textBox92)
        else:
            textBoxString += panelTextID92 + eol
        if textBox93 != "":
            textBoxString += panelTextID93 + self.textStringToBytes(textBox93)
        else:
            textBoxString += panelTextID93 + eol
        if textBox94 != "":
            textBoxString += panelTextID94 + self.textStringToBytes(textBox94)
        else:
            textBoxString += panelTextID94 + eol

        return textBoxString
    
    def panelKnobColous(self):
        knob1 = b'\x00\x04\x01'
        knob2 = b'\x01\x04\x01'
        knob3 = b'\x02\x04\x01'
        knob4 = b'\x03\x04\x01'
        knob5 = b'\x04\x04\x01'
        knob6 = b'\x05\x04\x01'
        knob7 = b'\x06\x04\x01'
        knob8 = b'\x07\x04\x01'

        num1 = int(self.root.get_screen('main').ids.panelKnob01.line_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelKnob01.line_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelKnob01.line_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        knobC1 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelKnob02.line_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelKnob02.line_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelKnob02.line_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        knobC2 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelKnob03.line_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelKnob03.line_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelKnob03.line_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        knobC3 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelKnob04.line_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelKnob04.line_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelKnob04.line_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        knobC4 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelKnob05.line_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelKnob05.line_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelKnob05.line_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        knobC5 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelKnob06.line_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelKnob06.line_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelKnob06.line_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        knobC6 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelKnob07.line_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelKnob07.line_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelKnob07.line_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        knobC7 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        num1 = int(self.root.get_screen('main').ids.panelKnob08.line_color[0]*127)
        num2 = int(self.root.get_screen('main').ids.panelKnob08.line_color[1]*127)
        num3 = int(self.root.get_screen('main').ids.panelKnob08.line_color[2]*127)
        num = self.rgb_to_hex((num1, num2, num3))
        num = '\\x' +  num[:2] + '\\x' + num[2:4] + '\\x' + num[4:6]
        knobC8 = num.encode().decode('unicode_escape').encode("raw_unicode_escape")

        panelKnobColours = knob1 + knobC1 + knob2 + knobC2 + knob3 + knobC3 + knob4 + knobC4 + knob5 + knobC5 + knob6 + knobC6 + knob7 + knobC7 + knob8 + knobC8

        return panelKnobColours

    def doButtons(self):
        button01 = b'\x04'
        button02 = b'\x05'
        button03 = b'\x06'
        button04 = b'\x07'
        button05 = b'\x08'
        button06 = b'\x09'
        button07 = b'\x0a'
        button08 = b'\x0b'

        button09 = b'\x0c'
        button10 = b'\x0d'
        button11 = b'\x0e'
        button12 = b'\x0f'
        button13 = b'\x10'
        button14 = b'\x11'
        button15 = b'\x12'
        button16 = b'\x13'

        button17 = b'\x14'
        button18 = b'\x15'
        button19 = b'\x16'
        button20 = b'\x17'
        button21 = b'\x18'
        button22 = b'\x19'
        button23 = b'\x1a'
        button24 = b'\x1b'

        button25ScreenUp = b'\x3e'
        button26ScreenDown = b'\x3b'
        button27SceneLaunchTop = b'\x02'
        button28SceneLaunchBottom = b'\x03'
        button29PadsUp = b'\x00'
        button30PadsDown = b'\x01'
        button31RightSoftUp = b'\x1c'
        button32RightSoftDown = b'\x1d'

        button33Grid = b'\x40'
        button34Options = b'\x41'
        #button35Shift = b'\x42'
        button36Duplicate = b'\x42'
        button37Clear = b'\x43'
        button38TrackLeft = b'\x1e'
        button39TrackRight = b'\x1f'

        button40Rewind = b'\x21'
        button41Forward = b'\x22'
        button42Stop = b'\x23'
        button43Play = b'\x24'
        button44Loop = b'\x25'
        button45Record = b'\x20'

        buttonColour01 = b'\x7f\x00\x00'
        buttonColour02 = b'\x7f\x00\x00'
        buttonColour03 = b'\x7f\x00\x00'
        buttonColour04 = b'\x7f\x00\x00'
        buttonColour05 = b'\x7f\x00\x00'
        buttonColour06 = b'\x7f\x00\x00'
        buttonColour07 = b'\x7f\x00\x00'
        buttonColour08 = b'\x7f\x00\x00'

        buttonColour09 = b'\x7f\x00\x00'
        buttonColour10 = b'\x7f\x00\x00'
        buttonColour11 = b'\x7f\x00\x00'
        buttonColour12 = b'\x7f\x00\x00'
        buttonColour13 = b'\x7f\x00\x00'
        buttonColour14 = b'\x7f\x00\x00'
        buttonColour15 = b'\x7f\x00\x00'
        buttonColour16 = b'\x7f\x00\x00'

        buttonColour17 = b'\x7f\x00\x00'
        buttonColour18 = b'\x7f\x00\x00'
        buttonColour19 = b'\x7f\x00\x00'
        buttonColour20 = b'\x7f\x00\x00'
        buttonColour21 = b'\x7f\x00\x00'
        buttonColour22 = b'\x7f\x00\x00'
        buttonColour23 = b'\x7f\x00\x00'
        buttonColour24 = b'\x7f\x00\x00'

        buttonColour25 = b'\x7f\x00\x00'
        buttonColour26 = b'\x7f\x00\x00'
        buttonColour27 = b'\x7f\x00\x00'
        buttonColour28 = b'\x7f\x00\x00'
        buttonColour29 = b'\x7f\x00\x00'
        buttonColour30 = b'\x7f\x00\x00'
        buttonColour31 = b'\x7f\x00\x00'
        buttonColour32 = b'\x7f\x00\x00'

        buttonColour33 = b'\x7f\x00\x00'
        buttonColour34 = b'\x7f\x00\x00'
        buttonColour35 = b'\x7f\x00\x00'
        buttonColour36 = b'\x7f\x00\x00'
        buttonColour37 = b'\x7f\x00\x00'
        buttonColour38 = b'\x7f\x00\x00'
        buttonColour39 = b'\x7f\x00\x00'
        buttonColour40 = b'\x7f\x00\x00'

        buttonColour41 = b'\x7f\x00\x00'
        buttonColour42 = b'\x7f\x00\x00'
        buttonColour43 = b'\x7f\x00\x00'
        buttonColour44 = b'\x7f\x00\x00'
        buttonColour45 = b'\x7f\x00\x00'
        buttonColour46 = b'\x7f\x00\x00'
        buttonColour47 = b'\x7f\x00\x00'
        buttonColour48 = b'\x7f\x00\x00'

    def open_color_picker(self, buttonID):
        self.root.current = "RGBPicker"
        clr_picker = ColorPicker()
        self.root.get_screen('RGBPicker').ids.colourPicker.add_widget(clr_picker)
        clr_picker.fbind('color', self.on_color, buttonID)

        exitColour = Button(text='Close', size_hint_y=0.1)
        self.root.get_screen('RGBPicker').ids.colourPicker.add_widget(exitColour)
        exitColour.bind(on_release=self.clearColourWheel)

    def on_color(self, buttonID, instance, value):

        if buttonID == 1:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "01\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp01.text = hexValue
            self.root.get_screen('main').ids.dp01.line_color = value
            button01 = '\\x' + hexValueOG[:2] + '\\x' + hexValueOG[2:4] + '\\x' + hexValueOG[4:6]
            button01col = button01.encode().decode('unicode_escape').encode("raw_unicode_escape")

        elif buttonID == 2:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "02\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp02.text = hexValue
            self.root.get_screen('main').ids.dp02.line_color = value
            button02 = '\\x' + hexValueOG[:2] + '\\x' + hexValueOG[2:4] + '\\x' + hexValueOG[4:6]
            button02col = button02.encode().decode('unicode_escape').encode("raw_unicode_escape")

        elif buttonID == 3:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "03\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp03.text = hexValue
            self.root.get_screen('main').ids.dp03.line_color = value
            button03 = '\\x' + hexValueOG[:2] + '\\x' + hexValueOG[2:4] + '\\x' + hexValueOG[4:6]
            button03col = button03.encode().decode('unicode_escape').encode("raw_unicode_escape")

        elif buttonID == 4:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "04\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp04.text = hexValue
            self.root.get_screen('main').ids.dp04.line_color = value
            button04 = '\\x' + hexValueOG[:2] + '\\x' + hexValueOG[2:4] + '\\x' + hexValueOG[4:6]
            button04col = button04.encode().decode('unicode_escape').encode("raw_unicode_escape")

        elif buttonID == 5:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "05\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp05.text = hexValue
            self.root.get_screen('main').ids.dp05.line_color = value
            button05col = hexValueOG

        elif buttonID == 6:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "06\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp06.text = hexValue
            self.root.get_screen('main').ids.dp06.line_color = value
            button06col = hexValueOG

        elif buttonID == 7:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "07\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp07.text = hexValue
            self.root.get_screen('main').ids.dp07.line_color = value
            button07col = hexValueOG

        elif buttonID == 8:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "08\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp08.text = hexValue
            self.root.get_screen('main').ids.dp08.line_color = value
            button08col = hexValueOG

        elif buttonID == 9:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "09\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp09.text = hexValue
            self.root.get_screen('main').ids.dp09.line_color = value
            button09col = hexValueOG

        elif buttonID == 10:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "10\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp10.text = hexValue
            self.root.get_screen('main').ids.dp10.line_color = value
            button10col = hexValueOG

        elif buttonID == 11:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "11\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp11.text = hexValue
            self.root.get_screen('main').ids.dp11.line_color = value
            button11col = hexValueOG

        elif buttonID == 12:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "12\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp12.text = hexValue
            self.root.get_screen('main').ids.dp12.line_color = value
            button12col = hexValueOG

        elif buttonID == 13:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "13\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp13.text = hexValue
            self.root.get_screen('main').ids.dp13.line_color = value
            button13col = hexValueOG

        elif buttonID == 14:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:]
            hexValue = "14\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp14.text = hexValue
            self.root.get_screen('main').ids.dp14.line_color = value
            button14col = hexValueOG

        elif buttonID == 15:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:6]
            hexValue = "15\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp15.text = hexValue
            self.root.get_screen('main').ids.dp15.line_color = value
            button15col = hexValueOG

        elif buttonID == 16:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:6]
            hexValue = "16\n" + hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.dp16.text = hexValue
            self.root.get_screen('main').ids.dp16.line_color = value
            button16col = hexValueOG

        elif buttonID == 17:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarTop01.md_bg_color = value
            panelTop1col = hexValueOG

        elif buttonID == 18:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarBot01.md_bg_color = value
            panelBot1col = hexValueOG

        elif buttonID == 19:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarTop02.md_bg_color = value
            panelTop2col = hexValueOG

        elif buttonID == 20:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarBot02.md_bg_color = value
            panelBot2col = hexValueOG

        elif buttonID == 21:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarTop03.md_bg_color = value
            panelTop3col = hexValueOG

        elif buttonID == 22:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarBot03.md_bg_color = value
            panelBot3col = hexValueOG

        elif buttonID == 23:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarTop04.md_bg_color = value
            panelTop4col = hexValueOG

        elif buttonID == 24:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarBot04.md_bg_color = value
            panelBot4col = hexValueOG

        elif buttonID == 25:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarTop05.md_bg_color = value
            panelTop5col = hexValueOG

        elif buttonID == 26:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarBot05.md_bg_color = value
            panelBot5col = hexValueOG

        elif buttonID == 27:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarTop06.md_bg_color = value
            panelTop6col = hexValueOG

        elif buttonID == 28:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarBot06.md_bg_color = value
            panelBot6col = hexValueOG

        elif buttonID == 29:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarTop07.md_bg_color = value
            panelTop7col = hexValueOG

        elif buttonID == 30:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarBot07.md_bg_color = value
            panelBot7col = hexValueOG

        elif buttonID == 31:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarTop08.md_bg_color = value
            panelTop8col = hexValueOG

        elif buttonID == 32:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelBarBot08.md_bg_color = value
            panelBot8col = hexValueOG

        elif buttonID == 33:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelKnob01.line_color = value
            panelKnob01col = hexValueOG

        elif buttonID == 34:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelKnob02.line_color = value
            panelKnob02col = hexValueOG

        elif buttonID == 35:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelKnob03.line_color = value
            panelKnob03col = hexValueOG

        elif buttonID == 36:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelKnob04.line_color = value
            panelKnob04col = hexValueOG

        elif buttonID == 37:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelKnob05.line_color = value
            panelKnob05col = hexValueOG

        elif buttonID == 38:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelKnob06.line_color = value
            panelKnob06col = hexValueOG

        elif buttonID == 39:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelKnob07.line_color = value
            panelKnob07col = hexValueOG

        elif buttonID == 40:
            hexValue = str(instance.hex_color)
            hexValueOG = hexValue[1:7]
            hexValue = hexValueOG[:2] + " " + hexValueOG[2:4] + " " + hexValueOG[4:6]
            self.root.get_screen('main').ids.panelKnob08.line_color = value
            panelKnob08col = hexValueOG

    def clearColourWheel(self, text):
        self.root.get_screen('RGBPicker').ids.colourPicker.clear_widgets()
        self.root.current = "main"

    def applyToTopBars(self):
        colourCopy = self.root.get_screen('main').ids.panelBarTop01.md_bg_color

        self.root.get_screen('main').ids.panelBarTop02.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop03.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop04.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop05.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop06.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop07.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop08.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarLeft09.md_bg_color = colourCopy

    def applyToAllBars(self):
        colourCopy = self.root.get_screen('main').ids.panelBarTop01.md_bg_color

        self.root.get_screen('main').ids.panelBarTop02.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop03.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop04.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop05.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop06.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop07.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarTop08.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarLeft09.md_bg_color = colourCopy

        self.root.get_screen('main').ids.panelBarBot01.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot02.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot03.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot04.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot05.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot06.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot07.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot08.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarRightTop09.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarRightBot09.md_bg_color = colourCopy

    def applyToBotBars(self):
        colourCopy = self.root.get_screen('main').ids.panelBarBot01.md_bg_color

        self.root.get_screen('main').ids.panelBarBot01.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot02.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot03.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot04.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot05.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot06.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot07.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarBot08.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarRightTop09.md_bg_color = colourCopy
        self.root.get_screen('main').ids.panelBarRightBot09.md_bg_color = colourCopy

    def applyToAllKnobs(self):
        colourCopy = self.root.get_screen('main').ids.panelKnob01.line_color

        self.root.get_screen('main').ids.panelKnob02.line_color = colourCopy
        self.root.get_screen('main').ids.panelKnob03.line_color = colourCopy
        self.root.get_screen('main').ids.panelKnob04.line_color = colourCopy
        self.root.get_screen('main').ids.panelKnob05.line_color = colourCopy
        self.root.get_screen('main').ids.panelKnob06.line_color = colourCopy
        self.root.get_screen('main').ids.panelKnob07.line_color = colourCopy
        self.root.get_screen('main').ids.panelKnob08.line_color = colourCopy

    def rgb_to_hex(self, rgb):
        return '%02x%02x%02x' % rgb

    def createFile(self):
        global setLayoutProperties
        global setLayoutToKnobs
        global setScreenProperties
        global header
        global footer

        sysEx = header + setLayoutProperties + setLayoutToKnobs + footer
        sysEx += header + setScreenProperties + self.panelKnobColous() + self.panelBarColours() + self.panelText() + footer

        fileName = self.root.get_screen('main').ids.textInputSaveSysEx.text + ".syx"

        with open(fileName, 'wb') as file:
            file.write(sysEx)

MainApp().run()