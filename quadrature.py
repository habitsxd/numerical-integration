import numpy as np

#-------------------------------------NEWTON-COTES DATA-----------------------------------------------------------------#
nx_nodes = np.array([-1,0.5,0,0.5,1])
nx_weights = np.array([0.156,0.7111,0.267,0.7111,0.156])
#-------------------------------------LOBATTO DATA----------------------------------------------------------------------#
lx_nodes = np.array([-1,-np.sqrt(0.4286),0,np.sqrt(0.4286),1])
lx_weights = np.array([0.1,0.5445,0.7111,0.5445,0.1])
#-------------------------------------GAUSSIAN DATA---------------------------------------------------------------------#
gx_nodes = np.array([-0.53846,-0.90617,0,0.90617,0.53846])
gx_weights = np.array([0.47862,0.23692,0.56888,0.47862,0.23692])
#-------------------------------------TRUE VALUES-----------------------------------------------------------------------#
true_s = 0.583853163453
true_sq = 3.885618083164
true_t = 1.325002747358
#-------------------------------------FUNCTION DEFINITIONS--------------------------------------------------------------#
def sin_func(x):
   return 1 - np.sin(1 - x)

def sqrt_func(x):
    return np.sqrt(x + 1) + 1

def tan_func(x):
    return np.tanh(x + 1)
#-------------------------------------QUADRATURE FUNCTION---------------------------------------------------------------#
def quadrature(weights, nodes, func):
    '''multiplies the weights vector by the function along the function vector
    and returns the result'''
    res = 0
    for i in range(len(nx_nodes)):
        res += weights[i] * func(nodes[i])
    return res
#-----------------------------------------OUTPUT FUNCTION---------------------------------------------------------------#
def print_array(method,type,array):
    '''prints formatted arrays for the given method'''
    print(method + " " + type + " are:")
    for i in array:
        print(str(i), end = "\t")
    print()
#-------------------------------------CALCULATIONS FOR NEWTON-COTES-----------------------------------------------------#
n_res0 = quadrature(nx_weights,nx_nodes,sin_func) 
n_res1 = quadrature(nx_weights,nx_nodes,sqrt_func)
n_res2 = quadrature(nx_weights,nx_nodes,tan_func)
#-------------------------------------CALCULATIONS FOR LOBATTO----------------------------------------------------------#
l_res0 = quadrature(lx_weights,lx_nodes,sin_func)
l_res1 = quadrature(lx_weights,lx_nodes,sqrt_func)
l_res2 = quadrature(lx_weights,lx_nodes,tan_func)
#-------------------------------------CALCULATIONS FOR GAUSSIAN---------------------------------------------------------#
g_res0 = quadrature(gx_weights,gx_nodes,sin_func)
g_res1 = quadrature(gx_weights,gx_nodes,sqrt_func)
g_res2 = quadrature(gx_weights,gx_nodes,tan_func)
#-------------------------------------CALCULATIONS FOR NEWTON-COTES ERROR-----------------------------------------------#
err_n0 = abs(true_s - n_res0)
err_n1 = abs(true_sq - n_res1)
err_n2 = abs(true_t - n_res2)
#-------------------------------------CALCULATIONS FOR LOBATTO ERROR----------------------------------------------------#
err_l0 = abs(true_s - l_res0)
err_l1 = abs(true_sq - l_res1)
err_l2 = abs(true_t - l_res2)
#-------------------------------------CALCULATIONS FOR GAUSSIAN ERROR---------------------------------------------------#
err_g0 = abs(true_s - g_res0)
err_g1 = abs(true_sq - g_res1)
err_g2 = abs(true_t - g_res2)
#-------------------------------------OUTPUT FORMATTING-----------------------------------------------------------------#
#output formatting for newton-cotes
print_array("Newton-Cotes", "nodes", nx_nodes)
print_array("Newton-Cotes", "weights", nx_weights)
print("Newton-Cotes Spacing Results: ") 
print("1 - sin(1 - x): " + str(n_res0) + "\t sqrt(x + 1) + 1: " + str(n_res1) + "\t tanh(x + 1): " + str(n_res2) + "\n")
print("Error For Newton- Cotes: ")
print("1 - sin(1 - x): " + str(err_n0) + "\t sqrt(x + 1) + 1: " + str(err_n1) + "\t tanh(x + 1): " + str(err_n2) + "\n")
#output formatting for Lobatto
print_array("Lobatto", "nodes", lx_nodes)
print_array("Lobatto", "weights", lx_weights)
print("Lobatto Spacing Results: ")
print("1 - sin(1 - x): " + str(l_res0) + "\t sqrt(x + 1) + 1: " + str(l_res1) + "\t tanh(x + 1): " + str(l_res2) + "\n")
print("Error For Lobatto: ")
print("1 - sin(1 - x): " + str(err_l0) + "\t sqrt(x + 1) + 1: " + str(err_l1) + "\t tanh(x + 1): " + str(err_l2) + "\n")
#output formatting for Gaussian
print_array("Gaussian", "nodes", gx_nodes)
print_array("Gaussian", "weights", gx_weights)
print("Gaussian Spacing Results: ")
print("1 - sin(1 - x): " + str(g_res0) + "\t sqrt(x + 1) + 1: " + str(g_res1) + "\t tanh(x + 1): " + str(g_res2) + "\n")
print("Error For Gaussian: ")
print("1 - sin(1 - x): " + str(err_g0) + "\t sqrt(x + 1) + 1: " + str(err_g1) + "\t tanh(x + 1): " + str(err_g2) + "\n")




    