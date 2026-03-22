from flask import Flask, jsonify, render_template
import random
import datetime

app = Flask(__name__)

# بيانات وهمية
DATA = [
    {"title": "AI System", "desc": "Advanced artificial intelligence module"},
    {"title": "Security Layer", "desc": "High level encryption & protection"},
    {"title": "Performance Engine", "desc": "Optimized backend processing"},
    {"title": "Analytics Core", "desc": "Real-time data analysis system"}
]

# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html")

# API يرجع بيانات
@app.route("/api/data")
def get_data():
    return jsonify({
        "status": "success",
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "data": random.sample(DATA, k=len(DATA))
    })

# API تاني
@app.route("/api/random")
def random_number():
    return jsonify({
        "number": random.randint(1, 1000)
    })

# تشغيل السيرفر
if __name__ == "__main__":
    app.run(debug=True)