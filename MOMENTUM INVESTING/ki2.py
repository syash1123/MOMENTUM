import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.table import Table

tickers = [
"ABB.NS", "ACC.NS", "APLAPOLLO.NS", "AUBANK.NS", "ADANIENSOL.NS", "ADANIENT.NS", "ADANIGREEN.NS", 
"ADANIPORTS.NS", "ADANIPOWER.NS", "ATGL.NS", "ABCAPITAL.NS", "ABFRL.NS", "ALKEM.NS", "AMBUJACEM.NS",
 "APOLLOHOSP.NS", "APOLLOTYRE.NS", "ASHOKLEY.NS", "ASIANPAINT.NS", "ASTRAL.NS", "AUROPHARMA.NS", 
 "DMART.NS", "AXISBANK.NS", "BSE.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", "BAJAJHLDNG.NS",
  "BALKRISIND.NS", "BANDHANBNK.NS", "BANKBARODA.NS", "BANKINDIA.NS", "MAHABANK.NS", "BERGEPAINT.NS", 
  "BDL.NS", "BEL.NS", "BHARATFORG.NS", "BHEL.NS", "BPCL.NS", "BHARTIARTL.NS", "BIOCON.NS", "BOSCHLTD.NS", 
  "BRITANNIA.NS", "CGPOWER.NS", "CANBK.NS", "CHOLAFIN.NS", "CIPLA.NS", "COALINDIA.NS", "COFORGE.NS", 
  "COLPAL.NS", "CONCOR.NS", "CUMMINSIND.NS", "DLF.NS", "DABUR.NS", "DALBHARAT.NS", "DEEPAKNTR.NS", "DELHIVERY.NS",
   "DIVISLAB.NS", "DIXON.NS", "LALPATHLAB.NS", "DRREDDY.NS", "EICHERMOT.NS", "ESCORTS.NS", "NYKAA.NS", "FEDERALBNK.NS", 
    "FACT.NS", "FORTIS.NS", "GAIL.NS", "GMRINFRA.NS", "GLAND.NS", "GODREJCP.NS", "GODREJPROP.NS", "GRASIM.NS", "GUJGASLTD.NS",
     "HCLTECH.NS", "HDFCAMC.NS", "HDFCBANK.NS", "HDFCLIFE.NS", "HAVELLS.NS", "HEROMOTOCO.NS", "HINDALCO.NS", "HAL.NS", "HINDPETRO.NS", 
     "HINDUNILVR.NS", "ICICIBANK.NS", "ICICIGI.NS", "ICICIPRULI.NS", "IDBI.NS", "IDFCFIRSTB.NS", "ITC.NS", "INDIANB.NS", "INDHOTEL.NS", 
     "IOC.NS", "IRCTC.NS", "IRFC.NS", "IGL.NS", "INDUSTOWER.NS", "INDUSINDBK.NS", "NAUKRI.NS", "INFY.NS", "INDIGO.NS", "IPCALAB.NS", 
     "JSWENERGY.NS", "JSWINFRA.NS", "JSWSTEEL.NS", "JINDALSTEL.NS", "JIOFIN.NS", "JUBLFOOD.NS", "KPITTECH.NS", "KALYANKJIL.NS", 
     "KOTAKBANK.NS", "LTF.NS", "LTTS.NS", "LICHSGFIN.NS", "LTIM.NS", "LT.NS", "LAURUSLABS.NS", "LICI.NS", "LUPIN.NS", "MRF.NS", 
     "LODHA.NS", "M&MFIN.NS", "M&M.NS", "MANKIND.NS", "MARICO.NS", "MARUTI.NS", "MFSL.NS", "MAXHEALTH.NS", "MAZDOCK.NS", "MPHASIS.NS", 
    "NHPC.NS", "NMDC.NS", "NTPC.NS", "NESTLEIND.NS", "OBEROIRLTY.NS", "ONGC.NS", "OIL.NS", "PAYTM.NS", "OFSS.NS", "POLICYBZR.NS", 
    "PIIND.NS", "PAGEIND.NS", "PATANJALI.NS", "PERSISTENT.NS", "PETRONET.NS", "PIDILITIND.NS", "PEL.NS", "POLYCAB.NS", "POONAWALLA.NS", 
    "PFC.NS", "POWERGRID.NS", "PRESTIGE.NS", "PNB.NS", "RECLTD.NS", "RVNL.NS", "RELIANCE.NS", "SBICARD.NS", "SBILIFE.NS", "SJVN.NS", "SRF.NS", 
    "MOTHERSON.NS", "SHREECEM.NS", "SHRIRAMFIN.NS", "SIEMENS.NS", "SONACOMS.NS", "SBIN.NS", "SAIL.NS", "SUNPHARMA.NS", "SUNTV.NS", "SUPREMEIND.NS",
     "SUZLON.NS", "SYNGENE.NS", "TVSMOTOR.NS", "TATACHEM.NS", "TATACOMM.NS", "TCS.NS", "TATACONSUM.NS", "TATAELXSI.NS", "TATAMOTORS.NS", 
     "TATAPOWER.NS", "TATASTEEL.NS", "TATATECH.NS", "TECHM.NS", "TITAN.NS", "TORNTPHARM.NS", "TORNTPOWER.NS", "TRENT.NS", "TIINDIA.NS", 
     "UPL.NS", "ULTRACEMCO.NS", "UNIONBANK.NS", "UNITDSPR.NS", "VBL.NS", "VEDL.NS", "IDEA.NS", "VOLTAS.NS", "WIPRO.NS", "YESBANK.NS",
      "ZEEL.NS", "ZOMATO.NS", "ZYDUSLIFE.NS"

]

