from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return render_template("home.html")

# AI-Powered Cattle Solutions Route
@app.route("/ai-cattle")
def ai_cattle():
    return render_template("ai_cattle.html")

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
    app.run(debug=True
# if 'render' in os.environ.get('SERVER_SOFTWARE', '').lower():
#     app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
