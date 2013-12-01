import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.listview import ListView
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Canvas
from kivy.config import Config
from kivy.uix.popup import Popup
#from kivy.uix.slider import Slider
#from kivy.uix.spinner import Spinner
from kivy.properties import StringProperty, ObjectProperty
#from kivy.uix.carousel import Carousel
#from kivy.animation import Animation




from kivy.uix.screenmanager import SlideTransition,SwapTransition,WipeTransition,FadeTransition
#from kivy.graphics import graphics
#Config.set('graphics', 'width', '720')
#Config.set('graphics', 'height', '1280')
Config.set('graphics', 'width', '280')
Config.set('graphics', 'height', '500')

Builder.load_file('dip.kv')


'''
    def save(self, path, selection):
        _file = codecs.open(selection, 'w', encoding='utf8')
        _file.write(self.text)
        Window.title = selection[selection.rfind(os.sep)+1:]
        _file.close()
        self.dismiss()
'''
class LLabel(Label):
	pass
# Declare screens
class MyScreen(Screen):
	def show_popup(self,but_text,label_text,title_text):
		content_popup = Button(text=but_text,size_hint=(.5,1),pos_hint={'center_x':.5,'y':.0})
		content = BoxLayout(orientation='vertical',padding=(0,self.height*0.01))
		content.add_widget(Label(text=label_text,halign='center',size_hint=(1,2)))
		content.add_widget(content_popup)
		popup = Popup(title=title_text,content=content,size_hint=(.9,.3))
		content_popup.bind(on_release=popup.dismiss)
		popup.open()	
class LoginScreen(MyScreen):
	global i
	i=0
	def reg(self):
		self.manager.current='authorization'
	def enter_system(self):
		global i
		i+= 1
		if i%2:
			self.show_popup('Ok','Неверное имя пользователя\nили пароль','Ошибка авторизации')
		else: 
			self.manager.current = 'main'

class AuthorizationScreen(MyScreen):
	global i
	i=0
	def register(self):
		global i
		i+= 1
		if i%2:
			self.show_popup('Ok','Неверно введены данные','Ошибка заполнения формы')
		else: 
			self.show_popup('Ok','Спасибо за регистрацию!','Регистрация успешна')
			self.manager.current = 'login'
	def code_sms(self):
		self.show_popup('Ok','Вам отправлено смс-сообщение\nс кодом подтверждения','Подтверждение регистрации')

class MainScreen(MyScreen):
	def on_pre_enter(self):
		self.ids.spin_products.text='Все товары'
		self.ids.spin_products.values=('Все товары', 'Хлебные изделия', 'Молочные продукты', 'Мясо')
		task=[]
		for line in open('tasks.txt'):
			fields=line.split(',')
			date=fields[0]
			name=fields[1]
			title=fields[2]
			prod1=fields[3]
			prod2=fields[4]
			prod3=fields[5]
			stock=(date,name,title,prod1,prod2,prod3)
			task.append(stock)
		for date,name,title,prod1,prod2,prod3 in task:
			box=BoxLayout(size_hint=(.33,1),orientation='vertical')
			box.add_widget(Button(text=str(date)+' '+str(name)+' '+str(title),color=[1,1,0,1],
					on_release=self.task_trans(title)))
			box.add_widget(Label(text=str(prod1)))
			box.add_widget(Label(text=str(prod2)))
			box.add_widget(Label(text=str(prod3)))
			self.ids.tasks_box.add_widget(box)
			self.ids.products.add_widget(Button(text=str(prod1),on_release=self.product_trans(prod1)))
			self.ids.products.add_widget(Button(text=str(prod2),on_release=self.product_trans(prod2)))
			self.ids.products.add_widget(Button(text=str(prod3),on_release=self.product_trans(prod3)))
	def product_trans(self,prod_name):
		pass
	def	product_inf(self,prod_name):
		pass
	def task_trans(self,task_name):
		pass

			
class TasksScreen(MyScreen):
	def on_pre_enter(self):
		task=[]
		self.ids.task_box.clear_widgets()
		for line in open('tasks.txt'):
			fields=line.split(',')
			date=fields[0]
			name=fields[1]
			title=fields[2]
			prod1=fields[3]
			prod2=fields[4]
			prod3=fields[5]
			stock=(date,name,title,prod1,prod2,prod3)
			task.append(stock)
		for date,name,title,prod1,prod2,prod3 in task:
			self.ids.task_box.add_widget(Button(text=str(date)+' '+str(name)+' '+str(title),color=[1,1,0,1],
					on_release=self.task_trans(title)))
			self.ids.task_box.add_widget(Label(text=str(prod1)))
			self.ids.task_box.add_widget(Label(text=str(prod2)))
			self.ids.task_box.add_widget(Label(text=str(prod3)))
	def task_trans(self,task_name):
		pass
			
