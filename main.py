from widgets_calc import Ui_MainWindow 
from PyQt5 import QtCore, QtGui, QtWidgets


class Calc(Ui_MainWindow):
    def __init__(self):
        self.setupUi(MainWindow)

        self.entry = "0"
        self.prev = None

        self.button_0.clicked.connect(lambda: self.enter(0))
        self.button_1.clicked.connect(lambda: self.enter(1))
        self.button_2.clicked.connect(lambda: self.enter(2))
        self.button_3.clicked.connect(lambda: self.enter(3))
        self.button_4.clicked.connect(lambda: self.enter(4))
        self.button_5.clicked.connect(lambda: self.enter(5))
        self.button_6.clicked.connect(lambda: self.enter(6))
        self.button_7.clicked.connect(lambda: self.enter(7))
        self.button_8.clicked.connect(lambda: self.enter(8))
        self.button_9.clicked.connect(lambda: self.enter(9))

        self.button_clearAll.clicked.connect(self.clearAll)
        self.button_clearEntry.clicked.connect(self.clearEntry)
        self.button_delete.clicked.connect(self.deleteChar)
        self.button_add.clicked.connect(lambda: self.operation("+"))
        self.button_subtract.clicked.connect(lambda: self.operation("−"))
        self.button_multiply.clicked.connect(lambda: self.operation("*"))
        self.button_divide.clicked.connect(lambda: self.operation("/"))
        self.button_equals.clicked.connect(lambda: self.operation("="))
        self.button_percent.clicked.connect(self.percent)
        self.button_square.clicked.connect(self.squared)
        self.pushButton_13.clicked.connect(self.squareroot)
        self.pushButton_2.clicked.connect(self.inverse)
        self.button_comma.clicked.connect(self.comma)
        self.button_sign.clicked.connect(self.changeSign)
    def clearUndefined(self):
        if self.label_2.text()[0]=="u":
            self.label_2.setText("0")
            self.entry = "0"
            self.label.setText("")
            return True
        return False
    def percent(self):
        if self.clearUndefined(): return
        if ("=" in self.label.text()):
            self.label.setText("")
        try:
            new = float(self.label_2.text())*0.01
            if int(new)==new:
                new = int(new)
            self.label_2.setText(str(new))
            self.entry = str(new)
        except:
            return
    def squared(self):
        if ("=" in self.label.text()):
            self.label.setText("")
        if self.clearUndefined(): return
        try:
            new = float(self.label_2.text())**2
            if int(new)==new:
                new = int(new)
            self.label_2.setText(str(new))
            self.entry = str(new)
        except:
            return
    def squareroot(self):
        if ("=" in self.label.text()):
            self.label.setText("")
        if self.clearUndefined(): return
        try:
            new = float(self.label_2.text())**0.5
            if int(new)==new:
                new = int(new)
            self.label_2.setText(str(new))
            self.entry = str(new)
        except:
            return
    def inverse(self):
        if ("=" in self.label.text()):
            self.label.setText("")
        if self.clearUndefined(): return
        try:
            new = 1/float(self.label_2.text())
            if int(new)==new:
                new = int(new)
            self.label_2.setText(str(new))
            self.entry = str(new)
        except:
            return
    def changeSign(self):
        if ("=" in self.label.text()):
            self.label.setText("")
        if self.label_2.text()[0] == "-":
            self.label_2.setText(self.label_2.text()[1:])
            return
        if self.label_2.text() == "0":
            return
        elif self.label_2.text()[0]=="u":
            self.label_2.setText("0")
            self.entry = "0"
            self.label.setText("")
            return
        self.label_2.setText("-"+self.label_2.text())
    def comma(self):
        if ("=" in self.label.text()):
            self.label.setText("")
        if "." in self.label_2.text():
            return
        if self.label_2.text()=="0":
            self.enter("0.")
        elif self.label_2.text()[0]=="u":
            self.label_2.setText("0.")
            self.entry = "0."
            self.label.setText("")
            self.prev=None
        else:
            self.enter(".")
    def enter(self,number):
        number = str(number)
        text_label2 = self.label_2.text()
        text_label = self.label.text()

        if self.label_2.text()[0]=="u":
            self.label_2.setText(number)
            self.entry = number
        if ("=" in text_label):
            self.label.setText("")
            self.entry = text_label2+number
            text_label2 = self.label_2.text()
            self.prev=None
        if (text_label2[0]=="0" and len(text_label2)==1):
            self.label_2.setText(number)
            self.entry = number
        else:
            self.label_2.setText(text_label2+number)
            self.entry = text_label2+number

    def clearAll(self):
        self.label_2.setText("0")
        self.label.setText("")
        self.entry="0"
    def clearEntry(self):
        if (self.entry!="0"):
            text_label = self.label.text()
            self.label.setText(text_label.removesuffix(self.label_2.text()))
        self.label_2.setText("0")
        self.entry="0"
    def deleteChar(self):
        if ("=" in self.label.text()):
            self.label.setText("")
        if (len(self.entry)<=1):
            self.label_2.setText("0")
            if (self.prev is None):
                self.label.setText("")
            else:
                if (self.entry != "0"):
                    self.label.setText(self.label.text()[:-1])
            self.entry="0"
        else:
            self.label_2.setText(self.label_2.text()[:-1])
            if (self.label_2.text()=="-"):
                self.label_2.setText("0")
            self.entry=self.label_2.text()
    def operation(self,sign: str):
        if self.label_2.text()[0]=="u":
            self.label_2.setText("0")
            self.entry = "0"
            self.label.setText("")
            return
        text_label2 = self.label_2.text()
        text_label = self.label.text()
        self.prev=text_label2
        if (text_label2=="."):
            return
        if ("=" in text_label):
            self.entry = text_label2
            text_label = ""

        self.label.setText(text_label+self.prev+sign)
        if sign!="=":
            self.label_2.setText("0")
        if sign=="=":
            self.calculate()
            self.entry = self.label_2.text()
            self.prev=None
    def calculate(self):
        text_label = self.label.text()
        num = ""
        num_sum = None
        last_sign = None
        for i in text_label:
            if i.isnumeric() or i=="." or i=="-" or i=="e":
                num+=i
            else:
                if num_sum is None:
                    num_sum = float(num)
                if last_sign is not None:
                    try:
                        num_sum=self.calc(num_sum,num,last_sign)
                    except ZeroDivisionError:
                        self.label_2.setText("undefined")
                        return
                last_sign=i
                num=""
        try:
            if int(num_sum)==num_sum:
                self.label_2.setText(str(int(num_sum)))
                return
        except:
            self.label_2.setText(str(num_sum))
        self.label_2.setText(str(num_sum))
    @staticmethod
    def calc(a,b,sign):
        if (a==""):
            a=0
        if (b==""):
            b=0
        if (sign=="+"):
            return float(a)+float(b)
        elif (sign=="−"):
            return float(a)-float(b)
        elif (sign=="*"):
            return float(a)*float(b)
        elif (sign=="/"):
            return float(a)/float(b)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Calc()
    MainWindow.show()
    sys.exit(app.exec_())
