import re
from bottle import post, request
import datetime

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    
    if not mail or not username:
        return "Please fill in all fields"
    
    if not re.match(r"^[^@]{1,16}@[A-Za-z]{1,7}..[A-Za-z]{2,3}$", mail):
        return "Please enter a valid email address"
    
    if not re.match(r"^{3,20}$", username):
            return "Please enter a correct name (long:3-20)"
    
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, current_date)
