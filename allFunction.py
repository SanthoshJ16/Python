class Calculator():
# Create a function that checks whether the given number is Odd or Even
    def oddEven():
        num=int(input("Enter the Number:" ))
        if((num%2)==0):
            print("Even Number")
            value='This is even Number'
        else:
            print("Odd Number")
            value='This is Odd Number'
        return value
# Create a function that checks the BMI
    def calcBMI():
        bmi=float(input("Enter the BMI Index"))
        if(bmi<=18.5):
            val="Underweight"
        elif(bmi<=24.9):
            val="Normal range"
        elif(bmi<=33.9):
            val="Overweight"
        else:
            val="Extremely Overweight"
        return val

class SubfieldsInAI():
    def subfields():
        list=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Subfields in AI are:")
        for subFields in list:
            print(subFields)

# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
class ElegiblityForMarriage():
    def eligible():
        gender=input("Enter your Gender:")
        age=int(input("Enter your Age:" ))
        if(gender=='Male' and age>=21):
            eligibilty="Eligible"
        elif(gender=='Female' and age>=18):
            eligibilty="Eligible"
        else:
            eligibilty="Not Eligible"
            return eligibilty
            
# calculate the percentage of your 10th mark using Class       
class FindPercent():
    def percentage(s1,s2,s3,s4,s5):# Used Parameterized function
        print('Subject1: ',s1)
        print('Subject2: ',s2)
        print('Subject3: ',s3)
        print('Subject4: ',s4)
        print('Subject5: ',s5)
        total=s1+s2+s3+s4+s5 
        percent=float(total/5)
        print('Percentage',percent) #To make sure % is calculated in Function
        return percent
        
#print area and perimeter of triangle using class and functions
class Triangle():
    def triangle(height,breadth,height1,height2,breadth2):
        print('Height: ',height)
        print('Breadth: ',breadth)
        print('Area formula: (Height*Breadth)/2')
        area=(height*breadth)/2
        print('Area of Triangle : ', area)
        print('Perimeter formula: Height1+Height2+Breadth')
        print('Height1: ',height1)
        print('Height2: ',height2)
        print('Breadth2: ',breadth2)
        perimeter=height1+height2+breadth2
        print('Perimeter of Triangle :', perimeter)
        #return perimeter