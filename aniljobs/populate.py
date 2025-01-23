import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aniljobs.settings')
import django
django.setup()

from testapp.models import BangaloreJobs
from faker import Faker
from random import *
faker = Faker()
def phonenumbergen():
	d1 = randint(6,9)
	num = '' + str(d1)
	for i in range(9):
		num += str(randint(0,9))
	return int(num)
def populate(n):
	for i in range(n):
		fdate = faker.date()
		fcompany = faker.company()
		ftitle = faker.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
		feligibility = faker.random_element(elements=('B.Tech','M.Tech','MCA','Mahesh Sir Student'))
		femail = faker.email()
		fphonenumber = phonenumbergen()
		faddress = faker.address()
		bangalore_jobs_record = BangaloreJobs.objects.get_or_create(
			date = fdate,
			company = fcompany,
			title = ftitle,
			eligibility = feligibility,
			address = faddress,
			email = femail,
			phonenumber = fphonenumber
			)
def populate(n):
	for i in range(n):
		fdate = faker.date()
		fcompany = faker.company()
		ftitle = faker.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
		feligibility = faker.random_element(elements=('B.Tech','M.Tech','MCA','Mahesh Sir Student'))
		femail = faker.email()
		fphonenumber = phonenumbergen()
		faddress = faker.address()
		bangalore_jobs_record = BangaloreJobs.objects.get_or_create(
			date = fdate,
			company = fcompany,
			title = ftitle,
			eligibility = feligibility,
			address = faddress,
			email = femail,
			phonenumber = fphonenumber
			)

n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted successfully......')

