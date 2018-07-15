import numpy as np
from MosaicPlot import MosaicPlot as mp
import Interpolations as pol
import time

def main():
	img = np.array([[0.20966011, 0.46244196, 0.85678337, 0.24892138, 0.65882897, 0.17479739],
	[0.65761386, 0.54535605, 0.20861746, 0.61597225, 0.88594544, 0.17675478],
	[0.81582248, 0.56669197, 0.47976072, 0.71329168, 0.08283209, 0.4012043 ],
	[0.64012971, 0.60011478, 0.65507587, 0.03107767, 0.217446,   0.65748758],
	[0.84188694, 0.74767014, 0.235597,   0.83863067, 0.75734715, 0.22550759],
	[0.12377143, 0.25691292, 0.01799602, 0.1075182, 0.04957209, 0.91041073]])

	img = np.array([
		[0,0,0,3,0,0,0,0],
		[0,3,0,0,0,0,0,3],
		[3,0,3,0,0,0,0,0],
		[0,0,0,5,0,0,6,0],
		[10,7,5,7,10,0,10, 0],
		[10,10,5,7,7,5,10, 0],
		[10,0,0,10,10,7,0, 0],
		[5,7,5,3,0,0,0, 0],
		[5,3,0,5,3,0,5,3],
		[3,5,0,0,0,0,3,4],
		[0,0,0,0,3,0,4,3],
	])

	new_img_nn = pol.resize(img=img, fac_x=15.0, fac_y=15.0, method="nn")
	new_img_bilinear = pol.resize(img=img, fac_x=15.0, fac_y=15.0, method="bilinear2")
	start = time.time()
	new_img_bicubic = pol.resize(img=img, fac_x=15.0, fac_y=15.0, method="bicubic")
	end = time.time()
	print(end-start)

	plot1 = mp(mat_data=new_img_nn)
	plot2 = mp(mat_data=new_img_bilinear)
	plot3 = mp(mat_data=new_img_bicubic)
	plot1.show()
	plot2.show()
	plot3.show()

	#pol.bicubic_refs(img, (200,200), f, f)
    
if __name__ == "__main__":
    main()
