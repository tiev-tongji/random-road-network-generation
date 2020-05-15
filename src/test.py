from City import City
import logging
from external.OSMGenerator import *
import argparse

RUNTIME_DIR = "../runtime/"
LOG_DIR = RUNTIME_DIR+"log/"
DATA_DIR = RUNTIME_DIR+"out/"


def init_logging(debug = False):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

    logging.basicConfig(
        filename=LOG_DIR + 'road-gen-INFO.log',
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=DATE_FORMAT,
        filemode='w')

    if debug:
        logging.basicConfig(
            filename=LOG_DIR + 'road-gen-DEBUG.log',
            level=logging.DEBUG,
            format=LOG_FORMAT,
            datefmt=DATE_FORMAT,
            filemode='w')

def draw(filename, debug = False):
    for segment in city.segments:
        plt.plot(
            [segment.start.x,
             segment.end.x],
            [segment.start.y,
             segment.end.y],
            color='k' if segment.meta['highway'] else 'b',
            linewidth=2 if segment.meta['highway'] else 1
        )

    if debug:
        for node in city.nodes:
            plt.plot(node.x, node.y, 'ro')
        plt.show()

    plt.savefig(filename, dpi=1024)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A random road generator')
    parser.add_argument('--debug', type=bool, default=False, help='Is using debug mode')
    parser.add_argument('--road_num', type=int, default=2000, help='Road number to generate')
    parser.add_argument('--generate', type=bool, default=True, help='Should generate road OSM file')
    parser.add_argument('--osm_filename', type=str, default='test.osm', help='Output OSM file name')
    parser.add_argument('--plt_filename', type=str, default='test.png', help='Output OSM file name')
    args = parser.parse_args()

    init_logging(args.debug)
    print(args)
    print('')

    print('Start generating city...')
    city = City(args.road_num)
    city.generate()
    print('Done generate, segment num=%d, road num=%d' % (len(city.segments), len(city.ways)))
    print('')

    if args.generate:
        osm = OSMGenerator(city.nodes, city.ways, 1000000)
        print('Writing OSM file...')
        osm.generate(DATA_DIR + args.osm_filename, args.debug)
        print('Written to ' + DATA_DIR + args.osm_filename)
        print('')

    print('Drawing...')
    draw(DATA_DIR + args.plt_filename)
    print('Saved to ' + DATA_DIR + args.plt_filename)
    print('All done')