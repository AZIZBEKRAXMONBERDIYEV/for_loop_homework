def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    s=[]
    for i in range(A, B+1,1):
        s.append(i)
        e=s[::-1]
    return e

print(main(2,7))
   