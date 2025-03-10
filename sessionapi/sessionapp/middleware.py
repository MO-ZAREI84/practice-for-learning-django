
from django.http import HttpResponse
class MyMiddleware:
    def __init__(self, get_response):
        # ذخیره تابع get_response برای فراخوانی بعدی
        self.get_response = get_response
        print("hiii mostashar")

    def __call__(self, request):
        print("Before request")
        # درخواست به تابع get_response ارسال می‌شود و پاسخ گرفته می‌شود
        response = self.get_response(request)
        print("After request")
        # پاسخ برگردانده می‌شود
        return response
class ExceptionHandelingMiddleware:
    def __init__(self, get_response):
        # ذخیره تابع get_response برای فراخوانی بعدی
        self.get_response = get_response
  

    def __call__(self, request):

        response = self.get_response(request)

        return response
    def process_exception(self,request,exception):
        return HttpResponse("ohhhhh.bad")
        print(exception)
        