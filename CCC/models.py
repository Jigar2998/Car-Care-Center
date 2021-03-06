from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from django.utils import timezone



class customer(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=7)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/') 


    def __str__(self):
        return self.fname   


class mechanic(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    salary = models.FloatField(max_length=10)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/',null = True,blank=True) 
    

    def __str__(self):
        return self.fname


class cus_request(models.Model):
    category = models.CharField(max_length=40)
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    problem = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    cost = models.IntegerField(null = True)
    Customer = models.ForeignKey('customer',on_delete=models.CASCADE,null=True)
    Mechanic = models.ForeignKey('mechanic',on_delete=models.CASCADE,null=True)
    stat = (('Pending','Pending'),('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'),('Released','Released'))
    status = models.CharField(max_length=40,choices=stat,default='Pending',null=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class feedback(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    msg = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

class contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    msg  = models.CharField(max_length=100)

class apply_leave(models.Model):
    reason = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    stat = (('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected'))
    status = models.CharField(max_length=40,choices=stat,default='Pending',null=True)
    Mechanic = models.ForeignKey('mechanic',on_delete=models.CASCADE,null=True)
    admin_reason = models.CharField(max_length=100)

class paytm(models.Model):

    ORDER_ID = models.CharField(max_length=50)
    TXN_AMOUNT = models.CharField(max_length=30)
    BANKTXNID = models.CharField(max_length=50)
    Customer = models.ForeignKey('customer',on_delete=models.CASCADE)
    Cus_Request = models.ForeignKey('cus_request',on_delete=models.CASCADE)
    BANKNAME = models.CharField(max_length=50)
    TXNDATE = models.DateField(auto_now=True)
    stat=(('TXN_SUCCESS','TXN_SUCCESS'),('TXN_FAIL','TXN_FAIL'))
    STATUS = models.CharField(max_length=30,choices=stat,default="TXN_FAIL")

class post_name(models.Model):
    post = models.CharField(max_length=100)

    def __str__(self):
        return self.post

class job_desc(models.Model):
    image = models.ImageField()
    post_name = models.ForeignKey('post_name',on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50)
    skill = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    job_location = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)

class job_apply(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    post_name = models.ForeignKey('post_name',on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50)
    skills = models.CharField(max_length=50)
    experience = models.CharField(max_length=50,null=True)
    resume = models.FileField()


class superuser(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=7)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/',null=True,blank=True)



    #Spare Parts Sale Model

class parts_category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()

class parts_subcategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    fit_model = models.CharField(max_length=50)
    Parts_Category = models.ForeignKey('parts_category',on_delete=models.CASCADE) 
    

    def __str__(self):
        return self.name

class order_cart(models.Model):
    Parts_Sub_Category = models.ForeignKey('parts_subcategory',on_delete=models.CASCADE)
    Customer = models.ForeignKey('customer',on_delete=models.CASCADE)
    name  = models.CharField(max_length=50)
    qty = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default = 0)

class customer_order(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    oaddress = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    ordernote = models.CharField(max_length=100,null=True)
    product = models.CharField(max_length=500)
    Customer = models.ForeignKey('customer', on_delete=models.CASCADE)


