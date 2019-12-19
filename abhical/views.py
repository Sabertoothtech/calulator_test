# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
#
# def index(request):
#     return render(request, 'index.html')


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def calculator(request):
    return render(request,"index.html")

@csrf_exempt
def CalculateResult(request):
    firstno = request.POST.get("firstno")
    secondno = request.POST.get("secondno")
    result = int(firstno)+int(secondno)
    print("result",result)
    return JsonResponse({"result":result})





