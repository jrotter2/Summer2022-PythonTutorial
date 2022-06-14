# Python Tutorial
The goal of this tutorial is to build familiarity with python and ROOT through development of a plotting script.

## Creating a file
You can create a file using the `touch` command
```
touch <filename>.<ext>
```

## Opening the file
You can edit files through the CLI using `vim`
```
vi <path>/<to>/<file>/<filename>.<ext>
```
For example,
```
vi plotter.py
```

Then to save you can press `ESC` and write `:w`. Similarly, to quit you can press `ESC` and write `:q`. To do both at the same time, press `ESC` then `:wq`.

## Importing ROOT
ROOT is natively written in `C++` but has been adapted to `Python` using PyROOT.We can easily import PyROOT when in a CMSSW Environment adding, 
`import ROOT` to the top of the `plotter.py` file.

## Defining Functions
In python you define functions using the sytax,
```
def functionName(vars):
    #FUNCTION CODE GOES HERE
```
