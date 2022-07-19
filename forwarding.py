from pyrogram import Client, filters

bot  = Client('userbot', api_hash="e454be121e26e7084623448be8e9eb39", api_id=10738602)

chan_list = { # channel/group ID target      :       channel/group ID to forward
             -1001645356328 : -1001702155604,
             #-100 : -100,
            }


@bot.on_message(filters.chat(list(chan_list)))
async def forwading_message(client, message):
    print(f'new message: {message.id}')
    chat_id = message.chat.id
    forward_chat = chan_list[chat_id]
    await message.forward(forward_chat)


bot.run()
