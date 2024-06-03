class Student:
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):

        gr_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            gr_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / gr_count
        res = f'Name: {self.name}\n' \
              f'Surname: {self.surname}\n' \
              f'Avarage grade for home task: {self.average_rating}\n' \
              f'Courses in process: {courses_in_progress_string}\n' \
              f'Finisged courses: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):

        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating

class Mentor:
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):

        gr_count = 0
        for k in self.grades:
            gr_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / gr_count
        res = f'Name: {self.name}\nSurname: {self.surname}\nAvarage grade for lectures: {self.average_rating}'
        return res

    def __lt__(self, other):

        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        res = f'Name: {self.name}\nSurname: {self.surname}'
        return res

best_lecturer_1 = Lecturer('Franklin', 'Roosevelt')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Harry', 'Truman')
best_lecturer_2.courses_attached += ['Git']

best_lecturer_3 = Lecturer('Dwight', 'Eisenhower')
best_lecturer_3.courses_attached += ['Python']

cool_reviewer_1 = Reviewer('John', 'Kennedy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Git']

cool_reviewer_2 = Reviewer('Lyndon', 'Lyndon')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Git']

student_1 = Student('Barack', 'Obama')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Donald', 'Trump')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Joseph', 'Biden')
student_3.courses_in_progress += ['Python', 'Git']
student_3.finished_courses += ['Введение в программирование']


student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Git', 5)
student_1.rate_hw(best_lecturer_2, 'Git', 7)
student_1.rate_hw(best_lecturer_2, 'Git', 8)

student_1.rate_hw(best_lecturer_3, 'Python', 7)
student_1.rate_hw(best_lecturer_3, 'Python', 8)
student_1.rate_hw(best_lecturer_3, 'Python', 9)

student_2.rate_hw(best_lecturer_1, 'Python', 10)
student_2.rate_hw(best_lecturer_1, 'Python', 10)
student_2.rate_hw(best_lecturer_1, 'Python', 10)

student_2.rate_hw(best_lecturer_2, 'Git', 10)
student_2.rate_hw(best_lecturer_2, 'Git', 8)
student_2.rate_hw(best_lecturer_2, 'Git', 9)

student_2.rate_hw(best_lecturer_3, 'Python', 10)
student_2.rate_hw(best_lecturer_3, 'Python', 10)
student_2.rate_hw(best_lecturer_3, 'Python', 10)

student_3.rate_hw(best_lecturer_1, 'Python', 10)
student_3.rate_hw(best_lecturer_1, 'Python', 10)
student_3.rate_hw(best_lecturer_1, 'Python', 10)

student_3.rate_hw(best_lecturer_2, 'Git', 10)
student_3.rate_hw(best_lecturer_2, 'Git', 10)
student_3.rate_hw(best_lecturer_3, 'Git', 10)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)

cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 10)

cool_reviewer_1.rate_hw(student_1, 'Git', 10)
cool_reviewer_1.rate_hw(student_1, 'Git', 10)
cool_reviewer_1.rate_hw(student_1, 'Git', 10)

cool_reviewer_1.rate_hw(student_2, 'Python', 10)
cool_reviewer_1.rate_hw(student_2, 'Python', 10)
cool_reviewer_1.rate_hw(student_2, 'Python', 10)

cool_reviewer_1.rate_hw(student_2, 'Git', 10)
cool_reviewer_1.rate_hw(student_2, 'Git', 10)
cool_reviewer_1.rate_hw(student_2, 'Git', 10)

cool_reviewer_1.rate_hw(student_3, 'Python', 10)
cool_reviewer_1.rate_hw(student_3, 'Python', 10)
cool_reviewer_1.rate_hw(student_3, 'Python', 10)

cool_reviewer_1.rate_hw(student_3, 'Git', 10)
cool_reviewer_1.rate_hw(student_3, 'Git', 10)
cool_reviewer_1.rate_hw(student_3, 'Git', 10)

cool_reviewer_2.rate_hw(student_1, 'Python', 8)
cool_reviewer_2.rate_hw(student_1, 'Python', 7)
cool_reviewer_2.rate_hw(student_1, 'Python', 9)

cool_reviewer_2.rate_hw(student_1, 'Git', 8)
cool_reviewer_2.rate_hw(student_1, 'Git', 7)
cool_reviewer_2.rate_hw(student_1, 'Git', 9)

cool_reviewer_2.rate_hw(student_2, 'Python', 8)
cool_reviewer_2.rate_hw(student_2, 'Python', 7)
cool_reviewer_2.rate_hw(student_2, 'Python', 9)

cool_reviewer_2.rate_hw(student_2, 'Git', 8)
cool_reviewer_2.rate_hw(student_2, 'Git', 7)
cool_reviewer_2.rate_hw(student_2, 'Git', 9)

cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)

cool_reviewer_2.rate_hw(student_3, 'Git', 8)
cool_reviewer_2.rate_hw(student_3, 'Git', 7)
cool_reviewer_2.rate_hw(student_3, 'Git', 9)

"""Как это делать?"""
print(f'List of students:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

print(f'List of lecturers:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()

print(f'Сравнение студентов по средним оценкам за домашние задания: '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

print(f'Сравнение лекторов по средним оценкам за лекции: '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

student_list = [student_1, student_2, student_3]

lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def student_rating(student_list, course_name):

    suma = 0
    count = 0
    for stud in student_list:
        if course_name in stud.courses_in_progress:
            suma += stud.average_rating
        count += 1
        average_for_all = suma / count
        return f'{average_for_all:.2f}'

def lecturer_rating(lecturer_list, course_name):

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if course_name in lect.courses_attached:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return f'{average_for_all:.2f}'

print(f"Avarage grade for all students on course  {'Python'}: {student_rating(student_list, 'Python')}")
print()

print(f"Avarage grade for all students on course {'Git'}: {student_rating(student_list, 'Git')}")
print()

print(f"Avarage grade for all lectures on course {'Pytnon'}: {lecturer_rating(lecturer_list, 'Python')}")
print()

print(f"Avarage grade for all lectures on course {'Git'}: {lecturer_rating(lecturer_list, 'Git')}")
print()