from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.graphics.context_instructions import Color



class WidgetExample(GridLayout):
    my_text = StringProperty('Lest Start\nCounting!')
    counter =1
    #slider_value_txt = StringProperty('50')
    state = BooleanProperty(False)
    text_input_str = StringProperty('Type Here')
    
    def on_button_click(self):
        print('Button Clicked')
        if self.state:
            self.my_text = f'{self.counter}'
            self.counter +=1

    def on_toggle_button_state(self, widget):
        print('Toggle state: ' + widget.state)
        if widget.state == 'normal':
            widget.text = 'Off'
            self.state = False
        else:
            widget.text = 'On'
            self.state = True

    def on_switch_active(self, widget):
        print('Switch: ' + str(widget.active))
        
            

    def on_slider_value(self, widget):
        print('Slider: ' + str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        
        

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'lr-tb'
        for i in range(0,100):
            b = Button(text = str(i+1), size_hint = (None, None),size= (dp(100), dp(100)))
            self.add_widget(b)
        

class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
'''
sssssss    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        b1 = Button(text = 'A')
        b2 = Button(text = 'B')
        self.add_widget(b1)
        self.add_widget(b2)
'''

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points = (100,100,400,500), width = 2)
            Color(0,1,0)
            Line(circle = (400, 200,80), width = 2)
            Line(rectangle = (700, 500,150, 100), width = 5)
            self.rect = Rectangle(pos=(400,200), size=(150,100))

    def on_button_a_click(self):
        #print('Button A pressed')
        x,y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        dif = self.width - (x+w)
        if dif < inc:
            inc=dif
        
        x +=inc
        self.rect.pos = (x,y)
            

TheLabApp().run()
