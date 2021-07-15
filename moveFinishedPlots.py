import sys
from os import listdir, remove
from os.path import isfile, join
import shutil
import time

def freeSpace(deletionDir, numPlots):
	"""
	Deleted at most <numPlots> many files from deletionDir. The assumption is that
	deletionDir only contains plots of the same size as the new plots they are evicted for.
	"""
	print(f"Disk full. Trying to make space for {numPlots} plots by deleting old plots from {deletionDir}.")
	plotFiles = [f for f in listdir(deletionDir) if isfile(join(deletionDir, f)) and (".plot" in f or ".PLOT" in f)]
	for i in range(numPlots):
		if i < len(plotFiles):
			filePath: str = join(deletionDir, plotFiles[i])
			print(f"Removing old plot file {filePath}")
			remove(filePath)


if len(sys.argv) < 2:
	print(f"Usage: {sys.argv[0]} <source directory> <target directory> [<target to delete files from when necessary>]", file=sys.stderr)
	sys.exit(1)

source: str = sys.argv[1]
target: str = sys.argv[2]
deletionDir: str = None
if len(sys.argv) == 4:
	deletionDir = sys.argv[3]

while True:
	print(f"Looking for plot files in {source}.")
	sourceFiles = [f for f in listdir(source) if isfile(join(source, f)) and (".plot" in f or ".PLOT" in f)]
	numPlots: int = len(sourceFiles)
	print(f"Found {numPlots} plots in {source}.")
	_, _, free = shutil.disk_usage(target)
	if deletionDir != None and free < 100*2**30:
		freeSpace(deletionDir, numPlots)
	t: float = time.monotonic()
	for f in sourceFiles:
		print(f"Moving file {f} from {source} to {target}.")
		shutil.move(join(source, f), join(target,f))
	if numPlots > 0:
		t = time.monotonic() - t
		print(f"Moving {numPlots} to {target} took {t/60} minutes.")
	print("Waiting 30 minutes and then checking again.")
	time.sleep(1800)

