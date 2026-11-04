# nuitka-project: --product-name=IRON SOL Better Controls
# nuitka-project-if: {OS} == "Windows":
#   nuitka-project: --output-filename=IRON_SOL_Better_Controls.exe
# nuitka-project-else:
#   nuitka-project: --output-filename=IRON_SOL_Better_Controls.bin
# nuitka-project: --mode=app
# nuitka-project: --windows-console-mode=force

import time
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

from pynput import keyboard


@dataclass
class Config:
	jump_key_macro: str = field(default="a")
	ability_key_macro: str = field(default="s")
	jump_key: str = field(default="z")
	ability_key: str = field(default="x")

	@classmethod
	def parse(cls, filename: str) -> "Config":
		if Path(filename).exists():
			with Path(filename).open("rb") as f:
				config = cls(**tomllib.load(f))
			print("Loaded config file successfully.")
		else:
			config = cls()
			print("Config file not found. Using default values.")
		return config

config = Config.parse("config.toml")


def print_status(message):
	print("\r" + " " * 30 + "\r" + message, end="", flush=True)

def on_press(key):
	if key == keyboard.KeyCode.from_char(config.jump_key_macro):
		print_status("Jump key macro pressed.")
		controller.tap(config.jump_key)
		controller.release(config.ability_key)
	elif key == keyboard.KeyCode.from_char(config.ability_key_macro):
		print_status("Ability key macro pressed.")
		controller.release(config.ability_key)
		controller.press(config.ability_key)
		controller.release(config.ability_key)
	else:
		return

	FRAME_DURATION = 1 / 30

	time.sleep(FRAME_DURATION)
	controller.press(config.ability_key)

if __name__ == "__main__":
	controller = keyboard.Controller()

	print("Press Ctrl+C to exit.")

	controller.press(config.ability_key)

	try:
		with keyboard.Listener(on_press=on_press) as listener:
			listener.join()
	except KeyboardInterrupt:
		pass
	finally:
		listener.stop()
		del controller
