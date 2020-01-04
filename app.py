from flask import Flask, render_template     
import pandas as pd
from datetime import datetime
import calendar
import time

sch = pd.read_excel("schedule.xlsx")

app = Flask(__name__)

def myData(campus,current_time):
    
    my_date = datetime.today()
    d = calendar.day_name[my_date.weekday()]

    if(d=="Monday"):
        dd = ("M")
    elif (d=="Tuesday"):
        dd="T"
    elif (d=="Wednesday"):
        dd = "W"
    elif (d=="Thursday"):
        dd = "R"
    elif (d=="Friday"):
        dd = "F"
    elif (d=="Saturday"):
        dd = "S"
    elif (d=="Sunday"):
        dd = "U"
    
        
    s = sch[sch["Campus"]==campus]
    s = s[s["Course Day"].str.contains(dd)==True]
    snow = s[s["End Time"]>current_time]

    
    snow = snow[["Course Location","Course",'Course Title', "Name", "Start Time","End Time","Course Day"]]
    html = snow.to_html()
    
    return("<p>" + html +"</p")


@app.route("/")
def home():  
    now = datetime.now()
    current_time = now.strftime("%H.%M")
    campus = "AA"
    header = "<center><img src='https://www.adu.ac.ae/images/default-source/default-album/logo.png?sfvrsn=5ca9a21a_0'><h3>Current and upcoming classes for today: " + campus + " at " + current_time + "<h3>" 
    return("<meta http-equiv='refresh' content='60' >" + header + myData(campus,current_time)+"</center>")

@app.route("/odhabi")
def odhabi():
    
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=False)