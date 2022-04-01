from django.shortcuts import render
from .models import(
    VideoBanner,
    About,
    MembershipPerks,
    ProfitScreenshots,
    KeyPoints,
    FeaturedIn,
    FeaturedInPhoto,
    TestiminialPass,
    Testimonial,
    Certificate,
    CertificateImage,
    RecommendedBooks,
    BookImage,
    IntroVideo,
    Subscriber,
    
)

def home(request):
    video_banner = VideoBanner.objects.all()
    about = About.objects.all()
    membership_perks_description = MembershipPerks.objects.all()
    key_points = KeyPoints.objects.all() 
    screenshot = ProfitScreenshots.objects.all() 
    featured_photo = FeaturedInPhoto.objects.all()
    testimonial = Testimonial.objects.all()
    certificate_image = CertificateImage.objects.all()
    books_image = BookImage.objects.all()
    intro = IntroVideo.objects.all()
    subscriber = Subscriber.objects.all()
    
    
    data = {
        'video_banner': video_banner,
        'about': about,
        'membership_perks' : membership_perks_description,
        'key_points' : key_points,
        'profit_screenshot': screenshot,
        'featured_photo' : featured_photo,
        'testimonials' : testimonial,
        'certificate_image' : certificate_image,
        'books_image' : books_image,
        'intro' : intro,
        'subscriber' : subscriber,
    }
    
    return render (request, 'pages/home.html', data)
