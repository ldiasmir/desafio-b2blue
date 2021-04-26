from django import template
from django import forms
from datetime import datetime
import requests


register = template.Library()

my_api_key = '96a8c8272f4feffdff0d3e57d2f32dc9'
base_url = 'https://api.themoviedb.org/3/'

def api_page_append(pages):
	context = {}
	results = []
	for page in range(1,pages+1):
		url = f'{base_url}tv/popular?api_key={my_api_key}&language=en-US&page={page}'
		popular = requests.get(url)
		result = popular.json()
		for show in result['results']:
			results.append(show)

	context = { 'results' : results}
	return context

def get_details(tv_id):
	url = f'{base_url}tv/{tv_id}?api_key={my_api_key}&language=en-US'
	details = requests.get(url)
	result = details.json()
	return result

def get_lastest_reviews(tv_id):
	url = f'{base_url}tv/{tv_id}/reviews?api_key={my_api_key}'
	latest = requests.get(url)
	result = latest.json()
	return result['results']

def get_guest_session_id():
	url = f'{base_url}authentication/guest_session/new?api_key={my_api_key}'
	latest = requests.get(url)
	result = latest.json()
	return result['guest_session_id']

def post_new_rating(tv_id, guest_session_id, rating):
	url = f'{base_url}tv/{tv_id}/rating?api_key={my_api_key}&guest_session_id={guest_session_id}'
	payload = { 'value' : rating}
	latest = requests.post(url, payload)
	print(latest.json())

@register.filter
def year_from_date(value):
	dt = datetime.strptime(value, '%Y-%m-%d')
	return dt.year

@register.filter
def image_from_path(value):
	base_url = 'https://image.tmdb.org/t/p/w185_and_h278_bestv2/'
	return base_url + value

class rating_form(forms.Form):
	rating = forms.DecimalField(min_value = 0.5, max_value = 10)