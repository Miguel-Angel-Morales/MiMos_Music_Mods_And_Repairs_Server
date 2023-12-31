from django.db import models
from datetime import date

class ServiceTicket(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name='submitted_tickets')
    employee = models.ForeignKey("Employee", null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_tickets')
    instrument = models.ForeignKey("Instrument", on_delete=models.CASCADE, related_name='chosen_instrument')
    description = models.CharField(max_length=20000, default="")
    notes = models.CharField(max_length=20000, default="")
    date = models.DateField(default= date.today)
    modification = models.BooleanField(default=False)  # Default value can be True or False
    repair = models.BooleanField(default=False)
    setup = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)