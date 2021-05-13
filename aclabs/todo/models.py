from django.db import models


# Create your models here.
class Todo(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    priority = models.CharField(
        choices=(
            ('HIGH', 'Very Important'),
            ('MEDIUM', 'Important'),
            ('LOW', 'Not So Important'),
        ),
        default='LOW',
        max_length=6
    )
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.text