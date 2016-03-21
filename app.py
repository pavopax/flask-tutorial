from flask import Flask, render_template, request, redirect
from Quandl import Quandl
import time
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

app.vars={}

auth_tok = "ad1xk_Hf1MdMZpF72a_X"

# lead main page to index
@app.route('/')
def main():
  return redirect('/index')

# upon first load, 'GET' information from user
# once submitted, go to graph page
@app.route('/index', methods=['GET', 'POST'])
def index():
  if request.method=='GET':
    return render_template('index.html')
  else:
    app.vars['stock'] = request.form['ticker']
    return redirect('/graph')




@app.route('/graph')
def graph():
  stock = app.vars['stock']
  stockq = "/".join(("WIKI", stock))
  data = Quandl.get(stockq, rows=20, authtoken=auth_tok, returns="pandas")
  df = data[['Close']]
  p = figure(width=700, height=500, title=stock, x_axis_type='datetime')
  p.circle(x=df.index, y=df[['Close']])
  script, div = components(p)
  return render_template('graph.html', script=script, div=div)


if __name__ == '__main__':
  app.run(debug=True)
  

