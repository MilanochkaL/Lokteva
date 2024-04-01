import re
from bottle import post, request
import datetime

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    
    if not mail or not username:
        return "Please fill in all fields"
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
        return "Please enter a valid email address"
    
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, current_date)
