from django.db import models


# Create your models here.

class login_table(models.Model):
    Username= models.CharField(max_length=100)
    Password= models.CharField(max_length=100)
    type= models.CharField(max_length=60)

class Policy_table(models.Model):
    Policyname= models.CharField(max_length=100)
    Policydetails= models.CharField(max_length=500)
    Date= models.DateField()
    type= models.CharField(max_length=60)
    # premium=models.BigIntegerField()


class Premium_Details_table(models.Model):
    POLICY= models.ForeignKey(Policy_table,on_delete=models.CASCADE)
    minage= models.CharField(max_length=500)
    maxage= models.CharField(max_length=500)
    premium_amount=models.BigIntegerField()


class vehicle_premium_table(models.Model):
    POLICY = models.ForeignKey(Policy_table, on_delete=models.CASCADE)
    model=models.CharField(max_length=100)
    year=models.DateField()
    premium_amount = models.BigIntegerField()


class Policy_details_table(models.Model):
    POLICY=models.ForeignKey(Policy_table,on_delete=models.CASCADE)
    min_age=models.IntegerField()
    max_age=models.IntegerField()
    Type=models.CharField(max_length=100)
    Dependents_count=models.IntegerField()
    Dependents_agelimit=models.CharField(max_length=100)

class Agent_table(models.Model):
    Name= models.CharField(max_length=100)
    Place= models.CharField(max_length=100)
    Post= models.CharField(max_length=100)
    Pin= models.BigIntegerField()
    Phone= models.BigIntegerField()
    Email= models.CharField(max_length=100)
    Dob= models.CharField(max_length=100)
    Photo= models.FileField()
    LOGIN= models.ForeignKey(login_table, on_delete=models.CASCADE)

class User_table(models.Model):
    LOGIN= models.ForeignKey(login_table, on_delete=models.CASCADE)
    Firstname= models.CharField(max_length=100)
    Lastname= models.CharField(max_length=100)
    Gender= models.CharField(max_length=100)
    Place= models.CharField(max_length=100)
    Post= models.CharField(max_length=100)
    Dob= models.DateField()
    Phone= models.BigIntegerField()
    Pin= models.BigIntegerField()
    Email= models.CharField(max_length=100)
    Photo= models.FileField()

class Request_table(models.Model):
    Date= models.DateField()
    Status= models.CharField(max_length=100)
    USERID= models.ForeignKey(User_table, on_delete=models.CASCADE)
    POLICY= models.ForeignKey(Policy_table, on_delete=models.CASCADE)

class family_table(models.Model):
    name=models.CharField(max_length=100)
    REQUEST=models.ForeignKey(Request_table,on_delete=models.CASCADE)
    dob=models.DateField()
    id_proof=models.FileField()
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    relation=models.CharField(max_length=100)

class vehicle_table(models.Model):
    REQUEST=models.ForeignKey(Request_table,on_delete=models.CASCADE)
    vehicle_type=models.CharField(max_length=100)
    vehicle_no=models.CharField(max_length=100)
    rcbook=models.FileField()

class payment_table(models.Model):
    Date= models.DateField()
    Amount= models.BigIntegerField()
    USER= models.ForeignKey(User_table, on_delete=models.CASCADE)
    POLICY= models.ForeignKey(Policy_table, on_delete=models.CASCADE)

class Assign_table(models.Model):
    Date= models.DateField()
    Status= models.CharField(max_length=100)
    AGENT=  models.ForeignKey(Agent_table, on_delete=models.CASCADE)
    REQUEST= models.ForeignKey(Request_table, on_delete=models.CASCADE)

class Claim_request_table(models.Model):
    Reason= models.CharField(max_length=100)
    status= models.CharField(max_length=100)
    Date= models.DateField()
    Documents= models.FileField()
    ASSIGN= models.ForeignKey(Assign_table, on_delete=models.CASCADE)

class Claim_table(models.Model):
    Date= models.DateField()
    CLAIM_REQ= models.ForeignKey(Claim_request_table, on_delete=models.CASCADE)
    claimamount= models.BigIntegerField()
    Photo=models.FileField()

class Feedback_table(models.Model):
    Feedback= models.CharField(max_length=200)
    Date= models.DateField()
    Rating= models.CharField(max_length=200)
    USER= models.ForeignKey(User_table, on_delete=models.CASCADE)

class Complaint_table(models.Model):
    Complaint= models.CharField(max_length=200)
    Reply= models.CharField(max_length=200)
    Date= models.DateField()
    USER= models.ForeignKey(User_table, on_delete=models.CASCADE)

class Chat_table(models.Model):
    Message= models.CharField(max_length=200)
    Date= models.DateField()
    FromID= models.ForeignKey(login_table, on_delete=models.CASCADE, related_name='FromID')
    ToID= models.ForeignKey(login_table, on_delete=models.CASCADE, related_name='ToID')


