from flask import Flask
AI=Flask(__name__)

@AI.route('/venkat')
def venkat():
    return '<h1>this is database file</h1>'




if __name__=='__main__':
    AI.run(debug=True)