from django.shortcuts import get_object_or_404, render
from models import Video, Term

def videos(request):

	videos = Video.objects.order_by('-published')

	context = {
		'videos': videos,
	}

	return render(request, 'videos.html', context)


def detail(request, object_id):
    video_details = get_object_or_404(Term, video_id=object_id)
    context = {
    	'details': video_details
    }
    return render(request, 'details.html', context)