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
    def update_age(self,self.id,new_age):
        user=self.get_user(user_id)
        if user:
            user['age']=new_age
            return True
        return False
    def remove_user(self,user_id):
        user = self.get_user(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
    def list_users(self):
        return self.users
    def save_to_json(self,filename):
        with open(filename,'r'encoding='utf-8')as f:
            json.dump(self.users,f,ensure_ascii=False,indent=4)
   