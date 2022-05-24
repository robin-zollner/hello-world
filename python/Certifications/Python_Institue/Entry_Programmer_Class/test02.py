hline = "-"*10
print(hline)
print("Original arrow")
print("    *    ")
print("   * *   ")
print("  *   *  ")
print(" *     * ")
print("***   ***")
print("  *   *  ")
print("  *   *  ")
print("  *****  ")

print(hline)

def arrow(size, qty=1, sp=2):
    ind = 4*size
    center = 3*size
    lines = 8*size
    ar=""
    sep = " "*(ind+1)*sp
    nl="\n"
    for i in range(lines-1):
        if(i==0):
            for j in range(qty):
                ar+=" "*(ind)+"*"+" "*ind
                ar+=sep
            ar+=nl
        elif (i<ind):
            prt = " "*(ind-i)+"*"
            for j in range(qty):
                ar+=prt+" "*((2*i)-1)+prt[::-1]
                ar+=sep
            ar+=nl
        elif (i==ind):
            prt = ("*"*center)
            for j in range(qty):
                ar+="*"*center+" "*(center-size+1)+"*"*center
                ar+=sep
            ar+=nl
        else:
            prt = " "*round((ind/2)+(size-1))+"*"
            for j in range(qty):
                ar+=prt+" "*(center-size+1)+prt[::-1]
                ar+=sep
            ar+=nl
    prt = " "*round((ind/2)+(size-1))+"*"
    for j in range(qty):
        ar+=prt+"*"*(center-size+1)+prt[::-1]
        ar+=sep
    ar+=nl
    return ar

print(arrow(4))
