# CoronaVirusSimulation

This is an attempt to simulate the spread of corona virus (COVID-19) which was declared as pandemic in March 2020.

Factors considered:
1. Time span of 600 units
2. Time needed to create vaccine is considered = 100 time units
3. Population of 100
4. Initially infected: 1 person out of 100
5. Gaussian distribution of immunity power of people in simulation
6. Mortality rate of Corona Virus
7. Time taken by the victim to recover based on his immunity to recover from virus infection

Factors in real life that are not considered:
1. Density distribution of population over the given area
2. Flow/movement of population according to places which are defined as public places f.e.:Bus stop, shopping mall, etc.
3. Effect of weather on virus spread
4. Minimum distance between two people in order to spread the virus. Here it is considered only on touch.
5. Time taken to mass produce vaccine, once it is developed
6. Measures taken for the vaccine to reach the victim's place
7. Time taken to determine if a person is infected by the virus or not
8. Quarantine of victims as well as others, for certain time units

The power of a victim to survive the disease depends majorly on two things:
  -his age
  -his immunity
Therefore power of individual = (1/age)*(immunity)

The ages and immunity list considered here is derived from Gaussian distribution. The ages are sorted and thus ascending,
but one can see the gaussian distribution in the immune as it is not sorted.
The ages considered are from 20 to 90.
Considering the given scenario of ages and immunities, best possible power is (1/age)*immunity = 0.04668
The worst possible power is = 0.0020002. Thus we are considering 0.000 as our threshold power to stay alive.
The mortality rate of Corona virus is dependent on age according to the reference:
https://www.businessinsider.de/international/coronavirus-death-age-older-people-higher-risk-2020-2/?r=US&IR=T
