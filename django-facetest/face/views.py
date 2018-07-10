from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Image, Number
from .forms import ImageForm
import cv2 as cv

# Create your views here.
def test(request):
    if request.method != 'POST':
        form = ImageForm()
    else:
        form = ImageForm(request.POST)
        if form.is_valid():
            img = form.save(commit=False)
            img.save()
            p_n = get_face(img)
            img.number_set = p_n
            return HttpResponseRedirect(reverse('face:test'))
    context = {form: 'form'}
    return render(request, 'face/index.html', context)

def show(request):
    img = Image.objects.all()
    people_number = img.number_set
    context = {'img': img, 'people_number': people_number}
    return render(request, 'face/result.html', context)

def get_face(img):
    image = str(img) + '.jpg'
    face_patterns = cv.CascadeClassifier('static/face/haarcascade_frontalface_default.xml')  # 级联分类器
    image_sample = cv.imread(image)
    number = 0
    faces = face_patterns.detectMultiScale(image_sample, scaleFactor=1.1, minNeighbors=5, minSize=(15, 15))
    for (x, y, w, h) in faces:
        cv.rectangle(image_sample, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 左下角，右上角，线颜色，线宽
        number += 1
    #cv.imshow('face', image_sample)
    cv.imwrite('media/face/show.png', image_sample)
    return number




