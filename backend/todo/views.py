import jwt
from rest_framework.exceptions import (
    AuthenticationFailed,
    NotFound,
    PermissionDenied,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from users.models import User
from .models import Todo


class AddTodoView(APIView):

    def post(self, request):
        user = check_request(request)

        request.data['assignee'] = user.id
        for_serializer = {}
        for k, v in request.data.items():
            if v != '':
                for_serializer[k] = v
        serializer = TodoSerializer(data=for_serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class ListTodoView(APIView):

    def get(self, request):
        user = check_request(request)

        todos = Todo.objects.filter(assignee=user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class GetTodoView(APIView):

    def get(self, request, **kwargs):
        user = check_request(request)
        todo = check_index(kwargs.get('pk'), user)

        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        pk = kwargs.get('pk')
        user = check_request(request)
        check_index(pk, user)

        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            Todo.objects.filter(id=pk).update(**request.data)

        todo = Todo.objects.filter(id=pk).first()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, **kwargs):
        pk = kwargs.get('pk')
        user = check_request(request)
        check_index(pk, user)

        Todo.objects.filter(id=pk).update(**request.data)

        todo = Todo.objects.filter(id=pk).first()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def delete(self, request, **kwargs):
        pk = kwargs.get('pk')
        user = check_request(request)
        check_index(pk, user)

        todo = Todo.objects.filter(id=pk).first()
        todo.delete()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


### Some Utils ###
def check_request(request):
    token = request.headers.get('Authorization')

    if not token or token == '':
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    if not user:
        raise AuthenticationFailed('Unauthenticated - No User found!')

    return user


def check_index(pk, user):
    todo = Todo.objects.filter(id=pk).first()

    if not todo:
        raise NotFound('NotFound - No Todo found!')

    if todo.assignee.id != user.id:
        raise PermissionDenied('Forbidden - wrong user')

    return todo
