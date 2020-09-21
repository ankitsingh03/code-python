exam_st_date = '(11, 12, 2014)'
# Sample Output : The examination will start from : 11 / 12 / 2014

date = exam_st_date[1:-1]
print(" /".join(date.strip().split(',')))
