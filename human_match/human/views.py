from rest_framework import status as statuses, permissions
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from human.serializers import HumanSerializer
from human.models import Human


class HumanViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = HumanSerializer

    def _get_response_data(self, pk):
        try:
            instance = Human.objects.get(pk=pk)
        except Exception as ex:
            return {'error': str(ex)}, statuses.HTTP_400_BAD_REQUEST
        else:
            return instance, statuses.HTTP_200_OK

    def list(self, request):
        return Response(Human.objects.values(), status=statuses.HTTP_200_OK)

    def retreive(self, request, pk):
        data, status = self._get_response_data(pk)
        if status != statuses.HTTP_200_OK:
            return Response(data, status)
        return Response(data.jsonify(), status)

    def delete(self, request, pk):
        instance, status = self._get_response_data(pk)
        data = instance
        if status == statuses.HTTP_200_OK:
            data = instance.jsonify()
            Human.objects.filter(id=instance.id).delete()
            data['status'] = 'deleted'
        return Response(data, status)

    def change(self, request, pk):
        data, status = self._get_response_data(pk)
        if status == statuses.HTTP_400_BAD_REQUEST:
            return Response(data, status)

        instance = data
        serializer = self.serializer_class(instance=instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=statuses.HTTP_400_BAD_REQUEST)
        try:
            serializer.save()
        except Exception as ex:
            return Response({'error': str(ex)})
        else:
            instance_data = instance.jsonify()
            instance_data.update(serializer.validated_data)
            return Response(instance_data, status=statuses.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=statuses.HTTP_400_BAD_REQUEST)
        try:
            instance = serializer.save()
        except AssertionError as ex:
            return Response({'error': str(ex)}, status=statuses.HTTP_400_BAD_REQUEST)
        else:
            instance, status = self._get_response_data(instance.pk)
            return Response(instance.jsonify(), status=status)
