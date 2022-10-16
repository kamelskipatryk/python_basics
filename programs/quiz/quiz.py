import requests
import html


class Question:
    def __init__(self, category, question_str, correct_answer_flag):
        # przypsianie wartości do obiektu tej klasy/assigning a value to an object of this class
        self.category = category
        self.question_str = question_str
        self.correct_answer_flag = correct_answer_flag
    
    def print_data(self):
        print(self.category, self.question_str, self.correct_answer_flag)

class Quiz:
    def __init__(self, num_questions):
        self.api_url = 'https://opentdb.com/api.php?difficulty=easy&type=boolean&amount='
        self.num_questions = num_questions
        self.questions_list = []
        self.load_questions(num_questions)
    
    def load_questions(self, num_questions):
        response = requests.get(self.api_url + str(num_questions))

        if response.ok:
            # print(response.json())
            data = response.json()
            results = data['results']

            for q in results:
                # print(q['category'])
                category = q['category']
                question_type = q['type']
                difficulty = q['difficulty']
                question_str = html.unescape(q['question']) # removing special signs from html
                # print(question_str)
                correct_answer_flag = q['correct_answer'].lower() in ['true', '1', 'yes'] # zwraca false jeśli nie ma takich odpowiedzi ['true', '1', 'yes']/return false if answer is not ['true', '1', 'yes']

                q_obj = Question(category, question_str, correct_answer_flag)
                self.questions_list.append(q_obj)
                q_obj.print_data()
    
    def start_quiz(self):
        print('\nWelcome in Quiz!')
        num_correct_user_answers = 0
        n = 0
        num_questions = len(self.questions_list)
        
        while( n < num_questions ):
            q = self.questions_list[n]
            print('Category:', q.category)
            print('\nQuestion number: ' + str(n + 1) + ': ' + q.question_str)
            # print('Answer flag:', q.correct_answer_flag)

            answer = input('Answer yes/no?: ')
            answer_bool = False
            if answer == 'yes': answer_bool = True

            if answer_bool == q.correct_answer_flag:
                print('Correct!')
                num_correct_user_answers += 1
            else:
                print('Not correct!')

            n += 1

        print('Points:', num_correct_user_answers, '/', len(self.questions_list))

quiz = Quiz(3)
quiz.start_quiz()

