# Listens for keystrokes and moves the turret in the appropriate direction
# WASD for motion
# E to toggle LED
# F to fire

# Alan Ness
# https://github.com/Avidness

import sys
import termios
import contextlib
import movement

@contextlib.contextmanager
def raw_mode(file):
	old_attrs = termios.tcgetattr(file.fileno())
	new_attrs = old_attrs[:]
	new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
	try:
		termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
		yield
	finally:
		termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)

def main():
	onOff = False 
	movement.init()
	with raw_mode(sys.stdin):
		try:
			while True:
				ch = sys.stdin.read(1)
				if not ch or ch == chr(4):
					break
				if str(ch) == 'a':
					movement.left(200)
				if str(ch) == 'd':
					movement.right(200)
				if str(ch) == 'w':
					movement.up(100)
				if str(ch) == 's':
					movement.down(100)
				if str(ch) == 'f':
					movement.fire()
				if str(ch) == 'e':
					movement.led_toggle(onOff)
					onOff = not onOff
		except (KeyboardInterrupt, EOFError):
			pass

if __name__ == '__main__':
	main()
