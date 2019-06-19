# scan2gif

scan2gif is a simple command line tool to quikly make gif from scans.

For help, run `python3 scan2gif -h`.

## Install


Install dependencies :

    # apt-get install sane-utils 
    # apt-get install imagemagick

Install scan2gif :

    # pip install git+https://github.com/LeonLenclos/osc-utils.git@master

### Optional

If you want colorfull file names you can `pip install color`

## Usage

Basically if you want to make a gif called *dancing.gif* from three drawing you must run :

    $ scan2gif 3 dancing

The scanner will scan the 3 drawings in a row. You'll have to be as fast as he is to change the drawings between each pass.

There is some options. Run `python3 scan2gif -h` to know them.

## Copying

This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the LICENSE file for more details.

