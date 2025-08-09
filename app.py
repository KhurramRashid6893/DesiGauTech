from flask import Flask, render_template, url_for
import google.generativeai as genai

app = Flask(__name__)
 
# Home Route 
@app.route("/")
def home():
    return render_template("home.html")
 
# AI-Powered Cattle Solutions Route
genai.configure(api_key="AIzaSyD7yvvskWyuzMypw9AyaGQ1BF54yNjIgl4")
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route('/ai_cattle', methods=['GET'])
def ai_cattle():
    # Use Gemini to explain AI's role
    response = model.generate_content("Explain how AI helps in modern cattle farming in simple terms.")
    ai_explanation = response.text.replace('\n', '<br>')  # Rendered safely with HTML line breaks
    return render_template('ai_cattle.html', ai_explanation=ai_explanation)

# Smart Dairy & Sustainable Farming Route
@app.route("/dairy-farming")
def dairy_farming():
    return render_template("dairy_farming.html")

# Digital Veterinary Services Route
@app.route("/veterinary")
def veterinary():
    return render_template("veterinary.html")

# Farmer Hub & Skill Development Route
@app.route("/farmer-hub")
def farmer_hub():
    return render_template("farmer_hub.html")

# Blockchain & Digital Records Route
@app.route("/blockchain")
def blockchain():
    return render_template("blockchain.html")

# Research & Innovation Route
@app.route("/research")
def research():
    return render_template("research.html")

# Community & Awareness Route
@app.route("/community")
def community():
    return render_template("community.html")

# Government & Policy Support Route
@app.route("/government")
def government():
    return render_template("government.html")

# Contact & Help Center Route
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
