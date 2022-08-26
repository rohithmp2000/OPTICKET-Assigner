from http.client import HTTPResponse
from django.shortcuts import render,redirect
from app.models import tbl_dept,tbl_complaint,tbl_staff,tbl_doctor,tbl_login,tbl_patient,tbl_opdays,tbl_opticket,tbl_diagnosis,tbl_labtest,tbl_medicine,tbl_leave
from django.core.files.storage import FileSystemStorage
import datetime
from django.core.mail import send_mail
def form(request):  
    return render(request,"form.html")
def header(request):  
    return render(request,"header.html")
def home(request):  
    return render(request,"index.html")
def adminheader(request):  
    return render(request,"adminheader.html")
def doctorheader(request):  
    return render(request,"doctorheader.html")
def labheader(request):  
    return render(request,"labheader.html")
def patientheader(request):  
    return render(request,"patientheader.html")
def publicheader(request):  
    return render(request,"publicheader.html")
def adminhome(request):  
    return render(request,"adminhome.html")
def doctorhome(request):  
    return render(request,"doctorhome.html")
def labhome(request):  
    return render(request,"labhome.html")
def patienthome(request):  
    return render(request,"patienthome.html")
def appointment(request):  
    return render(request,"appointment.html")
def adddept(request):  
    return render(request,"adddept.html")
def registercomplaint(request):  
    return render(request,"registercomplaint.html")
def patientregister(request):  
    return render(request,"patientregister.html")
def publichome(request):  
    return render(request,"publichome.html")
def adddept1(request):
    if request.method == 'POST':
        data = tbl_dept()
        data.Dept_id="na"
        data.Department=request.POST.get('deptname')
        data.Description=request.POST.get('description')
        data.save()
        data.Dept_id = "DEPT_00" + str(data.id)
        data.save()



        return render(request,"adddept.html")
def staffappoint(request):
    if request.method == 'POST':
        data = tbl_staff()
        data.staff_id="na"
        data.name=request.POST.get('name')
        data.address=request.POST.get('address')
        data.phoneno=request.POST.get('phoneno')
        data.email=request.POST.get('email')
        data.gender=request.POST.get('Gender')
        data.category=request.POST.get('category')
        data.doj=request.POST.get('doj')
        data.remark=request.POST.get('remark')
        data.age=request.POST.get('age') 
        data.status="not"


        data.save()


        category=request.POST.get('category')
        data.staff_id = "staff_00" + str(data.id)
        data.save()
        if category=="labstaff":
            data1=tbl_login()
            data1.user_id="staff_00" + str(data.id)
            data1.password=request.POST.get('phoneno')
            data1.category="lab"
            data1.save()



        return render(request,"appointment.html")
def regcomplaint(request):
    if request.method == 'POST':
        data = tbl_complaint()
        data.complaint_id="na"
        data.patient_id=request.POST.get('patientid')
        data.complaint=request.POST.get('complaint')
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.complaint_date=time1
        
        data.save()
        data.complaint_id = "CMP_00" + str(data.id)
        data.save()
        return render(request,"registercomplaint.html")

def remove_dept(request):
    items = tbl_dept.objects.all()
    return render(request,"remove_dept.html",{'items':items })

def remove_dept1(request,id):  
    items = tbl_dept.objects.get(id=id) 
    items.delete()
    return redirect('/remove_dept')

def regpatient(request):
    if request.method == 'POST':
        data = tbl_patient()
        data.patient_id="na"
        data.name=request.POST.get('name')
        data.age=request.POST.get('age')
        data.gender=request.POST.get('gender')
        data.address=request.POST.get('address')
        data.phone_no=request.POST.get('phone')
        data.email=request.POST.get('email')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.photo=uploaded_file_url
        data.status="pending"
        data.save()
        data.patient_id = "PATIENT_00" + str(data.id)
        data.save()
        data1=tbl_login()
        data1.user_id="PATIENT_00" + str(data.id)
        data1.password=request.POST.get('phone')
        data1.category="patient"
        data1.save()
        send_mail('username and password','username is'+'PATIENT_00' + str(data.id)+'password is'+request.POST.get('phone'),'from@example.co',[request.POST.get('email'),])
        
        return render(request,"patientregister.html")

def givecomplaint1(request):
    uid=request.session['uid']
    return render(request,"givecomplaint.html",{'uid':uid})

def givecomplaint(request):
    if request.method == 'POST':
        data = tbl_complaint()
        data.complaint_id="na"
        data.patient_id=request.POST.get('patientid')
        data.complaint=request.POST.get('complaint')
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.complaint_date=time1
        data.save()
        data.complaint_id = "CMP_00" + str(data.id)
        data.save()
        return render(request,"patienthome.html")

def searchdept(request):
    items = tbl_dept.objects.all()
    return render(request,"searchdept.html",{'items':items })

def searchdept1(request):
    items = tbl_dept.objects.all()
    return render(request,"searchdept1.html",{'items':items })


