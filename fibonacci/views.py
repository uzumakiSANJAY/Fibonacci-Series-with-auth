from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse


# Create your views here.
class Fibonacci(APIView):
    def post(self,request, format=None):
        firstnumber =request.data.get("firstnumber")
        secondnumber =request.data.get("secondnumber")
        n=request.data.get("n")
        firstnumber = int(firstnumber)
        secondnumber = int(secondnumber)
        n = int(n)
        p = [firstnumber , "," , secondnumber , "," ]
        while (n > 2):
            s = firstnumber + secondnumber
            s = int(s)
            firstnumber = secondnumber
            secondnumber = s
            p.append(  s )
            p.append(  "," )
            n -= 1     
        return HttpResponse(list(p), content_type='application/json')
