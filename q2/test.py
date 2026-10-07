
from main import UserManager
def test_user_manager():
    print('开始测试')
    um=UserManager()
    user1=um.add_user('张三',18)
    assert user1=={'id':1,'name':'张三','age':18}
    user2=um.add_user('李四', 20)
    assert user2["id"]==2
    print("添加用户测试通过")
    assert um.get_user(1)["name"]=='张三'
    assert um.get_user(99) is None
    print("查询用户测试通过")
    assert um.update_age(1, 19)==True
    assert um.get_user(1)['age']==19
    assert um.update_age(99, 20)==False
    print('修改年龄测试通过')
    assert um.remove_user(2)==True
    assert um.remove_user(2)==False
    print('删除用户测试通过')
    um.save_to_json('users.json')
    um2 = UserManager()
    um2.load_from_json('users.json')
    assert len(um2.list_users())==1
    assert um2.list_users()[0]['id']==1
    user3 = um2.add_user('王五',25)
    assert user3["id"] == 2
    print('持久化与ID接续测试通过')

if __name__=='__main__':
    test_user_manager()