from abc import ABC, abstractmethod
from datetime import datetime
class Person():
    def __init__(self):
        self.role=None
        self.profile_approved=False
        self.is_admin=False
    def assign_values(self):
        self.first_name=self.get_first_name()
        self.middle_name=self.get_middle_name()
        self.last_name=self.get_last_name()
        self.personal_id=self.get_personal_id()
        self.contact_num=self.get_contact_num()
        self.email=self.get_email()
        self.date_of_birth=self.get_date_of_birth()
        #//////////////////////////////////////////////////
        self.profile_approved=self.get_profile_approved()
        self.age=self.get_age()
        self.profile_id=self.get_id()
        self.role=self.get_role()
    
    # def generate_id(self):
    #     pass
    
    # def view_profile():
    #     pass
    
    #==========setters & getters=========
    def get_is_admin(self):
        return self.is_admin
    #==================================
    def get_role(self):
        return self.role
    #===========f-name===========
    def set_first_name(self,f_name):
        self.first_name=f_name
    
    def get_first_name(self):
        return self.first_name
    #=============================
    
    #=========m-name=============
    def set_middle_name(self,m_name):
        self.middle_name=m_name
    
    def get_middle_name(self):
        return self.middle_name
    #===========================
    
    #========l-name=============
    def set_last_name(self,l_name):
        self.last_name=l_name
    
    def get_last_name(self):
        return self.last_name
    #===========================
    
    #=========personal_id=========
    def set_personal_id(self,personal_id):
        self.personal_id=personal_id
    
    def get_personal_id(self):
        return self.personal_id
    #===========================
    
    #========contact_num=========
    def set_contact_num(self,contact_num):
        self.contact_num=contact_num
    
    def get_contact_num(self):
        return self.contact_num
    #==============================
    
    #==========e-mail=============
    def set_email(self,email):
        self.email=email
    
    def get_email(self):
        return self.email
    #===============================
    
    #=========profile_approved========
    def get_profile_approved(self):
        return self.profile_approved
    #==================================
    
    #===========date_of_birth==========
    def set_date_of_birth(self,date_of_birth:str):
        self.date_of_birth=date_of_birth
    
    def get_date_of_birth(self):
        return self.date_of_birth
    #======================================
    
    #===========ID====================
    def get_id(self):
        return self.profile_id
    #============age=====================
    def calc_age(self):
        today = datetime.now()
        birthdate= datetime.strptime(str(self.get_date_of_birth()), '%m/%d/%Y') #the format will be based on html form
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    
    def get_age(self):
        age=self.calc_age()
        return age

#================================End of Person class==============================================


class Student(Person):
    student_count=0

    def __init__(self):
        super().__init__()
        Student.student_count+=1
        self.courses_enrolled=set()
        self.labs_taking=set()
        self.current_hours=0
        self.max_hours=18
        self.role="student"
        self.profile_id=Student.student_count
        self.is_admin=False
        self.profile_approved=False
        

        
        
        
    
    
#==================setters & getters=======================
    def assign_values(self):
        return super().assign_values()
    
#==========================================================
    
    
#===================coursed enrolled========================
    def enroll_in_course(self,course):
        if self.current_hours+course.get_course_hours()<=self.max_hours:
            self.courses_enrolled.add(course.get_course_id()) # here we are storing courses as the whole object so we can use its attributes & methods
            self.current_hours+=course.get_course_hours()
            if course.is_with_lab:
                self.labs_taking.add(course.get_lab_id())
            professor=course.get_professor_teaching_course()
            assistant=course.get_assistant_giving_lab()
        #add student who enrolled the course in course set 
            for enrolled_course in self.courses_enrolled:
                if enrolled_course==course.get_course_id():
                    course.student_enrolled_course.add(self)
                    professor.get_all_students_teaching().setdefault(course.get_course_id(), set()).add(self)
                    if course.is_with_lab:
                        assistant.get_all_students_teaching().setdefault(course.get_lab_id(), set()).add(self)
                        
                else:
                    pass
        
        else:
            pass
    
    def get_enrolled_courses(self):
        return self.courses_enrolled
#======================level===================================
    def set_level(self,level):
        self.level=level
        
    def get_level(self):
        return self.level
        
#========================department======================
    def set_department(self,department):
        if self.get_level()==1 or self.get_level()==2:
            self.department="general"
        else:
            self.department=department

    def get_department(self):
        return self.department
#=======================end of Student class=====================

class Instructor(Person):
    is_admin=False
    
    def __init__(self):
        super().__init__()
        self.is_admin=False
        self.profile_approved=False
        
#==================setters & getters=======================
    def assign_values(self):
        return super().assign_values()
#================department==============================
    def set_department(self,department):
        self.department=department

    def get_department(self):
        return self.department
    
