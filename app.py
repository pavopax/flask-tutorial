from flask import Flask, render_template, request, redirect
from Quandl import Quandl
import time
from bokeh.plotting import figure
from bokeh.embed import components


app = Flask(__name__)


auth_tok = "ad1xk_Hf1MdMZpF72a_X"

stock = "AAPL"
stockq = "/".join(("WIKI", stock))


#

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
  if request.method=='GET':
    return render_template('index.html')
  else:
    return redirect('/graph')

if __name__ == '__main__':
  #app.run(host='0.0.0.0', port=33507)
  app.run(debug=True)

@app.route('/graph')
def graph():
  data = Quandl.get(stockq, rows=20, authtoken=auth_tok, returns="pandas")
  df = data[['Close']]
  p = figure(width=500, height=500, title="Stock Graphs", x_axis_type='datetime')
  p.circle(x=df.index, y=df[['Close']])
  script, div = components(p)
  return render_template('graph.html', script=script, div=div)


  
