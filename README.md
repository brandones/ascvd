# Python ASCVD

Install it: `pip install ascvd`

Should be compatible with Python 2 and 3 alike.

Should agree with http://tools.acc.org/ASCVD-Risk-Estimator-Plus/#!/calculate/estimate/

Code mostly borrowed from https://github.com/cerner/ascvd-risk-calculator

Referring to the README for that project, this calculates the ASCVD risk according 
to the [2013 ACC/AHA Guideline on the Assessment of Cardiovascular Risk](http://circ.ahajournals.org/content/circulationaha/129/25_suppl_2/S49.full.pdf)
and the [2013 ACC/AHA Guideline on the Treatment of Blood Cholesterol to Reduce Atherosclerotic Cardiovascular Risk in Adults](http://circ.ahajournals.org/content/circulationaha/129/25_suppl_2/S1.full.pdf). 


## Documentation:

It's a single function.

```
compute_ten_year_score -> int
    Args:
        isMale (bool)
        isBlack (bool)
        smoker (bool)
        hypertensive (bool)
        diabetic (bool)
        age (int)
        systolicBloodPressure (int)
        totalCholesterol (int)
        hdl (int)
```

## Contributing

This could really use some tests! The code right now pretty much just assumes
that the good folks at Cerner are superhumans who don't make mistakes.

Feel free to fork and open a pull request. Please, one pull request per
functional change.

