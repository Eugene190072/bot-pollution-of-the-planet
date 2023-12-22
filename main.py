import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
        print('Ready')

hello_worls =['hi','ку','прив','привет','здравствуйте']

@client.event
async def on_messge(message):
        if message.author == client.user:
                return
        
        msg = message.content.lower()

        if msg in hello_worls:
                await message.channel.send('и тебе привет, человек')
        elif message.content.startswith('help'):
            await message.channel.send('''1.батарейка
                                       2.стекло
                                       3.жестяные банки
                                       4.фольга
                                       5.резина
                                       6.пластик
                                       7.бумага
                                       8.список
                                       9.hi, ку, прив, привет, здравствуйте''')
        
        elif message.content.startswith('батарейка'):
            await message.channel.send('''Их необходимо сдавать в специальные пункты приема,
                                        которые есть во всех крупных городах страны.
                                        Чаще всего они располагаются в крупных магазинах или торговых центрах.''')
        
        elif message.content.startswith('стекло'):
            await message.channel.send('''Помимо специальных контейнеров, стекло можно сдать в специальные приемные пункты – как в стационарные, так и передвижные.
                                    Также сбором занимаются специальные организации, в которые принимают его за деньги.
                                        Но не все стекло принимают на переработку: Обычно без проблем принимают стеклотару: бутылки, банки, пузырьки.''')
        elif message.content.startswith('жестяные банки'):
            await message.channel.send('''Вместо того, чтобы выкидывать консервные банки,
                                        вы можете сдать их в специальный приёмный пункт. 
                                       Таим образом вы не только поможете экономике РФ,
                                        но и пополните семейный бюджет.''')
        elif message.content.startswith('фольга'):
            await message.channel.send('''Переработчики говорят, что наряду с алюминиевыми банками могут переработать и фольгу,
                                        но она не должна быть сильно загрязнена.
                                        Именно поэтому её также можно отправлять в специальные контейнеры или сдавать в заготовительные пункты. ''')
        elif message.content.startswith('резина'):
            await message.channel.send('''сдать в специализированные компании, которые утилизируют такие отходы.''')
        elif message.content.startswith('пластик'):
            await message.channel.send('''1.захоронения на специально отведенных участках;
                                        2.переработка на заводах;
                                        3.сжигание вместе с городским мусором;
                                        4.раздельное сжигание;
                                        5.пиролиз-Пиролиз может определяться как высокотемпературный (750—800 °С) термолиз углеводородов,
                                        проводимый при низком давлении и малой продолжительности;
                                        6.повторное использование.''')
        elif message.content.startswith('бумага'):
            await message.channel.send('''Сортируйте''')
        elif message.content.startswith('список'):
            await message.channel.send('''1.бумага - 2 года
                                       2.жестяная банка - до 90 лет
                                       3.фольга - 100 лет
                                       4.резина - 100 лет
                                       5.пластик - 100 лет
                                       6.аккумуляторы, батарейки - 100 лет
                                       7.стекло - более 1000 лет''')
        else:
               await message.channel.send(message.content)
client.run('token!!!')
