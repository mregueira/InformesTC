import control as ctrl
from control import matlab
# aca deberia hacer una funcion que recibe polos
# que tiene un algoritmo definido
# y que devuelve el array de numerador y denominador para poder ponerlo en una funcion lti

def gather1stand2ndOrder(poles):
    newPoles=[]
    for i in range(len(poles)):
        if poles[i].imag>=0:
            newPoles.append(poles[i])
    return newPoles

def LP_FreqTransform2ndOrd(sk,wp): #esta funcion necesita un solo conjugado!!
    num=[1]
    den=[1/wp**2,-2*sk.real/wp, abs(sk)**2]
    return num,den
def LP_FreqTransform2ndOrd(sk,wp):
    num = [wp]
    den = [1,-sk*wp]
    return num,den

poles=[(-0.3826834323650897+0.9238795325112867j), (-0.9238795325112867+0.3826834323650899j), (-0.9238795325112868-0.38268343236508967j), (-0.38268343236509034-0.9238795325112865j)]
# wp/(s-sk*wp)
wp=100
x= ctrl.TransferFunction([1],[1])
poles=gather1stand2ndOrder(poles)
for i in range(len(poles)):
    if poles[i].imag>0:
        num,den =LP_FreqTransform2ndOrd(poles[i],wp)
    elif poles[i].imag==0:
        num,den =LP_FreqTransform2ndOrd(poles[i],wp)
    x*=ctrl.TransferFunction(num,den)
print(x)
num,den=matlab.tfdata(x)

print(num[0][0]) # se accede asi
print(den[0][0])
# print(den[0][0])
