from flask import Flask, request, send_file, abort
from PIL import Image
import io

app = Flask(__name__)

uploaded_image = None
image_path = "signup.jpg"

@app.route('/put/blacks')
def upload_image():
    global uploaded_image
    global image_path

    try:
        with open(image_path, 'rb') as f:
            uploaded_image = f.read()
        return "Successfully imported image", 200
    except Exception as e:
        return str(e), 500

@app.route('/get/blacks')
def convert_image():
    global uploaded_image

    if uploaded_image is None:
        return "Successfully downloaded image !!", 404

    try:
        img = Image.open(io.BytesIO(uploaded_image))
        img = img.convert('L')

        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='JPEG')
        img_byte_array.seek(0)

        return send_file(img_byte_array, mimetype='image/jpeg')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)