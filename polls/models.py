from django.db import models # create your models here
from django.utils import timezone # had to import both timezone and datetime because the function was_published_recenlty kept throwing errors.
import datetime
#from django.utils import datetime

#we"ll create two models: Poll and Choice. A Poll has a question and a publication date.
#A Choice has two fields: the text of the choice and a vote tally. 
#Each Choice is associated with a Poll.'''
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		now = timezone.now() #was_published_recently() should return False for polls whose pub_date is in the future
		return now - datetime.timedelta(days=1) <= self.pub_date < now
		#return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	def __unicode__(self): # Python 3: def_str_(self)
		return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self): # Python 3 : def_str_(self):
    	return self.choice_text


