from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import LegendaryMoment
from .forms import LegendaryMomentForm


def home(request):
    return render(request, 'CelticsArchive/home.html')

def create_legendary_moment(request):
    if request.method == 'POST':
        form = LegendaryMomentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CelticsArchive_home')
    else:
        form = LegendaryMomentForm()
    return render(request, 'CelticsArchive/create_legendary_moment.html', {'form': form})

def legendary_moments_list(request):
    search_query = request.GET.get('search', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    page = request.GET.get('page', 1)

    moments = LegendaryMoment.objects.all()

    if search_query:
        moments = moments.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    if start_date and end_date:
        moments = moments.filter(date__range=[start_date, end_date])

    paginator = Paginator(moments, 9)  # Show 9 moments per page
    moments_page = paginator.get_page(page)

    return render(request, 'CelticsArchive/legendary_moments_list.html', {
        'moments': moments_page,
        'search_query': search_query,
        'start_date': start_date,
        'end_date': end_date,
        'has_next': moments_page.has_next(),
    })

def legendary_moment_detail(request, id):
    moment = get_object_or_404(LegendaryMoment, id=id)
    return render(request, 'CelticsArchive/legendary_moment_detail.html', {'moment': moment})
