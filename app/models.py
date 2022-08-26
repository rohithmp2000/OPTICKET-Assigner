
from django.db import models
class tbl_dept(models.Model):
    Dept_id = models.CharField(max_length=30)
    Department = models.CharField(max_length=40)
    Description = models.CharField(max_length=30) 
    class Meta:
         db_table = "tbl_dept"







         

class tbl_login(models.Model):
    user_id = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
    category= models.CharField(max_length=30) 
    class Meta:
         db_table = "tbl_login"

class tbl_patient(models.Model):
    patient_id = models.CharField(max_length=30)
    name= models.CharField(max_length=40)
    age= models.CharField(max_length=30) 
    gender= models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    phone_no= models.CharField(max_length=30) 
    email= models.CharField(max_length=30)
    photo= models.CharField(max_length=150)
    status= models.CharField(max_length=50)
    class Meta:
         db_table = "tbl_patient"

class tbl_complaint(models.Model):
    complaint_id = models.CharField(max_length=30)
    patient_id = models.CharField(max_length=40)
    complaint= models.CharField(max_length=30) 
    complaint_date = models.CharField(max_length=30)
    
    class Meta:
         db_table = "tbl_complaint"

class tbl_staff(models.Model):
    staff_id= models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    age= models.CharField(max_length=30) 
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    phoneno= models.CharField(max_length=30) 
    email= models.CharField(max_length=30)
    category= models.CharField(max_length=150)
    doj= models.CharField(max_length=30)
    remark= models.CharField(max_length=30)
    status=models.CharField(max_length=30)

    class Meta:
         db_table = "tbl_staff"


class tbl_doctor(models.Model):
    doctor_id= models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    staff_id= models.CharField(max_length=30) 
    dept_id= models.CharField(max_length=30)
    description= models.CharField(max_length=30) 
    photo= models.CharField(max_length=150)
    status= models.CharField(max_length=150)
    phoneno= models.CharField(max_length=30) 


    class Meta:
         db_table = "tbl_doctor"

class tbl_opdays(models.Model):
    op_id = models.CharField(max_length=30)
    doctor_id = models.CharField(max_length=40)
    dept_id = models.CharField(max_length=40)
    days= models.CharField(max_length=30) 
   
    
    class Meta:
         db_table = "tbl_opdays"

class tbl_opticket(models.Model):
    doctor_id= models.CharField(max_length=30)
    op_id= models.CharField(max_length=40)
    patient_id= models.CharField(max_length=30) 
    dept_id= models.CharField(max_length=30)
    opday= models.CharField(max_length=30) 
    date= models.CharField(max_length=150)
    status= models.CharField(max_length=150)
    time= models.CharField(max_length=30) 


    class Meta:
         db_table = "tbl_opticket"

class tbl_diagnosis(models.Model):
    diagnosis_id= models.CharField(max_length=30)
    op_id= models.CharField(max_length=40)
    patient_id= models.CharField(max_length=30) 
    doctor_id= models.CharField(max_length=30)
    date= models.CharField(max_length=150)
    diagnosis= models.CharField(max_length=150)
    status= models.CharField(max_length=50)


    class Meta:
         db_table = "tbl_diagnosis"

class tbl_labtest(models.Model):
    test_id= models.CharField(max_length=30)
    op_id= models.CharField(max_length=40)
    patient_id= models.CharField(max_length=30) 
    testname= models.CharField(max_length=30)
    result= models.CharField(max_length=150)
    status= models.CharField(max_length=150)


    class Meta:
         db_table = "tbl_labtest"

class tbl_medicine(models.Model):
    medicine_id= models.CharField(max_length=30)
    patient_id= models.CharField(max_length=30)
    diagnosis_id= models.CharField(max_length=40)
    medicinename= models.CharField(max_length=30) 
    dosage= models.CharField(max_length=30)
    rate= models.CharField(max_length=150)
    status= models.CharField(max_length=50)


    class Meta:
         db_table = "tbl_medicine"

class tbl_leave(models.Model):
    doctor_id= models.CharField(max_length=30)
    date= models.CharField(max_length=40)
    days= models.CharField(max_length=30) 



    class Meta:
         db_table = "tbl_leave"







# Create your models here.

