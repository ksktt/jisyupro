from servo import controller
import math

def calculate():
    x_deg, y_deg, dis = controller()

    #print("x deg {}, y deg {}, dis {}".format(x_deg, y_deg, dis))
    dim2_dis = dis * math.sin(math.radians(y_deg))
    #print(dim2_dis)
    x_pos = dim2_dis * math.cos(math.radians(x_deg))
    y_pos = dim2_dis * math.sin(math.radians(x_deg))

    return x_pos, y_pos

if __name__=="__main__":
    x, y = calculate()
    print("x {}, y {}".format(x, y))
