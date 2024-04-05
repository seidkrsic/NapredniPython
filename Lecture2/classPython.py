

# dictionary 
# object oriented programming 

class Student: 
    def __init__(self, name, house, patronus):
        if not name: 
            raise ValueError("Missing name.") 
        if house not in ["Gryffindor", "Hufflepuff", "Raveclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house  
        self.patronus = patronus 
    
    def charm(self): 
        return self.patronus 

def main(): 
    student = get_student()
    print(f"{student.name} from {student.house}") 
    print(student.charm()) 

def get_student(): 
    name = input("Name: ")
    house = input("House: ") 
    patronus = input("Patronus: ")
    student = Student(name, house, patronus)   
    return student 



if __name__ == "__main__": 
    main() 

