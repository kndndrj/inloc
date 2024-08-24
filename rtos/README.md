# Real-Time Operating System

| Language | Lines of Code |
| :------: | :-----------: |
|    C     |      96       |

## Running

Install prerequisites:

- `avrdude`
- `avr-gcc`
- `avr-libc`
- `avr-binutils`

Connect Arduino UNO to the PC using a USB cable and find the device using:

```sh
ls /dev/ttyUSB*
```

Once you know the name of the port, run the build script by passing the port as the first argument:

```sh
./build.sh <port>
```

## Sources

Code from [AVR example](https://www.cs.ucr.edu/~vahid/rios/rios_avr.htm) on RIOS Website.

## License

For C code:

```
Developed by: Frank Vahid and Bailey Miller, University of California Riverside; and Tony Givargis,
University of California Irvine.

Refer to the source website for licensing.
```
