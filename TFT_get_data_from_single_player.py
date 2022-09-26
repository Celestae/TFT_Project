import requests
import json

api_key = "api_key=" + open("C:\\Users\\love-\\Documents\\tft_project_key_api.txt", "r").read()

class Player():
    #pass

    

    def __init__(self, summoner_name):
        self.summoner_name = summoner_name

    #For each match id, I want to get the data of the game
    def get_matchdata_with_matchid(self, matchids):
        for  matchid in matchids:
            api_url_matchdata =  "https://americas.api.riotgames.com/tft/match/v1/matches/" + matchid + "?" + api_key
            matchdata = requests.get(api_url_matchdata).json()
            
            out_file = open("myfile.json", "w")

            json.dump(matchdata, out_file, indent=4)

            out_file.close()

    def get_matchids_with_puuid(self, puuid):
        api_url_matchids = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/" + puuid + "/ids?start=0&count=20&" + api_key
        matchids = requests.get(api_url_matchids).json()
        
        self.get_matchdata_with_matchid(matchids)
          

    def get_puuid_with_summoner_name(self):
        
        # add your api_key
        api_url_summoner_name  = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/" + self.summoner_name  + "?" + api_key

        response_summoner_name = requests.get(api_url_summoner_name).json()
        puuid = response_summoner_name["puuid"]
        print("1")
    
        self.get_matchids_with_puuid(puuid)
    
    





Celestae = Player("Celestae")

print(Celestae.get_puuid_with_summoner_name())