from django.db import models

# we represent our database structure with classes
# each class is its own tabel
# each attribute is a different field in the database

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.TextField(null=True)
    orderedItemID = models.IntegerField()
    amount = models.IntegerField()
    gender = models.TextField()

    def __str__(self):
        return self.customer