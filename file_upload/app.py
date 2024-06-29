import os
from flask import Flask, request, url_for, render_template, redirect, flash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv  # type: ignore

# load env variables from the env file
load_dotenv()

app = Flask(__name__)
app.secret_key=os.getenv('SECRET_KEY')

# configure the upload folder and maximum file size limit
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # you can try 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 # 2MB maximum file size

# set the allowed file extension
ALLOWED_EXTENSIONS = {'pdf', 'img', 'jpg', 'jpeg', 'docx'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # you can try 'uploads/' in (UPLOAD_FOLDER)

@app.errorhandler(413)
def max_size_exceeded(error):
    flash('File too large. Maximum file size is 2MB.', 'danger')
    return redirect(url_for('home'))

@app.route('/')
def home():
    return render_template('upload_file.html')

@app.route('/upload', methods=['POST'])
def file_upload():
    # this checks if a file was uploaded
    if 'file' not in request.files:
        flash('No file found', 'danger')
        return redirect(request.url)
    
    file = request.files['file']
    # this checks if there is a filename in the file uploaded or if it empty
    if file.filename == '':
        flash('No filename shown', 'danger')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Successfully uploaded', 'success')
        return redirect(url_for('home'))
    else:
        flash('File type not supported', 'danger')
        return redirect(request.url)
    
if __name__ == '__main__':
    app.run(debug=True)

