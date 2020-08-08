import json
from imdbRatings.settings import movies_json_file

class moviesMiddleware:
    def __init__(self, get_response):
        self.get_response =get_response
        all_list = Movie_id() #calling function fetchMovie_id #we are getting movie list ID here
        import requests
        list_of_data =[]
        for id in all_list:
            url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/" + id

            headers = {
                'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
                'x-rapidapi-key': "0ac662495cmsha3ddbe01a85b038p1b0e32jsn0541b2f89aff"
            }

            response = requests.request("GET", url, headers=headers)
            dict_data = json.loads(response.text) #loads -returns data in the form of a Python dictionary
            list_of_data.append(dict_data)
        with open(movies_json_file,'w') as file:  #using with we dont need to close file ex. close()
            #print(list_of_data)
            json.dump(list_of_data,file,indent=2) #indent to provide indentation.. provide spaces that are
            print("data is written")
            #beginning of line
            #dump method is used when python objects have to store in a file

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        return response

def Movie_id():
    import requests

    url = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"

    querystring = {"genre": "%2Fchart%2Fpopular%2Fgenre%2Fadventure"}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "0ac662495cmsha3ddbe01a85b038p1b0e32jsn0541b2f89aff"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    list_data =[]
    for x in data:
        list = x.split('/')[2]
        list_data.append(list)
    #print(list_data)
    return list_data



