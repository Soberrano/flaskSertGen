import os
import platform
import subprocess, sys
from flask import Flask, request, render_template
import pandas as pd

from config import Config
from serGenerator import sertGeneratorList, sertGeneratorSingle
from forms import sertForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def hello():
  name = ""
  return render_template('index.html',download = f"Download{name}")



@app.route('/sertlist', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        data = pd.read_excel(file)
        download = sertGeneratorList(data,'kvant')
        open_folder(r'uploads')
        return render_template('index.html',download = download)


@app.route('/singleSert', methods=['GET', 'POST'])
def singleSert():
    form = sertForm()
    if form.validate_on_submit():
        name = form.name.data
        sname = form.sname.data
        patronymic = form.patronymic.data
        status = form.status.data
        kvant = form.kvant.data
        mod = form.mod.data
        hour = form.hour.data
        number = form.number.data
        podr = 'kvant' if form.kvantbool.data else 'cube'
        if form.kvantbool.data and form.cube.data:
            return render_template('index.html')
        sertGeneratorSingle(name,sname,patronymic,status,kvant,mod,hour,number,podr)
        open_folder(r'uploads')
    return render_template('data.html', form = form)



def open_folder(file_path):
    if platform.system() == "Windows":
        os.startfile(file_path)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, file_path])


if __name__ == '__main__':
  app.run(debug=True)