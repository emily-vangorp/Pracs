TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_period = int(input("Enter number of billing days: "))
if tariff == 11:
    estimated_bill = TARIFF_11 * daily_use * billing_period
else:
    estimated_bill = TARIFF_31 * daily_use * billing_period
print("Estimated bill:", "{:.2f}".format(estimated_bill))
