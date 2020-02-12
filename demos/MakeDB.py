import json

class MakeDB():

    dbConfig = None

    def __init__(self):
        self.dbConfig = "Yo"
        with open('../dbConfig.json') as db_config_file:
            self.dbConfig = json.load(db_config_file)

    print(dbConfig)
