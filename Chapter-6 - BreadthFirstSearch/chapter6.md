# Summary of Chapter - 6

###  Breadth First Search

- 1. The algorithm to solve a shortest-path problem is called breadth-first search.
- 2. Graphs are a way to model how different things are connected to one another.

### Queue & BFS
- 1. `Enqueue` add an item to queue
- 2. `Dequeue` remove an item from the queue 
- 3. `FIFO`-First In, First Out-Queue 
- 4. `LIFO` - Last In , First Out - Stack
- 5. Hash Table is used to represent the graphs. 
- 6. Each key is mapped to an array of neighbouring nodes . 
- 7. BFS PseudoCode:
        - Pop from queue
        - Check if the node is not visited 
        - If not visted 
        - check if it meets the condition , if yes , you are done , if not add its neighbours to the queue
        - keep doing this untill your condition is satisfied . 
- 8. BFS complexity is O(Verices+Edges)

### Tree

- 1. A tree is a special type of graph, where no edges ever point back.
