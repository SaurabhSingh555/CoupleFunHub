from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# ==================== DARES ====================
DARES = [
    "💖 Give a 10-sec hug right now",
    "🤳 Send a cringey selfie to your partner",
    "👶 Speak in baby voice for 1 min",
    "💃🕺 Dance together for 30 seconds",
    "📸 Recreate your first photo together",
    "🧠 Share your favorite memory of each other",
    "💌 Give 3 genuine compliments",
    "📸 पार्टनर की सबसे क्यूट फोटो क्लिक करो अभी",
    "🎈 1 मिनट में अपने पार्टनर के लिए एक गिफ्ट पैक करो (कुछ भी)",
    "🙈 आंख बंद करके अपने पार्टनर को पहचानो सिर्फ़ छूकर",
    "🗓 Plan a surprise date for next weekend",
    "🍳 Cook a meal together tonight",
    "✏ Write a short love note to each other",
    "🤪 Take a silly couple photo",
    "💆 Massage your partner for 2 minutes",
    "📱 Share your phone backgrounds",
    "🛏️ झूठ-मूठ की लोरी सुनाओ जैसे बच्चा सुला रहे हो",
    "💭 अपने सपनों का future बताओ – शादी, घर, बच्चे 😂",
    "🧸 अपने पार्टनर को कोई प्यारा nickname दो और पूरा दिन वही बुलाओ",
    "👕 अपने पार्टनर की कोई चीज़ पहन लो और फोटो लो",
    "🎉 घर में अभी एक छोटा सा celebration करो – कुछ भी मजेदार!",
    "💘 Tell each other what first attracted you",
    "✊ Play thumb war - loser makes breakfast",
    "🌟 अपने पार्टनर के लिए एक बॉलीवुड डायलॉग एक्ट करो",
    "🎭 पार्टनर के लिए एक शायरी बनाओ और सुनाओ",
    "🧁 अपने पार्टनर को आँख बंद करके कुछ मीठा खिलाओ",
    "💑 अपने पहले डेट का नाटक करो - एक्टिंग करो!",
    "🎤 एक फिल्मी गाना गाओ और डेडिकेट करो",
    "📦 पार्टनर को एक छोटा सा सरप्राइज दो (घर में ही)"
]

# ==================== LOVE STORY ====================
LOVE_STORY_TEMPLATES = [
    """✨ Once upon a time, {name1} met {name2} at {place}. Their eyes locked over {memory}, and the rest was history. 💕""",
    """🌌 In a world of billions, {name1} and {name2} found each other at {place}. It all started with {memory}. ✨""",
    """💫 {name1} never believed in love at first sight... until they met {name2} at {place}. That day, {memory} changed everything. 🌊❤️""",
    """🌠 The story of {name1} and {name2} began at {place}, where fate brought them together. {memory} was just the beginning. 📖💞""",
    """🔥 From the moment {name1} saw {name2} at {place}, sparks flew. {memory} sealed the deal. 🌞❤️🛌"""
]

# ==================== COMPATIBILITY ====================
COMPATIBILITY_PHRASES = [
    "🌟 Your energies align like stars in the cosmos",
    "💬 You communicate like two peas in a pod",
    "💝 Your love languages complement each other perfectly",
    "🧪 You have the kind of chemistry that poets write about",
    "📶 Your connection is stronger than Wi-Fi",
    "🎵 You're more in sync than a metronome",
    "🔐 Your bond is tighter than a pickle jar lid",
    "🧩 You fit together like puzzle pieces",
    "🎶 Your wavelengths match like perfect harmonies",
    "🥜 You're compatible like peanut butter and jelly"
]

# ==================== BUCKET LIST ====================
BUCKET_LIST_ITEMS = [
    "Watch sunrise together",
    "Go on a spontaneous road trip",
    "Learn to dance together",
    "Write letters to each other to open in 5 years",
    "Have a picnic under the stars",
    "Visit 5 new countries together",
    "Build a fort and sleep in it",
    "Take a cooking class together",
    "Go camping in the wilderness",
    "Volunteer together"
]

# ==================== LOVE METER ====================
LOVE_METER_QUESTIONS = [
    "How often do you think about your partner when apart?",
    "How much do you trust your partner?",
    "How well do you communicate during disagreements?",
    "How much do your life goals align?",
    "How physically affectionate are you?"
]

# ==================== DATE IDEAS ====================
DATE_IDEAS = [
    "Romantic candlelit dinner at home",
    "Picnic in the park",
    "Movie marathon with all your favorite films",
    "Take a cooking class together",
    "Visit a museum or art gallery",
    "Go stargazing with blankets and hot chocolate",
    "Try a new restaurant in town",
    "Take a dance class together",
    "Go on a scenic hike",
    "Have a game night with your favorite board games",
    "Visit a local farmers market",
    "Take a weekend getaway to a nearby town",
    "Go to a comedy club",
    "Try an escape room together",
    "Have a spa day at home"
]

# ==================== ROUTES ====================

@app.route('/')
def home():
    return render_template('home.html')

# ------------------ Dare ------------------
@app.route('/dare', methods=['GET', 'POST'])
def dare():
    if request.method == 'POST':
        dare = random.choice(DARES)
        return jsonify({"dare": dare})
    return render_template('dare.html')

