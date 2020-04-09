import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return 'Welcome to messenger Main Page'



@app.route("/status")
def status():
   date = datetime.datetime.now()
   str_from_date = datetime.datetime.strftime
   return {
       'status': True,
       'date': str_from_date(date, '%Y-%m-%d'),
       'time': str_from_date(date, '%H:%M:%S'),
   }


app.run()