def removestaff(request):
    items = tbl_staff.objects.all()
    return render(request,"removestaff.html",{'items':items })

def removestaff1(request,id):  
    items = tbl_staff.objects.get(id=id) 
    items.delete()
    return redirect('/removestaff')

def drallotment(request):
    items = tbl_staff.objects.filter(category="doctor").filter(status="not")
    return render(request,"drallotment.html",{'items':items })

def doctorallotment1(request,id):
    items=tbl_staff.objects.get(id=id)
    data= tbl_dept.objects.all()
    return render(request,"drallotment1.html",{'items':items,'data':data })

def drallotment3(request):
    if request.method == 'POST':
        data = tbl_doctor()
        data.doctor_id="na"
        data.name=request.POST.get('name')
        data.staff_id=request.POST.get('staff_id')
        data.dept_id=request.POST.get('department_id')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.photo=uploaded_file_url
        data.description=request.POST.get('description')
        data.phoneno=request.POST.get('phoneno')
        data.status="active"
        data.save()
        data.doctor_id = "DOCTOR_00" + str(data.id)
        data.save()
        data1=tbl_login()
        data1.user_id="DOCTOR_00" + str(data.id)
        data1.password=request.POST.get('phoneno')
        data1.category="doctor"
        data1.save()
        data2=tbl_staff.objects.get(staff_id=request.POST.get('staff_id'))
        data2.status="ok"
        data2.save()
        return render(request,"drallotment1.html")
def login1(request):  
    return render(request,"login.html")   
def login2(request):  
    if request.method == 'POST':
        data = tbl_login.objects.all()
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        flag = 0
        for d in data:
            if uname == d.user_id and pwd == d.password:
                type = d.category
                request.session['uid'] = uname
                flag = 1
                if type == "admin":
                    return redirect('/adminhome/')
                elif type == "doctor":
                    return redirect('/doctorhome/')
                elif type == "patient":
                    return redirect('/patienthome/')
                elif type == "lab":
                    return redirect('/labhome/')
                else:
                    return HTTPResponse("Invalid acc type.")
        if flag == 0:
            return HTTPResponse("Invalid user.") 

def opallot1(request):
    items = tbl_dept.objects.all()
    return render(request,"opallot.html",{'items':items })   

def opallot3(request,id):
    items = tbl_doctor.objects.filter(dept_id=id)
    return render(request,"oplist.html",{'items':items }) 

def opdays4(request):
    if request.method == 'POST':
        data = tbl_opdays()
        data.op_id="na"
        data.doctor_id=request.POST.get('doctor_id')
        data.dept_id=request.POST.get('dept_id')
        data.days=request.POST.get('days')
        data.save()
        data.op_id = "OP_00" + str(data.id)
        data.save()
        return redirect('/opallot1')

def opdays1(request,id):
    items = tbl_doctor.objects.get(id=id)
    return render(request,"opdays.html",{'items':items })

def viewdoctor(request,id):
    items = tbl_doctor.objects.filter(dept_id=id)
    return render(request,"viewdoctor.html",{'items':items }) 



def viewop(request,id):
    items = tbl_doctor.objects.filter(doctor_id=id)
    return render(request,"viewop.html",{'items':items })


def viewdoctor1(request,id):
    items = tbl_doctor.objects.filter(dept_id=id)
    return render(request,"viewdoctor1.html",{'items':items }) 



def viewop1(request,id):
    items = tbl_opdays.objects.filter(doctor_id=id)
    return render(request,"viewop1.html",{'items':items })
def collectop(request,id):    
    items = tbl_opdays.objects.get(id=id)
    uid=request.session['uid']
    return render(request,"opticket.html",{'items':items,'uid':uid})


def collectop1(request):
    if request.method == 'POST':
        data = tbl_opticket()
        data.doctor_id=request.POST.get('doctor_id')
        data.patient_id=request.POST.get('patient_id')
        data.op_id="na"
        data.dept_id=request.POST.get('dept_id')
        data.opday=request.POST.get('opday')
        data.date=request.POST.get('date')
        data.time=request.POST.get('time')
        data.status="pending"
        data.save()
        data.op_id = "OP_00" + str(data.id)
        data.save()
        return render(request,"patienthome.html")

def opid(request):
    uid=request.session['uid']
    items = tbl_opticket.objects.filter(doctor_id=uid).filter(status="pending")
    return render(request,"opid.html",{'items':items }) 

def patdetails(request,id):
    
    request.session['pid']=id
    items = tbl_patient.objects.filter(patient_id=id)
    return render(request,"patdetails.html",{'items':items }) 

def diagnosis(request,id):  
    data=tbl_opticket.objects.get(patient_id=id)
    return render(request,"diagnosis.html",{'data':data})

