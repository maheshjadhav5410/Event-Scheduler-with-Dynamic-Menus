from django.contrib import admin
from events.models import EventsList,EventType,indoorImages,outdoorImages,VegMenu150,NonVegMenu200

# Register your models here.
admin.site.register(EventsList)
admin.site.register(EventType)
admin.site.register(indoorImages)
admin.site.register(outdoorImages)
admin.site.register(VegMenu150)
admin.site.register(NonVegMenu200)




# admin.site.register(InDoor)
# admin.site.register(OutDoor)
