# Overview

This CLI is used to invoke the musicality python package and provide a friendly interface for the user to try out.

The purpose of the musicality package is to help music players devise new musical excercises for practising on the fly. 

Dexterity excercises for musicians usually do not help much with imagination and improvisation. But! If we find a way to devise excercises that also sound "good" maybe we can breach this gap. This is what musicality aims to achieve, although yet no substantial results can be found. 

The goal is to be able given an initial idea, to create and manipulate melodic excercises that also sound intresting.  

More info regarding musicality python package: https://github.com/estafons/music-exercises

# Installation

User can install with pip:
```
pip install git+ssh://git@github.com/estafons/musicality-cli.git
```

# Basic Usage

run without arguements for --help:

```
musicality
```

or:

```
musicality [COMMAND] --help
```

## Composing with the genetic algorithm


```
musicality compose --help

Usage: musicality compose [OPTIONS]

  Compose a melody based on an initial idea.

Options:
  -i, --idea TEXT    Initial musical idea example: "C D C"  [required]
  -s, --scale TEXT   Scale associated with the idea
  -o, --output TEXT  Output file name
  --help             Show this message and exit.
```


example:
```
musicality compose -i "40 45 47" -s Dm
```

NOTE: Only input as a string of midi notes is implemented currently as shown above.
