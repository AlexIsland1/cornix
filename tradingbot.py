import re
def trading(message1,message2):
    try:
      if 'Стоп' in message1:     
        new = message1.split('\n')
        symbol = new[0][1:]
        for i in new:
          if i :
            if '#'in i:
              split = i.split('-')
              s = ''.join(split[0]).find('#')
              symbol = ''.join(split[0])[s:].replace('*','')
              signal_type = "LONG" if "LONG" in i else "SHORT"             
            elif 'Открытие' in i:
              entry = re.search(r"\d+\.\d+", i).group()                              
    except TypeError:
      pass
    try:
      formatted_targets = re.findall(r'\d+\.\d+', message2) 
    except TypeError:
      pass
    entry2 = (float(formatted_targets[3])+float(entry))/2 
    converted_message = f"""{symbol}/USDT
Exchanges: Binance Futures
Signal Type: {signal_type}
Entry - {entry}-{entry2}
Take-Profit Targets: 
1) {formatted_targets[0]}
2) {formatted_targets[1]}
3) {formatted_targets[2]}
Leverage: Cross х20
Stop Loss - {formatted_targets[3]}
"""
    return converted_message

