# 🎓 Joseph's Learning Adventure

A fun and interactive educational website designed for Joseph, a 3rd grader, to make learning exciting across multiple subjects!

## 🌟 Features

- **🔐 Login System**: Secure login page for Joseph
- **📚 English**: Interactive spelling challenges with audio pronunciation
- **🔢 Math**: Addition, subtraction, and multiplication practice with streak tracking
- **🏛️ Social Studies**: Quiz about communities, history, and citizenship
- **🌱 Environmental Studies**: Learn about nature, animals, and conservation
- **🌍 Geography**: Explore the world with fun geography quizzes
- **🔊 Sound Effects**: Engaging audio feedback for interactions
- **🎨 Colorful Design**: Kid-friendly interface with animations and emojis

## 📋 Requirements

- Python 3.7 or higher
- Flask

## 🚀 Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your web browser and go to:
```
http://localhost:5000
```

## 🔑 Login Credentials

- **Username**: joseph
- **Password**: joseph123

## 📁 Project Structure

```
JosephLearning/
├── app.py                          # Main Flask application
├── templates/                      # HTML templates
│   ├── login.html                  # Login page
│   ├── dashboard.html              # Subject selection dashboard
│   ├── english.html                # English learning page
│   ├── math.html                   # Math learning page
│   ├── social_studies.html         # Social Studies page
│   ├── environmental_studies.html  # Environmental Studies page
│   └── geography.html              # Geography page
├── static/                         # Static files
│   ├── style.css                   # Main stylesheet
│   └── sounds/                     # Sound effects (optional)
│       ├── click.mp3
│       ├── success.mp3
│       └── error.mp3
└── README.md                       # This file
```

## 🎮 How to Use

1. **Login**: Enter username "joseph" and password "joseph123"
2. **Choose a Subject**: Click on any colorful subject card
3. **Play & Learn**: 
   - English: Type the spelling of words you hear
   - Math: Solve addition, subtraction, and multiplication problems
   - Social Studies: Answer questions about communities and history
   - Environmental Studies: Learn about nature and animals
   - Geography: Explore world facts and locations
4. **Track Your Score**: Earn points for correct answers!

## 🔊 Sound Effects (Optional)

The app uses sound effects for better engagement. To add sound effects:

1. Place MP3 files in `static/sounds/` folder:
   - `click.mp3` - Button click sound
   - `success.mp3` - Correct answer sound
   - `error.mp3` - Incorrect answer sound

You can download free sound effects from websites like:
- [Freesound.org](https://freesound.org/)
- [Zapsplat.com](https://www.zapsplat.com/)

The app will work fine without sound files - errors will be silently caught.

## 🎨 Customization

- **Colors**: Edit `static/style.css` to change colors and styles
- **Questions**: Edit the `questions` arrays in each HTML template to add/modify quiz questions
- **Difficulty**: Modify `app.py` to adjust math problem ranges and word difficulty

## 📚 Educational Content

All content is designed for 3rd grade level (ages 8-9):
- **English**: Common 3rd grade spelling words
- **Math**: Addition, subtraction (1-20), and basic multiplication
- **Social Studies**: Community, citizenship, and basic US history
- **Environmental Studies**: Nature, animals, recycling
- **Geography**: Continents, oceans, directions, basic world facts

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Features**: 
  - Text-to-Speech API for word pronunciation
  - Responsive design for different screen sizes
  - Animated gradients and transitions
  - Interactive quizzes with immediate feedback

## 📝 Notes

- The app uses session management for login
- All scores are reset when the page refreshes (no database storage)
- Speech synthesis requires a modern browser with Web Speech API support
- Best viewed on Chrome, Firefox, or Edge browsers

## 🎉 Have Fun Learning!

This application is designed to make learning fun and engaging for Joseph. The colorful interface, interactive games, and immediate feedback help create a positive learning experience!

---

Made with ❤️ for Joseph's learning journey!
