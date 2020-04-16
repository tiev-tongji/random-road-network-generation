
EPSILON = 1e-2

SEGMENT_COUNT_LIMIT = 1000

# length
STREET_SEGMENT_LENGTH = 400
STREET_SEGMENT_LENGTH_OFFSET_LIMIT = 200
HIGHWAY_SEGMENT_LENGTH = 1000
HIGHWAY_SEGMENT_LENGTH_OFFSET_LIMIT = 200

# width
STREET_SEGMENT_WIDTH = 6
STREET_SEGMENT_WIDTH_OFFSET_LIMIT = 1
HIGHWAY_SEGMENT_WIDTH = 10

# strench
HIGHWAY_CURVE_DIRECTION_OFFSET_LIMIT = 5
STREET_CURVE_DIRECTION_OFFSET_LIMIT = 5

# heat
STREET_HEAT_THRESHOLD = 0.1
HIGHWAY_BRANCH_HEAT_THRESHOLD = 0.2

# branch
STREET_BRANCH_PROBABILITY = 0.6
STREET_BRANCH_RIGHT_PROBABILITY = 0.5
STREET_BRANCH_LEFT_PROBABILITY = 0.5
HIGHWAY_BRANCH_PROBABILITY = 0.2
HIGHWAY_BRANCH_RIGHT_PROBABILITY = 0.5
HIGHWAY_BRANCH_DIRECTION_OFFSET_LIMIT = 5
STREET_BRANCH_DIRECTION_OFFSET_LIMIT = 5

# degeneration
HIGHWAY_DEGENERATE_PROBABILITY = 0.8

# time delay
BRANCH_TIME_DELAY_HIGHWAY = 5
BRANCH_TIME_DELAY_STREET = 0
STRENCH_TIME_DELAY_HIGHWAY = 1
STRENCH_TIME_DELAY_STREET = 0

# local constrains
MINIMUM_INTERSECTION_DEVIATION = 30 
ROAD_SNAP_DISTANCE = 50
QUADTREE_PARAMS_X = -20000
QUADTREE_PARAMS_Y = -20000
QUADTREE_PARAMS_W = -40000
QUADTREE_PARAMS_H = -40000
