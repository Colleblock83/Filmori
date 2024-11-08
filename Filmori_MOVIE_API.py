import requests

head1 = "Welcome to \033[1;35mFilmori\033[0m!"
mid1 = head1.center(130)
head2 = "My PayPal: \033[1;34m@FabioBaensch\033[0m"
mid2 = head2.center(130)
print(mid1)
print(mid2)
print()
print()
#Getting the information from the database
def data():
    #sending ip request
    choice =  paratype
    url = "https://api.themoviedb.org/3/search/movie"  #url with movie list
    
        
    headers = {
                    #headers we need:
        "accept": "filmori/json",
        "Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MDY5ODFlMzIzMDI0YTcwMDAyODA3YjBhZTMwYjMwZCIsIm5iZiI6MTczMTA2OTU5MC44NDM3Njg4LCJzdWIiOiI2NzJlMDU5NGZjNjU4ZmQzM2MyYTE0MDYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.bsZCjy1Zlo5KT-vt3kBlaqah0DYks0D5LOTquaCK_1M"
        }
    parameters = {
        "query" : choice

        }

        
    send_request = requests.get(url, headers=headers, params=parameters)
    if send_request.status_code == 200:
            data_list = send_request.json()
            
            print(f"""
            Movie Information: 
                  
                  Page: {data_list["page"]}
                  \033[1;31mResults\033[0m:  
                        Adult:  \033[1;31m{data_list["results"][0]["adult"]}\033[0m
                        Movie ID: \033[1;31m{data_list["results"][0]["id"]}\033[0m
                        Release-Date: \033[1;31m{data_list["results"][0]["release_date"]}\033[0m
                        Original Language: \033[1;31m{data_list["results"][0]["original_language"]}\033[0m
                        Original Title: \033[1;31m{data_list["results"][0]["original_title"]}\033[0m
                        \033[1;34mDescription\033[0m: 
                            {data_list["results"][0]["overview"]}

                        Vote-Rating: \033[1;31m{data_list["results"][0]["vote_average"]}\033[0m
                        Vote Count: \033[1;31m{data_list["results"][0]["vote_count"]}\033[0m

            """)

    else:
          print(f"CRITICAL ERROR!: {send_request.status_code}")
    
            
    
paratype = input("What movie do you search for?: ")
while True:
    data()
    paratype = input("What movie do you search for?: ")
