import json
import os
class UserManager:
    def __init__(self):
        self.users=[]
        self.id=1
    def add_user(self,name,age):
        user={
            'id':self.id,
            'name':name,
            'age'age
        }
        self.users.append(user)
        self.id+=1
        return user
    def get_user(self,user_id):
        for user in self.users:
            if user['id']==user_id:
                return user
        return None
