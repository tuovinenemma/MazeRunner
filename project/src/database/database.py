import json
import os
from operator import itemgetter

class Database():

    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.path = os.path.join(dirname, "data.txt")

    def get_data_(self):

        with open(self.path, 'r') as file:
            # Read the contents of the file into a dictionary
            data = json.load(file)
        return data


    def add_score(self, player_name, score):

        data = self.get_data_()
        player = {"player": player_name, "score": score}
        data.append(player)

        json_data = json.dumps(data)

        with open(self.path, 'w') as file:
            # Write the JSON string to the file
            file.write(json_data)

    def sort_key(self, score):
        return score['score'], score['player']

    def get_top_10(self):
        data = self.get_data_()
        top_scores = sorted(data, key=itemgetter('score', 'player'), reverse=True)
        return top_scores[:10]

database = Database()
database.add_score("Miisa", 73)
top = database.get_top_10()

print(top[0]['player'])
print(top[0]['score'])
