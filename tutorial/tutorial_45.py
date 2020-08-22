name,age = input("enter name and age with comma separated :  ").split(",")

if (name[0] == "a" or name[0] == "A") and 10 < int(age):
    print("you can watch coco movie")
else:
    print("sorry, you can't watch coco movie")


