import os
from flask import Flask,request, jsonify, render_template
import machine


template_dir = os.path.abspath('.')
app = Flask(__name__,template_folder=template_dir)
# section can be `all` `verbs` `nouns` `enteties`
@app.route('/<section>', methods = ['POST'])
def runKeyword(section):
    json_data = request.json
    text = json_data["text"]
    keywords = machine.run(text, section)
    return jsonify(keywords)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)