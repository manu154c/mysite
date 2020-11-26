from django.shortcuts import render

# Create your views here.

def index(request):
    
    #pk=request.POST['choice']
    
    data_list = [10, 15, 28, 19, 35, 8, 5, 29, 31, 13, 12, 17, 28, 35, 40, 45]
    
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
        self.no_of_nodes = 0
        
    def update_root_list():
        """ Monotonically incrementing degree. """
        
        return True
    
    
    def insert(self, value):
        
        if len(self.root_list) == 0:
            new_node = Node(value)
            self.root_list.append(new_node)
            self.head = self.root_list[0]
        else:
            # create a new heap as the single node
            # perform union
            new_heap = BinomialHeap()
            new_heap.insert(value)
            self.union(self, new_heap)
        
        return True
    
    def union(heap1, heap2):
        # for each node in root list, corresponding degree is available
        # 
        
        
        return True