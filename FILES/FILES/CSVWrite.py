#prpgram for creating csv file by using csv.writer()

import csv

with open("C:\\Users\saipr\\PycharmProjects\\FILES\\citizen.csv","a") as fp:
    #choose header names or col names

      hnames=["CID","NAME","STATE"]
#choose set of records in the form list in list
      records=[[1000,"sai","MAHA"],
              [2000,"ramesh","TS"],
              [3000,"ganesh","AP"],
              [4000,"nagesh","BANG"]]

#create an object of writer class by using writer() of csv module
      csvwro=csv.writer(fp) #here  csvwro is an object of class
      csvwro.writerow(hnames) #writing the colnames ti the csv file
      csvwro.writerows(records) #writing the columns to the csv file
      print("csv file created")
