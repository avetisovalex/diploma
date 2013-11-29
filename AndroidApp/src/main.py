#coding=utf-8
import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Canvas
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.carousel import Carousel
from kivy.animation import Animation

from kivy.uix.screenmanager import SlideTransition,SwapTransition,WipeTransition,FadeTransition
#from kivy.graphics import graphics
#Config.set('graphics', 'width', '720')
#Config.set('graphics', 'height', '1280')
Config.set('graphics', 'width', '280')
Config.set('graphics', 'height', '500')

Builder.load_file('dip.kv')

# Declare screens
class LoginScreen(Screen):
	global i
	i=0
	def reg(self):
		self.manager.current='authorization'
	def enter_system(self):
		global i
		i+= 1
		if i%2:
			content_cancel = Button(text='Ok',size_hint=(.5,1),pos_hint={'center_x':.5,'y':.0})
			content = BoxLayout(orientation='vertical',padding=(0,self.height*0.01))
			content.add_widget(Label(text='Неверное имя пользователя\nили пароль',halign='center',size_hint=(1,2)))
			content.add_widget(content_cancel)
			popup = Popup(title='Ошибка авторизации', content=content,size_hint=(.9,.3))
			content_cancel.bind(on_press=popup.dismiss)
			popup.open()
		else: 
			self.manager.current = 'main'

class CustomPopup(Popup):
    pass
class AuthorizationScreen(Screen):
	global i
	i=0
	def register(self):
		global i
		i+= 1
		if i%2:
			content_cancel = Button(text='Ok',size_hint=(.5,1),pos_hint={'center_x':.5,'y':.0})
			content = BoxLayout(orientation='vertical',padding=(0,self.height*0.01))
			content.add_widget(Label(text='Неверно введены данные',halign='center',size_hint=(1,2)))
			content.add_widget(content_cancel)
			popup = Popup(title='Ошибка заполнения формы', content=content,size_hint=(.9,.3))
			content_cancel.bind(on_press=popup.dismiss)
			popup.open()
		else: 
			content_cancel = Button(text='Ok',size_hint=(.5,1),pos_hint={'center_x':.5,'y':.0})
			content = BoxLayout(orientation='vertical',padding=(0,self.height*0.01))
			content.add_widget(Label(text='Спасибо за регистрацию!',halign='center',size_hint=(1,2)))
			content.add_widget(content_cancel)
			popup = Popup(title='Регистрация успешна', content=content,size_hint=(.9,.3))
			content_cancel.bind(on_press=popup.dismiss)
			popup.open()
			self.manager.current = 'login'
	def code_sms(self):
		content_cancel = Button(text='Ok',size_hint=(.5,1),pos_hint={'center_x':.5,'y':.0})
		content = BoxLayout(orientation='vertical',padding=(0,self.height*0.01))
		content.add_widget(Label(text='Вам отправлено смс-сообщение\nс кодом подтверждения',halign='center',size_hint=(1,2)))
		content.add_widget(content_cancel)
		popup = Popup(title='Подтверждение регистрации', content=content,size_hint=(.9,.3))
		content_cancel.bind(on_press=popup.dismiss)
		popup.open()
	

    
class MainScreen(Screen):
    pass
class TasksScreen(Screen):
    pass
class TaskEditScreen(Screen):
    pass
class ProductsScreen(Screen):
    pass
class ProductsInfScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass
class StatisticsScreen(Screen):
    pass
class MenuScreen(Screen):
    def on_exit(self):
		exit()
class AboutScreen(Screen):
    pass
'''class MyScreenManager(ScrollView, ScreenManager):
	def swipe(self,touch):
		self.touch_start = touch.pos
		if self.do_scroll_x and self.effect_x:
			self.effect_x.start(touch.x)
		if self.do_scroll_y and self.effect_y:
			self.effect_y.start(touch.y)

	def effect_x(touch):
		sm.current = 'MenuScreen'
	return 
	def effect_y(touch):

return	
'''
class DipApp(App):
	def build(self):
		sm = ScreenManager()
		sm.transition = SlideTransition(direction="down")
		sm.add_widget(LoginScreen(name='login'))
		sm.add_widget(AuthorizationScreen(name='authorization'))
		sm.add_widget(MainScreen(name='main'))
		sm.add_widget(TasksScreen(name='tasks'))
		sm.add_widget(TaskEditScreen(name='task_edit'))
		sm.add_widget(ProductsScreen(name='products'))
		sm.add_widget(ProductsInfScreen(name='products_inf'))
		sm.add_widget(SettingsScreen(name='settings'))
		sm.add_widget(StatisticsScreen(name='statistics'))
		sm.add_widget(MenuScreen(name='menu'))
		sm.add_widget(AboutScreen(name='about'))
		sm.current = 'main'
		return sm
		
	

if __name__ in ('__main__', '__android__'):
    DipApp().run()

