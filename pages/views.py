from django.shortcuts import render
from .models import(
    VideoBanner,
    About,
    MembershipPerks,
    KeyPoints,
    ProfitScreenshots,
    
)

def home(request):
    video_banner = VideoBanner.objects.all()
    about = About.objects.all()
    membership_perks_description = MembershipPerks.objects.all()
    key_points = KeyPoints.objects.all() 
    screenshot = ProfitScreenshots.objects.all() 
    
    data = {
        'video_banner': video_banner,
        'about': about,
        'membership_perks' : membership_perks_description,
        'key_points' : key_points,
        'profit_screenshot': screenshot,
    }
    
    return render (request, 'pages/home.html', data)
