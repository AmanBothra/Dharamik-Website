from django.db import models
from base.models import (
    BaseModel,
    get_image_file_extension_validator,)
from django.utils.translation import gettext_lazy as _
from utils.helper import converter_to_webp
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


class BannerImage(BaseModel):
    class Meta:
        verbose_name = "Banner Image"
        
    title = models.CharField(_("Title"), default="", max_length=50, blank=True)
    image = models.FileField(_("Banner Image | 1280x1280"), upload_to="course/banner",
        validators=get_image_file_extension_validator())

    def __str__(self):
        return "# {}".format(self.id) 
    
    def save(self, *args, **kwargs):
        if self.image:
            converter_to_webp(self.image)

        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if not self.id and BannerImage.objects.exists():
            raise ValidationError('You cannot add more somethings.')
        
class AboutCourse(BaseModel):
    
    class Meta:
        verbose_name = "About Course"

    title = models.CharField(_("Title"), default="", max_length=50)
    description = RichTextField()
    url = models.URLField(_("Catalouge Download Url"))

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if not self.id and AboutCourse.objects.exists():
            raise ValidationError('You cannot add more somethings.')
        
class Course(BaseModel):

    class Meta:
        verbose_name = "Course Details"
        
    one_million_image = models.FileField(upload_to="course",
        validators=get_image_file_extension_validator())
    one_million_description = RichTextField()
    platinum_plus_image = models.FileField(upload_to="course",
        validators=get_image_file_extension_validator())
    platinum_plus_description = RichTextField()
    platinum_image = models.FileField(upload_to="course",
        validators=get_image_file_extension_validator())
    platinum_description = RichTextField()
    copymytrade_image = models.FileField(upload_to="course",
        validators=get_image_file_extension_validator())
    copymytrade_description = RichTextField()

    def __str__(self):
        return "Course Details"

    def clean(self):
        super().clean()
        if not self.id and AboutCourse.objects.exists():
            raise ValidationError('You cannot add more somethings.')
        
class Events(BaseModel):
    
    class Meta:
        verbose_name = "Event"
    
    def __str__(self):
        return "Event"

class EventModel(BaseModel):

    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event')    
    name = models.CharField(_("Event Name"), default="", max_length=50)
    date = models.CharField(_("Date "), default="20 April", max_length=50)
    event_description = models.TextField(_("Event Description"))

    class Meta:
        verbose_name = "Events"
    
    def __str__(self):
        return "Events"
    
class CourseTestiminial(BaseModel):
    
    class Meta:
        verbose_name_plural = "Course Testimonial"

class CourseTestimonialModel(BaseModel):
    
    demo = models.ForeignKey(CourseTestiminial, on_delete=models.CASCADE, related_name='testimonial')
    testimonial = models.TextField(_("Testimonial"), default="")
    name = models.CharField(_("CLient Name"), default="", max_length=50)

    def __str__(self):
        return self.name
    class Meta:
            verbose_name_plural = "Course Testimonial"