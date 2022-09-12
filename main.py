import networkx as nx
from pyvis.network import Network
import json


class DarkSoulsMap():
    def __init__(self, game_number):
        self.game_number = game_number
        self.map = self.choose_map(game_number)

    def choose_map(self, game_number):
        maps_file = open("maps.json")
        maps_dict = json.load(maps_file)
        maps_list = [maps_dict[key] for key in maps_dict.keys()]

        desired_map = game_number - 1

        return maps_list[desired_map]

    def create_network(self):
        map_graph = nx.DiGraph(self.map)

        network = Network(notebook=True, height='750px', width='100%')
        network.from_nx(map_graph)
        
        return network
    
    def create_visualization(self):
        self.create_network().show(f"visualizations/dark_souls_{self.game_number}_map.html")

    def find_all_routes(self, start, end, current_path=[], path_list=[]): # Maybe this one
        current_path.append(start)

        if start == end:
            path_list.append(DarkSoulsRoute(self, current_path))
            return

        for area in self.map[start]:
            if area not in current_path:
                new_path = []
                new_path.extend(current_path)
                self.find_all_routes(area, end, new_path, path_list)
        return path_list
    
    def find_smallest_route(self, start, end):
        routes = self.find_all_routes(start, end)
        smallest_route = min(routes, key=len)
        return smallest_route

class DarkSoulsRoute():
    def __init__(self, map, array):
        self.map = map
        self.array = array

    def __len__(self):
        return len(self.array)
    
    def create_network(self):
        network = Network(notebook=True, height='750px', width='100%')
        network.add_nodes(self.array)

        current_area = 0
        while True:
            try:
                network.add_edge(self.array[current_area], self.array[current_area + 1])
                current_area += 1
            except:
                break

        return network
    
    def create_visualization(self):
        self.create_network().show(f"visualizations/dark_souls_{self.map.game_number}_route.html")

my_map = DarkSoulsMap(2).find_smallest_route("Majula", "Undead Crypt").create_visualization()