library(BoxPacking)

# create medical package
# setClass("Med", slots=list(ID="character", Weight="numeric", Box(length = "numeric", height = "numeric", width = "numeric"  )))

# Med1 = new("Med", a = 12, b = 42)

Box1 = Box(length = 14, height = 7, width = 5)
Box2 = Box(length = 5, height = 8, width = 5)
Box3 = Box(length = 12, height = 4, width = 7)


# create containers
containers <- list()
n_containers <- 1


for (i in 1:n_containers) {
  containers <- c(containers,
                  Container(length = 8, height = 14, width = 10)
  )
}


# containers < c(containers, Container(length = 24, height = 20, width = 20)
# print(Med1)

# create boxes
boxes <- list()
n_boxes <- 20

weights <- list(3.5,8,11)
med_weights <- list(2,2,3)
print(weights)
weight <-0
  

for (i in 1:7) {
  index = sample(c(1, 2, 3), 1)
  print(c(Box1, Box2, Box3)[index])
  length <- sample(c(0.4, 0.5, 1), 1)
  height <- sample(c(0.4, 0.5, 1), 1)
  width <- sample(c(0.4, 0.5, 1), 1)
  
  # boxes <- c(boxes, Box(length = length, height = height, width = width) )
  
  boxes <- c(boxes, Box2)
}

# Box Packing
solution <- PerformBoxPacking(containers = containers,
                    boxes = boxes,
                    n_iter = 1,
                    population_size = 3,
                    elitism_size = 1,
                    crossover_prob = 1,
                    mutation_prob = 1,
                    verbose = TRUE,
                    plotSolution = TRUE
)

# print(solution)
# View(solution)
print(summary(solution)[1])



