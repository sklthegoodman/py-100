import requests
from draw_bar_chart import draw_bar

url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'

result = requests.get(url)

print('Status Code:', result.status_code)

r_dict = result.json()
print('Total Repos：', r_dict['total_count'])

repo_dicts = r_dict['items']
repo_dict = repo_dicts[0]

name, stars = [], []
for repo_dict in repo_dicts:
    # print('Name:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repository:', repo_dict['html_url'])
    # print('Created:', repo_dict['created_at'])
    # print('Updated:', repo_dict['updated_at'])
    # print('Description:', repo_dict['description'])
    name.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


draw_bar(name, stars)