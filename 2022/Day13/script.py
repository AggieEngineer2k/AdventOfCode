import ast
import logging
logging.basicConfig(level=logging.WARN)
indent_step = 2

def testPairIsInRightOrder(left, right, indent = 0) -> bool:
    logging.info(f"{' ' * indent}- Compare {left} vs {right}")
    left_is_an_int = isinstance(left,int)
    right_is_an_int = isinstance(right,int)
    if left_is_an_int and right_is_an_int:
        indent += indent_step
        if left < right:
            logging.debug(f'True: {left} <= {right}')
            logging.info(f"{' ' * indent}- Left side is smaller, so inputs are in the right order")
            return True
        elif left > right:
            logging.debug(f'False: {left} > {right}')
            logging.info(f"{' ' * indent}- Right side is smaller, so inputs are not in the right order")
            return False
        else:
            return None
    elif not left_is_an_int and not right_is_an_int:
        length = min(len(left),len(right))
        i = 0
        test = None
        while i < length and test == None:
            test = testPairIsInRightOrder(left[i],right[i],indent + indent_step)
            i += 1
        if test != None:
            return test
        else:
            if len(left) < len(right):
                logging.info(f"{' ' * indent}- Left side ran out of items, so inputs are in the right order")
                return True
            elif len(left) > len(right):
                logging.info(f"{' ' * indent}- Right side ran out of items, so inputs are not in the right order")
                return False
            else:
                return None
    elif left_is_an_int and not right_is_an_int:
        logging.info(f"{' ' * indent}- Mixed types; convert left to {[left]} and retry comparison")
        return testPairIsInRightOrder([left],right,indent + indent_step)
    elif not left_is_an_int and right_is_an_int:
        logging.info(f"{' ' * indent}- Mixed types; convert right to {[right]} and retry comparison")
        return testPairIsInRightOrder(left,[right],indent + indent_step)

with open('input.txt','r') as inputFile:
    lines = [line.rstrip() for line in inputFile if line.rstrip() != '']

pairs_in_right_order = []
for i in range(len(lines) // 2):
    logging.info(f'== Pair {i + 1} ==')
    left = ast.literal_eval(lines[i * 2])
    right = ast.literal_eval(lines[i * 2 + 1])
    is_pair_in_right_order = testPairIsInRightOrder(left,right)
    if is_pair_in_right_order:
        pairs_in_right_order.append(i + 1)
print(f'Part 1: {pairs_in_right_order} = {sum(pairs_in_right_order)}')