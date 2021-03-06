from rest_framework import viewsets

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from serializers import BoundarySerializer, BoundaryListSerializer, CountryListSerializer, CountrySerializer, \
    DistrictListSerializer, DistrictSerializer, StateListSerializer, StateSerializer
from models import Boundary, Country, State, District
import json
from geo import Geo

import time

# Create your views here.


class BoundaryViewSet(viewsets.ModelViewSet):
    """
    This viewset is a test written by leon
    """
    queryset = Boundary.objects.only("country","level")
    serializer_class = BoundaryListSerializer

    def list(self, request):
        """
        List method of Api viewset. Lists should not contain geojson
        :param request: 
        :return: 
        """
        queryset = Boundary.objects.only("country","level")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Filter retrieve requests to include only the necessary
        :param request: 
        :param pk: The object id to retrieve 
        :return: 
        """
        queryset = Boundary.objects.all().filter(id=pk)
        self.serializer_class = BoundarySerializer
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.only("code")
    serializer_class = CountryListSerializer

    def list(self, request):
        """
        List method of Api viewset. Lists should not contain geojson
        :param request: 
        :return: 
        """
        queryset = Country.objects.only("code")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Filter retrieve requests to include only the necessary
        :param request: 
        :param pk: The object id to retrieve 
        :return: 
        """
        queryset = Country.objects.all().filter(id=pk)
        self.serializer_class = CountrySerializer
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.only("code")
    serializer_class = StateListSerializer

    def list(self, request):
        """
        List method of Api viewset. Lists should not contain geojson
        :param request: 
        :return: 
        """
        queryset = State.objects.only("code")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Filter retrieve requests to include only the necessary
        :param request: 
        :param pk: The object id to retrieve 
        :return: 
        """
        queryset = State.objects.all().filter(id=pk)
        self.serializer_class = StateSerializer
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.only("code", "name", "country", "state")
    serializer_class = DistrictListSerializer

    def list(self, request):
        """
        List method of Api viewset. Lists should not contain geojson
        :param request: 
        :return: 
        """
        queryset = District.objects.only("code", "name", "country", "state")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Filter retrieve requests to include only the necessary
        :param request: 
        :param pk: The object id to retrieve 
        :return: 
        """
        queryset = District.objects.all().filter(id=pk)
        self.serializer_class = DistrictSerializer
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def read_detail(request, testparam):
    """
    Retrieve, update or delete a snippet instance.
    """
    """try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)"""

    if request.method == 'GET':
        print(testparam)
        testboundaries = '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[-0.08651733398437501,51.5058576545476],[-0.07827758789062501,51.505109712517786],[-0.06849288940429689,51.50115610069437],[-0.06196975708007813,51.50030122060505],[-0.05493164062500001,51.50083552254009],[-0.04737854003906251,51.5038274976179],[-0.0418853759765625,51.50681927626061],[-0.03656387329101563,51.50660558430045],[-0.03295898437500001,51.50286581276557],[-0.03313064575195313,51.499766912405946],[-0.03278732299804688,51.497202145853784],[-0.03244400024414063,51.49506473014368],[-0.03072738647460938,51.49089648122356],[-0.028495788574218753,51.487689876549595],[-0.026092529296875003,51.486086489639675],[-0.026607513427734375,51.48373475351443],[-0.03107070922851563,51.4811690848672],[-0.05407333374023438,51.49068271459497],[-0.06797790527343751,51.49709527744871],[-0.08651733398437501,51.5058576545476]]]}}]}'
        return Response(testboundaries)

    elif request.method == 'PUT':
        print(request.data)
        print(request.data["test"]) # highly vulnerable

        return Response("PUT", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        data = json.dumps(request.data)
        Boundary.objects.create(geo_json=data)
        print(data)
        return Response("POST", status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        return Response("DELETE", status=status.HTTP_204_NO_CONTENT)



"""

should be something within alabama
curl -H "Authorization: Token a20447173155cd89f6cc5c6a1c41dc8b604824ec" -X GET 'http://localhost:8000/testapi/fetchcountry/USA?lon=-86.91667938232422&lat=32.664310455322266'

should be indianapolis
curl -H "Authorization: Token a20447173155cd89f6cc5c6a1c41dc8b604824ec" -X GET 'http://localhost:8000/testapi/fetchcountry/USA?lat=39.715638&lon=-86.165771'

should be Abu ghraib
curl -H "Authorization: Token a20447173155cd89f6cc5c6a1c41dc8b604824ec" -X GET 'http://localhost:8000/testapi/fetchcountry/IRQ?lon=44.227119445800781&lat=33.137374877929801'

Should be Al-anbar Ar ruthbah
curl -H "Authorization: Token a20447173155cd89f6cc5c6a1c41dc8b604824ec" -X GET 'http://localhost:8000/testapi/fetchcountry/IRQ?lon=43.172088623046932&lat=32.49156570434576'

"""
@api_view(['GET'])
def fetch_country_boundaries(request, country):
    """
    Fetch country boundaries
    """
    t1 = time.time()

    if request.method == 'GET':
        print(country)
        gadm = Boundary.objects.all().filter(country=country)
        #print type(gadm[0].geo_json)
        gj = gadm[0].geo_json
        #print(gj)
        point = (float(request.query_params["lon"]), float(request.query_params["lat"]))
        geo = Geo()
        dist = geo.find_district(point, gj)
        t2 = time.time()
        print("%f seconds" % (t2-t1))
        return Response(dist)
