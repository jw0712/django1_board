import datetime
from django.db import models
from django.utils import timezone

# Question & Choice

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('data published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

'''
A Question has a question and a publication date.
A Choice has two fields: the text of the choice and a vote tally.
Each Choice is associated with a single Question=>ForeignKey

field e.g. Question.pub_date

https://docs.djangoproject.com/en/2.2/intro/tutorial02/
'''
