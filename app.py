from flask import Flask, render_template, request
import base64
from PIL import Image
import io

app = Flask(__name__)

# Konversi RGB ke grayscale (rata-rata)
def rgb_to_grayscale(r, g, b):
    return (r + g + b) // 3

# Ubah data piksel ke format data URI untuk ditampilkan di web
def image_to_data_uri(pixels, width, height):
    img = Image.new('RGB', (width, height))
    img.putdata(pixels)
    
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}"

@app.route('/', methods=['GET', 'POST'])
def index():
    original_img = grayscale_img = binary_img = indexed_img = None
    
    if request.method == 'POST' and 'image' in request.files:
        file = request.files['image']
        
        if file.filename != '':
            img = Image.open(io.BytesIO(file.read()))
            width, height = img.size
            pixels = list(img.getdata())
            
            original_img = image_to_data_uri(pixels, width, height)
            grayscale_pixels, binary_pixels, indexed_pixels = [], [], []
            
            for r, g, b in pixels:
                # Grayscale
                gray = rgb_to_grayscale(r, g, b)
                grayscale_pixels.append((gray, gray, gray))
                
                # Binner
                bw = 255 if gray > 128 else 0
                binary_pixels.append((bw, bw, bw))
                
                # Indexed Color
                r_idx, g_idx, b_idx = (r // 32) * 32, (g // 32) * 32, (b // 32) * 32
                indexed_pixels.append((r_idx, g_idx, b_idx))
            
            grayscale_img = image_to_data_uri(grayscale_pixels, width, height)
            binary_img = image_to_data_uri(binary_pixels, width, height)
            indexed_img = image_to_data_uri(indexed_pixels, width, height)
    
    return render_template('index.html',
                         original_img=original_img,
                         grayscale_img=grayscale_img,
                         binary_img=binary_img,
                         indexed_img=indexed_img)

if __name__ == '__main__':
    app.run(debug=True)
