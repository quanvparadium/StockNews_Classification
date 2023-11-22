import pandas as pd

HOSE_PATH = 'dataset/tickers/hose_tickers.csv'
HNX_PATH = 'dataset/tickers/hnx_tickers.csv'
UPCOM_PATH = 'dataset/tickers/uc_tickers.csv'

def get_ticker(get_market=False):
    """
        Trả về mã cổ phiếu của 3 sàn chứng khoán (HoSE, HNX, UpCOM)
        Parameter:
            get_market: True thì Kết quả sẽ trả về mã chứng khoán và sàn chứng khoán ứng với mã chứng khoán đó
                        False thì chỉ trả về mã chứng khoán
    """
    hose_ticker = pd.read_csv(HOSE_PATH)['Stock Code']
    hnx_ticker = pd.read_csv(HNX_PATH)['Stock Code']
    uc_ticker = pd.read_csv(UPCOM_PATH)['Stock Code']
    # print(len(hose_ticker))
    tickers = [*hose_ticker, *hnx_ticker, *uc_ticker]
    if get_market:
        market = ['HoSe'] * len(hose_ticker) + ['HNX'] * len(hnx_ticker) + ['UpCOM'] * len(uc_ticker)
        return tickers, market
    else:
        return tickers
    
if __name__ == "__main__":
    tickers, market = get_ticker(get_market=True)
    for i in list(zip(tickers, market)):
        print(i)