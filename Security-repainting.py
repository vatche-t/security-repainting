
study("HTF High/Low", overlay=true)

//ورودی کاربر
res = input(title="Timeframe", type=input.resolution, defval="D")

//non-repainting security function
rp_security(_symbol, _res, _src) => security(_symbol, _res, _src[barstate.isrealtime ? 1 : 0])

//HTF price data
htfHigh = rp_security(syminfo.tickerid, res, high)
htfLow = rp_security(syminfo.tickerid, res, low)

// Plot data to chart
plot(htfHigh, color=color.red, title="HTF High")
plot(htfLow, color=color.blue, title="HTF Low")

// Trigger breakout alerts
alسertcondition(close > htfHigh or close < htfLow, title="HTF Breakout Alert!", message="HTF Breakout Alert For: {{ticker}}")