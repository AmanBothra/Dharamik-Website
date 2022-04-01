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
    image = models.FileField(_("Banner Image | 1280x1280"), upload_to="about/banner",
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
        
class WhyChooseUsModel(BaseModel):
    
    class Meta:
        verbose_name_plural = "Why Choose Us"
        
    step_one_title = models.CharField(_("Step One Title"), default="", max_length=50)
    step_one_description = models.TextField(_("Step One Description"), max_length=500)
    step_two_title = models.CharField(_("Step Two Title"), default="", max_length=50)
    step_two_description = models.TextField(_("Step Two Description"), max_length=500)
    step_three_title = models.CharField(_("Step Three Title"), default="", max_length=50)
    step_three_description = models.TextField(_("Step Three Description"), max_length=500)
    
    def __str__(self):
        return "Why Choose Us Step"
    
    def clean(self):
        super().clean()
        if not self.id and WhyChooseUsModel.objects.exists():
            raise ValidationError('You cannot add more somethings.')
    
class Faq(BaseModel):

    class Meta:
        verbose_name_plural = "FAQ"

    def __str__(self):
        return "FAQ"

class FaqModel(BaseModel):

    class Meta:
        verbose_name_plural = "FAQ"
    
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name="faq")
    question = models.CharField(_("Question"), default="", max_length=255)
    answer = models.TextField(_("Answer"), default="", max_length=10000)
    
    def __str__(self):
        return "FAQ"


class WhatWeDo(BaseModel):
    
    class Meta:
            verbose_name_plural = "What We Do"
            
    title = models.CharField(_("Title"), default="", max_length=50)
    description = models.TextField(_("Description"), default="", max_length=10000)
    
    def __str__(self):
        return "What We Do"

    def clean(self):
        super().clean()
        if not self.id and WhatWeDo.objects.exists():
            raise ValidationError('You cannot add more somethings.')

