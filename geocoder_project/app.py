from flask import Flask, render_template, request, send_file
import pandas
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgresql@localhost/geocoder'

@app.route('/')
def index():
    return render_template('index.html', table=None)

@app.route('/', methods=['POST'])
def geocoder_form():
    try:
        global filename
        file = request.files['file']
        df = pandas.read_csv(file)
        columns = list(df.columns.values)
        if 'Address' not in columns and 'address' not in columns:
            return render_template("index.html", table=None, error="Please make sure you have Address in your CSV file.")

        table = dict()
        table['columns'] = columns

        data = df.values.tolist()
        table['data'] = data

        filename = datetime.now().strftime("sample_files/%Y-%m-%d-%H-%M-%S-%f" + ".csv")
        df.to_csv(filename, index=None)

        return render_template("index.html", table=table, btn="download.html")
    except Exception as e:
        return render_template("index.html", error=str(e), table=None)

@app.route('/download')
def download():
    return send_file(filename, attachment_filename="yourfile.csv", as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run()
