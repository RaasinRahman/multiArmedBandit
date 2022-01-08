# Multi-Armed Bandit

This project is a simulation of 3 methods that have a goal of optimizing the hapiness of a person deciding between 3 places to eat. Each of the 3 food-places that the person can choose from will have an average level of hapiness along with a standard deviation. Given the likelihood of hapiness of each food-place the person can choose 3 methods of selcting a place to eat.

Explore: The person will go to a random food place and be given a level of hapiness based on the average and standard deviation of each food-place out of 100 visits.

Exploit: The person will go to each food-place once, and after going to each location, the food-place that gives the highest hapiness will be chosen every single time out of 100 visits.

e-Greedy: The person will have a variation between explorartion and exploitation. The value of e will determine what percentage of visits the person will choose to exploit instead of explore. e-Greedy can provide an optimal level of hapiness by adding a slight variation to the choice of where to eat. Eating the same thing over and over even though it may be the best will get boring and decline in satisfaction.
