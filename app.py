from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

class Person():
    def __init__(self):
        pass
        
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
    
    def generate_id(self):
        pass
    
    def view_profile():
        pass
    
    #==========setters & getters=========
    
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
        birthdate= datetime.strptime(str(self.get_date_of_birth()), '%d/%m/%Y')
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    
    def get_age(self):
        age=self.calc_age()
        return age
    

app = Flask(__name__)


class Instructor(Person):
    is_admin = False

    def __init__(self):
        pass

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



from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

class Professor(Instructor):
    def __init__(self, email):
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

professor = Professor(email="professor@example.com")

@app.route('/')
def tasks():
    return render_template('tasks.html', professor=professor)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form.get('task_description')
    deadline = datetime.strptime(request.form.get('deadline'), '%Y%d%mT%H:%M')
    file = request.files['file']
    
    professor.add_task(task_description, deadline, file)
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    app.run(debug=True)


