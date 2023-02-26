from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QGroupBox, QButtonGroup
from time import sleep
from random import shuffle , randint
app = QApplication([])

class Question():
    def __init__(self, q, r , w1, w2, w3):
        self.question = q
        self.right = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3

question_list = []
q1 = Question('The national language of Brazil', 'Portuguese', 'Brazilian', 'Spanish', 'Italian')
question_list.append(q1)
question_list.append(Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'))
question_list.append(Question('A traditional residence of the Yakut people', 'Urasa', 'Yurt', 'Igloo', 'Hut'))
question_list.append(Question('The best partisan in WW2', 'Yugoslavia', 'France', 'Soviet union', 'Poland'))
question_list.append(Question('When ww2 Start', '1939', '1940', '1941', '1945'))
question_list.append(Question('When ww2 end', '1945', '1943', '1947', '1946'))


btn_Ok = QPushButton('No Answer')
lb_Question = QLabel('No question')
radiogroup = QGroupBox('Answer options')
rbtn_1 = QRadioButton('There question here')
rbtn_2 = QRadioButton('There question here')
rbtn_3 = QRadioButton('There question here')
rbtn_4 = QRadioButton('Yes')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

choiceGroup = QButtonGroup()
choiceGroup.addButton(rbtn_1)
choiceGroup.addButton(rbtn_2)
choiceGroup.addButton(rbtn_3)
choiceGroup.addButton(rbtn_4)

layout_ans = QHBoxLayout()
layout_ans_left = QVBoxLayout()
layout_ans_left.addWidget(rbtn_1)
layout_ans_left.addWidget(rbtn_2)

layout_ans_right = QVBoxLayout()
layout_ans_right.addWidget(rbtn_3)
layout_ans_right.addWidget(rbtn_4)
layout_ans.addLayout(layout_ans_left)
layout_ans.addLayout(layout_ans_right)
radiogroup.setLayout(layout_ans)

labelgroup = QGroupBox('No Result')
layout_label = QVBoxLayout()
lb_Truefalse = QLabel('False')
lb_answer = QLabel('No answer')
layout_label.addWidget(lb_Truefalse)
layout_label.addWidget(lb_answer)
labelgroup.setLayout(layout_label)
labelgroup.hide()

main_layout = QVBoxLayout()
main_layout.addWidget(lb_Question, alignment= Qt.AlignCenter)
main_layout.addWidget(radiogroup)
main_layout.addWidget(labelgroup)
main_layout.addWidget(btn_Ok, alignment= Qt.AlignCenter)


def show_result():
    radiogroup.hide()
    labelgroup.show()
    btn_Ok.setText('No question')
def show_question():
    radiogroup.show()
    labelgroup.hide()
    btn_Ok.setText('No Answer')
    choiceGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    choiceGroup.setExclusive(True)
def check_answer():
    if answers[0].isChecked():
        lb_Truefalse.setText('Correct!')
        window.score += 1
    else:
        lb_Truefalse.setText('Incorrect!')
    show_result()
    print('statistics')
    print('Total question:', window.total)
    print('Right answer:', window.score)
    print('Rating:', (window.score/window.total)*100, '%')

def ask(q: Question):
    lb_Question.setText(q.question)
    lb_answer.setText(q.right)
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    show_question()

def next_question():
    window.total += 1
    window.cur_question = randint(0, len(question_list) - 1)
    q = question_list[window.cur_question]
    ask(q)

def start_test():
    if btn_Ok.text() == 'No question':
        next_question()
    else:
        check_answer()


window = QWidget()
window.resize(400, 200)
window.setWindowTitle('I said no questiion here why you still finding for question')
window.setLayout(main_layout)
window.score = 0
window.total = 0
btn_Ok.clicked.connect(start_test)
next_question()
window.show()
app.exec()