from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import mimetypes
from .forms import ImageForm
from .models import Image
from .stitch import MultipleImageStitching
import os
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        files = request.FILES.getlist('Images')
        if form.is_valid():
            img_path_list = []
            for img in files:
                img_instance = Image(Images=img)
                img_instance.save()
                img_path_list.append(img_instance.Images.path)
            
            final_obj = MultipleImageStitching(img_path_list)
            print(Image.objects.get(id = final_obj.id))
            return render(request,'download.html',{'form':form,'result':final_obj})
        
    else:
        form = ImageForm()
        return render(request,'home.html',{'form':form})


def download(request,image_id):
    img = Image.objects.get(id = image_id)
    wrapper = FileWrapper(open(img.Images.path,'rb'))
    content_type = mimetypes.guess_type(img.Images.name)[0]
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length'] = os.path.getsize(img.Images.path)
    response['Content-Disposition'] = "attachment; filename=%s" % img.Images.name
    return response