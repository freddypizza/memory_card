from PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
class Question():
    def __init__(self, question_text, right_answer, wrong1, wrong2, wrong3):
        self.question_text = question_text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
q1 = Question('Государственный язык Бразилии?', 'Португальский', 'Францусзкий', 'Итальянский', 'Английский')
q2 = Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Поляки', 'Чуваши')
q3 = Question('Кто открыл мыс Доброй Надежды?', 'Бартоломеу Диаш', 'Христофор Колумб', 'Фернан Магеллан', 'Леонардо да Винчи')
q4 = Question('В каком году была выпущена GTA V?', '2013', '2015', '2023', '2000')
q5 = Question('На что похожа территория Италии?', 'Сапог', 'Дракон', 'Слон', 'Кошка')
q6 = Question('Самое популярное животное в мире?', 'Крокодил', 'Обезьяна', 'Слон', 'Собака')
questions_list = [q1, q2, q3, q4, q5, q6]
app = QApplication([])
main_win  = QWidget()
main_win.total = 0
main_win.score = 0
main_win.cur_question = -1
main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')
Qgroup = QGroupBox('Варианты ответов')
answer12 = QPushButton('Ответить')
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Смурфы')
btn_answer3 = QRadioButton('Чулымцы')
btn_answer4 = QRadioButton('Алеуты')
layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()
layout_2.addWidget(btn_answer1)
layout_2.addWidget(btn_answer2)
layout_3.addWidget(btn_answer3)
layout_3.addWidget(btn_answer4)
layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)
Qgroup.setLayout(layout_1)
Group = QButtonGroup()
Group.addButton(btn_answer1)
Group.addButton(btn_answer2)
Group.addButton(btn_answer3)
Group.addButton(btn_answer4)

Sgroup = QGroupBox('Результат теста')
result = QLabel('прав ты или нет?')
answer = QLabel('ответ будет тут')

v_line = QVBoxLayout()
v_line.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
v_line.addWidget(answer, alignment=Qt.AlignHCenter, stretch=2)
Sgroup.setLayout(v_line)

v_line2 = QHBoxLayout()
v_line3 = QHBoxLayout()
v_line4 = QHBoxLayout()
v_line2.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
v_line3.addWidget(Qgroup)
v_line3.addWidget(Sgroup)
v_line4.addStretch(1)
v_line4.addWidget(answer12, stretch=2)
v_line4.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(v_line2, stretch=2)
layout_card.addLayout(v_line3, stretch=8)
layout_card.addLayout(v_line4, stretch=3)
layout_card.addStretch(1)
layout_card.setSpacing(5)
main_win.setLayout(layout_card)
Qgroup.show()
Sgroup.hide()
def show_result():
    Qgroup.hide()
    Sgroup.show()
    answer12.setText('Следующий вопрос')
def show_question():
    Sgroup.hide()
    Qgroup.show()
    answer12.setText('Ответить')
    Group.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    Group.setExclusive(True)
answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question_text)
    answer.setText(q.right_answer)
    show_question()
def show_correct(res):
    result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Кол-во заданных вопросов:', main_win.total, 'Кол-во правильных ответов:', main_win.score, 'Рейтинг:', main_win.score/main_win.total * 100)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
def next_question():
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
    main_win.total += 1
    print('Кол-во заданных вопросов:', main_win.total, 'Кол-во правильных ответов:', main_win.score)
def click_ok():
    if answer12.text() == 'Ответить':
        check_answer()
    else:
        next_question()

answer12.clicked.connect(click_ok)
next_question()
main_win.resize(400, 200)
main_win.show()
app.exec_()

