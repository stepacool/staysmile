from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from StaySmile.pagination import FiftyPagination
from preferences.models import Preference
from preferences.serializers import PreferenceSerializer, RecommendationSerializer


class RecommendationView(GenericAPIView):

    serializer_class = RecommendationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = {
                'type': 'strong',
                'address': 'Buryatiya, Ulan-Ude',
                'latitude': 90.432,
                'longitude': 90.23,
                'google_link': 'google.com',
                'title': 'Hello world',
                'description': 'This is mock data',
                'cost': '20 USD',
                'website': 'example.com',
                'tel': '911',
                'restriction': "",
                'workhours': {
                    'start': '12:40',
                    'end': '20:00',
                },
                'rating': 4.59,
                'review_counts': 100000,
            }
            return Response(data=data, status=200)
        return Response(data=serializer.errors, status=400)


class ListCreatePreferences(ListCreateAPIView):
    serializer_class = PreferenceSerializer
    # permission_classes = (IsAuthenticated,)
    pagination_class = FiftyPagination
    queryset = Preference.objects.all()

    def get(self, request, *args, **kwargs):
        preferences = self.get_queryset()
        paginate_queryset = self.paginate_queryset(preferences)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PreferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetDeleteUpdatePreference(RetrieveUpdateDestroyAPIView):
    serializer_class = PreferenceSerializer
    # permission_classes = (IsAuthenticated, )
    queryset = Preference.objects.all()


def bulk_create(request, id):
    objs = []
    for i in range(id, id+1000):
        objs.append(Preference(name=i))
    Preference.objects.bulk_create(objs)