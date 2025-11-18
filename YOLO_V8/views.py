from django.shortcuts import render



def Home(request):
    
    a = 0
    return render(request, 'YOLO_V8/HomeYolo.html')