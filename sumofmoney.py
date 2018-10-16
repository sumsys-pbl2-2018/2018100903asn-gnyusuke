# -*- coding: utf-8 -*-
# This is a program calculating the total amount of money

yen_dollar_rate = 112.70

print ('Input the number of JPY500 coins: ')
n_jpy500_coins = int( input()) # キーボードから数値入力を受け付ける

print ('Input the number of JP100 coins: ')
n_jpy100_coins = int( input()) # キーボードから数値入力を受け付ける

print ('Input the number of JPY50 coins: ')
n_jpy50_coins = int( input()) # キーボードから数値入力を受け付ける

print ('Input the number of JPY10 coins: ')
n_jpy10_coins = int( input()) # キーボードから数値入力を受け付ける

print ('Input the number of JPY5 coins: ')
n_jpy5_coins =int( input()) # キーボードから数値入力を受け付ける


total_jpy = n_jpy500_coins*500+n_jpy100_coins*100+n_jpy50_coins*50+n_jpy10_coins*10+n_jpy5_coins*5

print( 'The total amount of money is JPY {0}.'.format(total_jpy))

total_us_dollar = total_jpy//113.36
total_us_cents = int(total_jpy%%113.36)
print ('The total amount of money is {0} dollar and {1} cents.'.format(total_us_dollar, total_us_cents) )
