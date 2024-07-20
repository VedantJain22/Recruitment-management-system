from django.db import models

class PlacementDrive(models.Model):
    company_name = models.CharField(max_length=255)
    job_role = models.CharField(max_length=255)
    eligibility_criteria = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.company_name
