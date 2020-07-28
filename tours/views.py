import random

from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

from tours.data import (title, subtitle, description, departures, tours)


class MainView(View):

    def get(self, request):
        main_tour_ids = random.sample(set(tours), 6)
        main_tours = {id: tours[id] for id in main_tour_ids}
        return render(request, 'index.html', context={'title': title,
                                                      'subtitle': subtitle,
                                                      'description': description,
                                                      'departures': departures,
                                                      'tours': main_tours})


class DepartureView(View):

    def get(self, request, departure):
        if departure not in departures:
            raise Http404
        dep_tours = {id: tours[id] for id in tours if tours[id]['departure'] == departure}
        dep_name = departures[departure].split()[1]
        return render(request, 'departure.html', context={'depart_city_name': dep_name,
                                                          'tours': dep_tours,
                                                          'tours_count': len(dep_tours),
                                                          'departures': departures,
                                                          'min_price': min([x['price'] for x in dep_tours.values()]),
                                                          'max_price': max([x['price'] for x in dep_tours.values()]),
                                                          'min_nights': min([x['nights'] for x in dep_tours.values()]),
                                                          'max_nights': max([x['nights'] for x in dep_tours.values()])})


class TourView(View):

    def get(self, request, id):
        if id not in tours:
            raise Http404
        return render(request, 'tour.html', context={'tour': tours[id],
                                                     'departures': departures,
                                                     'departure': departures[tours[id]['departure']].split()[1]

                                                     })
