from django.shortcuts import render

# Create your views here.

def index(request):
    
    context = {
        'heap_dict' : 1
    }
    
    return render(request, 'data_structures/index.html', context)

class Node:
    
    def __init__(self, value):
        
        self.value = value
        self.degree = NULL
        self.left_most_child = NULL
        self.parent = NULL
        self.right_sibling = NULL
        
    def update_degree(self):
        
        self.degree += 1
        return True
        
    def update_child(self, addr):
        
        self.left_most_child = addr
        
        return True
    
    def update_parent(self, addr):
        
        self.parent = addr
        
        return True
    
    def update_sibling(self, addr):
        
        self.right_sibling = addr
        
        return True
    
class BinomialHeap:
    
    def __init__(self):
        self.head = NULL
        self.root_list = []
        self.min_node = NULL
        
    def sort_root_list():
        return None
    
    
    def insert(self, value):
        
        return None