from unicodedata import name


def person(name,birth_year,weight):
    age=2002-birth_year
    if name=="": # if no name has been entered
         print("\n name : name","\n weight :",weight,"\n birthdate :",birth_year) 
         print("\n age",age)
    else:
        print("\n name :",name,"\n weight :",weight,"\n birthdate : ",birth_year,"\n age",age)
def main():
    name=input("enter the name :")  #let the user enter their name
    weight=float(input("enter the weight: "))
    birth_year=2002
    #making all the users have same birthdate of 2002


main()    
