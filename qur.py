import requests
import json

# we take the  api to  take data  from saral website using request module.


saral_api = "http://saral.navgurukul.org/api/courses" 
saral_url = requests.get(saral_api)
data = saral_url.json()

# we create the json file to store data as a saral data and store using dump. 

with open ("courses.json","w") as saral_data :
    json.dump(data,saral_data,indent = 4)

# we want the courses to selet among them. 
# we print the courses, and take a input from user to select courses.

serial_no = 0
for i in data["availableCourses"] :
    print(serial_no+1, i["name"],i["id"])
    serial_no+=1
user_input = int(input("enter the Course no. which you want to learn."))
print(data["availableCourses"][user_input-1]["name"])

# If we want to go back and choose courses which we want and confirm it.
# Here we used the navigation is user says no then it will go back to courses.


up_navigation = input("Do you want to continue the Course y/n")
if up_navigation == "n" :
    serial_no = 0
    for i in data["availableCourses"] :
        print(serial_no+1, i["name"],i["id"])
        serial_no+=1
    user_input = int(input("Confirm Your Course Again12 ."))
    print(data["availableCourses"][user_input-1]["name"])

#  Here we display the which topic included in Courses. Display the topic of the courses.
#  parent Exercise
#  here again we create api to  and using json create a file as child data.

    
saral_api1 = "http://saral.navgurukul.org/api/courses/" + str(data["availableCourses"][user_input-1]["id"]) + "/exercises"
response1=requests.get(saral_api1)
data1=response1.json()
with open("parents.json","w") as child_data:
    json.dump(data1,child_data,indent=4)

serial_no2=0
for i in data1["data"] :
    print(serial_no2+1,".",i["name"])
    if len(i["childExercises"])>0 :
        s = 0
        for j in i["childExercises"]:
            s= s + 1
            print("      ",s,j["name"])
    else:
        print("      ","1",i["slug"])
    serial_no2+=1



#  now we want the select topic number which we want to select.

topic_no = int(input("Enter the Topic which you want to Learn parent exercies: "))

serial_no3 = 0
slug_content=[]
for l in data1["data"] :
    serial_no3+=1
    if topic_no == serial_no3 :
    
        course_data = requests.get("http://saral.navgurukul.org/api/courses/"+str(l["id"]+"/exercise/getBySlug?slug="+l["slug"])).text 
        data_type = json.loads(course_data)
        if "childExercises" not in data_type:
            pass
        if len(l["childExercises"]) !=0 :
            k = 0
            for i in l["childExercises"]:
                k+=1
                print(k,i["name"])
                course_data = requests.get("http://saral.navgurukul.org/api/courses/" + str(data["availableCourses"][user_input-1]["id"])+"/exercise/getBySlug?slug="+i["slug"])
                data2 = course_data.json()
                slug_content.append(data2['content'])

    

#  Here if we are not confirm to continue then say y/n.
#  display the again questions child excersice

if len(slug_content)<0:
    up_navigation = input("Do you want to continue the Course y/n")
    if up_navigation=="n":                    
        saral_api1 = "http://saral.navgurukul.org/api/courses/" + str(data["availableCourses"][user_input-1]["id"]) + "/exercises"
        response1=requests.get(saral_api1)
        data1=response1.json()
        
        serial_no2=0
        for i in data1["data"] :
            print(serial_no2+1,".",i["name"])
            if len(i["childExercises"])>0 :
                s = 0
                for j in i["childExercises"]:
                    s= s + 1
                    print("      ",s,j["name"])
            else:
                print("      ","1",i["slug"])
            serial_no2+=1

#  select child exercise

if len(slug_content)<0:
    topic_no = int(input("Enter the Topic which you want to Learn childexercise : "))
    serial_no3 = 0
    slug_content=[]
    for l in data1["data"] :
        serial_no3+=1
        if topic_no == serial_no3 :
            course_data = requests.get("http://saral.navgurukul.org/api/courses/"+str(l["id"]+"/exercise/getBySlug?slug="+l["slug"])).text 
            data_type = json.loads(course_data)
            if len(l["childExercises"]) !=0 :
                k = 0
                for i in l["childExercises"]:
                    k+=1
                    print(k,i["name"])
                    course_data = requests.get("http://saral.navgurukul.org/api/courses/" + str(data["availableCourses"][user_input-1]["id"])+"/exercise/getBySlug?slug="+i["slug"])
                    data2 = course_data.json()
                    slug_content.append(data2['content'])


# select question among then which display from topic which you select. 

n = int(input("Enter the question number which you want learn : "))
index = 0
k=n-1
print(slug_content[k])
while index <= len(slug_content):
    prev_next = input("you want prev/next question p/n")
    if prev_next == "p":
        k=k-1
        if k==-1:
            print("last page")
            break
        else:
            print(slug_content[k])
            continue
    elif prev_next=="n":
        k=k+1
        if k==len(slug_content):
            print("last page")
            break
        else:
            print(slug_content[k])
            continue
    else:
        print("write properly")
        continue
    i+=1   



