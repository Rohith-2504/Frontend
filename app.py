from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-house-plan', methods=['POST'])
def generate_plan():
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    # Mock response — replace with your image generation logic
    if prompt:
        return jsonify({'imageUrl': '/static/templet/sample_plan.jpg'})  # Replace with real logic
    else:
        return jsonify({'error': 'No prompt provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
