from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QRadioButton, QGroupBox, QButtonGroup


from random import shuffle, choice
from main import *


#TODO
from menu_window import MenuWindow


# ---------- App ----------
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(600, 500)


# ---------- Widgets ----------
question = QLabel("Питання")
answer_btn = QPushButton("Відповідь")


RadioGroupBox = QGroupBox("Варіанти відповідей")


rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()


###
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


RadioGroup = QButtonGroup()
for btn in answers:
    RadioGroup.addButton(btn)
###
# ---------- Layout answers ----------
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)


# ---------- Result ----------
AnsGroupBox = QGroupBox("Результат")
lb_Result = QLabel('')
lb_Correct = QLabel('')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()


# ---------- Main layout ----------
layout_card = QVBoxLayout()


#TODO
menu_btn = QPushButton("📚 Меню")
layout_card.addWidget(menu_btn, alignment=Qt.AlignCenter)




layout_card.addWidget(question, alignment=Qt.AlignCenter)
layout_card.addWidget(RadioGroupBox)
layout_card.addWidget(AnsGroupBox)
layout_card.addWidget(answer_btn, alignment=Qt.AlignCenter)


window.setLayout(layout_card)


####
# ---------- Logic ----------


current_question = None


def show_question(q):
    global current_question
    current_question = q


    question.setText(q.question)


    answers_text = [
        q.answer,
        q.wrong_answer1,
        q.wrong_answer2,
        q.wrong_answer3
    ]
    shuffle(answers_text)


    RadioGroup.setExclusive(False)
    for btn in answers:
        btn.setChecked(False)
    RadioGroup.setExclusive(True)
    #Кожній кнопці присвоюється свій варіант відповіді
    for btn, text in zip(answers, answers_text):
        btn.setText(text)


    RadioGroupBox.show()
    AnsGroupBox.hide()
    answer_btn.setText("Відповідь")




def show_result(correct):
    RadioGroupBox.hide()
    AnsGroupBox.show()


    if correct:
        lb_Result.setText("✅ Правильно!")
    else:
        lb_Result.setText("❌ Неправильно!")


    lb_Correct.setText(f"Правильна відповідь: {current_question.answer}")
    answer_btn.setText("Наступне питання")




def check_answer():
    if answer_btn.text() == "Відповідь":
        selected = None
        for btn in answers:
            if btn.isChecked():
                selected = btn.text()


        if selected == current_question.answer:
            current_question.got_right()
            show_result(True)
        else:
            current_question.got_wrong()
            show_result(False)
    else:
        show_question(choice(questions))


#TODO
def open_menu():
    window.hide()
    window.menu = MenuWindow(window)
    window.menu.show()




# ---------- Start ----------
show_question(choice(questions))
answer_btn.clicked.connect(check_answer)


#TODO
menu_btn.clicked.connect(open_menu)


###
window.show()
app.exec()
