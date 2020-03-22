from flask import Flask, render_template, request
import numpy as np
from flask_bootstrap import Bootstrap
#from utils import read_from_file, save_in_filepth

app = Flask(__name__) #app is object and flask is a class
Bootstrap(app)


@app.route('/',methods=['GET','POST']) #@ starting is known as decorator functions
def index(): 
    if request.method == 'POST':
        print(request.form)
        start = request.form.get('start')
        end = request.form.get('end')
        result = np.random.randint(start,end,size=(3,3))
        return render_template("index.htm",result=result)
    return render_template("index.htm") #genetrate template or context data

@app.route('/panels')
def panels():
    return render_template('panels.html')

 

      

if __name__ == "__main__":
    app.run(debug=True)         