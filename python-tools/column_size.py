def column_width(image_width):
	
	col_width=[["col-lg-1",8.33332],["col-lg-2",16.66664],["col-lg-3",25],["col-lg-4",33.3333],["col-lg-5",41.66667],["col-lg-6",50],["col-lg-7",58.33336],["col-lg-8",66.6666],["col-lg-9",75],["col-lg-10",83.33334],["col-lg-11",91.6666],["col-lg-12",100]]
	
	for c in col_width:
		col_percentage = float(c[1])
		col_size = col_percentage / 100.0 * 940.0
		

		if image_width <= col_size:
			print "recommended div class is %s" % (c[0])
			print "for an image size of %d , max column size of %d, " % (image_width, col_size)
			break

column_width(940.0)