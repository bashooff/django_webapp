from django.db import models

# we represent our database structure with classes
# each class is its own tabel
# each attribute is a different field in the database

class Customer(models.Model):
    customer = models.CharField(max_length = 100)
    orderedItemID = models.IntegerField()
    amount = models.IntegerField()
    gender = models.TextField()

    def __str__(self):
        return self.customer