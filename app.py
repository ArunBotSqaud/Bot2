from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_notebook', methods=['POST'])
def run_notebook():
    notebook_path = 'Bot.ipynb'
    output_path = 'static/Bot.html'  # Make sure the output is within the static folder

    try:
        result = subprocess.run(
            ['jupyter', 'nbconvert', '--to', 'html', '--execute', notebook_path, '--output', output_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        with open(output_path, 'r') as f:
            notebook_html = f.read()
        return notebook_html
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
