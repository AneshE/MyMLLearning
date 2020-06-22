#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print(len(enron_data))
print (len(enron_data["SKILLING JEFFREY K"].keys()))
names_file = open(r"../final_project/poi_names.txt", "r")
names = names_file.read().upper()
sum = 0
poi = 0
salary = 0
email = 0
for (key, value) in enron_data.items():
    #print value["salary"]
    if value["poi"]:
        sum+=1
        if (names.find(key.split(' ')[1].strip())) > 0 :
            #print key
            poi+=1
    if value["salary"] != "NaN":
        salary+=1
    if value["email_address"] != "NaN":
        email +=1
print sum
print poi
print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print salary
print email
