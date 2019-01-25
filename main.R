library(BoxPacking)

# create medical package
# setClass("Med", slots=list(ID="character", Weight="numeric", Box(length = "numeric", height = "numeric", width = "numeric"  )))

# Med1 = new("Med", a = 12, b = 42)

Box1 = Box(length = 14, height = 5, width = 7)
Box2 = Box(length = 5, height = 8, width = 5)
Box3 = Box(length = 12, height = 4, width = 7)


# create containers
containers <- list()
n_containers <- 4

for (i in 1:n_containers) {
  containers <- c(containers,
                  Container(length = 2, height = 2, width = 2)
  )
}
# print(Med1)

# create boxes
boxes <- list()
n_boxes <- 20

for (i in 1:30) {
  length <- sample(c(0.4, 0.5, 1), 1)
  height <- sample(c(0.4, 0.5, 1), 1)
  width <- sample(c(0.4, 0.5, 1), 1)
  
  boxes <- c(boxes, Box(length = length, height = height, width = width) )
  # boxes <- c(boxes, Box1)
}

# Box Packing
solution <- PerformBoxPacking(containers = containers,
                    boxes = boxes,
                    n_iter = 4,
                    population_size = 20,
                    elitism_size = 5,
                    crossover_prob = 0.5,
                    mutation_prob = 0.5,
                    verbose = TRUE,
                    plotSolution = TRUE )



