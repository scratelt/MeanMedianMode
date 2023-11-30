



def mean_data(data):
	calculated_mean = sum(data) / len(data)
	return round(calculated_mean, 3)

def median_data(data: list[int]):
	ordered_data: list[int] = sorted(data)
	length: int = len(ordered_data)
	
	if length % 2 == 1:
		# odd
		# getting index of the median value for the above ordered data
		mid_point_index = length // 2
		# returning the value from the index for the median
		median_value = ordered_data[mid_point_index]
	else:
		# even 
		# Indexes
		upper_middle_index = length // 2
		lower_middle_index = upper_middle_index - 1
		# valued
		upper_middle_value = ordered_data[upper_middle_index]
		lower_middle_value = ordered_data[lower_middle_index]
		# get median using mid_point_index
		median_value = (upper_middle_value + lower_middle_value) / 2
		
	# round median to 2 decimals
	return round(median_value, 2)






def main():
	data_set_one = [6, 9, 1, 2, 6, 3, 7]
	data_set_two = [6, 9, 1, 2, 6, 3, 7, 4]
	data_set_three = [6, 9, 1, 2, 6, 3, 7, 4, 1]
	data_set_four = [6, 9, 1, 2, 3, 7, 4, 8] 

	print(mean_data(data_set_one))
	print(median_data(data_set_one))
	print(median_data(data_set_two))

if __name__ == '__main__':
	main()