import decimal #試試下面的指令

m = input("本金:")
m=decimal.Decimal(m)
r = input("利率:")
r=decimal.Decimal(r)
y = input("存幾年:")
y=decimal.Decimal(y)

print("本利和:{}".format(m*(1+r)**y))

# 本金:利率:存幾年:本利和:33930208.35144854913075581851
# 本金:利率:存幾年:33930208.35144854913075581851