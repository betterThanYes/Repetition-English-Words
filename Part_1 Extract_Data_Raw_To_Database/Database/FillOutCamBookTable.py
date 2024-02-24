import sqlite3
testNameList = ["Test 1","Test 2","Test 3","Test 4"]
# testNumberList = [1,2,3,4]
bookList = ["Cambridge 10","Cambridge 11","Cambridge 12","Cambridge 13","Cambridge 14","Cambridge 15","Cambridge 16","Cambridge 17","Cambridge 18"]
typeSection = ["Reading","Listening"]
list_reading = [1,2,3]
list_listening = [1,2,3,4]

if __name__ == "__main__":
	start =0
	connect = sqlite3.connect("CambridgeBookDatabase.db")
	cursor = connect.cursor()

	for book in bookList:
    	for testName in testNameList:
        	for read in list_reading:
            	start = start +1
            	cursor.execute(f"INSERT INTO CambridgeBook (CamBook_Id,Book_Name,Test,Section,Task) VALUES(?,?,?,?,?)",(start,book,testName,typeSection[0],read))
        	for listening in list_listening:
            	start = start +1
            	cursor.execute(f"INSERT INTO CambridgeBook (CamBook_Id,Book_Name,Test,Section,Task) VALUES(?,?,?,?,?)",(start,book,testName,typeSection[1],listening))
	connect.commit()
	connect.close()