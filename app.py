from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/feature.html')
def feature():
    return render_template('feature.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/donation.html')
def donation():
    return render_template('donation.html')

@app.route('/testimonial.html')
def testimonial():
    return render_template('testimonial.html')

if __name__ == '__main__':
    app.run()