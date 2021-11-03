# COMP10001-Project1
Project 1 for Foundations of Computing COMP10001, a sampling done on biodiversity

There were a total of 4 questions, each tackling different problems involving species richness, species eveness, comparing habitats, and finally sampling of the habitat data.

Running the different functions would yield the following results

```
>>> get_species_richness(['magpie', 'magpie', 'cockatoo', 'lyrebird', 'cockatoo', 'lyrebird', 'bellbird'])
(4, ['bellbird', 'cockatoo', 'lyrebird', 'magpie'])
>>> get_species_richness(['pardalote', 'pardalote', 'pardalote'])
(1, ['pardalote'])
>>> get_species_richness([])
(0, [])
```

```
>>> get_species_evenness(['magpie', 'magpie', 'cockatoo', 'lyrebird', 'cockatoo', 'lyrebird', 'bellbird'])
(3.769230769230769, [('bellbird', 1), ('cockatoo', 2), ('lyrebird', 2), ('magpie', 2)])
>>> get_species_evenness(['pardalote', 'pardalote', 'pardalote'])
(1.0, [('pardalote', 3)])
```

```
>>> compare_diversity([('magpie', 'A'), ('magpie', 'A'), ('magpie', 'A'), ('cockatoo', 'A'), ('lyrebird', 'A'), ('bellbird', 'A'), ('magpie', 'B'), ('bellbird', 'B'), ('cockatoo', 'B'), ('lyrebird', 'B')], "richness")
[('A', 4), ('B', 4)]
>>> compare_diversity([('magpie', 'A'), ('magpie', 'A'), ('magpie', 'A'), ('cockatoo', 'A'), ('lyrebird', 'A'), ('bellbird', 'A'), ('lyrebird', 'C'), ('bellbird', 'C'),('magpie', 'B'), ('bellbird', 'B'), ('cockatoo', 'B'), ('lyrebird', 'B'), ('fantail', 'C'), ('noisy miner', 'C')], "evenness")
[('B', 4.0), ('C', 4.0), ('A', 2.9999999999999996)]
```

```
>>> sample_data = [['magpie', 'yellow robin', 'fantail'], ['magpie', 'fantail', 'friarbird', 'warbler', 'noisy miner'], ['magpie', 'flycatcher', 'pardalote', 'noisy miner', 'superb parrot'], ['magpie', 'yellow robin', 'warbler'], ['magpie', 'thornbill', 'flycatcher', 'kookaburra'], ['magpie', 'pardalote', 'friarbird', 'raven'], ['magpie', 'pardalote', 'dollarbird'], ['magpie', 'flycatcher', 'fantail'], ['magpie', 'superb parrot', 'noisy miner'], ['night parrot']]
>>> optimise_study(sample_data, 2, 2)
(7, 0.9285714285714286)
>>> optimise_study(sample_data, 1, 2)
(9, 0.9285714285714286)
>>> optimise_study(sample_data, 2, 1)
(4, 0.6428571428571429)
```

# Results
 
 Final Mark: 91.167 %
