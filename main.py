#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QGroupBox, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self,que,right_ans,wrong_ans1,wrong_ans2,wrong_ans3):
        self.que = que
        self.right_ans = right_ans
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
questions = list()
questions.append(Question('Кто является спиритом другого порядка?', 'Войд спирит', 'Эмбер спирит', 'Ертх спирит', 'Шторм сприт'))
questions.append(Question('Кто такой сф?','Шадоу финд','Энигма','Сайленсер','Кез'))
questions.append(Question('Сколько скилов у инвокера?','10','4','6','15'))
questions.append(Question('Как зовут эмбер спирита?','Син','Каолин','Райджин','Инай'))
questions.append(Question('Кто умеет воровать способности?', 'Рубик', 'Сларк', 'Никс', 'Хускар'))
questions.append(Question('У какого героя нет маны?', 'Хускар', 'Акс', 'Антимаг', 'Спектра'))
questions.append(Question('Resonant Pulse - чей это скилл?', 'Войд спирит', 'Инвокер', 'Чен', 'Дарк сир'))
questions.append(Question('С какой преиодичностью выходят крипы?', '30 секунд', '1 минута', '10 секунд', '5 минут'))
questions.append(Question('Какой герой знает таймер возрождения рошана?', 'Темплар ассассин', 'Дроу ренджер', 'Спектра', 'Оракл'))
questions.append(Question('Сколько героев в доте', '125', '124', '123', '126'))
app = QApplication([])
main_win = QWidget()
main_win.resize(360,260)
main_win.setWindowTitle('Memory Card')
main_win.setStyleSheet('background-color: mediumorchid; color: black')
main_win.total = 0
main_win.correct = 0
main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
box_line1 = QHBoxLayout()
box_line2 = QVBoxLayout()
box_line3 = QVBoxLayout()
box_line4 = QVBoxLayout()
box_line5 = QHBoxLayout()
box_line6 = QHBoxLayout()
answer_box = QGroupBox('Варианты ответов')
answer_box.setStyleSheet('background-color: blueviolet; color: black')
result_box = QGroupBox('Результат теста')
result_box.setStyleSheet('background-color: blueviolet; color: black')
truefalse = QLabel()
answer = QLabel()
RadioGroup = QButtonGroup()
question = QLabel()
button_text = 'Ответить'
ok_button = QPushButton(button_text)
ok_button.setStyleSheet('background-color: purple; color: black')
ans1 = QRadioButton()
ans2 = QRadioButton()
ans3 = QRadioButton()
ans4 = QRadioButton()
answers = [ans1,ans2,ans3,ans4]

def ask(self):
    shuffle(answers)
    answers[0].setText(self.right_ans)
    answers[1].setText(self.wrong_ans1)
    answers[2].setText(self.wrong_ans2)
    answers[3].setText(self.wrong_ans3)
    question.setText(self.que)
    show_question()
def chek_answer():
    answer.setText(answers[0].text())
    if answers[0].isChecked() == True:
        show_correct('Правильно')
        main_win.correct += 1
    else:
        show_correct('Неверно')
    main_win.total += 1
    print(f'Статистика\n-Всего вопросов: {main_win.total}\n-Правильных ответов: {main_win.correct}\nРейтинг: {main_win.correct/main_win.total*100}')
def next_question():
    counter_que = randint(0,len(questions)-1)
    ask(questions[0 + counter_que])
    counter_que += 1
def click_ok():
    if button_text == 'Ответить':
        chek_answer()
    elif button_text == 'Следующий вопрос':
        next_question()
def show_correct(itog):
    truefalse.setText(itog)
    show_result()
def show_result():
    answer_box.hide()
    result_box.show()
    global button_text
    button_text = 'Следующий вопрос'
    ok_button.setText(button_text)
def show_question():
    result_box.hide()
    answer_box.show()
    global button_text
    button_text = 'Ответить'
    ok_button.setText(button_text)
    RadioGroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    RadioGroup.setExclusive(True)
#def start_test(): # не используем
#    if button_text == 'Ответить':
#        show_result()
#    elif button_text == 'Следующий вопрос':
#        show_question()

RadioGroup.addButton(ans1)
RadioGroup.addButton(ans2)
RadioGroup.addButton(ans3)
RadioGroup.addButton(ans4)
box_line2.addWidget(ans1)
box_line2.addWidget(ans2)
box_line3.addWidget(ans3)
box_line3.addWidget(ans4)
box_line1.addLayout(box_line2)
box_line1.addLayout(box_line3)
box_line5.addWidget(truefalse, alignment = Qt.AlignLeft)
box_line6.addWidget(answer, alignment = Qt.AlignCenter)
box_line4.addLayout(box_line5)
box_line4.addStretch(1)
box_line4.addLayout(box_line6)
box_line4.addStretch(1)
result_box.setLayout(box_line4)
answer_box.setLayout(box_line1)
line1.addWidget(question, alignment = Qt.AlignCenter)
line2.addStretch(1)
line2.addWidget(ok_button, stretch = 2)
line2.addStretch(1)
main_line.addStretch(1)
main_line.addLayout(line1)
main_line.addStretch(1)
main_line.addWidget(answer_box, stretch = 4)
main_line.addWidget(result_box, stretch = 4)
main_line.addStretch(1)
main_line.addLayout(line2)
main_line.addStretch(1)
main_win.setLayout(main_line)
result_box.hide()
next_question()
ok_button.clicked.connect(click_ok)   
main_win.show()
app.exec_()