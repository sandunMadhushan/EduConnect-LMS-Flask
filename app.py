from flask import Flask, render_template

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
