from django.db import models

class Interest(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title

class City(models.Model):
    title=models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Person(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    interest=models.ManyToManyField(Interest,related_name='person_interest')

    def __str__(self):
        return self.name

class PersonAddress(models.Model):
    person=models.OneToOneField(Person,on_delete=models.CASCADE,related_name='person_details')
    city=models.ForeignKey(City,on_delete=models.CASCADE,related_name='person_city')
    Street_address=models.CharField(max_length=50)

    def __str__(self):
      return self.person.name + "("+ self.Street_address + ")"


