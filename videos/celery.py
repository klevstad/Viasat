from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viasat.settings')

from django.conf import settings  # noqa

app = Celery('viasat')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def load_videos():
	
	response = urllib.urlopen(URL)
	data = json.loads(response.read())['videos']

	for raw_video in data:
		if entry_already_exists(raw_video):
			continue
		# Todo: Handle last_modified


		video = Video()
		video.videocloud_id = raw_video['videocloud_id']
		video.wp_id = raw_video['wp_id']
		video.title = raw_video['title']
		video.short_title = raw_video['short_title']
		video.description = raw_video['description']
		video.published = raw_video['published']
		video.aired = raw_video['aired']
		video.url = raw_video['url'].replace("\\", "")
		video.last_modified = raw_video['last_modified']
		video.save()

		create_terms(raw_video['terms'], video)


def create_terms(raw_video, video):

	term = Term()
	term.video_id = video

	if raw_video['sport']:
		term.sport = raw_video['sport'][0].encode("utf-8")
	
	if raw_video['competition']:
		term.competition = raw_video['competition'][0].encode("utf-8")
	
	if raw_video['team']:
		term.teams = raw_video['team'][0].encode("utf-8")
	
	if raw_video['participant']:
		term.participants = raw_video['participant'][0].encode("utf-8")
	
	if raw_video['tag']:
		term.tags = raw_video['tag'][0].encode("utf-8")
	
	if raw_video['video_type']:
		term.video_type = raw_video['video_type'][0].encode("utf-8")
	
	term.save()


def entry_already_exists(raw_video):
	existing_videos = Video.objects.filter(wp_id = raw_video['wp_id'])
	for video in existing_videos:
		if video.wp_id == long(raw_video['wp_id']):
			return True
	return False