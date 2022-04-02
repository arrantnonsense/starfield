import numpy as np
from numpy import random
import scipy
import matplotlib.pyplot as plt


def find_nearest_n(L, V):

    Results = []
    
    for a in range(0, len(L)):
        Diff_X = (L[a][0]-V[0])
        Diff_Y = (L[a][1]-V[1])
        Diff_Z = (L[a][2]-V[2])

        Abs_Diff_Y = np.abs(Diff_Y)

        Size = L[a][3]
        
        if Diff_X<=0:
            DirX = -1
        else: DirX = 1

        if Diff_Y <= 0:
            DirY = -1
        else:
            DirY = 1

        if Diff_Z <= 0:
            DirZ = -1
        else:
            DirZ = 1
            
        Dist = np.sqrt(((np.abs(Diff_X))**2)+(np.abs(Diff_Y)**2))
        Abs_Diff_Z = np.abs(Dist)
        Dist = np.sqrt(((np.abs(Dist))**2)+(np.abs(Diff_Z)**2))

        Results.append([Dist, a, L[a][0], L[a][1], L[a][2], Size, Abs_Diff_Y, Abs_Diff_Z, DirX, DirY, DirZ])

            
    if len(Results)>0:
        return Results
    else:
        return [0]

def new_coord(d1, d2, diff_y, diff_z, x, y, z, dirx, diry, dirz):
    Theta = np.arcsin(np.array(diff_y/d1))
    Phi = np.arcsin(np.array(diff_z/d1))
    X_Change = (d2*(np.cos(Theta)))*dirx
    Y_Change = (d2*(np.sin(Theta)))*diry
    Z_Change = (d2*(np.sin(Phi)))*dirz
    New_X = x + X_Change
    New_Y = y + Y_Change
    New_Z = z + Z_Change

    return [New_X, New_Y, New_Z]
    

Full_List = []
Coord_List = []
S_List = []

