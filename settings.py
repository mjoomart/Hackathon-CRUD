class Settings:
    TOKEN = 'Bearer key07Hm8tVVruIxpq'
    TABLE_NAME = 'Cars'
    ID_ = 'app4YyDsObAXQwrEg'
    HEADERS = {'Authorization': TOKEN, 'Content-Type': 'application/json'}

    def get_url(self):
        return f'https://api.airtable.com/v0/{self.ID_}/{self.TABLE_NAME}'

settings = Settings()