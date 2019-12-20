from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

def homePageView(request):
    return render(request,'home.html')

@csrf_exempt
def calc_result(request):
    input1=request.POST.get("input1")
    input2 = request.POST.get("input2")
    result=int(input1)%int(input2)
    print(result)
    return JsonResponse({"result":result})