from django.shortcuts import render

def renderTemplate(request):
    myDict = {"firstName" : "Asghar", "salary": 5000, "lastName":"Mirzie"}
    return render(request, 'templatesApp/firstTemplate.html', myDict)
