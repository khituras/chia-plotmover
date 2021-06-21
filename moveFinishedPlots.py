import sys
from os import listdir
from os.path import isfile, join
import shutil
import time

if len(sys.argv) < 2:
	print(f"Usage: {sys.argv[0]} <source directory> <target directory>", file=sys.stderr)
	sys.exit(1)

source: str = sys.argv[1]
target: str = sys.argv[2]

while True:
	print(f"Looking for plot files in {source}.")
	sourceFiles = [f for f in listdir(source) if isfile(join(source, f)) and (".plot" in f or ".PLOT" in f) ]
	numPlots: int = len(sourceFiles)
	print(f"Found {numPlots} plots.")
	t: float = time.monotonic()
	for f in sourceFiles:
		print(f"Moving file {f} from {source} to {target}.")
		shutil.move(join(source, f), join(target,f))
	if numPlots > 0:
		t = time.monotonic() - t
		print(f"Moving {numPlots} to {target} took {t/60} minutes.")
	print("Waiting 30 minutes and then checking again.")
	time.sleep(1800)