def diagnosis1(request):
    if request.method == 'POST':
        data = tbl_diagnosis()
        data.doctor_id=request.POST.get('doctor_id')
        data.patient_id=request.POST.get('patient_id')
        data.diagnosis_id="na"
        data.op_id=request.POST.get('op_id')
        data.diagnosis=request.POST.get('diagnosis')
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.date=time1
        data.status="active"
        data.save()
        data.diagnosis_id = "DG_00" + str(data.id)
        did="DG_00" + str(data.id)
        data.save()
        ptid=request.POST.get('patient_id')
        return render(request,"medicine.html",{'did':did,'ptid':ptid})

def labtest(request,id): 
    data=tbl_opticket.objects.get(patient_id=id) 
    return render(request,"labtest.html",{'data':data})

def labtest1(request):
    if request.method == 'POST':
        data = tbl_labtest()
        data.test_id="na"
        data.op_id=request.POST.get('op_id')
        data.patient_id=request.POST.get('patient_id')
        data.testname=request.POST.get('testname')
        data.status="active"
        data.save()
        data.test_id = "TEST_00" + str(data.id)
        data.save()
        items = tbl_patient.objects.filter(patient_id=request.POST.get('patient_id'))
        return render(request,"patdetails.html",{'items':items }) 


def medicine1(request):
    if request.method == 'POST':
        data = tbl_medicine()
        data.rate=request.POST.get('rate')
        data.medicine_id=request.POST.get('medicine_id')
        data.diagnosis_id=request.POST.get('diagnosis_id')
        data.patient_id=request.POST.get('patient_id')
        data.medicinename=request.POST.get('medicinename')
        data.dosage=request.POST.get('dosage')
        data.status="active"
        data.save()
        pid=request.session['pid']
        items = tbl_patient.objects.filter(patient_id=pid)
        items1 = tbl_opticket.objects.get(patient_id=request.POST.get('patient_id'))
        items1.status="completed"
        items1.save()
        
        return render(request,"patdetails.html",{'items':items }) 
        
def leave(request): 
    uid=request.session['uid']
    return render(request,"leave.html",{'uid':uid})

def leave1(request):
    if request.method == 'POST':
        data = tbl_leave()
        data.doctor_id=request.POST.get('doctor_id')
        data.date=request.POST.get('date')
        data.days=request.POST.get('days')
        data.save()
        return render(request,"doctorhome.html")
def changestaff1(request,id):  
    items = tbl_staff.objects.get(id=id) 
    return render(request,"changestaff.html",{'items':items})
def changestaff2(request):  
    items = tbl_staff.objects.get(staff_id=request.POST.get('staff_id')) 
    items.phoneno=request.POST.get('phoneno')
    items.email=request.POST.get('email')
    items.save()
    return render(request,"adminhome.html")  
def logout(request): 
    return render(request,"index.html",)   
def viewcomplaint(request):  
    items = tbl_complaint.objects.all()
    return render(request,"viewcomplaint.html",{'items':items})  
def report2(request):
    items = tbl_doctor.objects.all()
    return render(request,"report2.html",{'items':items })    
def report1(request):
    items = tbl_patient.objects.all()
    return render(request,"report1.html",{'items':items })     
def viewtest(request):
    items = tbl_labtest.objects.filter(status="active")
    return render(request,"viewtest.html",{'items':items })    
def viewtest1(request,id):
    items = tbl_labtest.objects.get(id=id)
    return render(request,"viewtest1.html",{'items':items })   
def viewtest2(request,id):
    items = tbl_labtest.objects.get(id=id)
    items.result=request.POST.get('result')
    items.status="ok"
    items.save()
    return render(request,"labhome.html")  
def viewresult(request):
    items = tbl_labtest.objects.filter(status="ok").filter(patient_id=request.session['uid'])
    items1 = tbl_diagnosis.objects.filter(status="active").filter(patient_id=request.session['uid'])
    items2 = tbl_medicine.objects.filter(status="active").filter(patient_id=request.session['uid'])
    return render(request,"viewresult.html",{'items':items,'items1':items1,'items2':items2})   
def viewresultdoctor(request):
    uid=request.session['uid']
    items = tbl_opticket.objects.filter(doctor_id=uid)
    return render(request,"viewresultdoctor.html",{'items':items }) 
def viewresultdoctor1(request,id):
    items = tbl_labtest.objects.filter(status="ok").filter(patient_id=id)
    items1 = tbl_diagnosis.objects.filter(status="active").filter(patient_id=id)
    items2 = tbl_medicine.objects.filter(status="active").filter(patient_id=id)
    return render(request,"viewresultdoctor1.html",{'items':items,'items1':items1,'items2':items2})    
def confirm(request):
    items = tbl_labtest.objects.filter(status="ok").filter(patient_id=request.session['uid'])
    for ct in items:
        ct.status="completed"
        ct.save()
    items1 = tbl_diagnosis.objects.filter(status="active").filter(patient_id=request.session['uid'])
    for ct in items1:
        ct.status="completed"
        ct.save()
    items2 = tbl_medicine.objects.filter(status="active").filter(patient_id=request.session['uid'])
    for ct in items2:
        ct.status="completed"
        ct.save()
    return render(request,"patienthome.html")         

                     
        









  




        
# Create your views here.
