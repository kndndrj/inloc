#!/bin/sh

cc -Wall -g simple-client.c  \
    $(pkg-config --cflags --libs dbusmenu-glib-0.4) \
    $(pkg-config --cflags --libs ayatana-appindicator3-0.1) \
    -DLOCAL_ICON="\"$(pwd)/simple-client-test-icon.png\""
