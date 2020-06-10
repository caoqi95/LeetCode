# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:26:16 2020

Breadth-First Search

@author: User
"""

from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'

def search(graph, name):
    
    search_queue = deque() # build the queue
    search_queue += graph[name]
    searched = [] # store the searched persons
    
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller.")
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False


if __name__ == "__main__":
    
    # graph
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []    
    
    search(graph, "you")