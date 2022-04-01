from django.contrib import admin
from .models import (
    BannerImage,
    WhyChooseUsModel,
    Faq,
    FaqModel,
    WhatWeDo
)

admin.site.register(BannerImage)
admin.site.register(WhyChooseUsModel)
admin.site.register(WhatWeDo)

class FaqInline(admin.StackedInline):
    model = FaqModel
    extra = 1

class FaqAdmin(admin.ModelAdmin):
    inlines = [FaqInline,]

admin.site.register(Faq, FaqAdmin)
