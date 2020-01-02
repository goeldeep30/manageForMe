import json
class Utility:
    def getRoomInfo(self):
        with open('mfm/room.json') as json_file:
            data = json.load(json_file)
        return data
