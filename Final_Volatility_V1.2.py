from ast import Try
import pyupbit
import time
import datetime


#변돌 감지 알고리즘
def get_target_price(ticker):
    df = pyupbit.get_ohlcv(f"KRW-{ticker}")
    volatility = (df.iloc[-2]['high'] - df.iloc[-2]['low']) * 0.5
    target_price = df.iloc[-1]['open'] + volatility
    return target_price


#매수주문
def buy_crypto_currency(upbit, percent,ticker):
    krw = upbit.get_balance("KRW")  
    unit = int(krw*percent)
    return upbit.buy_market_order(f"KRW-{ticker}", unit)


#매도주문
def sell_crypto_currency(upbit,ticker):
    unit = upbit.get_balance(f"KRW-{ticker}")
    return upbit.sell_market_order(f"KRW-{ticker}", unit)


# ma5 (5일 이동평균선)
def get_yersterday_ma5(ticker):
    df = pyupbit.get_ohlcv(f"KRW-{ticker}")
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]



#시작 알고리즘
if __name__ == "__main__":

    # API 받아오기
    key1 = " "
    key2 = " "

    try:
        try:
            upbit = pyupbit.Upbit(key1, key2)  #API 키 입력, 클래스 생성
        except:
            print("오류")
        # 비트코인 알고리즘

        BTC_hold_flag = False  # 코인 추가할 때 반드시 플래그 세워주기
        ETH_hold_flag = False
        XRP_hold_flag = False
        BSV_hold_flag = False
        LTC_hold_flag = False

        price= '0'
        while True:
            try:
                now = datetime.datetime.now()
                mid09 = datetime.datetime(now.year, now.month, now.day, 9)
                delta = datetime.timedelta(seconds = 30)

                BTC_target_price = get_target_price("BTC")
                BTC_ma5 = get_yersterday_ma5('BTC')

                ETH_target_price = get_target_price("ETH")
                ETH_ma5 = get_yersterday_ma5('ETH')

                XRP_target_price = get_target_price("XRP")
                XRP_ma5 = get_yersterday_ma5('XRP')

                BSV_target_price = get_target_price("BSV")
                BSV_ma5 = get_yersterday_ma5('BSV')

                LTC_target_price = get_target_price("LTC")
                LTC_ma5 = get_yersterday_ma5('LTC')

                for i in range(5):  # range('코인 개수') 바꿔주기!
                    if i == 0: #비트코인 매매
                        if mid09 <= now and now <= mid09 + delta:
                            if BTC_hold_flag == 'already_buy':  # 바꿔주기
                                try:
                                    ret = sell_crypto_currency(upbit,"BTC") # 바꿔주기
                                    ret = upbit.get_order(ret)
                                    print("비트코인 매도", ret) # 바꿔주기
                                except:
                                    pass
                            BTC_target_price = get_target_price('BTC') # 바꿔주기
                            BTC_hold_flag = False # 바꿔주기

                        else:
                            BTC_price = pyupbit.get_current_price("KRW-BTC")  # 비트코인의 현재가격
                            if BTC_target_price <= BTC_price and BTC_price >= BTC_ma5 and BTC_hold_flag == False: # 바꿔주기
                                ret = buy_crypto_currency(upbit, percent=0.33,ticker="BTC") # 바꿔주기
                                print("비트코인 매수", ret) # 바꿔주기
                                BTC_hold_flag = 'already_buy' # 바꿔주기


                    elif i == 1: #이더리움 매매
                        if mid09 <= now and now <= mid09 + delta:
                            if ETH_hold_flag == True:
                                try:
                                    ret = sell_crypto_currency(upbit,'ETH')
                                    ret = upbit.get_order(ret)
                                    print("이더리움 매도", ret)
                                except:
                                    pass
                            ETH_target_price = get_target_price('ETH')
                            ETH_hold_flag = False

                        else:
                            ETH_price = pyupbit.get_current_price("KRW-ETH")  # 이더리움의 현재가격
                            if ETH_target_price <= ETH_price and ETH_price >= ETH_ma5 and ETH_hold_flag == False:
                                ret = buy_crypto_currency(upbit, percent=0.33,ticker="ETH")
                                print("이더리움 매수", ret)
                                ETH_hold_flag = 'already_buy'


                    elif i == 2: #리플 매매
                        if mid09 <= now and now <= mid09 + delta:
                            if XRP_hold_flag == True:
                                try:
                                    ret = sell_crypto_currency(upbit,'XRP')
                                    ret = upbit.get_order(ret)
                                    print("리플 매도", ret)
                                except:
                                    pass
                            XRP_target_price = get_target_price('XRP')
                            XRP_hold_flag = False

                        else:
                            XRP_price = pyupbit.get_current_price("KRW-XRP")  # 리플의 현재가격
                            if XRP_target_price <= XRP_price and XRP_price >= XRP_ma5 and XRP_hold_flag == False:
                                ret = buy_crypto_currency(upbit, percent=0.33, ticker="XRP")
                                print("리플 매수", ret)
                                XRP_hold_flag = 'already_buy'


                    elif i == 3: #비트코인에스브이 매매
                        if mid09 <= now and now <= mid09 + delta:
                            if BSV_hold_flag == True:
                                try:
                                    ret = sell_crypto_currency(upbit,'BSV')
                                    ret = upbit.get_order(ret)
                                    print("BSV 매도", ret)
                                except:
                                    pass
                            BSV_target_price = get_target_price('BSV')
                            BSV_hold_flag = False

                        else:
                            BSV_price = pyupbit.get_current_price("KRW-BSV")  # 비트코인에스브이의 현재가격
                            if BSV_target_price <= BSV_price and BSV_price >= BSV_ma5 and BSV_hold_flag == False:
                                ret = buy_crypto_currency(upbit, percent=0.33, ticker="BSV")
                                print("BSV 매수", ret)
                                BSV_hold_flag = 'already_buy'


                    elif i == 4: #라이트코인 매매
                        if mid09 <= now and now <= mid09 + delta:
                            if LTC_hold_flag == True:
                                try:
                                    ret = sell_crypto_currency(upbit,'LTC')
                                    ret = upbit.get_order(ret)
                                    print("LTC 매도", ret)
                                except:
                                    pass
                            LTC_target_price = get_target_price('LTC')
                            LTC_hold_flag = False

                        else:
                            LTC_price = pyupbit.get_current_price("KRW-LTC")  # 라이트코인의 현재가격
                            if LTC_target_price <= LTC_price and LTC_price >= LTC_ma5 and LTC_hold_flag == False:
                                ret = buy_crypto_currency(upbit, percent=0.33, ticker="LTC")
                                print("LTC 매수", ret)
                                LTC_hold_flag = 'already_buy'
                
                print(now)
                print(f"비트:{BTC_target_price}", BTC_price)
                print(f"이더:{ETH_target_price}", ETH_price)
                print(f"리플:{XRP_target_price}", XRP_price)
                print(f"BSV:{BSV_target_price}", BSV_price)
                print(f"LTC:{LTC_target_price}", LTC_price)
                print("--------------------------------")
                time.sleep(1) # while True만 하면 과부하 걸리므로 time.sleep(1)로 1초마다 확인 & import time 도 위에 반드시 써주기

            except Exception as e:
                print(e)
                print("에러발생")
                print("1초뒤 재시작합니다.")
                time.sleep(1)
                pass
    except Exception as e:
        print(e)
        print("API 입력오류!")