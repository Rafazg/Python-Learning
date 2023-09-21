class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def data(self):
        return f"Name: {self.name} Age: {self.age} Job: {self.job}"

    def personality(self):
        personalitys = ['Happy', 'Intelligent', 'Ambicious']
        return personalitys


def createPerson():
    personName = str(input('Digite o nome da Pessoa: '))
    personAge = int(input('Digite a idade da Pessoa: '))
    personJob = str(input('Digite o trabalho da Pessoa: '))
    person = Person(personName, personAge, personJob)
  
    return person
  
def showData():
    person = createPerson()
    print(person.data())

showData()  