class TaskEditScreen(MyScreen):
	def on_pre_enter(self):
		task=[]
		for line in open('tasks.txt'):
			fields=line.split(',')
			prod1=fields[3]
			prod2=fields[4]
			prod3=fields[5]
			stock=(prod1,prod2,prod3)
			task.append(stock)
		for prod1,prod2,prod3 in task:
			self.ids.product_box.add_widget(ToggleButton(text=str(prod1),id=prod1))
			self.ids.product_box.add_widget(ToggleButton(text=str(prod2),id=prod1))
			self.ids.product_box.add_widget(ToggleButton(text=str(prod3),id=prod1))
		person=[]
		self.ids.grid.clear_widgets()
		for line in open('users.txt'):
			fields=line.split(',')
			name=fields[0]
			stock=(name)
			person.append(stock)
		self.ids.grid.add_widget(Label())
		self.ids.grid.add_widget(Image(source='1.png',allow_stretch=True))
		self.ids.grid.add_widget(Label())
		self.ids.grid.add_widget(Image(source='1.png',allow_stretch=True))
		for name in person:
			self.ids.grid.add_widget(Label(text=str(name),halign='left',size_hint=(3,1)))
			self.ids.grid.add_widget(CheckBox(id=name+'space'))
			self.ids.grid.add_widget(Label())
			self.ids.grid.add_widget(CheckBox(id=name+'sms'))
	def create_task(self):
		self.show_popup('Ok','Задание опубликовано!','Добавление задания')
		self.manager.current = 'tasks'
    
class ProductsScreen(MyScreen):
	def on_pre_enter(self):
		prod=[]
		self.ids.grid_products.clear_widgets()
		for line in open('categories.txt'):
			fields=line.split(',')
			cat=fields[0]
			prod1=fields[1]
			prod2=fields[2]
			prod3=fields[3]
			stock=(cat,prod1,prod2,prod3)
			prod.append(stock)
		for cat,prod1,prod2,prod3 in prod:
			self.ids.grid_products.add_widget(ToggleButton(size_hint=(.1,1)))
			self.ids.grid_products.add_widget(Label(text=str(prod1),size_hint=(.6,1),color=[1,1,0,1]))
			self.ids.grid_products.add_widget(Label(text=str(cat),size_hint=(.3,1)))
			self.ids.grid_products.add_widget(ToggleButton(size_hint=(.1,1)))
			self.ids.grid_products.add_widget(Label(text=str(prod2),size_hint=(.6,1),color=[1,1,0,1]))
			self.ids.grid_products.add_widget(Label(text=str(cat),size_hint=(.3,1)))
			self.ids.grid_products.add_widget(ToggleButton(size_hint=(.1,1)))
			self.ids.grid_products.add_widget(Label(text=str(prod3),size_hint=(.6,1),color=[1,1,0,1]))
			self.ids.grid_products.add_widget(Label(text=str(cat),size_hint=(.3,1)))

class ProductsInfScreen(MyScreen):
	def on_pre_enter(self):
		self.ids.name.text='Ряженка Домик в деревне 3,2% 1 л'				
		self.ids.image.source='domik.jpg'
		self.ids.cat.text='Молоко'	
		self.ids.bought.text='21.10.2013'	
		self.ids.made.text='19.10.2013'	
		self.ids.term.text='15'	
		self.ids.before.text='3.11.2013'	
		self.ids.ccal.text='57'	
		self.ids.price.text='45'	
		self.ids.description.text='Производитель: ОАО "Вимм-Билль-Данн", Россия\nСостав: молоко цельное, молоко обезжиренное и молоко сухое обезжиренное топленые, с использованием закваски.\nИзготовлено с использованием сухого молока.\n Пищевая ценность на 100г: белки - 2,9г, жир - 3,2г, углеводы - 4,1г.\nХранить при температуре от 2 С до 6 С 15 дней. ГОСТ Р 52094-2003'
	def in_task(self):
		pass
	def code(self):
		pass

	
class SettingsScreen(MyScreen):
	def on_pre_enter(self):
		person=[]
		for line in open('users.txt'):
			fields=line.split(',')
			name=fields[0]
			phone=fields[1]
			mail=fields[2]
			stock=(name,phone,mail)
			person.append(stock)
		self.ids.record_spin.text=str(person[0][2])
		self.ids.record_spin.values=(person[0][2],)
		for name,phone,mail in person[1:]:
			self.ids.users_grid.add_widget(TextInput(text=str(name),valign='middle',halign='left',size_hint_x=.8))
			self.ids.users_grid.add_widget(Label(text=str(phone)+'\n'+str(mail),valign='middle',halign='right'))
		
	def save_settings(self):
		self.show_popup('Ok','Настройки успешно сохранены!','Настройки')

	
class StatisticsScreen(MyScreen):
	def on_pre_enter(self):
		self.ids.spin_products.text='Все товары'
		self.ids.spin_products.values=('Все товары', 'Хлебные изделия', 'Молочные продукты', 'Мясо')
		self.ids.spin_period.text='Месяц'
		self.ids.spin_period.values=('Год', 'Сезон', 'Месяц', 'Неделя')
		self.ids.spin_param.text='Количество'
		self.ids.spin_param.values=('Количество', 'Цена')
	def show_stat(self):
		self.ids.image.source='stat.PNG'
		self.ids.image.allow_stretch=True
		self.ids.summary.text='За весь период куплено 233 товара'
		pass
class MenuScreen(MyScreen):
    def on_exit(self):
		exit()
class AboutScreen(MyScreen):
    pass

#class MyScreenManager(Carousel, ScreenManager):
#	pass
'''	def swipe(self,touch):
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
		sm.transition = SlideTransition(direction='right')
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
		sm.current = 'products_inf'
		return sm
		
	

if __name__ in ('__main__', '__android__'):
    DipApp().run()

