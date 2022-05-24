month = input()
nights_count = int(input())

if month in ['May', 'October']:
    ap_cost = nights_count * 65
    st_cost = nights_count * 50
    
    if 7 < nights_count <= 14:
        st_cost = st_cost * (1 - 0.05)
    elif 14 < nights_count:
        ap_cost = ap_cost * (1 - 0.1)
        st_cost = st_cost * (1 - 0.3)

elif month in ['June', 'September']:
    ap_cost = nights_count * 68.7
    st_cost = nights_count * 75.2
    
    if 14 < nights_count:
        ap_cost = ap_cost * (1 - 0.1)
        st_cost = st_cost * (1 - 0.2)

elif month in ['July', 'August']:
    ap_cost = nights_count * 77
    st_cost = nights_count * 76
    
    if 14 < nights_count:
        ap_cost = ap_cost * (1 - 0.1)
    
print(f'Apartment: {ap_cost:.2f} lv.\nStudio: {st_cost:.2f} lv.')
