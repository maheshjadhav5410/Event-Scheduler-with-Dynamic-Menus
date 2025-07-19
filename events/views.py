from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from events.models import EventsList, indoorImages, outdoorImages, Booking,VegMenu150, NonVegMenu200
from events.forms import BookingForm

def event_description(request, id=0):
    event = get_object_or_404(EventsList, id=id)
    return render(request, 'events/events_description.html', {'event': event})

def slotbooking(request):
    return render(request, 'events/slotbooking.html', {})

def indoorimages(request):
    indoor = indoorImages.objects.all()
    return render(request, 'events/indoorimages.html', {'indoor': indoor})

def outdoorimages(request):
    outdoor = outdoorImages.objects.all()
    return render(request, 'events/outdoorimages.html', {'outdoor': outdoor})

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            request.session['booking_id'] = booking.id  # ✅ STORE in session

            veg_items = VegMenu150.objects.all()
            nonveg_items = NonVegMenu200.objects.all()

            return render(request, 'events/select_menu.html', {
                'veg_items': veg_items,
                'nonveg_items': nonveg_items,
            })
    else:
        form = BookingForm()
    
    return render(request, 'events/booking_form.html', {'form': form})


def booking_success(request):
    booking_id = request.session.get('booking_id')
    booking = Booking.objects.filter(id=booking_id).first()
    return render(request, 'events/success.html', {'booking': booking})

def select_menu_view(request):
    veg_items = VegMenu150.objects.all()
    nonveg_items = NonVegMenu200.objects.all()
    return render(request, 'select_menu.html', {
        'veg_items': veg_items,
        'nonveg_items': nonveg_items
    })

def confirmation_view(request):
    if request.method == "POST":
        selected_menu = request.POST.get("menu")  # 'veg' or 'nonveg'

        booking_id = request.session.get("booking_id")

        if not booking_id:
            return HttpResponse("Booking ID not found in session.", status=400)

        booking = get_object_or_404(Booking, id=booking_id)
        total_persons = booking.total_persons
        event_price = booking.event.price  # Adjust if field name is different

        menu_price = 150 * total_persons if selected_menu == "veg" else 200 * total_persons
        total_price = round(menu_price + event_price)

        context = {
            "selected_menu": selected_menu,
            "booking": booking,
            "menu_price": menu_price,
            "event_price": event_price,
            "total_price": total_price,
        }
        return render(request, "events/confirmation.html", context)

    return redirect("booking")