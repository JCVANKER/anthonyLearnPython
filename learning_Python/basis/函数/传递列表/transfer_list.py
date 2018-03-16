#传递列表
def greet_users(names):
	'''向列表中的每位用户都发出简单的问候'''
	for name in names:
		msg="Hello, " + name.title() + "!"
		print(msg)
usernames = ['hannah','ty','margot']
greet_users(usernames)
print("----------------------------------")
#在函数中修改列表
def print_models(unprinted_designs,completed_models):
	"""
	模拟打印每个设计，直到没有未打印的设计为止
	打印每个设计后，都将其移到列表conpleted_models中
	"""
	while unprinted_designs:
		current_design=unprinted_designs.pop()
		#模拟根据设计制作3D打印模型的过程
		print("Printing model: "+current_design)
		completed_models.append(current_design)
def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

"""
	禁止函数修改列表:采用切片表示法[:]创建列表的副本，函数所做的修改不会影响到列表本身
	如：print_models(unprinted_designs[:],completed_models)
	unprinted_designs列表元素不会发生修改
	除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数，因为让函数使用现成
	列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此
"""
