F=[0]*2025
F[1]=1
for n in range(2,2025):
    F[n]=n*F[n-1]
print((2*F[2024]+F[2023])/F[2022])