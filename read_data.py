import json
def get_data_from_json(link):
    with open(link,'r',encoding='utf-8') as file:
        person = json.load(file)
    return person

def get_person_name(person):
    person_name= []
    for i in person:
        person_name.append(i['firstname']+', '+i['lastname'])
    return person_name

def find_person_by_name(name,person):
    two_names = name.split(', ')
    for eintrag in person:
        if eintrag['firstname'] == two_names[0] and eintrag['lastname'] == two_names[1]:
            return eintrag