@app.route('/get_dares')
def get_dares():
    return jsonify(DARES)

# ------------------ Love Story ------------------
@app.route('/love_story', methods=['GET', 'POST'])
def love_story():
    if request.method == 'POST':
        name1 = request.form.get('name1', '').strip()
        name2 = request.form.get('name2', '').strip()
        place = request.form.get('place', '').strip()
        memory = request.form.get('memory', '').strip()

        if not all([name1, name2, place, memory]):
            return render_template('love_story.html', error="Please fill all fields!")

        template = random.choice(LOVE_STORY_TEMPLATES)
        story = template.format(name1=name1, name2=name2, place=place, memory=memory)

        return render_template('love_story.html', story=story)

    return render_template('love_story.html')

# ------------------ Compatibility ------------------
@app.route('/compatibility', methods=['GET', 'POST'])
def compatibility():
    if request.method == 'POST':
        name1 = request.form.get('name1', '').strip()
        name2 = request.form.get('name2', '').strip()

        if not name1 or not name2:
            return render_template('compatibility.html', error="Please enter both names!")

        name_sum = sum(ord(c.lower()) for c in name1 + name2)
        score = (name_sum % 80) + 20
        phrase = random.choice(COMPATIBILITY_PHRASES)

        shared_letters = len(set(name1.lower()) & set(name2.lower()))
        vowel_match = len(set('aeiou') & set(name1.lower()) & set(name2.lower()))

        fun_facts = [
            f"✨ You have {shared_letters} letters in common!",
            f"💫 You share {vowel_match} vowel sounds!",
            f"🔮 Your names create magical energy when combined!",
            f"💞 {name1[:1] + name2[:1]} is your power couple initial!",
            f"🌈 Your combined name length is {len(name1 + name2)}!"
        ]

        return render_template('compatibility.html',
                             name1=name1,
                             name2=name2,
                             score=score,
                             phrase=phrase,
                             fun_facts=random.sample(fun_facts, 3))

    return render_template('compatibility.html')

# ------------------ Anniversary ------------------
@app.route('/anniversary')
def anniversary():
    return render_template('anniversary.html')

@app.route('/calculate_anniversary', methods=['POST'])
def calculate_anniversary():
    date_str = request.form.get('anniversary_date')

    try:
        anniversary_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        today = datetime.now().date()

        delta = today - anniversary_date
        days = delta.days
        weeks = days // 7
        months = (today.year - anniversary_date.year) * 12 + (today.month - anniversary_date.month)
        years = today.year - anniversary_date.year

        milestones = {
            100: "💯 100 days",
            365: "🎉 1 year",
            500: "🌟 500 days",
            730: "🎊 2 years",
            1000: "💖 1000 days"
        }

        next_milestone = min((m for m in milestones if m > days), default=None)

        if next_milestone:
            milestone_text = milestones[next_milestone]
            days_to_milestone = next_milestone - days
        else:
            milestone_text = "🎂 Anniversary!"
            days_to_milestone = 365 - (days % 365)

        return render_template('anniversary.html',
                             days=days,
                             weeks=weeks,
                             months=months,
                             years=years,
                             days_to_milestone=days_to_milestone,
                             milestone_text=milestone_text)

    except ValueError:
        return render_template('anniversary.html', error="Please enter a valid date in YYYY-MM-DD format")

# ------------------ Memory Lane ------------------
@app.route('/memory_lane')
def memory_lane():
    return render_template('memory_lane.html')

@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    photo = request.files['photo']
    if photo.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # In a real app, you'd save the file and store the path
    return jsonify({'success': True, 'message': 'Photo uploaded successfully'})

# ------------------ Bucket List ------------------
@app.route('/bucket_list')
def bucket_list():
    return render_template('bucket_list.html', items=BUCKET_LIST_ITEMS)

@app.route('/add_bucket_item', methods=['POST'])
def add_bucket_item():
    new_item = request.form.get('new_item')
    if new_item and new_item.strip():
        BUCKET_LIST_ITEMS.append(new_item.strip())
    return redirect(url_for('bucket_list'))

# ------------------ Love Meter ------------------
@app.route('/love_meter')
def love_meter():
    return render_template('love_meter.html', questions=LOVE_METER_QUESTIONS)

@app.route('/calculate_love', methods=['POST'])
def calculate_love():
    scores = [int(request.form.get(f'q{i}', 0)) for i in range(1, 6)]
    total = sum(scores)
    percentage = (total / (len(scores) * 10)) * 100
    
    if percentage >= 90:
        message = "🔥 Soulmates! Your connection is incredibly strong"
    elif percentage >= 70:
        message = "💖 Deeply in love! You have a wonderful relationship"
    elif percentage >= 50:
        message = "❤️ Good connection! Keep nurturing your love"
    else:
        message = "💔 Needs work! Focus on communication and quality time"
    
    return render_template('love_meter_results.html', 
                         percentage=round(percentage),
                         message=message,
                         scores=scores)

# ------------------ Date Ideas ------------------
@app.route('/date_ideas')
def date_ideas():
    return render_template('date_ideas.html')

@app.route('/generate_date_idea')
def generate_date_idea():
    idea = random.choice(DATE_IDEAS)
    return jsonify({'idea': idea})

# ==================== MAIN ====================
if __name__ == '__main__':
    app.run(debug=True)