import csv
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/text_input', methods=['POST'])
def text_input():
    name = request.form['name']
    class_num = int(request.form['class_num'])
    section = request.form['section']
    data = pd.read_csv("students.csv")
    row = data[(data['name'] == name) & (data['class'] == class_num) & (data['section'] == section)]
    if row.shape[0] == 1:
        remark = row['remark'].values[0]
        term1 = row['term1'].values[0] if 'term1' in row else None
        term2 = row['term2'].values[0] if 'term2' in row else None
        return render_template('remark.html', remark=remark, term1=term1, term2=term2)
    else:
        return "No student found with the given name, class, and section."

if __name__ == "__main__":
    app.run(debug=True)