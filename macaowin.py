# coding:utf8

import click


class Me(object):
    def __init__(self, name='张三', money=0):
        self.money = money
        self.name = name

    def spend(self, money):
        self.money -= money

    def win(self, money):
        self.money += money

    def lose(self, money):
        self.money -= money

    def __unicode__(self):
        return '%s 还有 %s 元钱' % (self.name, self.money)


class Plat(object):
    def __init__(self, name='赌博公司', money=0):
        self.money = money
        self.name = name

    def win(self, money):
        self.money += money

    def lose(self, money):
        self.money -= money

    def __unicode__(self):
        return '%s 还有 %s 元钱' % (self.name, self.money)


class Game(object):
    WIN = 'WIN'
    LOSE = 'LOSE'
    FAIR = 'FAIR'
    NOT_START = 'NOT START'

    def __init__(self):
        self.turn = 0
        self.result = self.NOT_START
        self.max_lose_count = 0
        self.current_continue_lose_count = 0
        self.total_lose = 0
        self.total_win = 0
        self.max_money = 0

    def start_new_turn(self, plat, person1, money):
        """开始新一轮赌局
        :type person1: Me
        :type plat: Plat
        :type money: int
        """
        self.turn += 1
        if self.max_money < person1.money:
            self.max_money = person1.money
        import random
        a = random.randint(0, 1)
        self.result = self.NOT_START
        if a:
            self.result = self.WIN
            self.current_continue_lose_count = 0
            self.total_win += 1
            plat.lose(money)
            person1.win(money)
        else:
            self.result = self.LOSE
            self.current_continue_lose_count += 1
            self.total_lose += 1
            if self.current_continue_lose_count > self.max_lose_count:
                self.max_lose_count = self.current_continue_lose_count
            plat.win(money)
            person1.lose(money)
        return self.result


def print_result(game, plat, person1, init_money, bet_money):
    if game.result == 'WIN':
        result = click.style(game.result, fg='green')
    else:
        result = click.style(game.result, fg='red')
    wallet_max = click.style(str(game.max_money), fg='red', underline=True)
    click.echo('Turn %s: %s, 我身上带了 %s 元, 这次下注 %s 元, 钱包还剩 %s 元(最多时钱包有 %s 元, 最多连输次数 %s, 累计赢 %s, 累计输 %s, 赢率: %d )' % (
    game.turn, result, init_money, bet_money, person1.money, wallet_max, game.max_lose_count, game.total_win,
    game.total_lose, game.total_win / float(game.total_lose + game.total_win) * 100 if game.total_lose > 0 else 0))


@click.command()
@click.option('--wallet', default=100000, help=u'带多少钱去澳门', prompt=u'带多少钱去澳门')
@click.option('--bet', default=1000, prompt=u'每次基础下注金额',
              help=u'每次基础下注金额')
def go(wallet, bet):
    game = Game()
    plat = Plat()
    me = Me()
    import sys
    my_wallet = wallet
    me.money = plat.money = my_wallet
    init_bet_money = bet
    import time
    click.echo('你带了 %s 元, 起始赌注: %s' % (my_wallet, init_bet_money))
    click.echo('开始赌局...')
    while 1:
        # time.sleep(0.01)
        # money_bet = click.prompt('赌注: ', init_bet_money)
        money_bet = init_bet_money
        result = game.start_new_turn(plat, me, money_bet)
        print_result(game, plat, me, my_wallet, money_bet)
        if result == Game.LOSE:
            init_bet_money *= 2
        else:
            init_bet_money = 100

        if me.money < 0: break
    click.echo('没钱了。。。')


if __name__ == '__main__':
    go()
