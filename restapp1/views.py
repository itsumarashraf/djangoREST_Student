from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .seralizers import StudentSerializer


def home(request):
    return HttpResponse("<h3>WELCOME TO THE REST APPLICATION<h3><br><i>api endpoint:</i><br><p>api/getallstudents</p>"
                        "<p>api/getstudent/id</p>"
                        "<p>api/createstudent</p>"
                        "<p>api/updatestudent/id</p>"
                        "<p>api/deletestudent/id</p>")

@api_view(['GET'])
def getallstudents(request):
    response ={'status' : 200}
    std =student.objects.all()
    serializer = StudentSerializer(std, many=True)
    response['data'] = serializer.data
    return Response(response)

@api_view(['GET'])
def get_student(request, id):
    resp ={'status': 200}
    std= student.objects.get(id=id)
    serializer = StudentSerializer(std, many=False)
    resp['data']= serializer.data
    return Response(resp)

@api_view(['POST'])
def create_student(request):
    resp={'status': 200}
    # requet.data return us the json
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(resp)
    
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_student(request,id):
    resp={'status': 200}
    std = student.objects.filter(id=id)
    if std:
        std.delete()
    else:
        resp={'status': 404, 'message':'user was not found'}
    return Response(resp)


@api_view(['POST'])
def update_student(request,id):
    resp={'status':200, 'message':'updated successfully'}
    std = student.objects.filter(id=id)
    if std:
        serializer = StudentSerializer(instance=std, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(resp)
        else:
            print(serializer.errors)
            return Response(serializer.errors)
    else:
        return Response({'status':404,'message':'user not found!'})
    






















# from django.contrib.auth import authenticate

# def login_api(request):
#     try:
#        data= request.data
#        username =data.get('username')
#        password=data.get('password')
#        user = authenticate(username=username, password=password)
#        if user:
#            token = Token.objects.get_or_create(user=user)
#            return Response({
#                'status':200,
#                'token': str(token)
#             })
#         return Response({
#             'status': 300,
#             'message': 'invalid credintials',
#         })
#     except Exception as e:
#         print(e)
#         return Response({
#             'status': 400,
#             'message':'something went wrong'
#         })

    