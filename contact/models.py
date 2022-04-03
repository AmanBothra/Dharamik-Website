from tabnanny import verbose
from django.db import models
from base.models import (
    BaseModel,
    get_image_file_extension_validator,)
from django.utils.translation import gettext_lazy as _
from utils.helper import converter_to_webp


class ContactUs(BaseModel):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural = "Contact Us Form"