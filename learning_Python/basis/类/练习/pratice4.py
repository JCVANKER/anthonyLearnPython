class User():
	"""模拟一次存储用户基本信息的类"""
	
	def __init__(self,user_name,user_age,user_gender='女'):
		#默认值形参放在最后面
		"""初始化用户基本信息"""
		self.user_name = user_name
		self.user_gender = user_gender
		self.user_age = user_age
	
	def show_user(self):
		"""显示用户基本信息"""
		print(self.user_name.title() + ' ' + self.user_gender + ' ' + 
			str(self.user_age))
	
	def set_user_gender(self,gender):
		"""设置用户性别"""
		if gender == '男':
			self.user_gender = gender
		elif gender == '女':
			self.user_gender = gender
		else:
			print("设置性别有误！默认为‘男性’")	
			
#创建Admin类，为User类的子类
class Admin(User):
	"""模拟一次管理员身份的类"""
	
	def __init__(self,user_name,user_age,user_gender='女'):
		"""初始化管理员身份的属性"""
		
		#不能给默认值，否知将会以父类的默认值设置
		super().__init__(user_name,user_age,user_gender)
		self.privileges=Privileges()#实例用作属性

#创建Privileges小类
class Privileges():
	"""对管理员类的privileges部分拆分"""
	
	def __init__(self,privileges=['can add post','can delete post',
		'can ban user']):
		"""初始化privileges的值"""
		
		self.privileges=privileges
		
	def show_privileges(self):
		"""显示priviles列表"""
		
		print("priviles are following:")
		for privilege in self.privileges:
			print("- ",privilege)
		
admin_anthony = Admin('吴敏锋',20,'男')
admin_anthony.show_user()
admin_anthony.privileges.show_privileges()
