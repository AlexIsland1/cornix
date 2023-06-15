import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from tradeindicator_new import trade_indicator
from tradingbot import trading
from wtpremium import wt
async def main():
    session_file = 'session.journal'
    client = TelegramClient(session_file, api_id="24620605", api_hash="7c287a8b251c3fe6548050b6cd216cda")
    await client.connect()
    if not await client.is_user_authorized():
        phone = '998900452030'
        await client.send_code_request(phone)
        code = input("Enter the code you received: ")
        try:
            await client.sign_in(phone, code)
        except Exception as e:
            if "Two-steps verification" in str(e):
                password = 'Ue,fkt[1'
                await client.sign_in(password=password)
    print('Authorized')
    await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer='username',
        limit=500,
        hash=0,))
    ls_channels = [1654577205]
    entities = []
    for channel_name in ls_channels:
        entity = await client.get_entity(channel_name)
        entities.append(entity)
    print('All set, starting to listen for a signals')        
    @client.on(events.NewMessage(chats=entities))
    async def handler(event):
        if event.peer_id.channel_id == 1869173929:
          if event.reply_to == None:
            await client.send_message(1751128690,trade_indicator(event))
        elif event.peer_id.channel_id == 1610165996:
          if event.reply_to != None:
              if 'TP:' and 'SL:' in event.message.message:
                message2 = event.message.message
                chat_id = event.message.reply_to_msg_id
                chanell = await client(GetFullChannelRequest(1610165996))
                chats = await client.get_messages(chanell.full_chat,limit=10)
                message1 = ''
                for chat in chats:
                  try:
                    if chat.id == chat_id:
                      message1 = chat.text
                  except TypeError:                                   
                    pass
                await client.send_message(1664498025,trading(message1,message2))
        elif event.peer_id.channel_id == 1810091012:
            if event.reply_to == None:
              if 'Вход:' and 'Стоп:' in event.message.message:
                  await client.send_message(1671710449,wt(event.message.message))
                   
                    
    await client.start()
    await client.run_until_disconnected()
asyncio.run(main())

