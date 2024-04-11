def load_obj(filename):
    vertices = []
    edges = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('v '):
                vertices.append(list(map(float, line.strip().split()[1:])))
            elif line.startswith('f '):
                face = list(map(int, line.strip().split()[1:]))
                edges.extend([(face[i], face[i + 1]) for i in range(len(face) - 1)])
                edges.append((face[-1], face[0]))  # Zamknięcie krawędzi

    edges = set(tuple(sorted(edge)) for edge in edges)
    return vertices, edges
