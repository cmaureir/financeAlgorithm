import numpy as np
import math as ma
import traceback
import sys

#Rows
rows = 2500

#Columns
cols = 1500

#Default lambda
l = 0.1

def concatMatrix(a,l):
	l_i = l*np.identity(cols)	
	return np.concatenate((a,l_i))

def iteration(A, C, b, l):
	#Step 0, qr factorization of C, and create Q_1, -inverse(rows+lI)
	try:
		q, r = np.linalg.qr(C)
		q1 = q[0:rows, 0:cols]
		M = np.dot(A,np.transpose(A))
		l_i = l*np.identity(cols)
		coe = - np.linalg.inv(M + l*np.identity(rows))	
	except:
		print "Step 0, problems"

	#Step 1, x_k = inv(R) * transpose(Q_1) * b
	try:
		inv_r = np.linalg.inv(r)
		trans_q1 = np.transpose(q1)
		rq = np.dot(inv_r, trans_q1)
		xk = np.dot(rq,b)
		print inv_r.shape, trans_q1.shape, b.shape
	except:
		print "Step 1, problems"

	#Step 2, s_0 = x_0
	try:
		sk = xk
	except:
		print "Step 2, problems"

	#Step 3, iteration
	try:
		print coe.shape
		print sk.shape
		for k in range(1):
			sk = np.dot(coe, sk)
			xk = xk + ma.pow(-1,k)*ma.pow(l,k)*sk
	except Exception, err:
		print "Step 3, problems"
		print traceback.format_exc()


A = np.random.rand(rows,cols)
b = np.random.rand(rows,1)
C = concatMatrix(A,ma.pow(l,0.5))

iteration(A, C, b, l)
#print matrixC("hola",l)



