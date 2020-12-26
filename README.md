# Logic Circuits <img src="images/diodo.png" height=25>
A logic circuits simulator program through textual description, in Python3.

## Steps to use

* You need to **translate** the visual circuit to textual;
* You need to **run** the main.py file.

## Translate

Visual Circuit Example:

![](images/visual%20circuit.png)

To translate to text, you need create a .txt file in the folder **descriptions**, following the format below:
```
n_inputs,[number of inputs],[input name1],[...],[input nameN]
n_outputs,[number of outputs],[output name1],[...],[output nameN]
n_gates,[number of gates],[gate name1],[...],[gate nameN]
[gate name1],[type gate],[output name],[input name1],[...],[input nameN]
[...]
[gate nameN],[type gate],[output name],[input name1],[...],[input nameN]
```
**Obs¹:* Gate types supported: And, Nand, Or, Nor, Xor, Xnor, Not.

So, the example of visual circuit above, in text is:
```
n_inputs,3,Cin,A,B
n_outputs,2,S,Cout
n_gates,5,g1,g2,g3,g4,g5
g1,xor,y1,A,B
g2,xor,S,y1,Cin
g3,and,y2,y1,Cin
g4,and,y3,B,A
g5,or,Cout,y2,y3
```

## Run

To run the program, you need to install the [Python3](https://www.python.org/downloads/) in your machine. After you ran the main.py file,
the .txt truth table file, with all input test cases, will be genereted in the folder **truth tables**. For the visual example used, it will be like:
```
|   Cin |   A |   B |   S |   Cout |
|-------+-----+-----+-----+--------|
|     0 |   0 |   0 |   0 |      0 |
|     0 |   0 |   1 |   1 |      0 |
|     0 |   1 |   0 |   1 |      0 |
|     0 |   1 |   1 |   0 |      1 |
|     1 |   0 |   0 |   1 |      0 |
|     1 |   0 |   1 |   0 |      1 |
|     1 |   1 |   0 |   0 |      1 |
|     1 |   1 |   1 |   1 |      1 |
```
**Obs²:* All the files in the folder **descriptions**, will have their respective truth tables, in the folder, **truth tables**.


## Contributing

1. Fork it (<https://github.com/rafaelalmeida2909/Logic-Circuits/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
