import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsproject.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *

faker = Faker()
def phonenumbergen():
    d1= randint(7,9)
    num = ''+str(d1)
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = faker.date()
        fcompany = faker.company()
        ftitle = faker.random_element(elements=('project manager','Teamlead','Software Engineer',
        'Developer'))
        feligibility = faker.random_element(elements=('B-tech','M-tech','MCA','phD'))
        faddress=faker.address()
        femail = faker.email()
        fphonenumber = phonenumbergen()
        punejobs_record = punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,
        eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)

populate(30)
