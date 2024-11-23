from flask import Flask, request, send_file
from flask_cors import CORS
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from random_color import get_random_contrasting_color
from flask import json
from werkzeug.exceptions import HTTPException, InternalServerError

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['DEBUG'] = True

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route('/generate-image', methods=['POST', 'OPTIONS'])
def generate_image():
    bg_color = request.form.get('bg_color', get_random_contrasting_color())
    font_color = request.form.get('font_color', 'white')
    width = int(request.form.get('width', 800))
    height = int(request.form.get('height', 600))
    font_size = int(request.form.get('font_size', 520))
    x1 = int(request.form.get('x', -100))
    y1 = int(request.form.get('y', -180))
    x2 = int(request.form.get('x', -100))
    y2 = int(request.form.get('y', 200))

    font_file = request.files.get('font_file')
    if not font_file:
        return "Font file is required.", 400
    font = ImageFont.truetype(BytesIO(font_file.read()), font_size)

    image = Image.new('RGB', (width, height), color=bg_color)

    draw = ImageDraw.Draw(image)
    draw.text((x1, y1), "Para", fill=font_color, font=font)
    draw.text((x2, y2), "graf", fill=font_color, font=font)

    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png', as_attachment=False, download_name='generated_image.png')

if __name__ == '__main__':
    app.run(debug=True)
