# nuitka-project: --product-name=IRON SOL Better Controls
# nuitka-project-set: PATCHER_VERSION = "1.0.0"
# nuitka-project: --product-version={PATCHER_VERSION}
# nuitka-project-if: {OS} == "Windows":
#   nuitka-project: --output-filename=IRON_SOL_Better_Controls_v{PATCHER_VERSION}-win.exe
# nuitka-project-else:
#   nuitka-project: --output-filename=IRON_SOL_Better_Controls_v{PATCHER_VERSION}-linux.bin

# nuitka-project: --mode=app
# nuitka-project: --windows-console-mode=force
# nuitka-project: --linux-app-console-mode=force

import time

from pynput import keyboard

JUMP_KEY_MACRO = "z"
ABILITY_KEY_MACRO = "c"

JUMP_KEY = "x"
ABILITY_KEY = "v"

FRAME_DURATION = 1 / 30

def on_press(key):
	if key == keyboard.KeyCode.from_char(JUMP_KEY_MACRO):
		print("\rJump key macro pressed.   ", end="")
		controller.tap(JUMP_KEY)
		controller.release(ABILITY_KEY)
	elif key == keyboard.KeyCode.from_char(ABILITY_KEY_MACRO):
		print("\rAbility key macro pressed.", end="")
		controller.release(ABILITY_KEY)
		controller.press(ABILITY_KEY)
		controller.release(ABILITY_KEY)
	else:
		return

	time.sleep(FRAME_DURATION)
	controller.press(ABILITY_KEY)

if __name__ == "__main__":
	controller = keyboard.Controller()

	print("IRON SOL Better Controls started. Press Ctrl+C to exit.")

	controller.press(ABILITY_KEY)

	try:
		with keyboard.Listener(on_press=on_press) as listener:
			listener.join()
	except KeyboardInterrupt:
		pass
	finally:
		listener.stop()
