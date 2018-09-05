import requests


def main():

    createGetRequest()
    createPostRequest()




def createGetRequest():
    #1. Create API - End Point
    URL = "http://maps.googleapis.com/maps/api/geocode/json"

    #2. Add location
    location = "McMaster University"

    #3. Define parameter dictionary to be sent to the API
    PARAMS = {"address" : location}

    #4. Send Get request & Save parameters as response Object
    response = requests.get(URL, PARAMS)

    #5. Extract data  in json format
    data = response.json()

    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']

    # printing the output
    print("Latitude:%s\nLongitude:%s\nFormatted Address:%s" % (latitude, longitude, formatted_address))


def createPostRequest():

    print("\nCreating Post Request URL")

    #1. Create API - End Point
    API_ENDPOINT = "http://pastebin.com/api/api_post.php"

    #2. Define parameters
    API_KEY = "9b69dce56a6aab2bda995f25ea539f23"

    #3. Add additional parameters
    sourceCode = "Helloworld"

    data = {"api_dev_key" : API_KEY,
            "api_option" : "paste",
            "api_paste_code" : sourceCode,
            "api_paste_format" : "python"}

    #4. Send Post request  & Save response as Object
    response = requests.post(API_ENDPOINT, data)

    #5. Extract response
    pastebin_url = response.text

    print("Response URL: ", pastebin_url)

    pass



if __name__ == '__main__':
    main()

'''

Get - to request a data from a server
POST - To submit data to be process from a server


To make HTTP Requests in python we can use libraries such as
- httplib
- urllib
- requests    (Most Simplest)


GET REQUEST

What is happening ? 
- We are getting the latitude, longtitude and formatted address of a given location

How ? 
- We are sending a get request to the Google Maps API
- We provide the location, Google api gives us the data (lat, long, address)
- Data is provided in the form of JSON which we parse D


So What are the steps in which we create a GET request
1. Set the API Endpoint - This is usually a URL
2. Define the parameters - This will in the form of dictionary
3. Send request & Store response in a response object
4. Parse 





POST REQUEST 

What is happening ? 
- We are pasting our source code onto Pastebin

How ? 
- We are sending a post request 
- We use the request.post() function to send the post
- If everything is ok, we get a Web URL like "https://pastebin.com/j3EDz3xn"
- If not, we get a error like "Bad API request, invalid api_dev_key"


Note
1. For Get Method - All form of data is encoded into the URL, added a query of String parameters
2. For Post Method - All form of data is encoded in the message body of the HTTP request
3. Only ASCII characters are allowed in GET, post can be whatever character
4. GET is less secure since data is set as part of the URL. Therefore, passwords should never be sent with a GET requests

'''