while True:
    if time.time() - timing > 3:
        timing = time.time()
        day += 1
        print('Ура!!!Вы смогли дожить до следующего дня! Это уже ваш ', day, 
            ' день в зоопарке! Самое время покормить животных и снова открыть двери зоопарка для гостей ')
        answer_8 = int(input('''
                               \nХотите покормить своих животных:
                               \n 1.Да, конечно, я ведь люблю своих животных!!!
                               \т 2.НЕЕТ, мне всё это надоело, я хочу закончить эту игру, пусть животные умирают с голода.
                                ''')
                           
        if answer_8 == 1:
            my_food.read_food()
            if self.f_price > self.budget:
                print('К сожалению, у тебя недостаточно средст для того, чтобы покормить всех животных. Ты обанкротился и потерял свой зоопарк. Грустно...')
            else:
                my_money.expenditure(self.f_price)
                my_money.read_budget()
                print('Ура!!!Все твои животные сыты. Зоопарк готов к новому рабочему дню!')
                
        if answer_8 == 2:
            print('Пока.')
            
            
class Food_for_animals(Zoo):
    
    def __init__(self):
        self.food = 0
        
    def need_food(self):
        self.food = i
        
    def price_food(self, f_price):
        self.f_price = f_price
        self.f_price = 4*self.food
        
    def read_food(self):
        print('Животным необходимо', self.food,'-едениц еды, это будет стоить ', self.f_price, ' монет')

my_food = Food_for_animals()
