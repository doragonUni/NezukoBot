
import json

class JsonUsers():
    #if the user does not have an account we create it 
    #return false is already has one
    async def verify_user(self, user):
        json_users = await self.get_json_users() 
        if str(user.id) in json_users:
                return False
        else:
            json_users[str(user.id)] = {}
            json_users[str(user.id)]["about_me"] = "Tell us about you"
            json_users[str(user.id)]["coins"] = 0
            json_users[str(user.id)]["bday"] = 0
            json_users[str(user.id)]["daily"] = True
        await self.set_json_users(json_users)
        return True

    #open the profile.json file for the users
    async def get_json_users(self):
        with open("profile.json", "r") as file:
            json_users = json.load(file)
        return json_users

    #save changes if there is any changes
    async def set_json_users(self, json_file):
        with open("profile.json", "w") as file:
            json.dump(json_file, file)