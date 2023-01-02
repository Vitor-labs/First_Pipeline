from typing import Dict

class DBRepositorySpi:
    def __init__(self)->None:
        self.insert_artist_params=[]

    def insert_artist(self, data:Dict)->None:
        self.insert_artist_params.append(data)
        