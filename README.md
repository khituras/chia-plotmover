# chia-plotmover
A simple python script to move finished plots to their final destination.
Usage: `python3 moveFinishedPlots.py <from dir> <to dir>`

The script scans the `<from dir>` in a regular interval, currently 30 minutes. If files with the `.plot` or `.PLOT` extensions are found, those are moved to the `<to dir>`.

The idea is to let the plotter put the final files to some place where it can put them quickly (like a second temporary directory of sorts) and then let this script move the plots to their actual final location.
The removes the time overhead of moving final plot files to potential slow external storages and having the plotter waiting all this time instead of creating new plots.

Of course, this can only work if plotting takes not less time than moving. Thus, this script won't help if you use the [madMAx plotter](https://github.com/madMAx43v3r/chia-plotter) with a strong CPU and a RAM disc and then copy the final plots over a 100mbit network.
