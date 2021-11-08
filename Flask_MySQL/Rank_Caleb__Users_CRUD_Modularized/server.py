from Rank_Caleb__Users_CRUD_Modularized import app
from Rank_Caleb__Users_CRUD_Modularized.controllers import users
from flask import redirect

@app.route('/')
def home():
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)