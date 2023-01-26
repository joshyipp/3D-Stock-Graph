import gspread
from oauth2client.service_account import ServiceAccountCredentials


class apiconnect:
    def __init__(self,names,year,time):
        #Variables to get from classes.py
        #stockname="TSLA"

        self.names=names
        self.time=time #time is time interval
        self.year=year
        self.even=1
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)
        
        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("google finance webscrape").sheet1
        sheet.clear()
        self.sheet=sheet
        '''''value insertion!!!'''
        datecol=['A','C','E','G','I','K','M','O','Q','S','U','W','Y','AA','AC','AE']
        for i in range(len(datecol)):
            sheet.format(str(datecol[i])+'1:'+str(datecol[i])+'366', { "numberFormat": {
                            "type": "DATE",
                            "pattern": "yyyy-mm-dd"}})
        
        
        
    def sheetids(self):    
        #this gives the format for the names in the sheets
        names=self.names
        sheet=self.sheet
        sheetformatnames = []
        for i in range(0, len(names) - 1):
            sheetformatnames.append(names[i])
            sheetformatnames.append("")
        sheetformatnames.append(names[-1])
        
        print(sheetformatnames)
        sheet.delete_rows(1)
        sheet.insert_row(sheetformatnames,1)
        
    def insertdata(self,stockname): #assign parameter stockname 
        sheet=self.sheet
        year=self.year
        time=self.time
        even=self.even
        self.stockname=stockname #every time its called, resets stock selected
        sheet.update_cell(2,even,'=GOOGLEFINANCE('
                           +'"'+stockname+'"'+','
                           +'"price"'+','
                           +"DATE("+year+",1,1)"+','
                           +"DATE("+year+",12,31)"+','
                           +'"'+time+'"'
                           +')')
        even+=2
        self.even=even
        
        # Extract and print all of the values
        #list_of_hashes = sheet.get_all_records()
        #list_of_hashes.pop(0)
        # clear sheet after using
        #sheet.clear()
        #print(list_of_hashes)
        
    def getdatedata(self):
        stockname=self.stockname
        sheet=self.sheet
        tempcell=sheet.find(stockname)
        tempdate=sheet.col_values(tempcell.col)
        tempdate=tempdate[2::]
        return tempdate
        #print(tempdate)
        
        
    def getpricedata(self): 
        stockname=self.stockname
        sheet=self.sheet
        tempcell=sheet.find(stockname)
        tempprice=sheet.col_values(tempcell.col+1)
        tempprice=tempprice[2::]   
        return tempprice
        #print(tempprice)
#class testing
'''
stocklist=['tsla','aapl']
test=apiconnect(stocklist,'2020','WEEKLY')
test.sheetids()
for stock in stocklist:
    test.insertdata(stock)
    test.getdata()'''