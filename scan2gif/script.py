#! /usr/bin/python3

import subprocess, argparse

# Do not crash if there are no colors
try:
    from color import yellow, magenta
except ImportError:
    yellow = magenta = lambda a:a

# Defaults values
DEFAULT_WIDTH = 150 # mm
DEFAULT_HEIGHT = 210 # mm
DEFAULT_RESOLUTION = 150 # dpi
DEFAULT_DELAY = 24 # ms
DEFAULT_ROTATION = 0 # degrees

# Commands
scan_cmd = "scanimage -x {width} -y {height} --resolution {resolution} --format png"
gif_cmd = "convert -delay {delay} {input_files} -rotate {rotate} {output_file}"

def main():
    parser = argparse.ArgumentParser(description='Scan n images to png and make a gif with them.')
    parser.add_argument('n', type=int, help='number of elements in the sequence')
    parser.add_argument('name', help='name of the sequence')
    parser.add_argument('--width', '-W', type=int, default=DEFAULT_WIDTH, help='width of the scanning area (in mm)')
    parser.add_argument('--height', '-H', type=int, default=DEFAULT_HEIGHT, help='height of the scanning area (in mm)')
    parser.add_argument('--delay', '-d', type=int, default=DEFAULT_DELAY, help='delay between images (in ms)')
    parser.add_argument('--resolution', '-r', type=int, default=DEFAULT_RESOLUTION, help='scanning resolution (in dpi)')
    parser.add_argument('--rotate', '-R', type=int, default=DEFAULT_ROTATION, help='rotate (in degrees)')
    args = vars(parser.parse_args())

    # Make PNG from scan
    png_list = []
    for i in range(args['n']):
        fi_name = '{}-{}.png'.format(args["name"], i)
        png_list.append(fi_name)
        with open(fi_name, 'wb') as fi:
            subprocess.call(scan_cmd.format(**args), shell=True, stdout=fi)
        print(yellow(fi_name))

    # Make GIF from PNG
    inp = ' '.join(png_list)
    out = '{}.gif'.format(args["name"])
    subprocess.call(gif_cmd.format(**args, input_files=inp, output_file=out), shell=True)
    print(magenta(out))

if __name__ == '__main__':
    main()