from django.db import models

# Create your models here.
class service_request(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone= models.CharField(max_length=10)
    request_type=models.CharField(max_length=100)
    details=models.TextField(max_length=200)
    attachment=models.FileField(upload_to='attachment/', blank=True, null=True )
    submit=models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    
    
    def __str__(self):
        return self.name
    
    
    
    