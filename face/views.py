from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Image, Number
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import numpy as np
import os
import cv2
import urllib
import json


# Create your views here.
@csrf_exempt
def test(request):
    if request.method == 'POST':
        pic = request.FILES.get('img')
        new_img = Image(img=pic)
        new_img.save()
    return render(request, 'face/index.html')

def show(request):
    image = Image.objects.all()
    context = {'image': image}
    return render(request, 'face/result.html', context)

'''def get_face(img):
    image = str(img) + '.jpg'
    face_patterns = cv2.CascadeClassifier('static/face/haarcascade_frontalface_default.xml')  # 级联分类器
    image_sample = cv2.imread(image)
    number = 0
    faces = face_patterns.detectMultiScale(image_sample, scaleFactor=1.1, minNeighbors=5, minSize=(15, 15))
    for (x, y, w, h) in faces:
        cv2.rectangle(image_sample, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 左下角，右上角，线颜色，线宽
        number += 1
    #cv.imshow('face', image_sample)
    cv2.imwrite('media/face/show.png', image_sample)
    return number'''

FACE_DETECTOR_PATH = '{base_path}/cascades/haarcascade_frontalface_default.xml'.format(
    base_path=os.path.abspath(os.path.dirname(__file__)))

@csrf_exempt
def detect(request):
    data = {'success': False}
    if request.method == 'POST':
        if request.FILES.get('image', None) is not None:
            img = request.FILES['image']
            image = get_image(stream=img)

        else:
            url = request.POST.get('url', None)
            if url is None:
                data['error'] = 'No such URL provided.'
                return JsonResponse(data)

            image = get_image(url=url)

        detector = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
        faces = detector.detectMultiScale(
            image, scaleFactor=1.1, minNeighbors=5, minSize=(15, 15), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
        face = [(int(x), int(y), int(x+w), int(y+h)) for (x, y, w, h) in faces]
        data.update({'num_faces': len(faces), 'face': face, 'success': True})

    return JsonResponse(data)

def get_image(path=None, url=None, stream=None):
    if path is not None:
        image = cv2.imread(path)

    else:
        if url is not None:
            resp = urllib.urlopen(url)
            data = resp.read()

        elif stream is not None:
            data = stream.read()

        image = np.asarray(bytearray(data), dtype='uint8')
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image





