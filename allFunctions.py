class allFunc():
    def BMI():
        bmi = float(input("Enter the BMI Index"))
        if bmi < 18.5:
            print("Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Normal weight")
        elif 25 <= bmi < 29.9:
            print("Overweight")
        else:
            print("Very Overweight")
    def OddorEven():
        val = int(input("Enter a number:"))
        if(val % 2 == 0):
            print(val ," is Even number")
        else:
            print(val, " is Odd number")
    def Subfields():
        print("Sub-fields in AI Are:")
        list = ('Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing')
        for lists in list:
            print(lists)
    def Elegible():
        Gender = input("Your Gender:")
        age = int(input("Your Age:"))
        if(Gender == "Male" and age >= 21) or (Gender == "Female" and age >= 18):
            if(age >= 21):
                print("Elegibile")
            else:
                print("Not Elegibile")
    def percentage():
        Sub1 = int(input("Subject1 = "))
        Sub2 = int(input("Subject2 = "))
        Sub3 = int(input("Subject3 = "))
        Sub4 = int(input("Subject4 = "))
        Sub5 = float(input("Subject5 = "))
        Total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
        print("Total : ", Total)
        print("Percentage : ", Total / 5)
    def triangle():
        Height = int(input("Height :"))
        Breadth1 = int(input("Breadth :"))
        print("Area formula : (Height * Breadth1)/2")
        print("Area of Triangle : ", ((Height * Breadth1)/2))
        Height1 = int(input("Height 1:"))
        Height2 = int(input("Height 2:"))
        Breadth = int(input("Breadth:"))
        print("Perimeter formula : Height1 + Height2 + Breadth")
        print("Perimeter of Triangle : ", Height1 + Height2 + Breadth)