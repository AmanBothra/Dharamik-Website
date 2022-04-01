from django.contrib import admin
from .models import (
    BannerImage,
    AboutCourse,
    Course,
    Events,
    EventModel,
    CourseTestiminial,
    CourseTestimonialModel,
)

admin.site.register(BannerImage)
admin.site.register(AboutCourse)
admin.site.register(Course)

class EventInline(admin.StackedInline):
    model = EventModel
    extra = 1
    
class EventAdmin(admin.ModelAdmin):
    inlines = [EventInline,]

admin.site.register(Events, EventAdmin)

class TestimonalInline(admin.StackedInline):
    model = CourseTestimonialModel
    extra = 1

class TestimonalAdmin(admin.ModelAdmin):
    inlines = [TestimonalInline,]

admin.site.register(CourseTestiminial, TestimonalAdmin)