for i in range (0, 8000):
    if i == 0:
        X = 0
        Y = 0
        Z = 0
        S = 50

        Full_List.append([X, Y, Z, S])
        Coord_List.append([X,Y, Z])
        S_List.append([S])
        
    if i >0 and i < 5:
        X = random.randint(10000)
        Y = random.randint(10000)
        Z = random.randint(10000)
        S = random.uniform(10,12)

        Test_Coord = [X,Y,Z]


        Near = find_nearest_n(Full_List, Test_Coord)
        
        if Near[0] == 0:
            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

        else:
            for q in Near:
                Dist = q[0]
                Near_X = q[2]
                Near_Y = q[3]
                Near_Z = q[4]
                Near_S = q[5]
                Near_Diff_Y = q[6]
                Near_Diff_Z = q[7]
                Near_DirX = q[8]
                Near_DirY = q[9]
                Near_DirZ = q[10]

                Grav = (1000*Near_S)/(Dist**2)

                if Grav<0.1:
                    Force = Grav*S
                else:
                    Force = (Grav/10)*S

                Move_Dist = Dist*Force
                
                New_XY = new_coord(Dist, Move_Dist, Near_Diff_Y, Near_Diff_Z, X, Y, Near_DirX, Near_DirY)

                X = New_XY[0]
                Y = New_XY[1]
                Z = New_XY[2]

            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])
        
    elif i >= 5 and i < 20:
        X = random.randint(10000)
        Y = random.randint(10000)
        Z = random.randint(10000)
        S = random.uniform(9,10)

        Test_Coord = [X,Y,Z]


        Near = find_nearest_n(Full_List, Test_Coord)
        
        if Near[0] == 0:
            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

        else:
            for q in Near:
                Dist = q[0]
                Near_X = q[2]
                Near_Y = q[3]
                Near_Z = q[4]
                Near_S = q[5]
                Near_Diff_Y = q[6]
                Near_Diff_Z = q[7]
                Near_DirX = q[8]
                Near_DirY = q[9]
                Near_DirZ = q[10]

                Grav = (1000*Near_S)/(Dist**2)

                if Grav<0.1:
                    Force = Grav*S
                else:
                    Force = (Grav/10)*S

                Move_Dist = Dist*Force
                
                New_XY = new_coord(Dist, Move_Dist, Near_Diff_Y, Near_Diff_Z, X, Y, Near_DirX, Near_DirY)

                X = New_XY[0]
                Y = New_XY[1]
                Z = New_XY[2]

            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])
            
    elif i >= 20 and i < 50:
        X = random.randint(10000)
        Y = random.randint(10000)
        Z = random.randint(10000)
        S = random.uniform(8,9)

        Test_Coord = [X,Y,Z]


        Near = find_nearest_n(Full_List, Test_Coord)
        
        if Near[0] == 0:
            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

        else:
            for q in Near:
                Dist = q[0]
                Near_X = q[2]
                Near_Y = q[3]
                Near_Z = q[4]
                Near_S = q[5]
                Near_Diff_Y = q[6]
                Near_Diff_Z = q[7]
                Near_DirX = q[8]
                Near_DirY = q[9]
                Near_DirZ = q[10]

                Grav = (1000*Near_S)/(Dist**2)

                if Grav<0.1:
                    Force = Grav*S
                else:
                    Force = (Grav/10)*S

                Move_Dist = Dist*Force
                
                New_XY = new_coord(Dist, Move_Dist, Near_Diff_Y, Near_Diff_Z, X, Y, Near_DirX, Near_DirY)

                X = New_XY[0]
                Y = New_XY[1]
                Z = New_XY[2]

            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])
            
    elif i >= 50 and i < 100:
        X = random.randint(10000)
        Y = random.randint(10000)
        Z = random.randint(10000)
        S = random.uniform(7,8)

        Test_Coord = [X,Y,Z]


        Near = find_nearest_n(Full_List, Test_Coord)
        
        if Near[0] == 0:
            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

        else:
            for q in Near:
                Dist = q[0]
                Near_X = q[2]
                Near_Y = q[3]
                Near_Z = q[4]
                Near_S = q[5]
                Near_Diff_Y = q[6]
                Near_Diff_Z = q[7]
                Near_DirX = q[8]
                Near_DirY = q[9]
                Near_DirZ = q[10]

                Grav = (1000*Near_S)/(Dist**2)

                if Grav<0.1:
                    Force = Grav*S
                else:
                    Force = (Grav/10)*S

                Move_Dist = Dist*Force
                
                New_XY = new_coord(Dist, Move_Dist, Near_Diff_Y, Near_Diff_Z, X, Y, Near_DirX, Near_DirY)

                X = New_XY[0]
                Y = New_XY[1]
                Z = New_XY[2]

            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])
            
    elif i >= 100 and i < 200:
        X = random.randint(10000)
        Y = random.randint(10000)
        Z = random.randint(10000)
        S = random.uniform(6,7)

        Test_Coord = [X,Y,Z]


        Near = find_nearest_n(Full_List, Test_Coord)
        
        if Near[0] == 0:
            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

        else:
            for q in Near:
                Dist = q[0]
                Near_X = q[2]
                Near_Y = q[3]
                Near_Z = q[4]
                Near_S = q[5]
                Near_Diff_Y = q[6]
                Near_Diff_Z = q[7]
                Near_DirX = q[8]
                Near_DirY = q[9]
                Near_DirZ = q[10]

                Grav = (1000*Near_S)/(Dist**2)

                if Grav<0.1:
                    Force = Grav*S
                else:
                    Force = (Grav/10)*S

                Move_Dist = Dist*Force
                
                New_XY = new_coord(Dist, Move_Dist, Near_Diff_Y, Near_Diff_Z, X, Y, Near_DirX, Near_DirY)

                X = New_XY[0]
                Y = New_XY[1]
                Z = New_XY[2]

            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])
            
    elif i >= 200 and i < 500:
        X = random.randint(10000)
        Y = random.randint(10000)
        Z = random.randint(10000)
        S = random.uniform(5,6)

        Test_Coord = [X,Y,Z]


        Near = find_nearest_n(Full_List, Test_Coord)
        
        if Near[0] == 0:
            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

        else:
            for q in Near:
                Dist = q[0]
                Near_X = q[2]
                Near_Y = q[3]
                Near_Z = q[4]
                Near_S = q[5]
                Near_Diff_Y = q[6]
                Near_Diff_Z = q[7]
                Near_DirX = q[8]
                Near_DirY = q[9]
                Near_DirZ = q[10]

                Grav = (1000*Near_S)/(Dist**2)

                if Grav<0.1:
                    Force = Grav*S
                else:
                    Force = (Grav/10)*S

                Move_Dist = Dist*Force
                
                New_XY = new_coord(Dist, Move_Dist, Near_Diff_Y, Near_Diff_Z, X, Y, Near_DirX, Near_DirY)

                X = New_XY[0]
                Y = New_XY[1]
                Z = New_XY[2]

            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])
            
    elif i >= 500 and i < 1000:
        X = random.randint(10000)
        Y = random.randint(10000)
        Z = random.randint(10000)
        S = random.uniform(4,5)

        Test_Coord = [X,Y,Z]


        Near = find_nearest_n(Full_List, Test_Coord)
        
        if Near[0] == 0:
            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

        else:
            for q in Near:
                Dist = q[0]
                Near_X = q[2]
                Near_Y = q[3]
                Near_Z = q[4]
                Near_S = q[5]
                Near_Diff_Y = q[6]
                Near_Diff_Z = q[7]
                Near_DirX = q[8]
                Near_DirY = q[9]
                Near_DirZ = q[10]

                Grav = (1000*Near_S)/(Dist**2)

                if Grav<0.1:
                    Force = Grav*S
                else:
                    Force = (Grav/10)*S

                Move_Dist = Dist*Force
                
                New_XY = new_coord(Dist, Move_Dist, Near_Diff_Y, Near_Diff_Z, X, Y, Near_DirX, Near_DirY)

                X = New_XY[0]
                Y = New_XY[1]
                Z = New_XY[2]

            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

    elif i >= 1000 and i < 3000:
        X = random.randint(10000)
        Y = random.randint(10000)
        Z = random.randint(10000)
        S = random.uniform(3,4)

        Test_Coord = [X,Y,Z]


        Near = find_nearest_n(Full_List, Test_Coord)
        
        if Near[0] == 0:
            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

        else:
            for q in Near:
                Dist = q[0]
                Near_X = q[2]
                Near_Y = q[3]
                Near_Z = q[4]
                Near_S = q[5]
                Near_Diff_Y = q[6]
                Near_Diff_Z = q[7]
                Near_DirX = q[8]
                Near_DirY = q[9]
                Near_DirZ = q[10]

                Grav = (1000*Near_S)/(Dist**2)

                if Grav<0.1:
                    Force = Grav*S
                else:
                    Force = (Grav/10)*S

                Move_Dist = Dist*Force
                
                New_XY = new_coord(Dist, Move_Dist, Near_Diff_Y, Near_Diff_Z, X, Y, Near_DirX, Near_DirY)

                X = New_XY[0]
                Y = New_XY[1]
                Z = New_XY[2]

            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])
            

    elif i >= 3000 and i < 5000:
        X = random.randint(10000)
        Y = random.randint(10000)
        Z = random.randint(10000)
        S = random.uniform(2,3)

        Test_Coord = [X,Y,Z]


        Near = find_nearest_n(Full_List, Test_Coord)
        
        if Near[0] == 0:
            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

        else:
            for q in Near:
                Dist = q[0]
                Near_X = q[2]
                Near_Y = q[3]
                Near_Z = q[4]
                Near_S = q[5]
                Near_Diff_Y = q[6]
                Near_Diff_Z = q[7]
                Near_DirX = q[8]
                Near_DirY = q[9]
                Near_DirZ = q[10]

                Grav = (1000*Near_S)/(Dist**2)

                if Grav<0.1:
                    Force = Grav*S
                else:
                    Force = (Grav/10)*S

                Move_Dist = Dist*Force
                
                New_XY = new_coord(Dist, Move_Dist, Near_Diff_Y, Near_Diff_Z, X, Y, Near_DirX, Near_DirY)

                X = New_XY[0]
                Y = New_XY[1]
                Z = New_XY[2]

            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

    elif i >= 5000 and i < 8000:
        X = random.randint(10000)
        Y = random.randint(10000)
        Z = random.randint(10000)
        S = random.uniform(1,2)

        Test_Coord = [X,Y,Z]


        Near = find_nearest_n(Full_List, Test_Coord)
        
        if Near[0] == 0:
            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

        else:
            for q in Near:
                Dist = q[0]
                Near_X = q[2]
                Near_Y = q[3]
                Near_Z = q[4]
                Near_S = q[5]
                Near_Diff_Y = q[6]
                Near_Diff_Z = q[7]
                Near_DirX = q[8]
                Near_DirY = q[9]
                Near_DirZ = q[10]

                Grav = (1000*Near_S)/(Dist**2)

                if Grav<0.1:
                    Force = Grav*S
                else:
                    Force = (Grav/10)*S

                Move_Dist = Dist*Force
                
                New_XY = new_coord(Dist, Move_Dist, Near_Diff_Y, Near_Diff_Z, X, Y, Near_DirX, Near_DirY)

                X = New_XY[0]
                Y = New_XY[1]
                Z = New_XY[2]

            Full_List.append([X, Y, Z, S])
            Coord_List.append([X,Y, Z])
            S_List.append([S])

X_Coord_List = [item[0] for item in Coord_List]
Y_Coord_List = [item[1] for item in Coord_List]
Z_Coord_List = [item[2] for item in Coord_List]

plt.scatter(X_Coord_List, Y_Coord_List, Z_Cood_List, s = S_List)
plt.show()
