from django.shortcuts import render, get_object_or_404, redirect

from poc import utils

# Create your views here.
def tvshows_list_view(request):
	#list of the top 100 most popular tv shows
    context = utils.api_page_append(5)

    return render(request, "tvshows_list.html", context)

def tvshows_detail_view(request, tv_id):
	#tv show details
	rating_form = utils.rating_form()
	if request.method == 'POST':
		rating_form = utils.rating_form(request.POST)
		if rating_form.is_valid():
			print(rating_form.cleaned_data['rating'])
			utils.post_new_rating(tv_id, utils.get_guest_session_id(), rating_form.cleaned_data['rating'])
	context = utils.get_details(tv_id)
	context['reviews'] = utils.get_lastest_reviews(tv_id)
	context['form'] = rating_form
	
	return render(request, "tvshow_detail.html", context)