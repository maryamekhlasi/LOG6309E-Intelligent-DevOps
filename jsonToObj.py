from asyncore import compact_traceback
import json
from types import SimpleNamespace
from anytree import Node, RenderTree 
import itertools
import networkx as nx
from matplotlib import pyplot as plt
from numpy import true_divide



class MyNode:
    pass


f = open('traces.txt','r')
 
# returns JSON object as
# a dictionary
data = json.load(f)
data2 = data

#print(" ParentTraceID= " + data["data"][0]["spans"][0]["traceID"] + " spanID= " + data["data"][0]["spans"][0]["spanID"] + " Name= "+ data["data"][0]["spans"][0]["operationName"])




jsonlen= len(data["data"][0]["spans"])
#print("len = " + str(len(data["data"][0]["spans"])))

node = MyNode()
for i in range(0, jsonlen, 1): 
    node.spanID = data["data"][0]["spans"][i]["spanID"]
    node.operationName = data["data"][0]["spans"][i]["operationName"]
    node.startTime = data["data"][0]["spans"][i]["startTime"]
    node.duration = data["data"][0]["spans"][i]["duration"]
    if i == 0:
        root = Node(node)
    else:
        Node(node, parent=root)
    node = MyNode()

#print(RenderTree(root))
for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, (node.name).operationName))


traceCount= len(data["data"])
spanCount= len(data["data"][0]["spans"])

"""
node = MyNode()
list_of_tuple=[]
for i in range(0, traceCount, 1):
    for j in range(0, spanCount, 1):
        node.spanID = data["data"][i]["spans"][j]["spanID"]
        node.operationName = data["data"][i]["spans"][j]["operationName"]
        node.startTime = data["data"][i]["spans"][j]["startTime"]
        node.duration = data["data"][i]["spans"][j]["duration"]
        if len(data["data"][i]["spans"][j]["references"])!=0 :
            node.parentTraceId = data["data"][i]["spans"][j]["references"][0]["traceID"]
            node.parentSpanId = data["data"][i]["spans"][j]["references"][0]["spanID"]
        #tuple = (data["data"][i]["traceID"], node)
        tuple = (node.operationName, node)
        list_of_tuple .append(tuple)
        node = MyNode()
"""

graph = nx.DiGraph()
node = MyNode()
list_of_tuple=[]
list_of_tuple2=[]
list_of_tuple_time=[]
for i in range(0, traceCount, 1):
    for j in range(0, spanCount, 1):
        node.spanID = data2["data"][i]["spans"][j]["spanID"]
        if len(data2["data"][i]["spans"][j]["references"]) == 0:
            print("parent node")
            node.parentSpanID = root
        else:
            node.parentSpanID = data2["data"][i]["spans"][j]["references"][0]["spanID"]
        node.operationName = data2["data"][i]["spans"][j]["operationName"]
        node.startTime = data2["data"][i]["spans"][j]["startTime"]
        node.duration = data2["data"][i]["spans"][j]["duration"]
        graph.add_edge(node.parentSpanID, node.spanID, weight = node.duration)
        tuple = (node.spanID, node)
        list_of_tuple2.append(tuple)
        list_of_tuple.append((node.parentSpanID, node))
        list_of_tuple_time.append((node.startTime, node))
        node = MyNode()


list_of_tuple_time.sort()
list = []
list_time = []
serviceNameSequence=""
serviceDurationSequence=""
for item in list_of_tuple_time:
    list.append(item[1].operationName)
    serviceNameSequence += item[1].operationName +","
    serviceDurationSequence += str(item[1].duration) +","
    list_time.append(item[1].duration)

print(list)
print(list_time)
print(serviceNameSequence)
print(serviceDurationSequence)


f = open("serviceNameSequences.txt", "a")
f.write(serviceNameSequence+'\n')
f.close()

f = open("serviceDurationSequence.txt", "a")
f.write(serviceDurationSequence+'\n')
f.close()









#graph = nx.DiGraph()
#graph.add_edges_from(list_of_tuple)
plt.tight_layout()
nx.draw_networkx(graph, arrows=True)
plt.savefig("graph2.png", format="PNG")
# tell matplotlib you're done with the plot: https://stackoverflow.com/questions/741877/how-do-i-tell-matplotlib-that-i-am-done-with-a-plot
plt.clf()





