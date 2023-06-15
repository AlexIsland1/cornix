import re
def wt(message):
    try:
      if 'Вход:' and 'Стоп:' in message:
        spl = message.split('\n')
        line = spl[0].split(' ')
        symbol = line[0][1:]
        signal_type = line[1]
        entry =''.join(re.findall(r'\d+\.\d+', spl[2]))
        target1 = ''.join(re.findall(r'\d+\.\d+', spl[4]))
        target2 = ''.join(re.findall(r'\d+\.\d+', spl[5]))
        target3 = ''.join(re.findall(r'\d+\.\d+', spl[6]))
        target4 = ''.join(re.findall(r'\d+\.\d+', spl[7]))
        stop_loss = ''.join(re.findall(r'\d+\.\d+', spl[9]))
        entry2 = (float(entry)+float(stop_loss))/2
        converted_message = f"""#{symbol}/USDT
Exchanges: Binance Futures
Signal Type: {signal_type}
Entry - {entry}-{entry2}
Take-Profit Targets: 
1) {target1}
2) {target2}
3) {target3}
4) {target4}
Leverage: Cross х20
Stop Loss - {stop_loss}
"""
        return converted_message
      else:
        pass
    except TypeError:
      pass
