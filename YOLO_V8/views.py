from django.shortcuts import render
import cv2
from ultralytics import YOLO
import numpy as np
import base64

model = YOLO('yolov8n.pt')

def Home(request):
    return render(request, 'YOLO_V8/HomeYolo.html')

def yolo_detect_view(request):

    file = request.FILES

    if request.method == "POST" and request.FILES.get('image_upload'):

        # doc anh
        uploaded_file = request.FILES['image_upload']
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)


        # du doan
        results = model(img)
        result_img = results[0].plot()

        # chuyen doi sang base64 string
        _, buffer = cv2.imencode('.jpg', result_img)
        img_str = base64.b64encode(buffer).decode('utf-8')

        # Tạo định dạng chuẩn để thẻ <img> hiểu
        img_data = f"data:image/jpeg;base64,{img_str}"

        return render(request, 'YOLO_V8/HomeYolo.html', {
                'result_image': img_data,
                'status': 'success'
            })