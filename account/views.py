from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_jwt.views import JSONWebTokenAPIView, jwt_response_payload_handler

from account.serializers import UserIdSerializer, JSONWebTokenSerializer
from fog.utils.restful_api.response import Response

class JSONWebTokenAPIWrapperMixin:

    def _auth_handler(self, request, data):
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)

            return Response(response_data)

        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(err_msg=str(serializer.errors), err_code=105)  # TODO: 少了Token相关的code

    def post(self, request, *args, **kwargs):
        return self._auth_handler(request, request.data)

    def get(self, request, *args, **kwargs):
        return self._auth_handler(request, request.GET)

@api_view(['GET', 'POST'])
def get_user_id(request):
    '''
    获得用户 id
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
    elif request.method == 'GET':
        username = request.GET.get('username')
    else:
        return Response(err_code=101, err_msg='用户名输入错误')

    user_obj = User.objects.filter(Q(username=username) | Q(email=username)) # TODO: 加入手机号啥的

    # TODO: 命中两个怎么办？
    if not user_obj:
        return Response(err_code=101, err_msg='用户不存在')

    obj = UserIdSerializer(user_obj[0])
    return Response(obj.data)



@api_view(['GET', 'POST'])
def user_register(request):
    if request.method == 'POST':
        params = request.POST
    elif request.method == 'GET':
        params = request.GET
    else:
        return Response(err_code=106, err_msg='请求不合法')

    username = params['username']
    password = params['pwd']

    try:
        user_obj = User.objects.create_user(username=username, password=password)
        user_obj.save()
    except Exception as e:
        return Response(err_code=104, err_msg='没法注册，原因你懂得')

    return Response({'uid': user_obj.pk})


class UserSignIn(JSONWebTokenAPIWrapperMixin,
                 JSONWebTokenAPIView):

    serializer = JSONWebTokenSerializer



