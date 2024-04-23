import re
from bottle import post, request
import datetime
import pdb
import json

@post('/home', method='post')
def my_form():
    # Получаем значения из формы
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    quest = request.forms.get('QUEST')
    
    # Проверяем заполнены ли все поля
    if not mail or not username:
        return "Please fill in all fields"
    
    # Проверяем правильность формата email
    if not re.match(r"^[^\W^_]{1}[^@]{1,16}@[A-Za-z]{1,7}(?:.[A-Za-z]{2,3}){1,3}$", mail):
        return "Please enter a valid email address"
    
    # Проверяем длину имени пользователя
    if not re.match(r"^[\w]{3,20}$", username):
        return "Please enter a correct name"
    
    if not re.match(r"^[a-zA-Zd]{3,}.*?$", quest) or quest.isdigit() or not any(char.isalpha() or char.isspace() for char in quest) or quest.count('?') > 1:
        return "Please enter a longer question (3 characters or more), check that the question consists of more than just numbers"
    
    # Получаем текущую дату
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    save_question(mail, username, quest)    
    
    # Возвращаем сообщение с данными пользователя
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, current_date)


# Запись вопроса в JSON файлы
def save_question(mail, username, quest):
    with open('questions.json', 'r', encoding='utf-8') as f:
        try:
            questions = json.load(f)
        except json.JSONDecodeError:
            questions = {}

    if mail in questions:
        if quest.lower() not in [q.lower() for q in questions[mail][1]]:
            questions[mail][1].append(quest)
    else:
        questions[mail] = [username, [quest]]

    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)

    
    
