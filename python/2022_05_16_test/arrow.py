def arrow(size=1, qty=1, sp=2, ln="*", fill=" ", back=" "):
    ind = 4*size
    center = 3*size
    lines = 8*size
    ar=""
    sep = back*(ind+1)*sp
    nl="\n"
    for i in range(lines-1):
        if(i==0):
            for j in range(qty):
                ar+=back*(ind)+ln+back*ind
                ar+=sep
            ar+=nl
        elif (i<ind):
            prt = back*(ind-i)+ln
            for j in range(qty):
                ar+=prt+fill*((2*i)-1)+prt[::-1]
                ar+=sep
            ar+=nl
        elif (i==ind):
            prt = (ln*center)
            for j in range(qty):
                ar+=ln*center+fill*(center-size+1)+ln*center
                ar+=sep
            ar+=nl
        else:
            prt = back*round((ind/2)+(size-1))+ln
            for j in range(qty):
                ar+=prt+fill*(center-size+1)+prt[::-1]
                ar+=sep
            ar+=nl
    prt = back*round((ind/2)+(size-1))+ln
    for j in range(qty):
        ar+=prt+ln*(center-size+1)+prt[::-1]
        ar+=sep
    ar+=nl
    return ar
