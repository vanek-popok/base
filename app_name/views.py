from django.shortcuts import render
from app_name.models import Video

# Create your views here.
def playlist(request):
    videos = Video.objects.all()
    return render(request, 'app_name/playlist.html',{'videos':videos})
def uploader(request):
    if request.method == "POST":
        Video.objects.create(
            title = request.POST['title'],
            embed = request.POST['embed'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name']
        )
    return render(request, 'app_name/uploader.html')