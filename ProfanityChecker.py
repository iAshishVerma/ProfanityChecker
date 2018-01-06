import urllib

def readText():
    quotes=open("C:\Users\ANKIT\Desktop\movie_quotes.txt")
    red=quotes.read()
    print(red)
    quotes.close()
    checkProfanity(red)

def checkProfanity(toBeRead):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+toBeRead)#establishing the connection with website
    output=connection.read()#reads the response from the website
    print(output)
    connection.close()
readText()

    






    
    
