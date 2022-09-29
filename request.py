import requests,json
def req():
    url=requests.get("http://saral.navgurukul.org/api/courses")
    f= open("Course.json","w")
    Dct=json.loads(url.text)
    json.dump(Dct,f,indent=4)
    f= open("Course.json","r")
    data=json.load(f)
    
    i=0
    id=[]
    while i<len(data["availableCourses"]):
        print(i+1,data["availableCourses"][i]["name"],"=",data["availableCourses"][i]["id"])
        id.append(data["availableCourses"][i]["id"])
        i=i+1
    
    user= int(input("enter the id number:"))
    n1=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises")
    a=n1.json()
    j=0
    l=0
    slug=[]
    while j<len(a["data"]):
        print(l+1,"=",a["data"][j]["name"])
        slug.append(a['data'][j]["slug"])
        
        l=l+1
        j=j+1
    slugnumber=int(input("Enter slug number:-"))
    list=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugnumber])
    b=list.json()
    print("CONTENT",b["content"])
    
    with open('id.json',"w")as f:
        json.dump(a,f,indent=4)
    
    
    for i in range(len(slug)):
        m=(input("Enter the 'n' for next page:-"))
        if m=='n':
            i=0
            if i<len(slug):
                print(slug[i])
                print(b["content"])
                break
        else:
            print("Your page is not found")
            i=i+1
        g=input("your request accpect:")
        if  g=="yes":
            print("oke then your exist ")
        else:
            print("your req not accpect")
req()
        
