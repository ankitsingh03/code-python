user = {}
name = input("enter name: ")
age = int(input("enter age: "))
movies = input("enter movies with comma").split(",")
song = input("enter songs").split(",")

user['name']=name
user['age']=age
user['fav_movies']=movies
user['fav_song']=song

for i,j in user.items():
    print(f"{i} : {j}")
