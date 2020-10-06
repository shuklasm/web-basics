import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *

faker = Faker()
def populate(n):
    for i in range(n):
        feno=randint(111,999)
        fename = faker.name()
        fesal=randint(1000,10000)
        feaddr=faker.city()
        emp_record = Employee.objects.get_or_create(eno = feno,ename = fename,
        esal = fesal,eaddr = feaddr)

populate(30)      
