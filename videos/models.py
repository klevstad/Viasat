import sys
from django.db import models

reload(sys)
sys.setdefaultencoding('utf-8')

# MySQL
class Video(models.Model):
	object_id		= models.AutoField(primary_key=True)
	videocloud_id	= models.BigIntegerField(unique=True)
	wp_id			= models.IntegerField(unique=True)
	title			= models.CharField(max_length=200)
	short_title		= models.CharField(max_length=200)
	description		= models.CharField(max_length=2000)
	published		= models.DateTimeField()
	aired			= models.DateTimeField()
	url				= models.CharField(max_length=200)
	last_modified	= models.DateTimeField()

	def join_object(self):
		return "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}".format(self.videocloud_id, self.wp_id, self.title, self.short_title, self.description, self.published, self.aired, self.url, self.last_modified)

	def __str__(self):
		return "[{0}]\t{1}".format(self.wp_id, self.title)

class Term(models.Model):
	term_id			= models.AutoField(primary_key=True)
	video_id 		= models.ForeignKey(Video)
	sport			= models.CharField(max_length=30)
	competition		= models.CharField(max_length=50)
	teams			= models.CharField(max_length=200)
	participants	= models.CharField(max_length=200)
	tags			= models.CharField(max_length=200)
	video_type		= models.CharField(max_length=30)

	def __str__(self):
		return "{0}\t({1})".format(self.video_id, self.video_type)