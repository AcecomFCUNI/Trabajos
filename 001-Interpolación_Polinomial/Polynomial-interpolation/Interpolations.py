import numpy as np
import math
#import numerico as nc
import time

def resize(img, fac_x, fac_y, method):
	if method is "nn":
		result = nearest_neighbor(img, fac_x, fac_y)
	if method is "bilinear":
		result = bilinear_interpol(img, fac_x, fac_y)
	if method is "bilinear2":
		result = bilinear_interpol_2(img, fac_x, fac_y)
	if method is "bicubic":
		result = bicubic_interpol(img, fac_x, fac_y)
	
	return result

def nearest_neighbor(data, by_x, by_y):
	new_x = int(np.ceil( data.shape[0]*by_x ))
	new_y = int(np.ceil( data.shape[1]*by_y ))
	
	new_img = np.empty((new_x,  new_y))
		
	dec_ratio_x = 1.0/by_x
	dec_ratio_y = 1.0/by_y
	
	for i in range(0, new_img.shape[0]):
		for j in range(0, new_img.shape[1]):
			back_index_x = int(np.floor(i*dec_ratio_x))
			back_index_y = int(np.floor(j*dec_ratio_y))
			new_img[i, j] = data[back_index_x, back_index_y]
	
	return new_img
	
# Obtiene las referencias al primero de los 4 puntos de 'p'
# de la data antes de redimensionar, o retorna None si p
# esta fuera de los límites
def bilinear_refs(old_data, p, factor_x, factor_y):
	i_floor = np.floor(p[0]/factor_x)
	j_floor = np.floor(p[1]/factor_y)
	i_ceil = np.ceil(p[0]/factor_x)
	j_ceil = np.ceil(p[1]/factor_y)
	
	if i_ceil >= old_data.shape[0] or j_ceil >= old_data.shape[1]:
		return math.nan, math.nan
	else:
		Q_00_x = int(i_floor)
		Q_00_y = int(j_floor)
		
		return Q_00_x, Q_00_y
		
def bilinear_interpol(data, by_x, by_y):
	new_x = int(np.ceil( data.shape[0]*by_x ))
	new_y = int(np.ceil( data.shape[1]*by_y ))
	
	new_img = np.empty((new_x,  new_y))
		
	for i in range(0, new_img.shape[0]):
		for j in range(0, new_img.shape[1]):
			coord = (i, j)
			Q = bilinear_refs(data, coord ,by_x, by_y)
			
			x_0 = Q[0]
			y_0 = Q[1]
			x_1 = Q[0]+1
			y_1 = Q[1]+1
			
			if(x_1 >= data.shape[0]):
				x_1 -= 1
				x_0 -= 1
			
			if(y_1 >= data.shape[1]):
				y_1 -= 1
				y_0 -= 1
			
			if not (math.isnan(x_0) or math.isnan(y_0)):
				factor = 1/((x_1 - x_0)*(y_1 - y_0))
				X = np.array([
				[x_1 - i/by_x],
				[i/by_x - x_0]
				]).T
				
				fQ = np.array([
				[ data[x_0, y_0],  data[x_0, y_1] ],
				[ data[x_1, y_0],  data[x_1, y_1] ]
				])
				
				Y = np.array([
				[y_1 - j/by_y],
				[j/by_y - y_0]
				])
				
				new_img[i, j] = factor*np.matmul(np.matmul(X, fQ) , Y)
	return new_img[:int((data.shape[0]-1)*by_x),:int((data.shape[1]-1)*by_y)]
	
def bilinear_interpol_2(data, by_x, by_y):
	new_x = int(np.ceil( data.shape[0]*by_x ))
	new_y = int(np.ceil( data.shape[1]*by_y ))
	
	new_img = np.empty((new_x,  new_y))
		
	start = time.time()	
	for i in range(0, new_img.shape[0]):
		for j in range(0, new_img.shape[1]):
			coord = (i, j)
			Q = bilinear_refs(data, coord ,by_x, by_y)
			
			x_0 = Q[0]
			y_0 = Q[1]
			x_1 = Q[0]+1
			y_1 = Q[1]+1
			
			if(x_1 >= data.shape[0]):
				x_1 -= 1
				x_0 -= 1
			
			if(y_1 >= data.shape[1]):
				y_1 -= 1
				y_0 -= 1
			
			if not (math.isnan(x_0) or math.isnan(y_0)):
				A = np.array([
				[1.0, x_0, y_0, x_0*y_0],
				[1.0, x_0, y_1, x_0*y_1],
				[1.0, x_1, y_0, x_1*y_0],
				[1.0, x_1, y_1, x_1*y_1]
				])

				fQ = np.array([
				[ data[x_0, y_0] ],
				[ data[x_0, y_1] ],
				[ data[x_1, y_0] ],
				[ data[x_1, y_1] ]
				])
			
			result = np.linalg.solve(A, fQ)
			new_img[i,j] = result[0] + result[1]*i/by_x + result[2]*j/by_y + result[3]*i*j/(by_x*by_y)
		end = time.time()
	#print("Bilinear interpolation exec. time: ", end - start)
	return new_img[:int((data.shape[0]-1)*by_x),:int((data.shape[1]-1)*by_y)]

def w_cub(x):
	val = 0

	if (0 <= np.abs(x)) and (np.abs(x) < 1):
		val = np.abs(x)**3 - 2*np.abs(x)**2 + 1.0
	elif (1 <= np.abs(x)) and (np.abs(x) < 2):
		val = -np.abs(x)**3 + 5*np.abs(x)**2 - 8*np.abs(x) + 4.0
	else:
		val = 0
	return val

def p_bicubic_interpol(data, p_ij):
	q = 0
	for j in range(0, 3):
		v = int(np.floor(p_ij[1] - 1 + j))
		p = 0
		for i in range(0, 3):
			u = int(np.floor(p_ij[0]) - 1 + i)
			p = p + data[u, v]*w_cub(p_ij[0] - u)
		q = q + p*w_cub(p_ij[1] - v)
	return q

def bicubic_interpol(data, by_x, by_y):
	new_data = np.empty((int(data.shape[0]*by_x), int(data.shape[1]*by_y)))

	for i in range(0, new_data.shape[0] - int(by_x)):
		for j in range(0, new_data.shape[1] - int(by_y)):
			new_data[i, j] = p_bicubic_interpol(data, (float(i)/by_x, float(j)/by_y))

	return new_data[:int((data.shape[0]-1)*by_x),:int((data.shape[1]-1)*by_y)]
