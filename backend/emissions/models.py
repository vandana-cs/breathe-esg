from django.db import models

class EmissionRecord(models.Model):

    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    ]

    REVIEW_CHOICES = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    ]

    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)

    activity_type = models.CharField(max_length=100)

    quantity = models.FloatField()

    unit = models.CharField(max_length=20)

    record_date = models.DateField()

    emissions = models.FloatField()

    suspicious = models.BooleanField(default=False)

    review_status = models.CharField(
        max_length=20,
        choices=REVIEW_CHOICES,
        default='PENDING'
    )

    raw_data = models.JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} - {self.activity_type}"