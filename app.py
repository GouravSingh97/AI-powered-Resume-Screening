from flask import Flask, request, jsonify
import your_model 

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to AI-powered Resume Screening System!"

@app.route('/screen_resume', methods=['POST'])
def screen_resume():
    resume_text = request.form['resume']
    prediction = your_model.predict(resume_text) 
    return jsonify({"suitability_score": prediction})

if __name__ == "__main__":
    app.run(debug=True)
