def time_saved(s_lim, s_avg, d):
	return round(((d/s_lim)-(d/s_avg))*60,1)
print(time_saved(80, 90, 4000))
