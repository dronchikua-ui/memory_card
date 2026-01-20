# ---------- Question class ----------
class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_ans1
        self.wrong_answer2 = wrong_ans2
        self.wrong_answer3 = wrong_ans3
        self.count_asked = 0
        self.count_right = 0


    def got_right(self):
        self.count_asked += 1
        self.count_right += 1


    def got_wrong(self):
        self.count_asked += 1


questions = [
    Question('На что у Антона алергия?',
    'Рис🍚','Фрукты🍏','Овощи🥔','Шоколод🍫'),
    Question('Какой Арсений?',
    'Скрытный🫣','Жадный🫸','Стеснительный☺️','Разговорчивый🙃'),
    Question('Когда закрыли импровизацию?',
    '5 декобря','2 декобря','6 декобря','7 декобря'),
    Question('Какой проэкт закрыли?',
    'чдки','тейбл тайм','громкий вопрос','истории'),
    Question('Сколько сезонов в тейбл тайм?',
    '6 сезонов','3 сезона','2 сезона','4 сезона'),
]