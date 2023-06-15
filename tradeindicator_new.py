import re
def trade_indicator(event):
    try:
      if 'Стоп' and '#' in event.message.message:
        message = event.message.message
        symbol = re.findall(r"#(\w+/\w+)", message)[0]
        signal_type = "LONG" if "LONG" in message else "SHORT"
        entry = message.split("Открытие - ")[1].split("\n")[0]
        targets = re.findall(r"\d-\d+\.\d+", message)
        formatted_targets = [f"{i+1}) {target.split('-')[1].strip()}" for i, target in enumerate(targets)]
        leverage = message.split("Плечо - х")[1].split(" (")[0]
        stop_loss = message.split("Стоп - ")[1].split("\n")[0]
        converted_message = f"""#{symbol}
Exchanges: Binance Futures
Signal Type: {signal_type}
Entry - {entry}
Take-Profit Targets: 
{formatted_targets[0]}
{formatted_targets[1]}
{formatted_targets[2]}
{formatted_targets[3]}
Leverage: Cross х{leverage}
Stop Loss - {stop_loss}
"""
        return converted_message
      else:
        pass
    except TypeError:
      pass