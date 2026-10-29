class Employee:                          
    def __init__(self, name):
        self.__name = name
        self.__jobs = []
    @property
    def name(self):
        return self.__name
    @property
    def jobs(self):
        return self.__jobs
    def add_job(self, job):
        self.__jobs.append(job)
    def display_info(self):
        print(f"Имя: {self.__name} ")
    def work(self):
        print(f"{self.name} работает")

class Job:
    def __init__(self, title, company):
        self.__title = title
        self.__company = company
    @property
    def title(self):
        return self.__title
    @property
    def company(self):
        return self.__company
    def display_info(self):
        print(f"Работает: {self.__title} на/в {self.__company}")

class Student:
    def __init__(self, name, faculty):
        self.__name = name
        self.__faculty = faculty
    @property
    def name(self):
        return self.__name
    @property
    def faculty(self):
        return self.__faculty
    def display_info(self):
        print(f"Студент: {self.__name}")
    def study(self):
        print(f"{self.name} учится на {self.faculty.name} факультете")

class Faculty:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    def display_info(self):
        print(f"Факультет: {self.__name}")
      
def main():
    fit = Faculty("ФМ")
    student = Student("Иванов Иван Ильич", fit)
    student.display_info()
    student.study()
    print(f"Факультет студента: {student.faculty.name}")
    employee = Employee("Васильев Василий Артемович")
    employee.add_job(Job("Python-разработчик", "ООО Кремень"))
    employee.add_job(Job("ДНД-мастер", "НРИклуб монетка"))
    employee.display_info()
    employee.work()
    for job in employee.jobs:
        job.display_info()
if __name__ == "__main__":
    main()
