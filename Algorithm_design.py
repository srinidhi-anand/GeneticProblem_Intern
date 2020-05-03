# Modules importing Process
from random import randint
import random

# Variables Declaration
Number_of_chromosomes = 6
mutation_rate = 0.1
crossover_rate = 0.25
generation = 0
equality = 30
List_chrome = []


# STEP 6 : Result of the Best Chromosomes Pair
def final_function(result_chromosome, gen_count):
    result_chromosome = set(result_chromosome)
    object_count = list(
        sum([(j + 1) * int(str(var)[1:-1].split(';')[j]) for j in range(len(var[1:-1].split(';')))]) for var in
        result_chromosome)
    gen_count = gen_count-1
    # The best chromosomes pair is analysed and produced the result
    print('The best Chromosome is :' + str(result_chromosome))

    return ''


# STEP 5 : Mutation Function call to analyse based on Mutation rate
def mutation_function(new_chrome_list):
    old_data = ''
    new_data = ''
    random_range = len(new_chrome_list) * len(list(str(new_chrome_list[0][1:-1]).split(";")))
    loop_range = round(float(mutation_rate * random_range))
    random_mutant_list = [randint(1, random_range) for j in range(loop_range)]
    for num in random_mutant_list:
        rownumber = int(num / 4) if (num % 4) != 0 and num > 4 else int(num/4)+1
        pos_no = int(num % 4)-1 if (num % 4) != 0 else 3
        new_value = randint(0, equality)

        for strgs in range(len(new_chrome_list)):
            if strgs == rownumber:
                old_data = new_chrome_list[strgs]
                data = list(str(new_chrome_list[strgs][1:-1]).split(";"))
                data[pos_no] = str(new_value)
                new_data = str([";".join(dat for dat in data)]).replace("'", "")

        new_chrome_list = [values.replace(old_data, new_data) for values in new_chrome_list]
        new_chrome_list = new_chrome_list

    # Calling objective function to evaluate the newly generated chromosomes pair
    objective_function(new_chrome_list)

    return ''


# STEP 4 : Crossover Function to determine the generate Chromosomes based on crossover rate
def crossover_function(parent_chromosome_list, new_chrome_list):
    random_cumulative_list = [randint(1, len(parent_chromosome_list)) for j in range(len(parent_chromosome_list))]
    for item in range(len(random_cumulative_list)):
        old_data = parent_chromosome_list[item]
        data = list(str(parent_chromosome_list[item][1:-1]).split(";"))
        index = random_cumulative_list[item]
        rep_data = list(parent_chromosome_list[item+1][1:-1].split(";")) if item != len(parent_chromosome_list)-1 else list(parent_chromosome_list[0][1:-1].split(";"))
        new_data = str([";".join(dat for dat in (data[:index]+rep_data[index:]))]).replace("'", "")
        new_chrome_list = [values.replace(old_data, new_data) for values in new_chrome_list]

    # Mutation Process Execution by Mutation Function call
    mutation_function(new_chrome_list)

    return ''


# STEP 3 : Selection Function to determine the Probability to get the Best Chromosomes
def fitness_function(object_count, chromelist):
    new_chrome_list = []
    fit_list = list(round((1/(1+int(val))), 6) if val >= 0 else 0 for val in object_count) # Fitness List of values
    prob_list = list(round((val/sum(fit_list)), 4) if sum(fit_list) > 0 else 0 for val in fit_list)  # Probability list
    cumulative_list = list(round((sum(prob_list[0:k+1])), 4) for k in range(len(prob_list)))  # Cumulative list
    random_list = list(round(random.random(), 4) for val in range(len(cumulative_list)))  # Random number generations
    # New Chromosomes list Generation
    for gene in range(len(random_list)):
        for val in range(len(cumulative_list)):
            if random_list[gene] < cumulative_list[val]:
                new_chrome_list.append(chromelist[val])
                break
            if val == len(cumulative_list)-1 and len(new_chrome_list) == gene:
                new_chrome_list.append(chromelist[gene])
    # Selection of Parent Chromosomes
    parent_chromosome_list = list(
        new_chrome_list[item] for item in range(len(random_list)) if random_list[item] < crossover_rate)

    # Cross over analysis function Call
    crossover_function(parent_chromosome_list, new_chrome_list)

    return ''


# STEP 2: Evaluation Function for best pair
def objective_function(chromelist):
    global generation
    object_count = list(
        sum([(j + 1) * int(str(var)[1:-1].split(';')[j]) for j in range(len(var[1:-1].split(';')))]) - 30 for var in
        chromelist)  # Summing up the value pairs of the each element in the list
    generation += 1  # Counting the number of generations
    result_chromosome = list(chromelist[k] for k in range(len(object_count)) if str(object_count[k]) == '0')
    # Selection Of chromosomes based on Chromosomes list and Objective type result considering the generation limit 50
    fitness_function(object_count, chromelist) if (len(result_chromosome) == 0 or generation == 1) and generation <= 50 else final_function(chromelist, generation)
    return ''


# STEP 1 : Creating gene value pair for the list of 6 chromosomes
def main():
    for i in range(Number_of_chromosomes):
        List_chrome.append(str([randint(0, equality) for j in range(4)]).replace(",", ";"))

    # STEP 2 : Calling the Evaluation Function for the gene paired chromosomes
    objective_function(List_chrome)
    return ''

# Initial Process Start / Calling for Genetic Problem program
main()
