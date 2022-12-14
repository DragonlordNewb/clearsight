memories = []

def write(data):
    global memories 

    memories.append(data)

def search(term):
    global memories

    output = []

    for memory in memories:
        if term in memory:
            output.append(memory)
        
    return output