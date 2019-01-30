def PerformBoxPacking(containers,
                      boxes,
                      n_iter,
                      population_size,
                      elitism_size,
                      crossover_prob,
                      mutation_prob,
                      verbose=False,
                      plotSolution=False):
    # TODO: think about case with 1-2 boxes, 1-2 containers

    # TODO: write verifiprintions of arguments
    if (elitism_size < 0):
        raise ('Elitism size cant be negative')
    elif (elitism_size == 0):
        print('Bad choice of elitism size')

    if (len(containers) == 0):
        raise ('Specify containers')

    if (len(boxes) == 0):
        raise ('Specify boxes')

    if (n_iter <= 0):
        raise ('Number of iterations cant be <= 0')

    if (population_size <= 0):
        raise ('Population size cant be <= 0')
    # elif (population_size > 0 & population_size < .) :
    #      print('Bad choice for Population Size')
    #
    if (crossover_prob < 0 | crossover_prob > 1):
        raise ('crossover_prob must be in [0;1]')
    elif (crossover_prob == 0):
        print('Not the best choice for crossover_prob')

    if (mutation_prob < 0 | mutation_prob > 1):
        raise ('mutation_prob must be in [0;1]')
    elif (mutation_prob == 0):
        print('Not the best choice for mutation_prob')

    n = len(containers)  # number of containers
    m = len(boxes)  # number of boxes

    # Initialization
    population = InitializePopulation(population_size=population_size,
                                      n_containers=n,
                                      boxes=boxes
                                      )
    chromosome_fitness = rep(0, population_size)

    elitism_chromosomes = list()
    elitism_chromosomes_fitness = c()

    for iter in range(n_iter):
        if (verbose):
            print('Iteration:', iter, 'out of ', n_iter, '\n')

        population_size = len(population)
        for chromosome_i in range(population_size):
            if (verbose):
                print('  Chromosome:', chromosome_i, 'out of ', population_size, '\n')

            chromosome = population[[chromosome_i]]

            # perform packing
            packing_solution =
            PackBoxes(boxes=boxes,
                      containers=containers,
                      box_packing_sequence=chromosome$BPS,
                                                      container_loading_sequence = chromosome$CLS
            )

            # calculate fitness of current chromosome
            chromosome_fitness[chromosome_i] = CalculateFitness(packing_solution)

        population = c(population, elitism_chromosomes)
        chromosome_fitness = c(chromosome_fitness, elitism_chromosomes_fitness)

        if (iter != n_iter):  # check if we are not on the last iteration

            # Select the best chromosomes to next generation
            best_chromosomes_ind =
            PerformElitism(chromosome_fitness,
                           elitism_size
                           )

        elitism_chromosomes = population[best_chromosomes_ind]
        elitism_chromosomes_fitness = chromosome_fitness[best_chromosomes_ind]

        # remove elitism chromosomes from the population
        population = population[-best_chromosomes_ind]
        chromosome_fitness = chromosome_fitness[-best_chromosomes_ind]

        # Selection
        mating_pool = PerformSelection(population, fitness=chromosome_fitness)

        # Crossover
        crossovered_chromosomes = PerformCrossover(mating_pool, crossover_prob=crossover_prob)

        # Mutation
        population = PerformMutation(crossovered_chromosomes, mutation_prob=mutation_prob)


# choose solution of packing after all iterations
best_chromosome = population[[which.min(chromosome_fitness)]]
best_chromosome_packing_solution =
PackBoxes(boxes=boxes,
          containers=containers,
          box_packing_sequence=best_chromosome$BPS,
                                               container_loading_sequence = best_chromosome$CLS
)

if (plotSolution):
    PlotPackingSolution(best_chromosome_packing_solution)

return (best_chromosome_packing_solution)