#=======================salary======================
    def set_salary(self,salary):
        self.salary=salary
    
    def get_salary(self):
        return self.salary
#===================end of class Instructor============
class Admin(Person):
    
    def __init__(self):
        self.is_admin=True
        Admin.profile_approved=True
        self.role="admin"
#=============setters & getters=================
    def assign_values(self):
        return super().assign_values()
        
        
        
        
class Professor(Instructor):
    professor_count=0
    
    def __init__(self,email):
        super().__init__()
        Professor.professor_count+=1
        self.courses_teaching=set()
        self.students_teaching={}
        self.role="professor"
        self.profile_id=Professor.professor_count
        self.email = email
        self.tasks = []

    def add_task(self, task_description, deadline, file):
        task = {'description': task_description, 'deadline': deadline, 'file_path': None}
        self.tasks.append(task)
        self.upload_task(len(self.tasks) - 1, file)

    def upload_task(self, task_index, file):
        if file.filename != '' and file.content_length <= 5 * 1024 * 1024:
            file_path = f"static/uploads/task_{task_index}_{file.filename}"
            file.save(file_path)
            self.tasks[task_index]['file_path'] = file_path

    

#===============setters and getters========================
    def assign_values(self):
        return super().assign_values()
#================courses teaching=======================
    def add_courses_teaching(self,course):
        self.courses_teaching.add(course)
        self.students_teaching[course]=set(course.get_students_enrolled_course())
    
    def get_courses_teaching(self):
        return self.courses_teaching
    
#====================Students he is teaching======================
    def get_all_students_teaching(self): #returns full dictionary of all students
        return self.students_teaching

    
    
    def get_students_teaching(self,course): #returns students of only one course
        return self.students_teaching[course]
        


class Professor_asst(Instructor):
    professor_asst_count=0
    def __init__(self):
        super().__init__()
        Professor_asst.professor_asst_count+=1
        self.labs_giving=set()
        self.students_teaching={}
        self.role="assistant"
        self.profile_id=Professor_asst.professor_asst_count
        
    #===============setters and getters========================
    def assign_values(self):
        return super().assign_values()
#================labs teaching=======================
    def add_labs_giving(self,lab):
        self.labs_giving.add(lab)
        self.students_teaching[lab]=set(lab.get_students_enrolled_course())
    
    def get_labs_giving(self):
        return self.labs_giving
    
#=========================students he is giving labs=================
    def get_all_students_teaching(self): #returns full dictionary of all students
        return self.students_teaching
        
    def get_students_teaching(self,lab): #returns students of only one lab
        return self.students_teaching[lab]
        
        

class Courses():
    courses_num=0
    labs_num=0
    def __init__(self):
        Courses.courses_num+=1
        self.professor_teaching_course=None
        self.assistant_giving_lab=None
        self.student_enrolled_course=set()
        
#assign unique id for course and its lab
        self.course_id=Courses.courses_num
        self.lab_id=Courses.courses_num
        
        
        
#=======================setters & getters===================

    def get_course_id(self):
        return self.course_id
    
    
    def get_lab_id(self):
        return self.lab_id




#===========================================================
    def add_new_course(self,course_name,course_hours,is_with_lab):
        #here will be a check sentence for is_admin
        self.course_name=course_name
        self.course_hours=course_hours
        self.is_with_lab=is_with_lab
        Courses.labs_num+=int(self.is_with_lab)
        
        
    
    def get_course_name(self):
        return self.course_name
    
    def get_course_hours(self):
        return self.course_hours
    
    def get_course_lab(self):
        return self.is_with_lab
#=====================enrolling students=====================================
    def students_enrolled_course(self,student):
        for course in student.courses_enrolled:
            if course.lower()==self.get_course_name().lower():
                self.student_enrolled_course.add(student)
            else:
                pass
        
    def get_students_enrolled_course(self):
        return self.student_enrolled_course
    
#=======================professor teaching====================================
    def set_professor_teaching_course(self,professor):
        if self.professor_teaching_course==None:
            self.professor_teaching_course=professor
            professor.add_courses_teaching(self)
        else:
            self.professor_teaching_course.get_courses_teaching().remove(self)
            self.professor_teaching_course.get_students_teaching().pop(self)
            self.professor_teaching_course=professor
            professor.add_courses_teaching(self)

    def get_professor_teaching_course(self):
        return self.professor_teaching_course

#==================================================================================

#==========================assistant giving lab===================================
    def set_assistant_giving_lab(self,assistant):
        if self.is_with_lab:
            if self.assistant_giving_lab==None:
                self.assistant_giving_lab=assistant
            else:
                self.assistant_giving_lab.get_labs_giving().remove(self)
                self.assistant_giving_lab=assistant
                assistant.add_labs_giving(self)
        else:
            pass
    
    def get_assistant_giving_lab(self):
        return self.assistant_giving_lab