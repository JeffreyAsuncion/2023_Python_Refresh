# this is like a heartbeat check

# import urllib
# use urllib.request to get data from the url
# write a function that takes the url and 
# returns the data from that url == response

# the purspose of this function is to check the connectivity of a site
# site is up and running or response 200
# site is down

import urllib.request as urllib

def check_url(url):
    print("Checking connectivity ...")
    
    response = urllib.urlopen(url)
    print(f"Connected to {url} successfully")
    print(f"The response code was : {response.getcode()}")
    
    return


if __name__ == "__main__":
    print("This is a site connectivity checker program")
    input_url = input("Enter the url of the site : ")
    check_url(input_url)


