import re
from bottle import post, request
import datetime

@post('/home', method='post')
def my_form():
    # Получаем значения из формы
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    
    # Проверяем заполнены ли все поля
    if not mail or not username:
        return "Please fill in all fields"
    
    # Проверяем правильность формата email
    if not re.match(r"^[^\W^_]{1}[^@]{1,16}@[A-Za-z]{1,7}(?:.[A-Za-z]{2,3}){1,3}$", mail):
        return "Please enter a valid email address"
    
    # Проверяем длину имени пользователя
    if not re.match(r"^[\w]{3,20}$", username):
        return "Please enter a correct name"
    
    # Получаем текущую дату
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Возвращаем сообщение с данными пользователя
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, current_date)
