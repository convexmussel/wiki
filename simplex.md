# Simplex
The implemented simplex algorithm is based on the [modified simplex method](https://doi.org/10.1016/0169-7439(90)80112-J). The modified simplex algorithm is searching for the global optimum using a shape consisting of N+1 vertices, n is the number of dimensions that the simplex is being executed on. Each vertex has different coordinates. The coupling intensity of the vertices is measured on their own coordinates and sorted with n=N+1 as the best vertex with highest coupling intensity and n=0 as the vertex with the worst coupling intensity. The vertices are put in an list Points<sub>n

The simplex algorithm requires first light to reliably converge on the global optimum of the PIC-fiberarry interface.  

<img src="https://github.com/convexmussel/wiki/blob/master/images/simplex2d.gif?raw=true" width="500">
<img src="https://github.com/convexmussel/wiki/blob/master/images/simplex3d.gif?raw=true" width="500"><br>
The above two GIF's are a demonstration how the simplex algorithm shrinks and grows to converge on the global optimum. Plaatjes moeten nog verbeterd worden.

## Code example

```python
print "hello world"
```






## Operation
<img src="https://github.com/convexmussel/wiki/blob/master/images/Simplex_coordinates.png?raw=true" width="400"><br>
<img src="https://github.com/convexmussel/wiki/blob/master/images/Simplex_flowchart.png?raw=true" width="800"><br>

<sub>C. Gabler, K. L. (1987). An optical alignment robot system. Proc. SPIE Integr. Packag. Optoelectron. Devices, vol. 703, 8-28.

In this situation L,M and H are the initial vertices of the vertex, L being the worst and H being the best. The vertices are sorted so that Points<sub>N+1</sub> = H and Points<sub>0</sub> = L. Then the operations are executed like in the flowchart above. When the shape changes (ea initial vertices change) a iteration of the algorithm has been executed

The locations of the potentially better vertices are calculated using the formulas below


<img src="https://github.com/convexmussel/wiki/blob/master/Equations/centroid.PNG?raw=true" width="250"><br>
<img src="https://github.com/convexmussel/wiki/blob/master/Equations/Reflection.PNG?raw=true" width="250"><br>
<img src="https://github.com/convexmussel/wiki/blob/master/Equations/Expention.PNG?raw=true" width="250"><br>
<img src="https://github.com/convexmussel/wiki/blob/master/Equations/incontraction.PNG?raw=true" width="250"><br>
<img src="https://github.com/convexmussel/wiki/blob/master/Equations/incentroid.PNG?raw=true" width="250"><br>
<img src="https://github.com/convexmussel/wiki/blob/master/Equations/inreflection.PNG?raw=true" width="250"><br>
<img src="https://github.com/convexmussel/wiki/blob/master/Equations/excontraction.PNG?raw=true" width="250"><br>
<img src="https://github.com/convexmussel/wiki/blob/master/Equations/excentroid.PNG?raw=true" width="250"><br>
<img src="https://github.com/convexmussel/wiki/blob/master/Equations/exreflection.PNG?raw=true" width="250"><br>
