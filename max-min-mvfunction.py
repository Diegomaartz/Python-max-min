from sympy import *
import numpy as np
from sympy import Subs, Function, sin, cos
from sympy import euler as e

#Martinez Mendez Diego
#2BM1
#Calculo Multivariable
#17/DIC/2022

#Declaracion de los simbolos empleados, coordenadas polares y clinidricas
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
t = Symbol('t')
deltax = Symbol("ΔX")
deltay = Symbol("ΔY")
deltaz = Symbol("ΔZ")
theta = Symbol("θ")
ro = Symbol("ρ")
phi = Symbol("φ")
lam = Symbol('λ')
r = Symbol("r")
rx = r*cos(theta)
ry = r*sin(theta)
cx = ro*cos(theta)*sin(phi)
cy = ro*sin(theta)*sin(phi)
cz = ro*cos(phi)

ltz = 0
pvz = 0
matdz = 0

#Ejemplos para R2
#fx = (x**3 + 3*x*y**2 - 15*x - 12*y)
#fx = (x**2 + y**2)
#fx = (y*x**2)/(x**2+ y**2)

#Ejemplos para R3
#fx = (x**2 + x*y - E**(x*y) - cos(x*z))
#fx = (x*y*E**z)/(y*z*x**3)


#Ingresamos la funcion
print("Ingresa la funcion a derivar:  ")
funcion = input()
fx = parse_expr(funcion)

#Ingresamos las variables a considerar
print("Ingresa el numero de variables a tomar en cuenta: ")
nv = int(input())
vars = []
print("Respecto a que variables deseas plantear tu funcion: ")
for i in range(nv):
    vars.append(input("Variable:"))

print("Ingresa el punto a evaluar en x: ")
pvx = int(input())
print("Ingresa el punto a evaluar en y: ")
pvy = int(input())
if "z" in vars:
    print("Ingresa el punto a evaluar en z: ")
    pvz = int(input())



#Primeras derivadas
dz = Derivative(fx, z).doit()
dy = Derivative(fx, y).doit()
dx = Derivative(fx, x).doit()

#Imprimimos la funcion ingresada y las variables a considerar
fxstr = str(fx)
print("La funcion ingresada fue: f",vars,"  = ",  fx)
print("\n")


#############################
#Comprobar diferenciabilidad#
#############################

    ####################################
    #Comprobacion de la matriz derivada#
    ####################################

print("===========================================")
print("    COMPROBACION DE DIFERENCIABILIDAD")
print("===========================================")
print("\n 1) Determinar si la matriz derivada existe")
if "z" in vars:  
    print("\n")
    print("Matriz Derivada")
    print("=====================")
    print("| ",dx,",", dy,",", dz,"|")
    print("=====================")
else:
    print("\n")
    print("Matriz Derivada")
    print("=====================")
    print("| ",dx,",", dy,"|")
    print("=====================")


#Sustituir los valores de las derivadas en 0


if "z" in vars:
    matdx = dx.subs({x:pvx, y: pvy, z: pvz})
    matdy = dy.subs({x:pvx, y: pvy, z: pvz})
    matdz = dz.subs({x:pvx, y: pvy, z: pvz})
else:
    matdx = dx.subs({x:pvx, y: pvy})
    matdy = dy.subs({x:pvx, y: pvy})


"""
#Sustituimos el punto dado y "t" para dx
ox = fx.subs({x:pvx, y: pvy, z: pvz})
px = fx.subs({x: t, y: pvy, z: pvz})
qx = fx.subs({x:pvx, y: pvy, z: pvz})

fltx = ((ox + px - qx) / t)
print(ox)
print(px)
print(qx)
print(fltx)
ltx = limit(fltx, t, 0)
#print(ltx)

#Sustituimos el punto dado y "t" para dy
oy = fx.subs({x:pvx, y: pvy, z: pvz})
py = fx.subs({x: pvx, y: t, z: pvz})
qy = fx.subs({x:pvx, y: pvy, z: pvz})

flty = ((oy + py - qy) / t)
lty = limit(flty, t, 0)
#print(lty)

#Sustituimos el punto dado y "t" para dz
oz = fx.subs({x:pvx, y: pvy, z: pvz})
pz = fx.subs({x: pvx, y: pvy, z: t})
qz = fx.subs({x:pvx, y: pvy, z: pvz})

fltz = ((oz + pz - qz) / t)
ltz = limit(fltz, t, 0)
#print(ltz)

#if(ltx != oo and lty != oo and ltz != oo):
print("\n")
"""

