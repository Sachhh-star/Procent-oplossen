
def prosenten():
    b = int(input("1: %van 2: hoeveel%van 3:% toenemen 4:% afnemen 5: Getal verhogen met percentage 6: Terugrekenen na verhoging/verlaging "))
    match b:
        case 1: a,o=float(input("%van")),float(input("getal: "));print(a*o/100)
        case 2: b,c=float(input("hoeveel%van")),float(input("getal: "));print(b*c/100)
        case 3: d,e=float(input("% toenemen")),float(input("getal: "));print(d*e/100)
        case 4: f,g=float(input("% afnemen")),float(input("getal: "));print(f*g/100)
        case 5: h,i=float(input("Getal verhogen met percentage")),float(input("getal: "));print(h*i/100)
        case 6: j,k=float(input("Terugrekenen na verhoging/verlaging")),float(input("getal: "));print(j*k/100)
prosenten()