import xlrd
from festivals import festivals



#constructor for creating a table in a database with the given schema
shows = festivals("shows", {"name": "text", "location": "text", "month": "text"})

#open up the the excel file that we need to import and make sure we are using the correct sheet in the excel file
workbook = xlrd.open_workbook('fests.xls')
ws = workbook.sheet_by_name('fests')
print(ws)

#iterate through all rows in the agenda
for row in range(ws.nrows):
        print("here")
        #insert the row into the db table
        shows.insert({"name": ws.cell(row, 0).value, "location": ws.cell(row, 1).value,
                       "month": ws.cell(row, 2).value})
