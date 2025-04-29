from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None
    city = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'cd59b873e498570f10625a4959b2b74a'  
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        url = f"{base_url}q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        if response['cod'] == 200:
            weather = response['main']
    return render_template('index.html', weather=weather, city=city)

if __name__ == "__main__":
    app.run(debug=True)
