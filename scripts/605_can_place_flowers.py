class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        else:
            for i in range(n):
                found = False
                prev = 0
                current = 0
                for key,i in enumerate(flowerbed):
                    prev = current
                    current = i
                    if prev == 0 and current == 0:
                        if key == len(flowerbed) - 1:
                            if flowerbed[key] == 0:
                                flowerbed[key] = 1
                                found = True
                                break                    
                        elif key < len(flowerbed)-1:
                            if flowerbed[key+1] == 0:
                                flowerbed[key] = 1
                                found = True
                                break
                if found == False:
                    break
        return found
         