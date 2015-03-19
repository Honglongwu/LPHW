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
	mtcars.m <- melt(mtcars, id = )
