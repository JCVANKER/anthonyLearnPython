def city_country(city_name,country_name):
	'''返回城市和所在国家'''
	city_country_name=city_name + ", " + country_name
	return city_country_name
city_country_name=city_country('Santiago','Chile')
print('"'+city_country_name+'"')
print("------------------------------------------")
def make_album(singer_name,album_name,song_numbers=''):#可选形参
	'''返回一个字典，其中包含歌手名、专辑名以及可选的歌曲名'''
	album={
		'singer_name':singer_name,
		'album_name':album_name,
		}
	if song_numbers:
		album['song_numbers']=song_numbers
	return album
album=make_album('张学友','吻别',song_numbers=10)
print(album)
album=make_album('林俊杰','不为谁而作的歌')
print(album)
print("------------------------------------------")
#结合while循环以及input()用户输入
def make_album(singer_name,album_name,song_numbers=''):#可选形参
	'''返回一个字典，其中包含歌手名、专辑名以及可选的歌曲名'''
	album={
		'singer_name':singer_name,
		'album_name':album_name,
		}
	if song_numbers:
		album['song_numbers']=song_numbers
	return album
print("Please input singer_name, album_name (and song_numbers):")
print("(Enter 'q' at any time to quit)")
while True:
	singer_name=input("singer_name:")
	if singer_name == 'q':
		break
	album_name=input("album_name:")
	if album_name == 'q':
		break
	song_numbers=input("song_numbers:")
	if song_numbers == 'q':
		break
	song_numbers=int(song_numbers)
	if song_numbers <= 0 :
		#调用函数
		album=make_album(singer_name,album_name)
		print(album + "\n")
	else:
		album=make_album(singer_name,album_name,song_numbers)
		print(album + "\n")
