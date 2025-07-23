import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
REMOVE_BG_API_KEY = 'eiha8Mk38PSWVz1tRXzi6PAf'  # <-- Replace this with your actual API key

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        image = request.files['image']
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': image},
            data={'size': 'auto'},
            headers={'X-Api-Key': REMOVE_BG_API_KEY},
        )

        if response.status_code == 200:
            output_path = "static/output.png"
            with open(output_path, 'wb') as out:
                out.write(response.content)
            return render_template('result.html', result_image=output_path)
        else:
            return f"Error: {response.status_code} - {response.text}"

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


