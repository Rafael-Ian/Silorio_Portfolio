
from flask import Flask, render_template, request
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'  
@app.route('/')
def index():
    
    return render_template('index.html', title='Home')

@app.route('/profile')
def profile():
    
    user = {
        'name': 'Rafael Silorio',
        'about': 'Likes computer-related stuff and wants to be a game developer.',
        'email': 'cabertesilorio@gmail.com',
        'image': 'Raf_pic.jpg'
    }
    return render_template('profile.html', title='Profile', user=user)

@app.route('/contact')
def contact():
    
    contact_info = {'email': 'cabertesilorio@gmail.com'}
    return render_template('contact.html', title='Contact', contact=contact_info)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result = None
    radius = None
    error = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', '').strip())
            if radius <= 0:
                raise ValueError('Radius must be positive')
            area = math.pi * (radius ** 2)
            result = round(area, 4)
        except Exception as e:
            error = 'Please enter a valid positive number for radius.'
    return render_template('circle.html', title='Area of Circle', result=result, radius=radius, error=error)

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    result = None
    base = None
    height = None
    error = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', '').strip())
            height = float(request.form.get('height', '').strip())
            if base <= 0 or height <= 0:
                raise ValueError('Values must be positive')
            area = 0.5 * base * height
            result = round(area, 4)
        except Exception as e:
            error = 'Please enter valid positive numbers for base and height.'
    return render_template('triangle.html', title='Area of Triangle', result=result, base=base, height=height, error=error)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
