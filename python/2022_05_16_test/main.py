from arrow import *
from gui import *
def main():
    a = arrow(2,2,sp=1,ln='x',fill='#')
    print(a[::-1])
    drawText(arrow(2, ln="#",sp=6, qty=2, fill="x"))
if __name__=="__main__":
    main()
