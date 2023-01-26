'''
Created on Aug 15, 2021

@author: josh_
'''
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
from datetime import timedelta, date,datetime as dt
import plotly as plotly
#LETS PUT A LIMIT OF ~15 STOCKS DUE TO GOOGLESHEET BEING COMPLICATED
counter=0 #for stocks on y axis
class main:

    def __init__(self,time,year):
        fig = make_subplots(
                rows=1, cols=1,
                specs=[[{"type": "scene"}]]
            )
        greatestprice=0.0

        self.fig=fig
        self.time=time
        self.year=year
        self.counter=counter
        self.stocknames=[]

        start_dt = date(int(year), 1, 1)
        end_dt = date(int(year), 12, 31)
        templist=[]
        '''following code enables date values'''
        def daterange(date1, date2):
            for n in range(int ((date2 - date1).days)+1):
                yield date1 + timedelta(n)
        for dt in daterange(start_dt, end_dt):
            tempdate=str((dt.strftime("%Y-%m-%d")))
            templist.append(tempdate)
           
        self.date=templist
        self.greatestprice=greatestprice



    '''
##### TO BE REPLACED
    def googlesheet(self,stockname):
        time=self.time 
        self.stocknames.append(stockname)
        year=self.year
        """Thus begins the webscraping...with SELENIUM
        time="WEEKLY"
        stockname="TSLA"
        year="2019"
        """
        
        url1="https://docs.google.com/spreadsheets/d/1X25kk2JHPpeEDrNxn6wCTj2uiMsfCkbteJ6lOu48ax0/edit?usp=sharing"#using AAPL as starting point
        driver = webdriver.Chrome('./chromedriver')
        #self.driver=driver
        driver.get(url1)
        clearbox=driver.find_element_by_class_name("cell-input")
        
        auto=automate(clearbox)
        auto.select()
        auto.delete()
        auto.stockname(stockname)
        auto.select() 
        auto.delete()
        auto.placeval(stockname,year,time)
        
        sheet_id='1X25kk2JHPpeEDrNxn6wCTj2uiMsfCkbteJ6lOu48ax0'
        df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
        newlist=df.values.tolist()
        self.stock1={}
        newlist.pop(0) #removes headers
        print(newlist)
        self.newlist=newlist
        
    def sendlist(self):
        newlist=self.newlist
        stock1=self.stock1
        x1=[]
        z1=[]
        for i in range(len(newlist)):
            tempdate=str(newlist[i][0])
            tempprice=(newlist[i][1])
            add={tempdate:tempprice}
            stock1.update(add)
        for i in stock1:
            
            x1.append(str(i))
            z1.append(stock1[i])
            ################################
        x1dates=[]
        for x in x1:
            datetime_object = dt.strptime(x,"%Y-%m-%d")
            x1dates.append(str(datetime_object))
        self.x1=x1dates
        self.z1=z1
        print(x1)
        print(x1dates)
'''
    def makegraph(self):
        fig = make_subplots(
                    rows=1, cols=1,
                    specs=[[{"type": "scene"}]]
                )
        camera = dict(eye=dict(x=0, y=2.5, z=0))
        self.fig=fig
        self.camera=camera
        date=self.date
        """
        Dimension Assignment:
        Z axis: Price
        X axis: Time
        Y axis: Stock Name
        """        
    def fromsheet(self,x1,z1):
        self.x1=x1 #time
        self.z1=z1 #price
       
    
    
        
    def addgraph(self):
        fig=self.fig
        counter=self.counter
        x1=self.x1
        z1=self.z1
        greatestprice=self.greatestprice
        date=self.date


        y1=[counter]*(len(z1))    
        self.counter+=1

        count=0
        countlist=[]
        
        #countlist=list(range(0,len(z1)) 
        
        for i in range(len(z1)):
            countlist.append(count)
            count+=1
            if float(z1[i]) > greatestprice:
                greatestprice=float(z1[i])
        self.greatestprice=greatestprice       
        
        
        #print(x1)
        #print(z1)
        fig.append_trace(go.Scatter3d(x=x1, y=y1,z=z1, mode="lines+markers",marker=dict(size=2)),row=1,col=1)
        self.fig=fig
       
        
        
    def showgraph(self,stocks):
        fig=self.fig
        date=self.date
        greatestprice=self.greatestprice
        camera = dict(eye=dict(x=0, y=-2.5, z=0.7))
        counterlist=list(range(0,len(stocks)))
        #print(counterlist)
        
        fig.update_layout(scene_camera=camera,title_text="3D Stock Graph",
                    #title="layout.hovermode='closest' (the default)",
                    scene = dict(    
                            aspectmode = "auto",
                            aspectratio = dict( x = 100, y =20, z = 20),
                            
                            yaxis = dict(
                                ticktext= list(stocks),
                                tickvals= counterlist,
                                autotypenumbers='convert types'),
                            
                            zaxis=dict(
                                range=(0,greatestprice),
                                autotypenumbers='convert types'
                               ),

                             xaxis = dict(
                                tickvals= date,
                                showticklabels=False,
                                autotypenumbers='strict'),
                             
                            
                            #set time differently
                            
                            xaxis_title='Time --> (x)',
                            yaxis_title='Stock Name (y)',
                            zaxis_title='Price (z)',
                                 ),
                            
                            width=1000,height=1000,margin=dict(t=30, r=10, l=20, b=10))
                                
        fig.update_layout(autotypenumbers='convert types',showlegend=False)
      
        '''THE MAGIC LINE'''
        #test=plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
       
        test=pio.to_html(fig, auto_play=True,full_html=False,post_script=False)
        
        f = open("templates/graph.html", "w")
        f.write("""<!DOCTYPE html><a href="/">BACK TO INPUTS</a><br>""")
        f.write(test)

        f.close()
        
        #print(test)
        #return test
        