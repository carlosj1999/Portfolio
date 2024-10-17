# aggregator/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import IPAggregatorForm
from .utils import aggregate_ip_addresses

def index(request):
    form = IPAggregatorForm()
    result = None

    if request.method == 'POST':
        form = IPAggregatorForm(request.POST)
        if form.is_valid():
            ip_addresses = form.cleaned_data['ip_addresses']
            output_format = form.cleaned_data['output_format']
            why_blocked = form.cleaned_data['why_blocked']
            asn_code = form.cleaned_data['asn_code']
            
            result = aggregate_ip_addresses(ip_addresses, output_format, why_blocked, asn_code)
            
    
    else:
        form = IPAggregatorForm()

    return render(request, 'aggregator/index.html', {'form': form, 'result': result})





from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ip_aggregator.API.serializers import IPAggregatorSerializer
from .utils import aggregate_ip_addresses_json

class IPAggregatorView(APIView):
    def post(self, request):
        serializer = IPAggregatorSerializer(data=request.data)
        if serializer.is_valid():
            ip_addresses = serializer.validated_data['ip_addresses']
            output_format = serializer.validated_data['output_format']
            why_blocked = serializer.validated_data.get('why_blocked', None)
            asn_code = serializer.validated_data.get('asn_code', None)
            
            # Call the aggregation logic from utils.py
            result = aggregate_ip_addresses_json(ip_addresses, output_format, why_blocked, asn_code)
            
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IPAddressListView(APIView):
    def get(self, request):
        # For now, this will return dummy data. You can connect it to a database later.
        data = {
            "ip_addresses": [
                "192.168.1.0/24",
                "10.0.0.0/8"
            ],
            "output_format": "cidr"
        }
        return Response(data, status=status.HTTP_200_OK)