class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # one lane highway, n cars, same direction 
        # positions (in miles)
        # speed

        # positions: ordered [0, 1, 4, 7]
        # [1,2,2,1]

        # limited by ARRIVAL times
        # calcualte the arrival times for each 
        # if car n-1 arrives before n, it has the same value as n

        # arrival = [3, 4.5, 10, 3]

        # arrival_sorted = [10, 4.5, 3, 3]
        # [1, 3, 4, 4, 2]
        
        cars = zip(position, speed)
        cars = sorted (cars, reverse =True)
        arrival = []

        # calcualte arrival times for each 
        for pos ,speed in cars:
            arrival.append((target-pos)/speed)
        
        # fleet happens if there is a number bigger or eqaul to 
        fleets = []
        for car in arrival:
            #if you see a smaller number put it in, put in the first one too
            if not fleets or car > fleets[-1]:
                # add to the fleets
                fleets.append(car)
        
        return len(fleets)
            

