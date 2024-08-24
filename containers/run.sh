#!/bin/sh

UBUNTU_VERSION="${1:-24.04}"
SCRIPT_PATH="$(realpath "$(dirname "$0")")"
echo "$SCRIPT_PATH"

TMPDIR="/tmp/deterministic_termpoprary_directory"
mkdir -p "$TMPDIR"

if [ ! -d "$TMPDIR/rootfs" ]; then
    printf "rootfs not located - downloading it now..."
    curl -sLo "$TMPDIR/image.tar.gz" "https://cdimage.ubuntu.com/ubuntu-base/releases/24.04/release/ubuntu-base-$UBUNTU_VERSION-base-amd64.tar.gz"

    mkdir -p "$TMPDIR/rootfs"
    tar -xzf "$TMPDIR/image.tar.gz" -C "$TMPDIR/rootfs"

    echo "  done"
fi

echo "starting up the container"

cd "$TMPDIR" || exit
sudo go run "$SCRIPT_PATH/main.go" run /bin/bash
