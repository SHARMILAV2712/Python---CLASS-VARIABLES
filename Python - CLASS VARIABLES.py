#Here I have created a simple information module which is used in library. 
#This program gives the information of books we need.
#BY: SHARMILA.V - SIST

from datetime import timedelta,datetime
print("Government Library")
print("The available books are:\nBrief answers to the big questions\nThirukkural\nHarry Potter\nPonniyin Selvan")
a = input("Enter the book name to know the details:")
rdt = datetime.now()+timedelta(days=30)
class Library:
    retdt = 30
    def __init__(self,author,totalpages,genere,language,pos):
        self.author = author
        self.totalpages = totalpages
        self.genere = genere
        self.language = language
        self.pos = pos
        
    def bookdetails(self):
        book = f"Author:{self.author}\nTotal Pages:{self.totalpages}\
        \nGenere:{self.genere}\nLanguage:{self.language}\nAvailable at:{self.pos}"
        return book
        

if a == "Brief answers to the big questions":
    b1 = Library('Stephen Hawking',200,'Science','English','Rack 2 - 1st book')
    print(b1.bookdetails())
   
elif a == "Thirukkural":
    b2 = Library('Thiruvalluvar',270,'Literature','Tamil','Rack 1 - 5th book')
    print(b2.bookdetails())
    
elif a == "Harry Potter":
    b3 = Library('J.K. Rowling',1000,'Fiction-Novel','English','Rack 7 - 1st book')
    print(b3.bookdetails())
    
elif a=="Ponniyin Selvan":
    b4 = Library('Kalki',1000,'Historical Novel','Tamil','Rack 1 - 1st book')
    print(b4.bookdetails())
    
else:
    print('Not Available')
print("Should return in",Library.retdt,"days")
print("Return Date:",rdt)