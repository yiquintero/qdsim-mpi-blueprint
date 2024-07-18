def getmysubset(inputdata, rank, comm_size):

    allsimulations = [
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
        },
        {
            "name": "Carol Martinez",
            "age": 25,
            "city": "Los Angeles",
            "occupation": "Graphic Designer"
        },
        {
            "name": "David Brown",
            "age": 45,
            "city": "Chicago",
            "occupation": "Project Manager"
        },
        {
            "name": "Emma Wilson",
            "age": 30,
            "city": "Seattle",
            "occupation": "UX Researcher"
        },
        {
            "name": "Frank Clark",
            "age": 50,
            "city": "Austin",
            "occupation": "Sales Director"
        },
        {
            "name": "Grace Lee",
            "age": 22,
            "city": "Boston",
            "occupation": "Marketing Coordinator"
        },
        {
            "name": "Henry Turner",
            "age": 39,
            "city": "Miami",
            "occupation": "Financial Analyst"
        },
        {
            "name": "Isabella White",
            "age": 27,
            "city": "Denver",
            "occupation": "Product Manager"
        },
        {
            "name": "Jack Harris",
            "age": 33,
            "city": "Houston",
            "occupation": "Mechanical Engineer"
        }
    ]

    base_size = len(allsimulations) // comm_size
    start = (rank * base_size)
    end = start + base_size - 1

    # Assign extra elements to the last rank
    if (rank == comm_size - 1):
        end = len(allsimulations) - 1

    return allsimulations[start:end+1]
