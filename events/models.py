from django.db import models


# Create your models here.
class EventsList(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='eventimg/',blank=True,null=True)
    
    # indoor = models.ImageField(upload_to='indoorimg/',blank=True,null=True)
    
    # outdoor = models.ImageField(upload_to='outdoorimg/',blank=True,null=True)
        
    
    def __str__(self):
        return self.name
    
class EventType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class indoorImages(models.Model):
    eventName = models.ForeignKey(EventsList,related_name='eventlists',on_delete=models.CASCADE)
    event_Type = models.ForeignKey(EventType,related_name='eventTypes',on_delete=models.CASCADE)
    indoorimg = models.ImageField(upload_to='indoorimg',blank=True,null=True)
    
class outdoorImages(models.Model):
    event_name = models.ForeignKey(EventsList,related_name='eventLists',on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType,related_name='eventtypes',on_delete=models.CASCADE)
    outdoorimg = models.ImageField(upload_to='outdoorimg',blank=True,null=True)    

class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time_slot = models.CharField(max_length=50, choices=[
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
    ('night', 'Night')
])
    
    total_persons = models.IntegerField()
    venue_type = models.CharField(max_length=50, choices=[('indoor', 'Indoor'), ('outdoor', 'Outdoor')])  # if you're using this
    menu_type = models.CharField(max_length=50, choices=[
        ('veg150', 'Veg Menu 150'),
        ('nonveg200', 'Non-Veg Menu 200')
    ])
    event = models.ForeignKey(EventsList, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

# models.py
class VegMenu150(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class NonVegMenu200(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
