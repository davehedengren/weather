library(sp)
library(maptools)
library(ggplot2)
x <- readShapeSpatial("/Users/davidhedengren/Downloads/study_16796/al_final.shp")
y <- coordinates(x)

polygon <- fortify(x)

square <- aggregate(list(polygon$long, polygon$lat),by=list(polygon$id, polygon$group, polygon$piece), FUN= "min")

s <- aggregate(polygon, by=list(polygon$id, polygon$group, polygon$piece), simplify = TRUE, min)
