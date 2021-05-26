# GraphTheoryProject

My implementation of Ford-Fulkerson method for Maximum Flow Problem written in python.

## Setup

The first thing to do is to clone the repository:

```sh
git clone https://github.com/sn3ak1/GraphTheoryProject.git
cd GraphTheoryProject
```
Then run the algorithm by typing:
```sh
python main.py
```

## Usage

Import graph by putting adjacency matrix in data.txt

Example data.txt content:
```
0, 1, 0, 2, 0,
0, 0, 1, 0, 0,
0, 0, 0, 0, 2,
0, 0, 1, 0, 1,
0, 0, 0, 0, 0,
```
Remember to use source as a first node and sink as a last one.

You can generate graphs in this format here: <https://graphonline.ru/en/>