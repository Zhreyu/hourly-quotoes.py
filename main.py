
from plyer import notification # importing modules 
from time import *
import requests 

# function to send notifications
def notif(m):
    notification.notify(
    title="Your daily quote has arrived",
    message= m,
    app_icon="",
    timeout=10
    )
    time.sleep(60*60) # you can use windows task schedular instead of making the program run 24/7 in backgroud 
    

if __name__ == '__main__':
    while True:
        response = requests.get(
        "https://quote-garden.herokuapp.com/api/v3/quotes/random") # making the get request 
        if response.status_code == 200: # extracting the core data
            q_data = response.json()
            data = q_data['data']
            quote = data[0]['quoteText'] # getting the quote from the data
            notif(quote) 
        else:
          m ="Error while getting quote"
          quote(m)

