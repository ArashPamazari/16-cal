# what is qt library ? : user interface - is library for designing user interface for applications ( graphics )
# frontEnd = client side , BackEnd = server side
# qt library in python = pyqt and pyside(offical)
#file.py = backend
# qt = file.ui
#terminal = pip install pyside6
# commond on terminal = pyside6-designer (enter)
# use tools , save file.ui / next to my python code.
# loading ui code in python
#-----------------------------------------------------------------------------------------------------------------#
import math

from PySide6.QtWidgets import * 
from PySide6.QtUiTools import * 
from PySide6.QtCore import *
from functools import partial

class HelloWorld(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()# in 3 khat baraye in bud betonim Ui ro bebinim

        #self.ui.btn_sum.clicked.connect(self.sum)
        #self.ui.btn_equal.clicked.connect(self.equal)
        #self.ui.btn_1.clicked.connect(self.function_num_1)

        self.ui.btn_Ac.clicked.connect(self.AC) #1

        self.ui.btn_sinos.clicked.connect(self.sinos)#1
        self.ui.btn_cosinos.clicked.connect(self.cosinos) #1
        self.ui.btn_tan_2.clicked.connect(self.tan_2) #1

        
        self.ui.btn_darsad.clicked.connect(self.darsad) #1
        self.ui.btn_sqrt.clicked.connect(self.sqrt) #1
        self.ui.btn_log.clicked.connect(self.log) #1
        self.ui.btn_neg.clicked.connect(self.neg)
                
        self.ui.btn_sum.clicked.connect(self.sum) #1
        self.ui.btn_tafrigh.clicked.connect(self.tafrigh) #1
        self.ui.btn_taghsim.clicked.connect(self.taghsim) #1
        self.ui.btn_zarb.clicked.connect(self.zarb) #1
        self.ui.btn_dot.clicked.connect(self.dot) #1
        
        self.ui.btn_mosavi.clicked.connect(self.mosavi) #1

#use flag is way to control the behavior of user segments in your application

        self.flag_tafrigh = False
        self.flag_sum = False
        self.flag_taghsim = False
        self.flag_zarb = False
        self.flag_sumf = False

        self.btn_number_list = [self.ui.btn_no0, self.ui.btn_no1, self.ui.btn_no2, self.ui.btn_no3, self.ui.btn_no4,self.ui.btn_no5, self.ui.btn_no6, self.ui.btn_no7, self.ui.btn_no8, self.ui.btn_no9]

#use partial function as an extension of another specified function
        
        for i in range(10):
            self.btn_number_list[i].clicked.connect((partial(self.btn_numbers, i)))        

    def sqrt(self):

        self.num1 = int(self.ui.textbox.text())
        self.num1 = math.sqrt(self.num1)
        self.ui.textbox.setText(str(self.num1))


    def log(self):
        self.num1 = math.log(int(self.ui.textbox.text()))
        self.ui.textbox.setText(str(self.num1))

    def sum(self):
            self.num1 = float(self.ui.textbox.text())
            self.ui.textbox.setText('')
            self.flag_sum = True

    def tafrigh(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_sub = True

    def taghsim(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_div = True

    def zarb(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_mul = True

    def sinos(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.sin(a)))

    def cosinos(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.cos(a)))

    def tan_2(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.tan(a)))


    def darsad(self):
        self.num1 = float(self.ui.textbox.text())
        self.num1 /= 100
        self.ui.textbox.setText(str(self.num1))

    def dot(self):
        for word in self.ui.textbox.text():
            if word == '.':
                break
            else:
                self.ui.textbox.setText(self.ui.textbox.text() + '.')

    def mosavi(self):
        self.num2 = float(self.ui.textbox.text())

        if self.flag_sum:
            result = self.num1 + self.num2
            self.ui.textbox.setText(str(result))

        elif self.flag_tafrigh:
            result = self.num1 - self.num2
            self.ui.textbox.setText(str(result))

        elif self.flag_taghsim:
            result = self.num1 // self.num2
            self.ui.textbox.setText(str(result))

        elif self.flag_zarb:
            result = self.num1 * self.num2
            self.ui.textbox.setText(str(result))

    def neg(self):
            self.num1 = float(self.ui.textbox.text())
            self.num1 *= -1
            self.ui.textbox.setText(str(self.num1))

    def AC(self):
        self.ui.textbox.setText('')


    def btn_numbers(self, i):
        if self.ui.textbox.text() == '' or self.ui.textbox.text() == '0' :
            self.ui.textbox.setText(str(i))
        else:
            self.ui.textbox.setText(str(self.ui.textbox.text()) + str(i))

    #def function_num_1(self):
    #    self.ui.textbox.setText(self.ui.textbox.text()+'1')

    #def sum(self):
     #   self.num1 = int(self.ui.textbox.text())
      #  self.ui.textbox.setText('')

    #def equal(self):
     #   self.num2 = int(self.ui.textbox.text())

      #  result = self.num1+self.num2
       # self.ui.textbox.setText(str(result))


app = QApplication([])
window = HelloWorld()
app.exec()