from django.shortcuts import render,HttpResponse

def home(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>hiiii</h1>")
def about(request):
    if request.session.test_cookie_worked():
        print("okkkk")
    request.session.delete_test_cookie()
    return HttpResponse("<h2> about page </h2>")
def CountView(request):
    if "count" in request.COOKIES:
      count = int (request.COOKIES["count"])+1
    else:
        count = 1
    response = render(request,"cookiapp/count.html",{'count': count})
    response.set_cookie('count' , count , max_age=604800,httponly=True)
    return response
