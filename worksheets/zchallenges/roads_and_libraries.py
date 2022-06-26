#https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs


"""

given the input:
n = count of cities
c_lib = cost of each library
c_road = cost of each road to connect two cities
cities = array of possible connections between cities represented as edges ([parent, child])

calculate the minimum cost to ensure every city has access to a library.
a city has access if it can travel any number of roads to get to a city with a library built within. 

in some cases it may be cheaper to build libraries in each city.

"""
from collections import deque

def roads_and_libraries(cities, n, c_lib, c_road, ):
    pass