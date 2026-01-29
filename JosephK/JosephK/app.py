from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import random

app = Flask(__name__)
app.secret_key = 'joseph_learning_secret_key_2024'
socketio = SocketIO(app, cors_allowed_origins="*")

# Simple login credentials for Joseph and creator
USERS = {
    'joseph': 'joseph123',
    'creator': 'creator123'  # Creator account for live lessons
}

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').lower()
        password = request.form.get('password', '')
        
        if username in USERS and USERS[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Oops! Wrong username or password. Try again!')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'].capitalize())

@app.route('/english')
def english():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('english.html')

@app.route('/math')
def math():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('math.html')

@app.route('/social-studies')
def social_studies():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('social_studies.html')

@app.route('/environmental-studies')
def environmental_studies():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('environmental_studies.html')

@app.route('/geography')
def geography():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('geography.html')

@app.route('/reading-practice')
def reading_practice():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('reading_practice.html')

@app.route('/live-lesson')
def live_lesson():
    if 'username' not in session:
        return redirect(url_for('login'))
    is_creator = session['username'] == 'creator'
    return render_template('live_lesson.html', is_creator=is_creator)

# API endpoints for interactive games
@app.route('/api/math-problem')
def math_problem():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '×'])
    
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        # Ensure no negative results for 3rd graders
        if num1 < num2:
            num1, num2 = num2, num1
        answer = num1 - num2
    else:  # multiplication
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        answer = num1 * num2
    
    return jsonify({
        'num1': num1,
        'num2': num2,
        'operation': operation,
        'answer': answer
    })

@app.route('/api/spelling-words')
def spelling_words():
    words = [
        'friend', 'school', 'happy', 'outside', 'beautiful',
        'family', 'favorite', 'adventure', 'imagine', 'science',
        'explore', 'rainbow', 'elephant', 'butterfly', 'guitar',
        'mountain', 'library', 'mystery', 'wonderful', 'journey'
    ]
    return jsonify({'words': random.sample(words, 5)})

@app.route('/api/reading-passages')
def reading_passages():
    passages = [
        {
            'title': 'The Happy Dog',
            'text': 'Max is a happy dog. He likes to play in the park. Every morning, Max runs and jumps with his friends. He loves chasing butterflies and playing fetch with his favorite ball.'
        },
        {
            'title': 'My Best Friend',
            'text': 'Emma is my best friend. We go to school together every day. She likes to read books and draw pictures. We always help each other with our homework.'
        },
        {
            'title': 'A Day at the Beach',
            'text': 'Last summer, I went to the beach with my family. The water was blue and the sand was warm. I built a big sandcastle and found many colorful shells.'
        },
        {
            'title': 'The Magic Garden',
            'text': 'In our backyard, we have a beautiful garden. Mom plants flowers and vegetables. I help her water the plants every evening. The tomatoes are my favorite.'
        },
        {
            'title': 'Space Adventure',
            'text': 'I dream about being an astronaut. I would fly to the moon and see the stars up close. Maybe I would discover a new planet or meet friendly aliens.'
        }
    ]
    return jsonify({'passage': random.choice(passages)})

# SocketIO events for live lessons
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('join_lesson')
def handle_join_lesson(data):
    username = data.get('username')
    join_room('live_lesson')
    emit('user_joined', {'username': username}, room='live_lesson')

@socketio.on('start_stream')
def handle_start_stream(data):
    emit('stream_started', {'message': 'Creator has started the lesson!'}, room='live_lesson')

@socketio.on('stream_data')
def handle_stream_data(data):
    # Broadcast video/audio stream to all students
    emit('receive_stream', data, room='live_lesson', include_self=False)

@socketio.on('chat_message')
def handle_chat_message(data):
    emit('chat_message', data, room='live_lesson')

@socketio.on('leave_lesson')
def handle_leave_lesson():
    leave_room('live_lesson')

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)
