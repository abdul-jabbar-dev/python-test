from inspect import getmembers


class School:
    def __init__(self, s_name, st_count, gpa_rate):
        self.name = s_name
        self.student_count = st_count
        self.gpa_rate = gpa_rate
        self.department = []

    def departments(self, dep):
        return self.department

    def add_department(self, dep):
        self.department.append(dep)
    
    def __eq__(self, o):
        return self.gpa_rate == o.gpa_rate
    
    


mist = School('MIST', 1500, 4.00)
pilot = School('pilot', 2000, 3.00)
mmsc = School('mmsc', 400, 1.50)
ssac = School('ssac', 5000, 4.00)
mist.add_department('cse')
mist.add_department('eee')
mist.add_department('architecture')

print(mist==ssac)
