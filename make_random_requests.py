from random import choice
import grequests


methods = ['get', 'post', 'put', 'delete']
base_url = 'http://127.0.0.1:8000/api/{}/'

# A simple task to do to each response object
def do_something(response):
    print(response.url)

# A list to hold our things to do via async
async_list = []


for i in range(1):
    method = choice(methods)
    url = base_url.format(method)
    action_item = getattr(grequests, method)(url)

    # The "hooks = {..." part is where you define what you want to do
    # 
    # Note the lack of parentheses following do_something, this is
    # because the response will be used as the first argument automatically
    # action_item = async.get(u, hooks = {'response' : do_something})

    # Add the task to our list of things to do via async
    async_list.append(action_item)

# Do our list of things to do via async
grequests.map(async_list)
