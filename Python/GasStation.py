class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        j = 0
        for j in range(len(gas)):
            if gas[0] < cost[0]:
                gas_0 = gas.pop(0)
                gas.append(gas_0)
                cost_0 = cost.pop(0)
                cost.append(cost_0)
                j += 1
            else:
                break
        else:
            return -1

        print(gas, cost)
        last_current = -1

        current = gas[0] - cost[1] + gas[1]

        for i in range(1, len(gas)):
            print(current)

            current = current - cost[i] + gas[i]

            print(current)

            if current == 0:
                last_current = i

        return last_current