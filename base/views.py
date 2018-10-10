import csv
from datetime import datetime
from pytz import timezone

from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from .serializers import GetOrderDataSerializer
from .models import Order


class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        file = request.FILES['file'].read().decode('utf-8').splitlines()
        fieldnames = [f.name for f in Order._meta.get_fields()]
        fieldnames.remove('id')
        data = csv.DictReader(file, delimiter=',', fieldnames=fieldnames)
        next(data, None)
        for row in data:
            row['amount'] = row['amount'].replace(',', '.')
            datetime_obj = datetime.strptime(row['create_date'], '%d.%m.%y %H:%M:%S')
            datetime_obj_utc = datetime_obj.replace(tzinfo=timezone('UTC'))
            row['create_date'] = datetime_obj_utc
            order = Order.objects.filter(inner_id=row['inner_id'])
            if order:
                order.update(**row)
            else:
                order = Order(**row)
                order.save()
        return Response(status=201)


class GetOrderDataApiView(RetrieveAPIView):
    serializer_class = GetOrderDataSerializer
    lookup_field = 'inner_id'
    queryset = Order.objects.all()

