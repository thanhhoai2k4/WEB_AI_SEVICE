from django.shortcuts import render, redirect, get_object_or_404
import cv2
from ultralytics import YOLO
import numpy as np
import base64
from .models import Musician, MusicianForm

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
    return redirect("Home_View")
    


def Learning_Dataset(request):
    # --- PHẦN 1: XỬ LÝ KHI NGƯỜI DÙNG BẤM NÚT THÊM (POST) ---
    if request.method == 'POST':
        # Đổ dữ liệu người dùng gửi lên vào cái khuôn Form
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save() # Lưu vào database
            return redirect('learning_dataset') # Load lại trang để thấy dữ liệu mới
    else:
        # Nếu chỉ là mở trang, tạo một cái form rỗng
        form = MusicianForm()

    # --- PHẦN 2: LẤY DỮ LIỆU HIỂN THỊ (GET) ---
    # Lấy tất cả nhạc sĩ trong database
    musicians = Musician.objects.all().order_by('-id') # Người mới nhất lên đầu

    # Đóng gói dữ liệu vào context để gửi sang HTML
    context = {
        'musicians': musicians,
        'form': form
    }
    
    return render(request, 'YOLO_V8/learning_dataset.html', context)



def delete_musician(request, id):

    # tim doi tuong
    musican = get_object_or_404(Musician, pk=int(id))
    if not musican:
        print("Khong ton tai doi tuong can xoa trong csdl.")

    if (request.method == 'POST'):
        musican.delete()
        return redirect("learning_dataset")
    else:
        return redirect('learning_dataset')
    

def gioithieu(request):
    return render(request,"YOLO_V8/gioithieu.html")