import csv
import io

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmissionRecord
from .serializers import EmissionRecordSerializer


@api_view(['GET'])
def records(request):

    records = EmissionRecord.objects.all().order_by('-created_at')

    serializer = EmissionRecordSerializer(records, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def upload_sap(request):

    file = request.FILES['file']

    decoded = file.read().decode('utf-8')

    reader = csv.DictReader(io.StringIO(decoded))

    for row in reader:

        quantity = float(row['quantity'])

        suspicious = quantity > 1000

        EmissionRecord.objects.create(
            source='SAP',
            activity_type=row['fuel_type'],
            quantity=quantity,
            unit=row['unit'],
            record_date=row['date'],
            emissions=quantity * 2.5,
            suspicious=suspicious,
            raw_data=row
        )

    return Response({"message": "SAP uploaded"})


@api_view(['POST'])
def upload_utility(request):

    file = request.FILES['file']

    decoded = file.read().decode('utf-8')

    reader = csv.DictReader(io.StringIO(decoded))

    for row in reader:

        kwh = float(row['kwh'])

        suspicious = kwh > 5000

        EmissionRecord.objects.create(
            source='UTILITY',
            activity_type='Electricity',
            quantity=kwh,
            unit='kWh',
            record_date=row['billing_end'],
            emissions=kwh * 0.8,
            suspicious=suspicious,
            raw_data=row
        )

    return Response({"message": "Utility uploaded"})


@api_view(['POST'])
def sync_travel(request):

    sample_data = [
        {
            "employee": "John",
            "origin": "BLR",
            "destination": "DEL",
            "distance": 1700
        }
    ]

    for row in sample_data:

        suspicious = row['distance'] > 5000

        EmissionRecord.objects.create(
            source='TRAVEL',
            activity_type='Flight',
            quantity=row['distance'],
            unit='km',
            record_date='2026-01-01',
            emissions=row['distance'] * 0.15,
            suspicious=suspicious,
            raw_data=row
        )

    return Response({"message": "Travel synced"})


@api_view(['POST'])
def approve_record(request, pk):

    record = EmissionRecord.objects.get(id=pk)

    record.review_status = 'APPROVED'

    record.save()

    return Response({"message": "Approved"})