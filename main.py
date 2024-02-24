from flask import (Flask, request, redirect, render_template, 
                    send_from_directory, url_for) 
#from werkzeug.utils import secure_filename
import os




BASE_DIR = os.getcwd()

app = Flask(
            __name__, 
            static_folder=os.path.join(BASE_DIR, 'static'), 
            template_folder=os.path.join(BASE_DIR, 'templates'), 
)

app.config['SECRET_KEY'] = 'skjhksjhdksjdhksjdhksjdhksjdhskj'

users = ['user1','user2','user3','user4', 'user5','user6','user7','user8']

@app.route('/')
def index():
    res = ''
    res += '<h4> ПОЛЬЗОВАТЕЛИ </h4>'
    for i, user in enumerate(users):
        res += f"<p> {i}. Пользователь: {user} </p>"
        
    return res

@app.route('/users/')
def vew_users():   
    return render_template('1.html', users=users, head='Пользователи' , color='red')





if __name__ == "__main__":
    app.run(debug=True)
