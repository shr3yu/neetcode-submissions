class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # you need to keep tack of the running sum to add
        # keep track of the record itll be as long as the operations
        # need a stack of all the numbers you got

        record = []

        for op in operations:
            if op == "C":
                record.pop()
                
            elif op == "D":
                record.append(2 * record[-1])

            elif op == "+":
                record.append(record[-1]+ record[-2])
            else: 
                record.append(int(op))
            print(record)

        return sum(record)



        