import os
import importlib
import argparse
import sys

sys.path.append(os.path.abspath("./modules/"))

parser = argparse.ArgumentParser(description="")
parser.add_argument('--model', type=str, help='')

args = parser.parse_args()

imported_modules = []

print("Installed modules:")

for filename in os.listdir("./modules/"):
    if filename.endswith("_five_module.py"):
        module_name = filename[:-3]

        try:
            module = importlib.import_module(module_name)
            imported_modules.append(module)

            print(f"[{imported_modules.index(module)}] {module.NAME}")
        except:
            pass

selected_module = imported_modules[int(input("Enter number: "))]

selected_module.run()

