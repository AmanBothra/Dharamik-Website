from django.contrib import admin
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class BaseAdmin(admin.ModelAdmin):
    pass


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseAdminStackLine(admin.StackedInline):
    pass


def get_image_file_extension_validator():
    return [
        FileExtensionValidator(allowed_extensions=["svg", "png", "jpg", "jpeg", "webp"])
    ]


class TawkToChatCredential(BaseModel):
    site_id = models.CharField(_("Site ID"), max_length=255)
    widget_id = models.CharField(_("Widget ID"), max_length=255)

    def __str__(self):
        return "Tawk To Chat Credential"

    class Meta:
        verbose_name_plural = "Tawk To Chat Credential"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        TawkToChatCredential.objects.all().exclude(id=self.id).delete()


