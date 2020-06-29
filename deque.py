from collections import deque

graph = {}
graph['you'] = ['ann', 'yegor', 'claire']
graph['yegor'] = ['anuj', 'peggy']
graph['ann'] = ['peggy']
graph['claire'] = ['thom', 'johny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['johny'] = []





def person_is_seller(name):
	return name[:-3] == 'ye'


def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []

	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print('Person ' + person + ' is seller!')
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	print('There are no seller!')
	return False

search("you")


