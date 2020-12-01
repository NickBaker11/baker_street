from django.shortcuts import render, get_object_or_404
from bookings.views import Rooms


def bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    # booking = get_object_or_404(Rooms, pk=item_id)
    # getting the number of players, date and time from the posted form
    num_of_players = int(request.POST.get('num_of_players'))
    date = (request.POST.get('date'))
    time = (request.POST.get('time'))
    bag = request.session.get('bag', {})
    # creating a dictionary for the details for the bag
    booking_details = {'num_of_players': num_of_players, 'date': date, 'time': time}  # noqa: E501
    print(f"number of players: {num_of_players}")
    print(f"date in the format received {date}")
    print(f"time in the format received {time}")
    bag[item_id] = booking_details

    request.session['bag'] = bag
    return render(request, 'bag/bag.html')