# Write your solution here

def create_tuple(x: int, y: int, z: int) -> tuple:
    mi = min(x, y, z)
    ma = max(x, y, z)
    su = sum([x + y + z])
    return (mi, ma, su)


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))