cpu_price_usd = float(input())
gpu_price_usd = float(input())
ram_price_usd = float(input())
ram_count = int(input())
discount = float(input())

cpu_cost_usd = cpu_price_usd * (1 - discount)
gpu_cost_usd = gpu_price_usd * (1 - discount)
ram_cost_usd = ram_count * ram_price_usd

total_cost_usd = cpu_cost_usd + gpu_cost_usd + ram_cost_usd

bgnusd = 1.57
total_cost_bgn = total_cost_usd * bgnusd

print(f'Money needed - {total_cost_bgn:.2f} leva.')