from classes import main
from apiconnect import apiconnect
from flask import Flask, render_template,request

app = Flask(__name__)
"""
while True:
    timefr=input("Choose time interval (WEEKLY or DAILY): ")
    timefr=timefr.upper()
    if (timefr.upper() == "WEEKLY") or (timefr.upper() == "DAILY"):
        break
    else:
        print("INVALID INPUT")
        continue
while True:
    try:
        timein=int(input("Choose a year(be mindful of when stocks were available): "))
        if timein < 2006:
            print("INVALID YEAR")
            continue
        else:
            timein=str(timein)
            break
    except:
        print("INVALID INPUT")
        continue


'''This loop allows the addition of multiple stocks until keyword STOP is typed'''
stock=""
print("Type 'stop' if finished adding stocks")
print("Stocks are identified by their abbreviations (example: TSLA, AAPL, etc.)")
while True:
    if "stop" in stock:
        stock = stock.replace(",stop,", "")
        break
    else:
        stock += input("Please enter stocks you want to graph(max is 15 stocks): ") + ","
        
stock = stock.split(',')
print(stock)
#VARIABLES TO USE ARE TIMEFR(WHICH IS WEEKLY/DAILY), TIMEIN(YEAR), and STOCK(list of stocknames)
conn=apiconnect(stock,timein,timefr)
execute=main(timefr,timein)
conn.sheetids()

execute.makegraph()    

for indiv in stock: #for each stock, appends it to the graph
    conn.insertdata(indiv)
    x1=conn.getdatedata()
    z1=conn.getpricedata()
    execute.fromsheet(x1,z1)
    execute.addgraph()




execute.showgraph(stock)

"""

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/homes/",methods=["POST"])
def fun_HOMES():
    stocklist=[]
    if 'submit' in request.form:
        tinterval=str(request.form['time']).upper()
        year=(request.form['year'])
    
    for i in range(15):
        stocklist.append(str(request.form['stock'+str(i)]))
    strtemp=""
    for stock in stocklist:
        strtemp+=stock
    if strtemp=="":
        return render_template('index.html')
    else:
        result=list(filter(None, stocklist)) #filters out empty strings
    conn=apiconnect(result,year,tinterval)
    execute=main(tinterval,year)
    conn.sheetids() #puts it in sheets format with spaces seperating each stock
    execute.makegraph()    
    for indiv in result: #for each stock, appends it to the graph
        conn.insertdata(indiv)
        x1=conn.getdatedata()
        z1=conn.getpricedata()
        execute.fromsheet(x1,z1)
        execute.addgraph()
    execute.showgraph(result)
    return render_template('graph.html')

    
        
        
        
if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", use_reloader=False)


""" PAST CODE without html form
from classes import main
from apiconnect import apiconnect
from flask import Flask, render_template
import time

app = Flask(__name__)
while True:
    timefr=input("Choose time interval (WEEKLY or DAILY): ")
    timefr=timefr.upper()
    if (timefr.upper() == "WEEKLY") or (timefr.upper() == "DAILY"):
        break
    else:
        print("INVALID INPUT")
        continue
while True:
    try:
        timein=int(input("Choose a year(be mindful of when stocks were available): "))
        if timein < 2006:
            print("INVALID YEAR")
            continue
        else:
            timein=str(timein)
            break
    except:
        print("INVALID INPUT")
        continue


'''This loop allows the addition of multiple stocks until keyword STOP is typed'''
stock=""
print("Type 'stop' if finished adding stocks")
print("Stocks are identified by their abbreviations (example: TSLA, AAPL, etc.)")
while True:
    if "stop" in stock:
        stock = stock.replace(",stop,", "")
        break
    else:
        stock += input("Please enter stocks you want to graph(max is 15 stocks): ") + ","
        
stock = stock.split(',')
print(stock)
#VARIABLES TO USE ARE TIMEFR(WHICH IS WEEKLY/DAILY), TIMEIN(YEAR), and STOCK(list of stocknames)
conn=apiconnect(stock,timein,timefr)
execute=main(timefr,timein)
conn.sheetids()

execute.makegraph()    

for indiv in stock:
    conn.insertdata(indiv)
    x1=conn.getdatedata()
    z1=conn.getpricedata()
    execute.fromsheet(x1,z1)
    execute.addgraph()




execute.showgraph(stock)


'''
for indivstock in stock:
    
    execute.googlesheet(indivstock)        
    execute.sendlist()
    execute.addgraph()
    '''









#@app.route("/")
def home():
    return render_template('index.html')
        
if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", use_reloader=False)



"""