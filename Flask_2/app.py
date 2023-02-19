from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/find')
def calc(number=None):
    # if user navigates to calculate page directly, there will be no requests.args
    if len(request.args)==0:
        return render_template('find.html')
    number = request.args['number']
    try:
        if int(number)%2==0:
            msg='even'
        elif int(number)%2!=0:
            msg='odd'
    except:
        msg='not an integer!'
    return render_template('find.html', num=number, name=msg)

if __name__ == "__main__":
    app.run()