"""if "z" in vars:
    print("Matriz Derivada lim t")
    print("=====================")
    print("| ",str(fltx),",", str(flty),",", str(fltz),"|")
    print("=====================")
else:
    print("Matriz Derivada lim t")
    print("=====================")
    print("| ",str(fltx),",", str(flty),"|")
    print("=====================")
"""
if "z" in vars:
    print("Matriz Derivada evaluando en el punto dado")
    print("=====================")
    print("| ",matdx,",", matdy,",", matdz,"|")
    print("=====================")
else:
    print("Matriz Derivada evaluando en el punto dado")
    print("=====================")
    print("| ",matdx,",", matdy,"|")
    print("=====================")


if(matdx != nan and matdy != nan and matdz != nan):
    print("Evaluando los puntos nos queda que, la matriz derivada existe")
    print("\n")


        #########################
        #Comprobacion del limite#
        #########################
    #Condicionamos la norma y el vector h de acuerdo con las variables establecidas
    if "x" and "y" and "z" in vars:
        normah = sqrt((deltax * deltax) + (deltay * deltay) + (deltaz * deltaz))
    elif "x" and "y" in vars:
        normah = sqrt((deltax * deltax) + (deltay * deltay))


    #Posible validacion por otro caso q se requiera de acuerdo a las variables q ingrese el profe
    elif "x" and "z" in vars:
        normah = sqrt((deltax * deltax) + (deltaz * deltaz))
    elif "y" and "z" in vars:
        normah = sqrt((deltay * deltay) + (deltaz * deltaz))

    print("\n")
    #print("La norma es: ",normah)


    #Sustituimos el punto dado -- en este caso (0,0) -- para hacer una nueva funcion para el limite
    if "x" in vars or "y" in vars or "z" in vars:
        up = fx.subs({x:pvx, y: pvy, z: pvz})
        uh = fx.subs({x: deltax, y: deltay, z: deltaz})
        v = fx.subs({x:pvx, y: pvy, z: pvz})

    if ("x" or "y" or "z" in dx) or ("x" or "y" or "z" in dy) or ("x" or "y" or "z" in dz):   
        wpx = (dx.subs({x:pvx, y: pvy, z: pvz}) * deltax)
        wpy = (dy.subs({x:pvx, y: pvy, z: pvz}) * deltay)
        wpz = (dz.subs({x:pvx, y: pvy, z: pvz}) * deltaz)


    ufinal = simplify(up + uh)
    wfinal = simplify(wpx + wpy + wpz)

    nfx = ((ufinal - v - wfinal) / normah)

    print(nfx)
    nfxstr = str(nfx)



    #Sustituimos los valores delta por las coordenadas polares o cilindricas
    if 3 == nv:
        rnfx = nfx.subs({deltax: cx, deltay: cy, deltaz: cz})
        print("2) Determinar si el limite = 0")
        print("Limite para comprobar diferenciabilidad:   lim (ΔX, ΔY, ΔZ)-->(0,0,0)  ", nfx)
        print("Funcion en coordenadas cilindricas: lim (ρ)-->(0) ",(rnfx))
        lim = limit(rnfx, ro, 0)
        print("\n")
        print("Resultado del lim: ", lim)
    elif 2 == nv:
            rnfx = nfx.subs({deltax: rx, deltay: ry})
            print("2) Determinar si el limite = 0")
            print("Limite para comprobar diferenciabilidad:   lim (ΔX, ΔY)-->(0,0)  ", nfx)
            print("Funcion en coordenadas polares: lim(r) --> (0) ",(rnfx))
            lim = limit(rnfx, r, 0)
            print("\n")
            print("Resultado del lim: ", lim)
        
    ############################################
    #De aqui pa abajo jala no le muevas wey pls#
    ############################################
    if lim == 0:
        print("Ya que el limite es igual a 0, la función es diferenciable")
        print("\n")

        if("x" in vars):
            print("Primera derivada (X):    ", simplify(dx))
        if("y" in vars):
            print("Primera derivada (Y):    ", simplify(dy))
        if("z" in vars):
            print("Primera derivada (Z):    ", simplify(dz))

        print("\n")
        if "z" in vars:
            puntose = solve([dx,dy,dz], [x,y,z], set = True) 
            if len(puntose) == 0:
                print("No hay soluciones")
            quit()
        else:
            puntose = solve([dx,dy], [x,y], set = True) 
            if len(puntose) == 0:
                print("No hay soluciones")
                quit()
        #nsol = len(puntose)

            
        print(puntose)
        puntoslista = list(puntose[1])
        nsol = len(puntoslista)
        print("Soluciones: ",nsol," ",puntoslista)
        pestx = int(puntoslista[0][0])
        pesty = int(puntoslista[0][1])
        if "z" in vars:
            pestz = int(puntoslista[0][2])

        #print(pestx)
        #print(pesty)
        if(nsol == 1):
            if(pestx == pvx):
                if(pesty == pvy):
                    print("El punto dado es un punto estacionario")
                    print("X =  ",pestx)
                    print("Y =  ", pesty)
                    if "z" in vars:
                        if(pestz == pvz):
                            print("Z = ", pestz)                   
        else:
            print("Existen: ", nsol, " puntos críticos: ")

            #Hessiana segun skldjasdl
            a = Derivative(fx,x,2).doit()

            b = Derivative(fx, y).doit()
            bf = Derivative(b, x).doit()

            c = Derivative(fx, x).doit()
            cf = Derivative(c, y).doit()

            d = Derivative(fx, y, 2).doit()

            print("\n")
            print("Matriz hessiana")
            print("==================")
            print("| ",a, bf,"|")
            print("| ",cf, d,"|")
            print("==================")

            astr = str(a)
            bstr = str(bf)
            cstr = str(cf)
            dstr = str(d)

            print("\n")
            print("\n")
            print("Evaluando: los puntos críticos: ")
            for i in range(nsol):
                print(i+1,"--> Para:")
                pei = puntoslista[i]
                print(pei)

                equis = puntoslista[i][0]
                ye = puntoslista[i][1]
                print("X=", equis)
                print("Y=", ye)

                if(equis == 0 and ye == 0):
                    print("Es un punto estacionario")
                    quit()

                asusx = 0
                asusy = 0

                bsusx = 0
                bsusy = 0

                csusx = 0
                csusy = 0

                dsusx = 0
                dsusy = 0

                if "x" in astr:    
                    asusx = a.subs(x, equis)
                if "x" in bstr:
                    bsusx = bf.subs(x, equis)
                if "x" in cstr:
                    csusx = cf.subs(x, equis)
                if "x" in dstr:
                    dsusx = d.subs(x, equis)

                if "y" in astr:
                    asusy = a.subs(y, ye)
                if "y" in bstr:
                    bsusy = bf.subs(y, ye)
                if "y" in cstr:
                    csusy = cf.subs(y, ye)
                if "y" in dstr:
                    dsusy = d.subs(y, ye)

                afinal = asusx + asusy
                bfinal = bsusx + bsusy
                cfinal = csusx + csusy
                dfinal = dsusx + dsusy

                print("Matriz hessiana en el punto crítico: ", i+1)
                print("==================")
                print("| ",afinal,      bfinal,"|"   ,"-",   "| ",lam, 0,"|")
                print("| ",cfinal,      dfinal,"|"   ,"-",   "| ",0, lam,"|")
                print("==================")
                print("\n")

                mla = afinal-lam
                mlb = bfinal
                mlc = cfinal
                mld = dfinal-lam

                print("Matriz con lambda para la solución: ", i+1)
                print("==================")
                print("| ",mla,      mlb,"|")
                print("| ",mlc,      mld,"|")
                print("==================")

                deter = (mla * mld) - (mlc * mlb)
                print(deter, "= 0")

                solus = solve(deter, lam) 
                print(solus, "\n")
                if((solus[0] > 0 and solus[1] <= 0) or (solus[0] <= 0 and solus[1] > 0)):
                    print("Punto de inflexion")
                    print("\n")
                    print("\n")
                elif((solus[0] and solus[1]) < 0):
                    print("Maximo")
                    print("\n")
                    print("\n")
                elif((solus[0] and solus[1]) > 0):
                    print("Minimo")
                    print("\n")
                    print("\n")
                elif(solus[0] and solus[1] == 0):
                    print("Es un punto estacionario")

    else:
        print("Como el resultado del limite es distinto de cero, la función no es diferenciable")
else:
    print("Evaluando los puntos nos queda que la matriz derivada no existe, por lo tanto no es diferenciable")