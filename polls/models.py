from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    description = models.TextField()
    date_start = models.DateField(auto_now_add=True)
    date_finish = models.DateField(blank=True)
    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.CharField(max_length=50)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions")
    QUESTION_TYPE_CHOICES = (
        ('text field', 'Text field'), 
        ('choose one', 'Choose one'),
        ('choose many', 'Choose many')
    )
    question_type = models.CharField(choices=QUESTION_TYPE_CHOICES, max_length=20, default='text field')
    def __str__(self):
        return self.text

class Choice(models.Model):
    text = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    def __str__(self):
        return self.text

class Vote(models.Model):
    user_id = models.IntegerField(null=True)
    poll = models.ForeignKey (Poll, on_delete=models.DO_NOTHING, null=True)
    answers = models.CharField(max_length=200, null=True)