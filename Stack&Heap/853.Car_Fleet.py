from typing import List
def carFleet(target: int, position: List[int], speed: List[int]) -> int:

    stack = []
    cars = [(p, s) for p, s in zip(position, speed)]
    for car in sorted(cars)[::-1]:
        time_taken = (target - car[0]) / car[1]
        if stack and time_taken <= stack[-1]:
            continue
        else:
            stack.append(time_taken)
    return len(stack)

carFleet(12, position = [10,8,0,5,3], speed = [2,4,1,1,3])


    
    