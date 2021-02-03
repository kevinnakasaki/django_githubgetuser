from django.shortcuts import render, HttpResponse
import requests
import json


def index(request):
    return HttpResponse('Hello guys')


def profile(request):
    parsed_data = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get(f'https://api.github.com/users/{username}')
        json_list = [json.loads(req.content)]
        user_data = {}
        for data in json_list:
            user_data['name'] = data['name']
            user_data['blog'] = data['blog']
            user_data['email'] = data['email']
            user_data['public_gists'] = data['public_gists']
            user_data['public_repos'] = data['public_repos']
            user_data['avatar_url'] = data['avatar_url']
            user_data['followers'] = data['followers']
            user_data['following'] = data['following']
        parsed_data.append(user_data)
    return render(request, 'app/profile.html', {'data': parsed_data})
