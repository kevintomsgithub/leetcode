# import numpy as np

# class selfReplaceBomb():
#     def __init__(self):
#         self.transition_prob = {
#             'M': {
#                 'M': 0.5,
#                 'F': 0.5
#             },
#             'F': {
#                 'F': 0.5,
#                 'M': 0.5
#             }
#         }
#         self.states = list(self.transition_prob.keys())

#     def next_state(self, current_state):
#         left_node = [sum()]
#         return np.random.choice(
#             self.states,
#             p=[self.transition_prob[current_state][next_state]
#                 for next_state in self.states]
#         )

#     def next_state(self, current_state):
#         left_node = [sum()]
#         return np.random.choice(
#             self.states,
#             p=[self.transition_prob[current_state][next_state]
#                 for next_state in self.states]
#         )
    
#     def generate_states(self, current_state, n=10):
#         future_states = []
#         for _ in range(n):
#             next_state = self.next_state(current_state)
#             future_states.append(next_state)
#             current_state = next_state
#         return future_states



# def solution_org(x, y):
#     x, y = int(x), int(y)
#     destination = str([x, y])
#     destination_rev = str(destination[::-1])
#     destination_sum = sum([x, y])
#     start = [1, 1]
#     queue = [start]
#     distance = {
#         str(start): 0
#     }
#     def add_to_queue(n, c):
#         node_str = str(n)
#         node_str_rev = str(n[::-1])
#         c_str = str(c)
#         queue.append(n)
#         if node_str not in distance and node_str_rev not in distance:
#             if node_str in distance:
#                 distance[node_str] += 1
#             else:
#                 distance[node_str] = distance[c_str] + 1

#     while queue:
#         print('\nQueue:     ', queue)
#         print('Distance: ', distance)
#         s = queue.pop(0)
#         # if s[0] > x and s[1] > y:
#         #     return "impossible"
#         if sum(s) > destination_sum:
#             return "impossible"

#         if destination in distance:
#             # return f"{distance[destination]}"
#             return "{}".format(distance[destination])

#         if destination_rev in distance:
#             # return f"{distance[destination_rev]}"
#             return "{}".format(distance[destination_rev])

#         left_node = [sum(s), s[1]]
#         right_node = [s[0], sum(s)]
#         add_to_queue(left_node, s)
#         add_to_queue(right_node, s)



# def solution_old(x, y):
#     x, y = int(x), int(y)
#     destination = str([x, y])
#     destination_rev = str(destination[::-1])
#     destination_sum = sum([x, y])
#     start = [1, 1]
#     queue = [start]
#     distance = { str(start): 0 }
    
#     def add_to_queue(n, c):
#         node_str = str(n)
#         # node_str_rev = str(n[::-1])
#         c_str = str(c)
#         queue.append(n)
#         if node_str in distance:
#             distance[node_str] += 1
#         else:
#             distance[node_str] = distance[c_str] + 1
#     while queue:
#         print('Queue: ', queue)
#         s = queue.pop(0)
#         if sum(s) > destination_sum:
#             return "impossible"
        
#         if destination in distance:
#             return "{}".format(distance[destination])
#         if destination_rev in distance:
#             return "{}".format(distance[destination_rev])
            
#         left_node = [sum(s), s[1]]
#         right_node = [s[0], sum(s)]
#         add_to_queue(left_node, s)
#         add_to_queue(right_node, s)


# def algebra_old(x, y):
#     x, y = int(x), int(y)
#     depth = 0
#     while 1:
#         if [x, y] == [1, 1]:
#             return str(depth)
#         if x == y:
#             return "impossible"
#         elif x>y:
#             x -= y
#         elif x<y:
#             y -= x
#         depth += 1


# def algebra(x, y):
#     x, y = int(x), int(y)
#     depth = 0
#     while 1:
#         if x == 1:
#             depth += y-1
#             return str(depth)
#         if y == 1:
#             depth += x-1
#             return str(depth)

#         if x == 2:
#             if y%x == 0:
#                 return "impossible"
#         if y == 2:
#             if x%y == 0:
#                 return "impossible"

#         if x == y:
#             return "impossible"
#         elif x>y:
#             depth = x//y
#             x = x%y
#         elif x<y:
#             depth = y//x
#             y = y%x
#         depth += 1

def solution_asd(x, y):
    x, y = int(x), int(y)
    depth = 0
    while 1:
        if x == 0 or y == 0:
            return "impossible"
        if x == 1:
            depth += y-1
            return str(depth)
        if y == 1:
            depth += x-1
            return str(depth)
        
        if x == 2:
            if y%x == 0:
                return "impossible"
        if y == 2:
            if x%y == 0:
                return "impossible"
        
        if x == y:
            return "impossible"
        elif x>y:
            depth += x//y
            x = x%y
        elif x<y:
            print(x, y)
            depth += y//x
            y = y%x
        
    
x = solution('36', '18')
print(x)

def solution(x, y):
    x, y = int(x), int(y)
    depth = 0
    while 1:
        # Checking cases with 0
        if x == 0 or y == 0:
            return "impossible"
        # Checking cases with 1
        if x == 1:
            depth += y-1
            return str(depth)
        if y == 1:
            depth += x-1
            return str(depth)
        # Checking cases with 2
        if x == 2:
            if y%x == 0:
                return "impossible"
        if y == 2:
            if x%y == 0:
                return "impossible"
        # Checking cases with numbers
        if x == y:
            return "impossible"
        elif x>y:
            # Returning to the parent node and incrementing depth
            depth += x//y
            x = x%y
        elif x<y:
            # Returning to the parent node and incrementing depth
            depth += y//x
            y = y%x