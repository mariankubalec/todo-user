import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from users.models import User
from .models import Todo


class AddTodoView(APIView):

    def post(self, request):
        token = request.COOKIES.get('jwt')   # TODO add to utils

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        if not user:
            raise AuthenticationFailed('Unauthenticated - No User found!')

        request.data['assignee'] = user.id

        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class ListTodoView(APIView):

    def get(self, request):
        # token = request.COOKIES.get('jwt')  # TODO add to utils
        #
        # if not token:
        #     raise AuthenticationFailed('Unauthenticated!')
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

        todos = Todo.objects.filter(assignee=user.id)

        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data)



