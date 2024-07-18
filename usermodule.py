import qdsimparallel

inputdata = [
    {
        "name": "Alice Johnson",
        "age": 28,
        "city": "New York",
        "occupation": "Software Engineer"
    },
    {
        "name": "Bob Smith",
        "age": 34,
        "city": "San Francisco",
        "occupation": "Data Scientist"
    }
]

qdsimparallel.run_parallel_simulation(inputdata)