Ah, So SLOW:

variance = 0
mp_mean = nba_stats["mp"].mean()
for p in nba_stats["mp"]:
    difference = p - mp_mean
    square_difference = difference ** 2
    mp_variance += square_difference
mp_variance = mp_variance / len(nba_stats["mp"])
mp_dev = mp_variance ** 1/2

ast_mean = nba_stats["ast"].mean()
for p in nba_stats["pts"]:
    difference = p - ast_mean
    square_difference = difference ** 2
    ast_variance += square_difference
ast_variance = ast_variance / len(nba_stats["ast"])
ast_dev = ast_variance ** 1/2

If that ^ was more or less the structure so far, why doesn’t this work for #10 on Standard deviations?:

wing_mean = sum(wing_lengths) / len(wing_lengths)
for l in wing_lengths:
    difference = l - wing_mean
    square_difference = difference ** 2
    variance += square_difference
variance = variance / len(wing_lengths)
std_wing = variance ** (1/2)

for l in wing_lengths:
    percentage = (l - wing_mean) / std_wing

##more importantly, how do you know WHEN TO DEFINE A FORMULA?

Is this the same?
mean = sum(wing_lengths) / len(wing_lengths)
variances = [(i - mean) ** 2 for i in wing_lengths]
variance = sum(variances)/len(variances)
std_dev = variance ** 2

for l in wing_lengths:
    difference = l - wing_mean
    square_difference = difference ** 2
    variance += square_difference
variance = variance / len(wing_lengths)
std_wing = variance ** (1/2)

Or this?
std_dev_list = [(i - mean) / std_dev for i in wing_lengths]

for l in wing_lengths:
    percentage = (l - wing_mean) / std_wing

Go back to this:
# Housefly wing lengths in millimeters
wing_lengths = [36, 37, 38, 38, 39, 39, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 52, 52, 53, 53, 54, 55]
mean = sum(wing_lengths) / len(wing_lengths)
variance_list = [(i - mean) ** 2 for i in wing_lengths]
variance = sum(variance_list)/len(variance_list)
std_dev = variance ** (1/2)

std_dev_list = [(i - mean) / std_dev for i in wing_lengths]
#how do I know I need to write this part, and how to calculate it?
def within_percent(deviations, count):
    within_list = [i for i in deviations if i <= count and i >= -count]
    count = len(within_list)
    return count /len(deviations)
#also, "Count" is defined, but not "deviations"--wtf?

More failed code: Lin regression:

def calc_yati(x):
    diff = [y - i] for i in y
    y = (slope * x) + intercept
    return sum(diff ** 2)

rss = wine_quality["density"].apply(calc_yati)

REAL answer:
import numpy as np

predicted_y = numpy.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_y) ** 2
rss = sum(residuals)

QUESTION: How to know when to import numpy or scipy? Also, how do you know when to use asarray[] vs .apply()?
