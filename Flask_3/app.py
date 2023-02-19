from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


ORGANIZATIONS = ['Soccer', 'Football', 'Chess', 'Science', 'Hokey']


users = {}


# The home page for the app
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']
        error = None
        if not name:
            error = 'Name is required.'
        elif not organization:
            error = 'Organization is required.'
        elif organization not in ORGANIZATIONS:
            error = 'Invalid organization. Choose one of: ' + ', '.join(ORGANIZATIONS)
        if error is None:
            users[name] = organization
            return redirect(url_for('data'))
        else:
            return render_template('home.html', error=error)
    else:
        return render_template('home.html')


@app.route('/data')
def registered():
    return render_template('data.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)