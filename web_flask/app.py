from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def landing_page():
    # Sample data for preview
    sample_data = {
        'variety': 'H6213',
        'ecozone': 'Highlands',
        'price': 420,
        'availability': 'Branches, Agents, Stockists'
    }
    return render_template('landing.html', sample_data=sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

