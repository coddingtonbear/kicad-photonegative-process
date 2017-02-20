# Kicad Photonegative Process

The photographic method of making PCBs requires plotting the front and
back layers of your board using different settings (both must be negatives,
but only the front layer has to be mirrored, of course).  This alone wouldn't
be too hard to manage, but once you begin working with mask and paste layers
(positives, but front layers still must be mirrored), making sure the
proper plotting settings are selected for each layer becomes error prone.
This solves that problem by making it easy for you to generate all of your
board plots correctly every single time.

## Installation

Either copy or symlink `default_plot.py` into Kicad's python path.

You can get a list of paths by opening "Tools" -> "Scripting Console" in
PCBNew and running the following commands:

```python
import sys
sys.path
```

## Use

Open the Kicad scripting console using "Tools" -> "Scripting Console" in
PCBNew and running the following commands:

```python
import default_plot
default_plot.plot()
```
