from math import *

# stop = 12
stop = 65536 # no stop
lim = 256
mlim = 65536
explim = 16
constcomp = 2
signcomp = 3
funccomp = 4
funccomp2 = 5

# val -> (comp, expr)
lib = {v + 0.0: (log(v + 1.0, 4), str(v)) for v in range(1, lim)}
lib[pi] = (constcomp, 'pi')
lib[e] = (constcomp, 'e')
lib[0] = (1, '0')

def add(comp, expr, val):
    if comp < stop and (not lib.has_key(val) or lib[val][0] > comp) and abs(val) < mlim:
        lib[val] = (comp, expr)

def do():
    oldlib = dict(lib)
    for aval, (acomp, aexpr) in oldlib.iteritems():
        add(acomp + signcomp, '(- ' + aexpr + ')', -aval)
        if aval > 0:
            add(acomp + funccomp, '(sqrt ' + aexpr + ')', sqrt(aval))
            if aval < explim:
                add(acomp + funccomp, '(' + aexpr + ' !)', gamma(aval + 1))
            if aval > 1 / explim:
                add(acomp + funccomp, '(log ' + aexpr + ')', log(aval))
                add(acomp + funccomp2, '(log10 ' + aexpr + ')', log10(aval))
                add(acomp + funccomp2, '(log2 ' + aexpr + ')', log(aval, 2))
        add(acomp + funccomp, '(sqr ' + aexpr + ')', aval ** 2)
        if abs(aval) < explim:
            add(acomp + funccomp, '(exp ' + aexpr + ')', e ** aval)
        if aval / pi != round(aval / pi):
            add(acomp + funccomp, '(sin ' + aexpr + ')', sin(aval))
            add(acomp + funccomp, '(cos ' + aexpr + ')', cos(aval))
            add(acomp + funccomp, '(tan ' + aexpr + ')', tan(aval))
        if aval != round(aval):
            add(acomp + funccomp2, '(sin ' + aexpr + '*pi)', sin(aval*pi))
            add(acomp + funccomp2, '(cos ' + aexpr + '*pi)', cos(aval*pi))
            add(acomp + funccomp2, '(tan ' + aexpr + '*pi)', tan(aval*pi))
        if abs(aval) < 1:
            add(acomp + funccomp2, '(asin ' + aexpr + ')', asin(aval))
            add(acomp + funccomp2, '(acos ' + aexpr + ')', acos(aval))
        add(acomp + funccomp, '(atan ' + aexpr + ')', atan(aval))
        for bval, (bcomp, bexpr) in oldlib.iteritems():
            if bval > 0:
                add(acomp + bcomp + signcomp, '(' + aexpr + ' + ' + bexpr + ')', aval + bval)
                add(acomp + bcomp + signcomp, '(' + aexpr + ' - ' + bexpr + ')', aval - bval)
                add(acomp + bcomp + signcomp, '(' + aexpr + ' * ' + bexpr + ')', aval * bval)
                add(acomp + bcomp + signcomp, '(' + aexpr + ' / ' + bexpr + ')', aval / bval)
            if aval > 0 and abs(bval) < 16:
                add(acomp + bcomp * 2 + signcomp, '(' + aexpr + ' ^ ' +  bexpr + ')', aval ** bval)

do()
# print(len(lib))
# do()
# print(len(lib))
# do()
# print(len(lib))
for a, (b,c) in lib.iteritems():
    if round(a) != a:
        print('{' +str(a) + ', "' + c + '"},')
        # print(str(a) + '   ' + str(b) + '   ' + c)
