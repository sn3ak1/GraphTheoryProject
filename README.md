# Graph Theory Project

My implementation of Ford-Fulkerson method for Maximum Flow Problem written in python.

## Requirements
Make sure you have installed all of the following prerequisites on your machine:
* Git - [Download Git](https://git-scm.com/downloads) (OSX and Linux machines typically have this already installed.)
* Python - [Download Python](https://www.python.org/getit/)

## Setup

The first thing to do is to clone the repository:

```sh
git clone https://github.com/sn3ak1/GraphTheoryProject.git
```
Then go to the project directory
```
cd GraphTheoryProject
```

## Usage

Import graph by putting adjacency matrix in `data.txt`

Example data.txt content:
```
0, 1, 0, 2, 0,
0, 0, 1, 0, 0,
0, 0, 0, 0, 2,
0, 0, 1, 0, 1,
0, 0, 0, 0, 0,
```
You can generate graphs in this format here: <https://graphonline.ru/en/>

Run the algorithm by typing:
```sh
python main.py
```
Next script will ask to provide source node index. If you click enter without typing anything first node will be chosen as source.  
Similarly, with the sink node but last node is default.

The output will be maximum flow and paths taken. Edges in path are represented by: \[start node, end node, flow/capacity]
