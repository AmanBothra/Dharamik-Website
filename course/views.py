from django.shortcuts import render
from .models import (
    BannerImage,
    AboutCourse,
    Course,
    EventModel,
    CourseTestiminial,
)

def course(request):
    
    banner = BannerImage.objects.all()
    about = AboutCourse.objects.all()
    course = Course.objects.all()
    event = EventModel.objects.all()
    testimonial = CourseTestiminial.objects.all()
    
    data = {
        "banner" : banner,
        "about" : about,
        "course" : course,
        "event" : event,
        "testimonial" : testimonial,
    }
    
    return render (request, 'pages/course.html', data)