from django.shortcuts import render
from .forms import YearForm
from gold_price_predictor.myModel import predict_price

def home(request):
    price = None
    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            if year > 1900:
                price = predict_price(year)
            else:
                price = "Past data is not currently available"
    else:
        form = YearForm()
    
    return render(request, 'goldApp/home.html', {'form': form, 'price': price})
