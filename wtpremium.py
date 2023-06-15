import re
def wt(message):
    try:
      spl = message.split('\n')
      line = spl[0].split(' ')
      symbol = line[0].replace('*','')[1:]
      signal_type = line[1].replace('*','')
      entry =''.join(re.findall(r'\d+\.\d+', spl[2]))
      if entry == '':
        entry =''.join(re.findall(r'\d+', spl[2]))
      target1 = ''.join(re.findall(r'\d+\.\d+', spl[4]))
      if target1 == '':
        target1 =''.join(re.findall(r'\d+', spl[4]))
      target2 = ''.join(re.findall(r'\d+\.\d+', spl[5]))
      if target2 == '':
        target2 =''.join(re.findall(r'\d+', spl[5]))
      target3 = ''.join(re.findall(r'\d+\.\d+', spl[6]))
      if target3 == '':
        target3 =''.join(re.findall(r'\d+', spl[6]))
      target4 = ''.join(re.findall(r'\d+\.\d+', spl[7]))
      if target4 == '':
        target4 =''.join(re.findall(r'\d+', spl[7]))
      stop_loss = ''.join(re.findall(r'\d+\.\d+', spl[9]))
      if stop_loss == '':
        stop_loss =''.join(re.findall(r'\d+', spl[9]))
      entry2 = (float(entry)+float(stop_loss))/2
      converted_message = f"""#{symbol}/USDT
Exchanges: Binance Futures
Signal Type: {signal_type}
Entry - {entry}-{round(entry2,5)}
Take-Profit Targets: 
1) {target1}
2) {target2}
3) {target3}
4) {target4}
Leverage: Cross х20
Stop Loss - {stop_loss}
"""
      return converted_message
    except TypeError:
      pass
