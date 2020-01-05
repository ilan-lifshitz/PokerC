COMPARING_NUMBER_INDEX = 0
QUARTRET_INDEX  = 1
THREESOME_INDEX = 2
SECOND_PAIR_INDEX = 3
PAIR_INDEX = 4
NUMBER_INDEX = 5


class PossibilityManager :

    Possibilities = ["Quartet+Num","Quartet","ThreeSome+Num","ThreeSome","TwoPairs+Num","TwoPairs","Pair+Num","Pair","Num"]
    PreviousBet = ['a']*6
    def IdentifyResults(self,arr):
        count = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        i=0
        counter=0
        results = ['a'] * 6
        if (len(arr)) > 5:
            print("Too many cards")
            return

        for i in range(len(arr)):
            if arr[i] == 2:
                count[0] = count[0] + 1
            elif arr[i] == 3:
                count[1] = count[1] + 1
            elif arr[i] == 4:
                count[2] = count[2] + 1
            elif arr[i] == 5:
                count[3] = count[3] + 1
            elif arr[i] == 6:
                count[4] = count[4] + 1
            elif arr[i] == 7:
                count[5] = count[5] + 1
            elif arr[i] == 8:
                count[6] = count[6] + 1
            elif arr[i] == 9:
                count[7] = count[7] + 1
            elif arr[i] == 10:
                count[8] = count[8] + 1
            elif arr[i] == "J" or arr[i] == "j":
                count[9] = count[9] + 1
            elif arr[i] == "Q" or arr[i] == "q":
                count[10] = count[10] + 1
            elif arr[i] == "K" or arr[i] == "k":
                count[11] = count[11] + 1
            elif arr[i] == "A" or arr[i] == "a":
                count[12] = count[12] + 1
            else:
                print("InvalidSyntax")
                return

        for i in range(len(count)):
            if count[i] == 1:
                counter = counter + 1
                results[NUMBER_INDEX] = i
            elif count[i] == 2:
                counter = counter + 10
                if results[PAIR_INDEX] == 'a':
                    results[PAIR_INDEX] = i
                else:
                    results[SECOND_PAIR_INDEX] = i
            elif count[i] == 3:
                counter = counter + 100
                results[THREESOME_INDEX] = i
            elif count[i] == 4:
                counter = counter + 1000
                results[QUARTRET_INDEX] = i
        if counter % 10 > 1:
            print("Too many single cards")
        results[COMPARING_NUMBER_INDEX] = counter
        print(results)
        return results

    def CompareExtraNumber(self, arr):
        if arr[NUMBER_INDEX] > self.PreviousBet[NUMBER_INDEX]:
            return True
        else:
            return False

    def ComparePair(self, arr):
        # The new pair is higher
        if arr[PAIR_INDEX] > self.PreviousBet[PAIR_INDEX]:
            return 1
        # Both of the pairs are the same
        elif arr[PAIR_INDEX] == self.PreviousBet[PAIR_INDEX]:
            return 0
        # The new pair is lower
        else:
            return -1

    def ComparePairAndExtra(self,arr):
        x = self.ComparePair(arr)
        # The new quartet is higher
        if x == 1:
            return True
        # Both of the quartets are the same
        elif x == 0:
            # The extra number is higher
            return self.CompareExtraNumber()
        else:
            return False

    def CompareTwoPairs(self, arr):
        HighPair1 = max(arr[PAIR_INDEX], arr[SECOND_PAIR_INDEX])
        LowPair1 = min(arr[PAIR_INDEX], arr[SECOND_PAIR_INDEX])
        HighPair2 = max(self[PAIR_INDEX], self[SECOND_PAIR_INDEX])
        LowPair2 = min(self[PAIR_INDEX], self[SECOND_PAIR_INDEX])
        # The new high pair is higher
        if HighPair1 > HighPair2:
            return 1
        # Both of the high pairs are the same
        elif HighPair1 == HighPair2:
            # The new low pair is higher
            if LowPair1 > LowPair2:
                return 1
            # The old low pair and the high pair are the same
            elif LowPair1 == LowPair2:
                return 0
            # The old low pair is higher or t
            else:
                return -1
        # The old high pair is higher
        else:
            return -1

    def CompareTwoPairsAndExtra(self,arr):
        x = self.CompareTwoPairs(arr)
        # The new quartet is higher
        if x == 1:
            return True
        # Both of the quartets are the same
        elif x == 0:
            # The extra number is higher
            return self.CompareExtraNumber()
        else:
            return False

    def CompareThreesome(self, arr):
        # The new quartet is higher
        if arr[THREESOME_INDEX] > self.PreviousBet[THREESOME_INDEX]:
            return 1
        # Both of the quartets are the same
        elif arr[THREESOME_INDEX] == self.PreviousBet[THREESOME_INDEX]:
            return 0
        # The old quartet is higher
        else:
            return -1

    def CompareThreesomeAndExtra(self,arr):
        x=self.CompareThreesome(arr)
        # The new quartet is higher
        if x == 1:
            return True
        # Both of the quartets are the same
        elif x == 0:
            # The extra number is higher
            return self.CompareExtraNumber(arr)
        else:
            return False

    def CompareFullHouse(self, arr):
        x = self.CompareThreesome(arr)
        y = -6
        if x == 1:
            return True
        elif x == 0:
            y = self.ComparePair(arr)
            if y == 1:
                return True
            else:
                return False
        else:
            return False

    def CompareQuartet(self, arr):
        # The new quartet is higher
        if arr[QUARTRET_INDEX] > self.PreviousBet[QUARTRET_INDEX]:
            return 1
        # Both of the quartets are the same
        elif arr[QUARTRET_INDEX] == self.PreviousBet[QUARTRET_INDEX]:
            return 0
        # The old quartet is higher
        else:
            return -1
    def CompareQuartetAndExtra(self,arr):
        x=self.CompareQuartet(arr)
        # The new quartet is higher
        if x == 1:
            return True
        # Both of the quartets are the same
        elif x == 0:
            # The extra number is higher
            return self.CompareExtraNumber(arr)
        else:
            return False


    def CompareFirst(self):
        if self.PreviousBet[COMPARING_NUMBER_INDEX] == 'a':
            return True

    def CheckCompare(self,x):
        if x==1:
            return True
        else:
            return False

    def RestartPreviousBet(self):
        self.PreviousBet = ['a'] * 6
    def SetPreviousBet(self,arr):
        self.PreviousBet=arr

    def Compare(self,InputArr):
        arr = self.IdentifyResults(InputArr)
        if self.CompareFirst() :
            return True
        if self.PreviousBet[COMPARING_NUMBER_INDEX]/10>arr[COMPARING_NUMBER_INDEX]/10:
            return False
        elif self.PreviousBet[COMPARING_NUMBER_INDEX]/10<arr[COMPARING_NUMBER_INDEX]/10:
            return True
        else:
            if arr[COMPARING_NUMBER_INDEX]==1:
                return self.CompareExtraNumber(arr)
            elif arr[COMPARING_NUMBER_INDEX]==10:
                return self.CheckCompare(self.ComparePair(arr))
            elif arr[COMPARING_NUMBER_INDEX]==11:
                return self.ComparePairAndExtra(arr)
            elif arr[COMPARING_NUMBER_INDEX]==20:
                return self.CheckCompare(self.CompareTwoPairs(arr))
            elif arr[COMPARING_NUMBER_INDEX]==21:
                return self.CompareTwoPairsAndExtra(arr)
            elif arr[COMPARING_NUMBER_INDEX]==100:
                return self.CheckCompare(self.CompareThreesome(arr))
            elif arr[COMPARING_NUMBER_INDEX]==101:
                return self.CompareThreesomeAndExtra(arr)
            elif arr[COMPARING_NUMBER_INDEX]==110:
                return self.CompareFullHouse(arr)
            elif arr[COMPARING_NUMBER_INDEX]==1000:
                return self.CheckCompare(self.CompareQuartet(arr))
            elif arr[COMPARING_NUMBER_INDEX]==10:
                return self.CompareQuartetAndExtra(arr)
            else:
                return False
