from django.shortcuts import render
from django.views import generic
from .models import MeasuredEntropy, Transactions
from itertools import combinations
import pdb
import numpy as np 
from anytree import Node, RenderTree, AnyNode, AsciiStyle
from anytree import find, findall_by_attr, Walker, findall
from anytree.exporter import JsonExporter, DictExporter
from anytree.dotexport import RenderTreeGraph

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'lang_entropy/index.html'
    context_object_name = 'list_transactions'

    def get_queryset(self):
        """Return the 20 five saved transactions."""
        #return Transactions.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return Transactions.objects.all()
        

def AddItem(request):
    return render(request, 'lang_entropy/add_view.html')

def SaveTransaction(request):
    item=request.POST['item']
    item_save = Transactions(items_bought=item)
    item_save.save()
    
    transactions = Transactions.objects.all()
    
    context = {
        'list_transactions': transactions,
    }
    
    return render(request, 'lang_entropy/index.html', context)

            

def ListState(request):
    min_sup = 2
    transactions = Transactions.objects.all()
    transaction_details = []
    item_frequency = {}
    
    for item in transactions:
        transaction_details.append(item.items_bought.split(','))
    
    print(transaction_details)
    #### itemset frequency ####
    for x in transaction_details:
        for y in x:
            if y in item_frequency.keys():
                item_frequency[y] = item_frequency[y] + 1
            else:
                item_frequency[y] = 1
    
    sorted_dict = {k: v for k, v in sorted(item_frequency.items(), key=lambda item: item[1])}
    
    priority_dict = {}
    
    i = 1
    for k, v in sorted_dict.items():
        priority_dict[k] = i
        i = i + 1
    
    ordered_transaction_list = []
    for transactions in transaction_details:
        innner_list = []
        for item in transactions:
            innner_list.append((item, priority_dict[item]))
        ordered_transaction_list.append(sorted(innner_list, key=lambda innner_list: innner_list[1], reverse=True))
        
    root = Node('root', count=1)
    #pdb.set_trace()
    for item_list in ordered_transaction_list:
        current_node = root
        for item in item_list:
            #print(item)
            #idx = item_list.index(item)
            #print(RenderTree(root, style=AsciiStyle()).by_attr())
            if item[0] in [node.name for node in current_node.children]:
                new_node = find(current_node, lambda node: node.name == item[0] and node.parent == current_node)
                count = new_node.count
                #print(count)
                new_node.count = count + 1
            else:
                new_node = Node(item[0], parent=current_node, count=1)
            current_node = new_node

    print(RenderTree(root, style=AsciiStyle()).by_attr('name'))
    #print(RenderTree(root))
    
    conditional_pattern_base_dict = {}
    
    #w = Walker()
    #w.walk(Node("root"), Node(key))
    
    for key, value in sorted_dict.items():
        conditional_pattern_base_dict[key] = findall(root, filter_=lambda node: node.name == key)
        #findall_by_attr(root, key, name=key, maxlevel=None, mincount=None, maxcount=None)
        #[find(root, lambda node: node.name == key)]
    
    print(conditional_pattern_base_dict['I5'][-1])
    
    #json_exporter = JsonExporter(indent=2, sort_keys=False)
    #dict_exporter = DictExporter()
    #dict_tree = dict_exporter.export(root)
    
    #print(dict_tree)
    
    #pdb.set_trace()
    RenderTreeGraph(root).to_picture("lang_entropy/static/lang_entropy/images/tree.png")
    
    context = {
        'dict_transactions': sorted_dict,
        'ordered_list' : ordered_transaction_list,
    }
    
    return render(request, 'lang_entropy/list_state.html', context)