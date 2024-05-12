import sys
import pyautogui
import pyperclip
# import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

prompts = ["Please search information in English Internet but answer in Chinese.",
           "请问在linux kernel的代码中",
           "请问这是什么报错？",
           "请问这是什么问题？应该怎么解决？",
           "如果你是拉康，你会怎么解释这个梦？",
           "如果你是荣格，你会怎么解释这个梦？",
           "请你给我介绍一下"]

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Prompts Shortcut")
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.WindowDoesNotAcceptFocus)
        button0 = QPushButton("请你在英文网络中查找相关内容")
        button0.clicked.connect(lambda: self.the_button_was_clicked(prompts[0]))

        button1 = QPushButton("请问在linux kernel的代码中")
        button1.clicked.connect(lambda: self.the_button_was_clicked(prompts[1]))

        button2 = QPushButton("请问这是什么报错？")
        button2.clicked.connect(lambda: self.the_button_was_clicked(prompts[2]))

        button3 = QPushButton("是什么问题？如何解决？")
        button3.clicked.connect(lambda: self.the_button_was_clicked(prompts[3]))        

        button4 = QPushButton("拉康解梦")
        button4.clicked.connect(lambda: self.the_button_was_clicked(prompts[4]))
        
        button5 = QPushButton("荣格解梦")
        button5.clicked.connect(lambda: self.the_button_was_clicked(prompts[5]))

        button6 = QPushButton("给我介绍一下")
        button6.clicked.connect(lambda: self.the_button_was_clicked(prompts[6]))
        
        
        layout = QVBoxLayout()
        layout.addWidget(button0)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)
        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self, promption):
        original_clipboard_content = pyperclip.paste()
        # 确保pyautogui在适当的文本输入界面中输入文本
        pyperclip.copy(promption)
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy(original_clipboard_content)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()


