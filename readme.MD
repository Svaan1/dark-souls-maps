# dark-souls-maps

After a failed "Airport Connections" interview question i decided to review the subject by implementing the concept of graphs with the Dark Souls maps, which, for allowing backtrack, are undirected graphs (they dont have direction restriction).

Note: The code layout works for any given graph, made them dark souls maps just for fun and to make them a little bit useful

Another Note: i plan to increase the complexity of the project by adding information to each node and edge, like bosses and gameplay restrictions (for example only being able to access certain areas when having certain requirements)

## Usage Example

### Creating a map visualization:

Input:

```
my_map = DarkSoulsMap(3)
my_map.create_visualization()

# you can also use a faster approach

DarkSoulsMap(3).create_visualization()

```

Outputs an interactive graph as an html file:

![image](https://user-images.githubusercontent.com/86506395/189635300-9d5ddfb5-025f-43fa-8df7-88a9da88a978.png)

### Creating a route visualization

Input:

```
my_map = DarkSoulsMap(2)
my_route = my_map.find_smallest_route("Majula", "Undead Crypt")
my_route.create_visualization()

# same as before, you can also use a more direct approach

DarkSoulsMap(2).find_smallest_route("Majula", "Undead Crypt").create_visualization()
```

Outputs another interactive graph:

![image](https://user-images.githubusercontent.com/86506395/189636459-27565ae7-cc10-4ab1-b29b-6da4d1601a6d.png)
