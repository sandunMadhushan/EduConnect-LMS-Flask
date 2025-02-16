from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/study-groups')
def studygroups():
    return render_template('study-groups.html')

# Route for Discussion Forums
@app.route('/discussion-forums')
def discussionforums():
    return render_template('discussion-forums.html')

# Route for AI Tools
@app.route('/ai-tools')
def aitools():
    return render_template('ai-tools.html')

# Route for Study Sessions
@app.route('/study-sessions')
def studysessions():
    return render_template('study-sessions.html')

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0000@localhost/educonnect_lms_flask'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username