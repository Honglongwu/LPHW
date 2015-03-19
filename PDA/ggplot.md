# The introduction of GGPLOT
## Outline
1. Data
2. Mapping
3. Geom
4. Stats
5. scale
6. coord
7. facet
8. Theme
9. Output
  All these elements can be glued together with "+" symbol that making plotting become intersting

### Data
The input data must be structured as dataframe
%+% change the content of figure without re-run the code
eg:
	p <- ggplot(mtcars, aes(mpg, wt, colour = cyl)) + geom_point()
	mtcars_c <- transform(mtcars, mpg = mpg ^ 2)
	p %+% mtcars_c
we can group our data with one element, but if we want to split data with more than one
variables, melt and cast functions of reshape2 pacakge can do it.
	mtcars.m <- melt(mtcars, id = c("mpg", "disp", "hp", "drat", "wt", "qsec", "vs", "carb"))
I will extend reshape2 and plyr package in the following days

### Mapping
1. The Data related with Elements of figure
2. mapping and setting
3. group
	ggplot(data = mtcars, mapping = aes(x = wt, y = hp, group = factor(gear))) + geom_line()
### Layer
1. mapping
	p <- ggplot(mtcars, aes(x = mpg, y = wt, color = factor(gear)))
	p + geom_point()
	p + geom_point(aes(shape = factor(carb))) 
	p + geom_point(aes(y = carb))) 
	p + geom_point(aes(color = NULL))
 
2. more than one datasets or vectors
	mtcars.c <- transform(mtcars, mpg = mpg^2)
	geom_point(aes(x = hp, y = mpg), data = mtcars, color = "red") + 
  	geom_point(aes(x = mtcars$hp, y = mtcars$disp), color = "green")+ 
  	geom_point(aes(x = hp, y= mpg), data = mtcars.c, color = "blue")
 
