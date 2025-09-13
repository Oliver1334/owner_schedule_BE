from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} on {self.date}"

class EventException(models.Model):
    event = models.ForeignKey(Event, related_name='exceptions', on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"Exception for {self.event.title} on {self.date}"