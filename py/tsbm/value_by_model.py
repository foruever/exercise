from statsmodels.tsa.arima_model import ARIMAResults
import sys


if __name__=='__main__' :
    sn=sys.argv[1]
    t_time=sys.argv[2]
    t_time=int(t_time)%163731;

    load_model = ARIMAResults.load('model/' + str(sn) + '.model')
    print(str(sn))
    values = load_model.fittedvalues
    print(values[t_time])