def get_data(ticker, start_date, end_date):
    return yf.download(ticker, start=start_date, end=end_date)

# Set dates
end_date = datetime.today().date()
print(end_date)
start_date = end_date - timedelta(days=365*2)  # 2 years of data for EMA
print(start_date)

# Dictionary to hold stock data
data = {}
i=0
for ticker in tickers:
    try:
        stock_data = get_data(ticker, start_date, end_date)
        # print(stock_data)
        if len(stock_data) > 0:
            data[ticker] = stock_data
            i=i+1
            print(i)
            
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

summary = []

# # Analyse each stock
# for ticker, df in data.items():

#     # Calculate EMA
#     df['EMA100'] = df['Close'].ewm(span=100).mean()
#     df['EMA200'] = df['Close'].ewm(span=200).mean()

#     # LAST 1 YEAR RETURN
#     one_year_return = (df['Close'].iloc[-1] / df['Close'].iloc[-252] - 1) * 100

#     # 52 week high
#     high_52_week = df['Close'].iloc[-252:].max()
#     within_2_pct_high = df['Close'].iloc[-1] >= high_52_week * 0.98  # Updated to get the latest value

#     # More than 50% up days in the last 6 months (126 trading days)
#     six_month_data = df['Close'].iloc[-126:]
#     up_days = (six_month_data.pct_change() > 0).sum()
#     up_days_pct = up_days / len(six_month_data) * 100

#     # Adjusted the condition to compare individual values
#     if (df['Close'].iloc[-1] >= df['EMA100'].iloc[-1] >= df['EMA200'].iloc[-1] and 
#         one_year_return >= 6.5 and within_2_pct_high and up_days_pct > 50):
        
#         return_6m = (df['Close'].iloc[-1] / df['Close'].iloc[-126] - 1) * 100
#         return_3m = (df['Close'].iloc[-1] / df['Close'].iloc[-63] - 1) * 100
#         return_1m = (df['Close'].iloc[-1] / df['Close'].iloc[-21] - 1) * 100

#         summary.append({
#             'Ticker': ticker,
#             'Return_6M': return_6m,
#             'Return_3m': return_3m,
#             'Return_1m': return_1m,
#         })
# Analyse each stock
for ticker, df in data.items():

    # Calculate EMA
    df['EMA100'] = df['Close'].ewm(span=100).mean()
    df['EMA200'] = df['Close'].ewm(span=200).mean()

    # Check if the DataFrame has at least 252 rows (1 year of data)
    if len(df) >= 252:
        # LAST 1 YEAR RETURN
        one_year_return = (df['Close'].iloc[-1] / df['Close'].iloc[-252] - 1) * 100

        # 52 week high
        high_52_week = df['Close'].iloc[-252:].max()
        within_2_pct_high = df['Close'].iloc[-1] >= high_52_week * 0.80

        # More than 50% up days in the last 6 months (126 trading days)
        six_month_data = df['Close'].iloc[-126:]
        up_days = (six_month_data.pct_change() > 0).sum()
        up_days_pct = up_days / len(six_month_data) * 100

        # Adjusted the condition to compare individual values
        if (df['Close'].iloc[-1] >= df['EMA100'].iloc[-1] >= df['EMA200'].iloc[-1] and 
            one_year_return >= 6.5 and within_2_pct_high and up_days_pct > 50):
            
            return_6m = (df['Close'].iloc[-1] / df['Close'].iloc[-126] - 1) * 100
            return_3m = (df['Close'].iloc[-1] / df['Close'].iloc[-63] - 1) * 100
            return_1m = (df['Close'].iloc[-1] / df['Close'].iloc[-21] - 1) * 100

            summary.append({
                'Ticker': ticker,
                'Return_6M': return_6m,
                'Return_3M': return_3m,
                'Return_1M': return_1m,
            })
    else:
        print(f"Not enough data for {ticker} (less than 252 trading days)")



# Convert summary list to DataFrame
df_summary = pd.DataFrame(summary)
print(df_summary)


df_summary['Return_6M'] = df_summary["Return_6M"].round(1)
df_summary['Return_3M'] = df_summary['Return_3M'].round(1)
df_summary['Return_1M'] = df_summary['Return_1M'].round(1)

# Ranking based on returns 
df_summary['Rank_6M'] =df_summary['Return_6M'].rank(ascending =False)
df_summary['Rank_3M'] =df_summary['Return_3M'].rank(ascending =False)
df_summary['Rank_1M'] =df_summary['Return_1M'].rank(ascending =False)

#CALCULATE FINAL RANk
df_summary['Final_Rank'] = 0.33*df_summary['Rank_6M'] + 0.33*df_summary['Rank_3M'] + 0.33*df_summary['Rank_1M']

#SORT THE FIANL RANK ABD GET TOP 30 

df_summary_sorted =df_summary.sort_values('Final_Rank').head(40)
print(df_summary_sorted)

top_15 =df_summary_sorted['POSITIN']= np.arange(1,len(df_summary_sorted)+1 )

#seperate the top 15 and end 15
top_15 =df_summary_sorted.head(20)
next_15= df_summary_sorted.iloc[20:40]

print(top_15)
print('HELLLLO')
print(next_15)
df_summary_sorted.to_excel("NIFTY_200_1_3_6.xlsx", index=False, engine='openpyxl')
