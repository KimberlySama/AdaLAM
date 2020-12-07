import argparse
import sys

def x(x_center, y_center):
    print ("X center:", x_center)
    print ("Y center:", y_center)

def main(args):
    parser = argparse.ArgumentParser(description="Do something.")
    parser.add_argument("-x", "--xcenter", type=float, default= 2, required=False)
    parser.add_argument("-y", "--ycenter", type=float, default= 4, required=False)
    args = parser.parse_args(args)
    x(args.xcenter, args.ycenter)

if __name__ == '__main__':
    main(sys.argv[1:])