#COMPARING_NUMBER_INDEX = 0
#QUARTRET_INDEX  = 1
#THREESOME_INDEX = 2
#SECOND_PAIR_INDEX = 3
#PAIR_INDEX = 4
#NUMBER_INDEX = 5
pm = PossibilityManager()
print(pm.Compare([4]))
print(pm.Compare(['K']))
print(pm.Compare([3]))
print(pm.Compare([6,6]))
print(pm.Compare([8,8]))
print(pm.Compare([2,2]))
print(pm.Compare([8,6,6]))
print(pm.Compare([8,'k',8]))
print(pm.Compare([9,9,2]))
print(pm.Compare([8,8,'k']))
print(pm.Compare([9,'k',9]))
print(pm.Compare([8,8,6]))
print(pm.Compare([2,2,3,3]))
print(pm.Compare(['j','j',2,2]))
print(pm.Compare([5,5,4,4]))
print(pm.Compare(['j','j',5,5]))
print(pm.Compare(['j','j',2,2,5]))
print(pm.Compare(['j','j',5,5,2]))
print(pm.Compare(['j','j',7,5,5]))
print(pm.Compare([8,8,8]))
print(pm.Compare([10,10,10]))
print(pm.Compare([6,6,6]))
print(pm.Compare([8,8,8,6]))
print(pm.Compare([10,10,10,9]))
print(pm.Compare(['j','j','j']))
print(pm.Compare(['j','j','j',6]))
print(pm.Compare(['j','j','j',9]))
print(pm.Compare(['k','k','k',6]))

























