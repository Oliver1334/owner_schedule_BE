from django.db import models

class Event(models.Model):
   # Recurrence choices
    RECURRENCE_CHOICES = [
        ('NONE', 'Never'),
        ('DAILY', 'Daily'),
        ('WORKDAYS', 'Every Workday (Mon–Fri)'),
        ('WEEKLY', 'Weekly'),
        ('FORTNIGHTLY', 'Fortnightly'),
    ]

    # Event type choices
    EVENT_TYPE_CHOICES = [
        ('MEETING', 'Meeting'),
        ('1ST_APPOINTMENT', '1st Appointment'),
        ('PRESENTATION', 'Presentation'),
        ('EVENT', 'Event'),
    ]

   # Meeting type choices
    MEETING_TYPE_CHOICES = [
        ('MORNING', 'Morning Meeting'),
        ('LEADERS', 'Leaders Meeting'),
        ('CLIENT', 'Client Meeting'),
        ('OWNER', 'Owner Meeting'),
        ('OTHER', 'Other'),
    ]

    # Host options for appointments/presentations
    HOST_CHOICES = [
        ('ROBERT_MILLER', 'Robert Miller'),
        ('STIG_MILLER', 'Stig Miller'),
        ('TRACY_PEW', 'Tracy Pew'),
        ('KLAUS_NOMI', 'Klaus Nomi'),
        ('ROSE_MCDOWALL', 'Rose McDowall'),
    ]   

    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)
    recurrence_rule = models.CharField(max_length=20, choices=RECURRENCE_CHOICES, default='NONE')
    notes = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    # Type conditional fields
    meeting_type = models.CharField(max_length=20, choices=MEETING_TYPE_CHOICES, blank=True, null=True)
    host = models.CharField(max_length=20, choices=HOST_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"{self.title} on {self.start_time}"

class EventException(models.Model):
    event = models.ForeignKey(Event, related_name='exceptions', on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"Exception for {self.title} on {self.start_time}"