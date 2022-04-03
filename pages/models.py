from tabnanny import verbose
from django.db import models
from base.models import (
    BaseModel,
    get_image_file_extension_validator,)
from django.utils.translation import gettext_lazy as _
from utils.helper import converter_to_webp
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


class VideoBanner(BaseModel):
    
    class Meta:
            verbose_name_plural = "Video Banner"
    video = models.FileField(_("Video"), upload_to="home/videos/")
    image = models.FileField(_("Backgroung Image"), upload_to="home/images/",
        validators=get_image_file_extension_validator())
    title = models.CharField(_("Title"), default="", max_length=50, blank=True)
    short_description = models.CharField(_("Short Description"), max_length=200, blank=True)
    button_title = models.CharField(_("Button Title"), default="Contact Us", max_length=50, blank=True)
    url = models.CharField(_("Button URL"), max_length=255, blank=True)
    
            
    def __str__(self):
        return "Video Banner"
        
    def save(self, *args, **kwargs):
        if self.image:
            converter_to_webp(self.image)

        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if not self.id and VideoBanner.objects.exists():
            raise ValidationError('You cannot add more somethings.')
        
class About(BaseModel):
    class Meta:
            verbose_name_plural = "About"
            
    title = models.CharField(_("Title"), default="", max_length=50)
    description = RichTextField()
    image = models.FileField(_("Backgroung Image"), upload_to="home/images/",
        validators=get_image_file_extension_validator())

    def __str__(self):
        return self.title
            
    def save(self, *args, **kwargs):
        if self.image:
            converter_to_webp(self.image)

        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if not self.id and About.objects.exists():
            raise ValidationError('You cannot add more somethings.')
        
class MembershipPerks(BaseModel):
    
    class Meta:
        verbose_name_plural = "Membership Perks"
        
    description = RichTextField()
    
    def __str__(self):
        return "Description"    
    
    def clean(self):
        super().clean()
        if not self.id and MembershipPerks.objects.exists():
            raise ValidationError('You cannot add more somethings.')

class KeyPoints(BaseModel):

    class Meta:
        verbose_name_plural = "Membership Perks Key Points"

    membership_perks = models.ForeignKey(MembershipPerks, on_delete=models.CASCADE, related_name='points')
    key_points = models.CharField(_("Key Points"), default="", max_length=50)

    def __str__(self):
        return self.key_points
    
class ProfitScreenshots(BaseModel):
    
    membership_perks = models.ForeignKey(MembershipPerks, on_delete=models.CASCADE, related_name='screenshot')
    image = models.FileField(_("Upload Profit Screenshot"), upload_to="home/membership_perks/",
        validators=get_image_file_extension_validator(),
    )
    class Meta:
            verbose_name_plural = "Profit Screenshots"
            
    def __str__(self):
        return self.image.name
    
    def save(self, *args, **kwargs):
        if self.image:
            converter_to_webp(self.image)

        super().save(*args, **kwargs) 
    
class Performance(BaseModel):
    
    year = models.IntegerField(_("Performance Year"), default=2019, unique=True)
    
    class Meta:
        verbose_name_plural = "Monthly Performance"
        
    def __int__(self):
        return self.year

class PerformanceModel(BaseModel):
     
    year = models.ForeignKey(Performance, on_delete=models.CASCADE)
    month = models.CharField(max_length=15, default="")
    percentage = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Monthly Performance"
        
class FeaturedIn(BaseModel):

    class Meta:
        verbose_name_plural = "Fetured In"
    
    def __str__(self):
        return "Freatured On"

    def clean(self):
        super().clean()
        if not self.id and FeaturedIn.objects.exists():
            raise ValidationError('You cannot add more somethings.')
    
class FeaturedInPhoto(BaseModel):

    featured_in = models.ForeignKey(FeaturedIn, on_delete=models.CASCADE, related_name='featured')
    image = models.FileField(_("Image"), upload_to="home/featured_in/",
        validators=get_image_file_extension_validator(),
    )
    url = models.URLField()
    class Meta:
            verbose_name_plural = "Image"
            
    def __str__(self):
        return self.image.name
    
    def save(self, *args, **kwargs):
        if self.image:
            converter_to_webp(self.image)

        super().save(*args, **kwargs) 
    
class TestiminialPass(BaseModel):
    
    class Meta:
        verbose_name_plural = "Testimonial"
        
    def __str__(self):
        return "Testimonial"

    def clean(self):
        super().clean()
        if not self.id and TestiminialPass.objects.exists():
            raise ValidationError('You cannot add more somethings.')

class Testimonial(BaseModel):
    
    demo = models.ForeignKey(TestiminialPass, on_delete=models.CASCADE, related_name='testimonial')
    testimonial = models.TextField(_("Testimonial"), default="")
    name = models.CharField(_("CLient Name"), default="", max_length=50)

    def __str__(self):
        return self.name
    class Meta:
            verbose_name_plural = "Testimonial"
        
class Certificate(BaseModel):
    
    def __str__(self):
        return "Certificate"

    def clean(self):
        super().clean()
        if not self.id and Certificate.objects.exists():
            raise ValidationError('You cannot add more somethings.')
    class Meta:
        verbose_name_plural = "Certificate"

class CertificateImage(BaseModel):

    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, related_name='certificate')
    image = models.FileField(_("Image"), upload_to="home/certificate/",
        validators=get_image_file_extension_validator(),
    )
    class Meta:
            verbose_name_plural = "Certificate"
            
    def __str__(self):
        return self.image.name
    
    def save(self, *args, **kwargs):
        if self.image:
            converter_to_webp(self.image)

        super().save(*args, **kwargs) 
        
class RecommendedBooks(BaseModel):

    class Meta:
        verbose_name_plural = "Recommend Book"
    
    def __str__(self):
        return "Recommend Book"

    def clean(self):
        super().clean()
        if not self.id and RecommendedBooks.objects.exists():
            raise ValidationError('You cannot add more somethings.')
    
class BookImage(BaseModel):

    book = models.ForeignKey(RecommendedBooks, on_delete=models.CASCADE, related_name='book')
    book_name = models.CharField(_("Book Name"), max_length=100,default="")
    url = models.CharField(_("Book URL"), max_length=255, default="")
    image = models.FileField(_("Book Image"), upload_to="home/books/",
        validators=get_image_file_extension_validator())
    
    class Meta:
            verbose_name_plural = "Book"
            
    def __str__(self):
        return self.image.name
    
    def save(self, *args, **kwargs):
        if self.image:
            converter_to_webp(self.image)

        super().save(*args, **kwargs) 


class IntroVideo(BaseModel):
    video = models.FileField(_("Video"), upload_to="home/videos/")
    image = models.FileField(_("Bachground Banner"), upload_to="home/images/",
        validators=get_image_file_extension_validator())
   
    def __str__(self):
            return "# {}".format(self.id)  
    
    class Meta:
         verbose_name = _("Intro Video")
         
    def clean(self):
        super().clean()
        if not self.id and IntroVideo.objects.exists():
            raise ValidationError('You cannot add more somethings.')

class Subscriber(BaseModel):

    premium_clients_users = models.IntegerField(_("Premium Clients"), default="")
    international_clients_users = models.IntegerField(_("International Clients"), default="")
    subscriber_users = models.IntegerField(_("Subscriber"), default="")
    
    def __str__(self):
        return "Subscriber" 
    
    class Meta:
        verbose_name = _("Subscriber")
    
    def clean(self):
        super().clean()
        if not self.id and Subscriber.objects.exists():
            raise ValidationError('You cannot add more somethings.')
    