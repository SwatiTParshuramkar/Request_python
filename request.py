import requests
import json

saral_api = "http://saral.navgurukul.org/api/courses" 
saral_url = requests.get(saral_api)
data = saral_url.json()
with open ("courses.json","w") as saral_data :
    json.dump(data,saral_data,indent = 4)
serial_no = 0
for i in data["availableCourses"] :
    print(serial_no+1, i["name"],i["id"])
    serial_no+=1
user_input = int(input("enter the Course no. which you want to learn."))
print(data["availableCourses"][user_input-1]["name"])

up_navigation = input("Do you want to continue the Course y/n")
if up_navigation == "n" :
    serial_no = 0
    for i in data["availableCourses"] :
        print(serial_no+1, i["name"],i["id"])
        serial_no+=1
user_input = int(input("Confirm the Course again to learn."))
print(data["availableCourses"][user_input-1]["name"])

    
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

up_navigation1 = input("Do you want to continue this topic y/n")
if up_navigation1 == "n" :
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
    

topic_no = int(input("Enter the Topic which you want to Learn : "))
serial_no3 = 0
slug_content=[]
for l in data1["data"] :
    serial_no3+=1
    if topic_no == serial_no3 :
        print(l["slug"])
        course_data = requests.get("http://saral.navgurukul.org/api/courses/"+str(l["id"]+"/exercise/getBySlug?slug="+l["slug"])).text 
        data_type = json.loads(course_data)
        print(data_type["content"])
        if len(l["childExercises"]) !=0 :
            k = 0
            for i in l["childExercises"]:
                k+=1
                print(k,i["slug"])
                course_data = requests.get("http://saral.navgurukul.org/api/courses/" + str(data["availableCourses"][user_input-1]["id"])+"/exercise/getBySlug?slug="+i["slug"])
                data2 = course_data.json()
                slug_content.append(data2['content'])
                
        up_navigation2 = input("Do want to continue this question y/n")
        if up_navigation2 == "n" :
            serial_no3 = 0
            slug_content=[]
            for l in data1["data"] :
                serial_no3+=1
                if topic_no == serial_no3 :
                    print(l["slug"])
                    course_data = requests.get("http://saral.navgurukul.org/api/courses/"+str(l["id"]+"/exercise/getBySlug?slug="+l["slug"])).text 
                    data_type = json.loads(course_data)
                    print(data_type["content"])
                    if len(l["childExercises"]) !=0 :
                        k = 0
                        for i in l["childExercises"]:
                            k+=1
                            print(k,i["slug"])
                            course_data = requests.get("http://saral.navgurukul.org/api/courses/" + str(data["availableCourses"][user_input-1]["id"])+"/exercise/getBySlug?slug="+i["slug"])
                            data2 = course_data.json()
                            slug_content.append(data2['content'])

        n = int(input("Enter the question number which you want learn : "))
        index = 0
        k=n-1
        print(slug_content[k])  
        while index <= len(slug_content):
            prev_next = input("you want prev/next question p/n")
            if prev_next == "p":
                # index=index-1
                k=k-1
                print(k)
                if k==-1:
                    print("last page")
                    break
                else:
                    print(slug_content[k])
                    continue
            elif prev_next=="n":
                # index+=1
                print(k)
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




