from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from blog.models import User, Upload
from form.form import *
from django.core.urlresolvers import reverse
from django.utils import timezone
import datetime
import re, requests, bs4, ast, os, sys

from tensor_model.label_image import rec_image
from opencv_model.detect_human import human_detect
from opencv_model.vehicles_detection import detect_car
# from tensor_model.detect_object import human_detect

# from classification.call_classification import classification_image
from classification.call_classification import classification
from object_detector.object_detector.test_classifier import detect_object

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import time
# from django.views import View
from django.views.generic import ListView 
    
sys.path.append('/home/minhdo/code')

from blog.lib.Config import Config
# Create your views here.

class get_config:
    def __init__(self):
        self.path = Config().get('output_file', 'BaseDir')
        self.file_score = Config().get('tensor', 'score')

def index(request):
    name = ""
    type_model = ""
    context = {
        'name':name,
        'type_model':type_model
    }
    return render(request,'blog/index.html',context= context)
    #return render(request, 'blog/index.html', context=context)

class BasicUploadView(ListView):
    def get(self, request):
        photos_list = Upload.objects.all() #photos/basic_upload/index.html
        return render(self.request, 'blog/upload_images.html', {'photos': photos_list})

    def post(self, request):
        form = PostImage(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()

            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        # return JsonResponse({'message': 'Success'})
        return JsonResponse(data)

### show result
def result_image(request):
    #url = 'https://pixabay.com/en/photos/?hp=&image_type=photo&cat=&min_width=&order=popular&min_height=&q='
    #fileID = '/code/log_file.txt'
    time.sleep(2)
    name, res, data, highest, \
        img_name, img, list_img, \
        image_path, class_score, two_class_score, \
        store_box_face, \
        flat_urban, flat_face, two_class_label_sorted, \
        class_score_label_sorted = "", "", "", "", "", "", [], "", "", "", [], False, False, [], []

    path_dir = get_config().path
    path_file = get_config().file_score
    path_full_file = os.path.join(path_dir, path_file)

    file_dir = Config().get('paths', 'svm_dir')
    file_pkl = Config().get('svm_filter_model', 'plant_model')
    file_retrain_label = Config().get('svm_filter_model', 'label')

    if request.method == "POST":
        img = PostImage(request.POST, request.FILES)
        if  img.is_valid():
            img.save()
            # Face detect in image
            # _ = human_detect.face_detect(name)
            # Classification image
            for filename, file in request.FILES.iteritems():
                img_name = request.FILES[filename].name
                data, list_res_name = rec_image.rec_img(img_name)
                # Face detect in image

                # image_path = Config().get('output_file','ImageDir')
                image_path = '/home/minhdo/media/images'
                print (os.path.join(image_path, img_name))

                _, store_box_face, flat_face = human_detect.face_detect(os.path.join(image_path, img_name))
                # _ = detect_car.in_image(os.path.join(image_path, img_name))
                class_score = classification.classification_img_file("/home/minhdo/code/blog/classification/all_classification.pkl",
                                                                     "/home/minhdo/code/blog/classification/back_up_retrain_label/all_model__retrain_label.ini",
                                                                     os.path.join(image_path, img_name))
                class_score_sorted = sorted([re.findall('([0-9.]+) - label: ([A-z\s]+)', i )[0] for i in class_score])[::-1]
                for item_val in class_score_sorted:
                    for item_label in class_score:
                        if item_val[0] in item_label and item_val[1] in item_label:
                            class_score_label_sorted.append(item_label)

                for item in data:
                    match = re.search(r'fruit|flowers', str(item))
                    match_urban = re.search(r'urban', str(item))
                    if match:
                        if float(re.findall(r'accuracy: ([0-9\.\s]+)', item)[0]) > 0.2:
                            two_class_score = classification.classification_img_file(os.path.join(file_dir, file_pkl),
                                                                      os.path.join(file_dir, file_retrain_label),
                                                                      os.path.join(image_path, img_name))
                            two_class_val_sorted = sorted([re.findall('([0-9.]+) - label: ([A-z\s]+)', i )[0] for i in two_class_score])[::-1]
                            for item_val in two_class_val_sorted:
                                for item_label in two_class_score:
                                    if item_val[0] in item_label and item_val[1] in item_label:
                                        two_class_label_sorted.append(item_label)

                            print (two_class_label_sorted)

                    if match_urban:
                        if float(re.findall(r'accuracy: ([0-9\.\s]+)', item)[0]) > 0.2:
                            _ = detect_object(os.path.join(image_path, img_name))
                            flat_urban = True
        else:
            img = PostImage()
            # list_img = []
            # images = Upload.objects.all()
        images = Upload.objects.order_by('-upload_date')[:5]
        list_img = [i.pic for i in images]
        context = {
                      'list_img':list_img,
                      'result_img':highest,
                      'result_acc':data,
                      'name_img':img_name,
                      'form':img,
                      'class_score': class_score_label_sorted,
                      'two_class_score': two_class_label_sorted,
                      'store_box_face': store_box_face,
                      'flat_urban': flat_urban,
                      'flat_face': flat_face
                  }
        print ('name of in image in result : {}'.format(img_name))
        return render(request, 'blog/result.html', context = context)
            # return JsonResponse(context)
        # else:
        #     render(request, 'blog/result.html')
        # else:
        #     return HttpResponse("Error !!! not a file")
    # else:
    #     img = PostImage()
    # images = Upload.objects.all()
    # fileID = os.path.join(path_dir, path_file)
    # list_img = []
    context = {
                  'list_img':list_img,
                  'result_img':highest,
                  'result_acc':data,
                  'name_img':img_name,
                  'form':img,
              }
    # print ('name of in image in result : {}'.format(img_name))
    return render(request, 'blog/result.html', context = context)

def classification_svm(request):
    file_dir = Config().get('paths', 'svm_dir')
    file_pkl = Config().get('svm_filter_model', 'plant_model')

    file_retrain_label = Config().get('svm_filter_model', 'label')

    url_image = request.POST['url_image']
    # password = request.POST['password']
    print (url_image)
    # class_score = classification_image(os.path.join(file_dir, file_pkl), os.path.join(file_dir, file_retrain_label), url_image)
    class_score = classification.classification_image_url(os.path.join(file_dir, file_pkl), os.path.join(file_dir, file_retrain_label), url_image)

    #print(class_score)
    #name = "unknow"
   # return HttpResponseRedirect(reverse('blog:result_image'))
    #return HttpResponse(url_img_link)
    return HttpResponse(class_score)

def register_acc(request):
    register_form = BlogUser
    print "here"
    context = {
        'form': register_form
    }
    return render(request, 'blog/register_acc.html', context = context)




