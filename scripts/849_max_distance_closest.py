class Solution:
    def maxDistToClosest(self, seats) -> int:
        start_flag= False
        end_flag= False
        occupied = [i for i, j in enumerate(seats) if j == 1]
        if 0 not in occupied:
            start_flag = True
            occupied.insert(0,0)
        if len(seats)-1 not in occupied:
            end_flag = True
            occupied.append(len(seats)-1)

        current = 0
        prev = 0
        seat_choice = {}
        for key in occupied:
            prev = current
            current = key
            if (start_flag and prev == 0) or (end_flag and current == len(seats)-1):
                seat_choice[current] = current - prev
            else:
                seat_choice[current] = (current - prev)//2
        max_seat = max(list(seat_choice.values()))
        if max_seat == 0:
            max_seat = 1
        return max_seat
            
            
