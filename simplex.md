# Simplex
The implemented simplex algorithm is based on the [modified simplex method](https://doi.org/10.1016/0169-7439(90)80112-J). The modified simplex algorithm is searching for the global optimum using a shape consisting of N+1 vertices, n is the number of dimensions that the simplex is being executed on. Each vertex has different coordinates. The coupling intensity of the vertices is measured on their own coordinates and sorted with N=N+1 as the best vertex with highest coupling intensity and N=0 as the vertex with the worst coupling intensity. The vertices are put in an list Points(n)

<img src="/docs/images/Simplex_coordinates.png" alt="drawing" width="500"/>

<sub>C. Gabler, K. L. (1987). An optical alignment robot system. Proc. SPIE Integr. Packag. Optoelectron. Devices, vol. 703, 8-28.

L,M and H are the initial vertices of the vertex, L being the worst and H being the best.
## Operation

<img src="/docs/images/Simplex_flowchart.png" alt="drawing" width="500"/>

<sub>C. Gabler, K. L. (1987). An optical alignment robot system. Proc. SPIE Integr. Packag. Optoelectron. Devices, vol. 703, 8-28.

![Simplex path 2d](/docs/images/simplex2d.gif)
![Simplex path 3d](/docs/images/simplex3d.gif)

![test](/docs/Equations/centroid.png)

![test](/docs/Equations/Reflection.PNG)

![test](/docs/Equations/Expention.PNG)
![test](/docs/Equations/incontraction.PNG)
![test](/docs/Equations/incentroid.PNG)
![test](/docs/Equations/inreflection.PNG)
![test](/docs/Equations/excontraction.PNG)
![test](/docs/Equations/excentroid.PNG)
![test](/docs/Equations/exreflection.PNG)