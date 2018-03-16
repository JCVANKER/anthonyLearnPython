#创建列表
invitations=['Anthony','Luke','treeson']
#逐个访问列表元素，邀请嘉宾
print("Dear "+invitations[0]+", Welcome to my party.")
print("Dear "+invitations[1]+", Welcome to my party.")
print("Dear "+invitations[2]+", Welcome to my party.")
#修改嘉宾名单
print("Dear "+invitations[0]+", Good night.")
invitations[0]='samual'
print("Dear "+invitations[0]+", Welcome to my party.")
print("Dear "+invitations[1]+", Welcome to my party.")
print("Dear "+invitations[2]+", Welcome to my party.")
#添加新嘉宾
invitations.insert(0,'Anthony')
invitations.insert(2,'Dick')
invitations.append('Frake')
print("Dear "+invitations[0]+", Welcome to my party.")
print("Dear "+invitations[1]+", Welcome to my party.")
print("Dear "+invitations[2]+", Welcome to my party.")
print("Dear "+invitations[3]+", Welcome to my party.")
print("Dear "+invitations[4]+", Welcome to my party.")
print("Dear "+invitations[5]+", Welcome to my party.")
print("I total invited ",len(invitations)," friends to join my party")
#删除嘉宾名单
print("Dear "+invitations.pop().title()+", sorry sir.")
print("Dear "+invitations.pop().title()+", sorry sir.")
print("Dear "+invitations.pop().title()+", sorry sir.")
print("Dear "+invitations.pop().title()+", sorry sir.")
del invitations[0]
del invitations[0]
print(invitations)
