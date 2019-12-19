from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse

def calculator(request):
    return render(request,'calculator_adil.html')

@csrf_exempt
def caculateresult(request):
    input1 = request.POST.get("input1")
    input2 = request.POST.get("input2")

    result = int(input1)*int(input2)
    print("result ",result)

    return JsonResponse({'result':result})
