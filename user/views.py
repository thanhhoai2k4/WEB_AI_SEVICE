# user/views.py
from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages


def register(request):
    # Logic: Nếu người dùng gửi dữ liệu (POST) -> Xử lý. Nếu mới vào (GET) -> Hiện form trống.
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu user vào Database (PostgreSQL của bạn)
            username = form.cleaned_data.get('username')
            messages.success(request, f"Tài khoản {username} đã được tạo! Hãy đăng nhập.")
            return redirect('login')  # Chuyển hướng sang trang login
        else:
            print("Dang ky that bai vi form ko hop le.")
    else:
        # by get
        form = CustomRegisterForm()

    return render(request, 'user/register.html', {'form': form})