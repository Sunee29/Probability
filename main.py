from prob_calculator import Hat, experiment

hat = Hat(yellow=5, red=1, green=3)
probability = experiment(hat=hat,
                  expected_balls={"yellow":2,"green":3},
                  num_balls_drawn=7,
                  num_experiments=1000)
print(probability)
