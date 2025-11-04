import arrow
brerwing_time = arrow.utcnow()
print(brerwing_time)
brerwing_time.to("Europe/Rome")
print(brerwing_time)