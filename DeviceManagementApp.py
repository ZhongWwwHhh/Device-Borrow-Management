from kivy.core.text import LabelBase
LabelBase.register(name='msyh',fn_regular='chinese.msyh.ttf')


from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


class MainMenu(FloatLayout):

    def releaseBorrowBtn(self, arg):
        from Basic.Borrow import Borrow
        Borrow.borrowStart()
    
    def releaseReturnBtn(self, arg):
        print('2')
    
    def releaseManageBtn(self, arg):
        print('3')


class DeviceManagementApp(App):

    def build(self):
        return MainMenu()


if __name__ == '__main__':
    DeviceManagementApp().run()