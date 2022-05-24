time_record = float(input()) # seconds
distance = float(input()) # meters
velocity_ivan = float(input()) # meters / seconds

delay_ivan = distance // 15 * 12.5 # for each 15m a delay of 12.5 seconds

time_ivan = distance * velocity_ivan + delay_ivan

time_difference = time_ivan - time_record
if time_difference < 0:
    print(f'Yes, he succeeded! The new world record is {time_ivan:.2f} seconds.')
else:
    print(f'No, he failed! He was {time_difference:.2f} seconds slower.')