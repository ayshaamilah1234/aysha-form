from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    # Collecting form data
    userid = request.form['userid']
    password = request.form['password']
    name = request.form['name']
    address = request.form['address']
    country = request.form['country']
    zipcode = request.form['zipcode']
    email = request.form['email']
    gender = request.form.get('gender')  # Use get to avoid errors if not selected
    language = request.form.getlist('language')  # getlist() for checkboxes

    # Display all the submitted data
    return f"""
    <h2>Registration Details</h2>
    <p><strong>User ID:</strong> {userid}</p>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Address:</strong> {address}</p>
    <p><strong>Country:</strong> {country}</p>
    <p><strong>Zip-code:</strong> {zipcode}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Gender:</strong> {gender}</p>
    <p><strong>Preferred Language(s):</strong> {', '.join(language)}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
