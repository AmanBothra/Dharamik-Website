from django.contrib import admin
from .models import (
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


admin.site.register(VideoBanner)
admin.site.register(About)

class ScreenshotInline(admin.StackedInline):
    model = ProfitScreenshots
    extra = 1

class PointsInline(admin.StackedInline):
    model = KeyPoints
    extra = 1
    
    
class MembershipAdmin(admin.ModelAdmin):
    inlines = [PointsInline,ScreenshotInline,]
    
admin.site.register(MembershipPerks, MembershipAdmin)

class FeaturedInline(admin.StackedInline):
    model = FeaturedInPhoto
    extra = 1

class FeaturedAdmin(admin.ModelAdmin):
    inlines = [FeaturedInline,]

admin.site.register(FeaturedIn, FeaturedAdmin)


class TestimonalInline(admin.StackedInline):
    model = Testimonial
    extra = 1

class TestimonalAdmin(admin.ModelAdmin):
    inlines = [TestimonalInline,]

admin.site.register(TestiminialPass, TestimonalAdmin)

class CertificateInline(admin.StackedInline):
    model = CertificateImage
    extra = 1

class CertificateAdmin(admin.ModelAdmin):
    inlines = [CertificateInline,]

admin.site.register(Certificate, CertificateAdmin)

class BookInline(admin.StackedInline):
    model = BookImage
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [BookInline,]

admin.site.register(RecommendedBooks, BookAdmin)
admin.site.register(IntroVideo)
admin.site.register(Subscriber)


