from django.shortcuts import render
from .models import (
    BannerImage,
    WhyChooseUsModel,
    FaqModel,
    WhatWeDo,
    WorkProcess,
)

# Create your views here.
def about(request):
    
    banner = BannerImage.objects.all()
    why_choose = WhyChooseUsModel.objects.all()
    faq = FaqModel.objects.all()
    what_we_do = WhatWeDo.objects.all()
    work_process = WorkProcess.objects.all()
    
    data = {
        "banner" : banner,
        "why_choose" : why_choose,
        "faq" : faq,
        "what_we_do" : what_we_do,
        "process" : work_process,
    }
    
    return render (request, 'pages/about.html', data)