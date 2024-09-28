import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.table import Table


tickers = [
"360ONE.NS", "3MINDIA.NS", "ABB.NS", "ACC.NS", "AIAENG.NS", "APLAPOLLO.NS", "AUBANK.NS", 
"AARTIIND.NS", "AAVAS.NS", "ABBOTINDIA.NS", "ACE.NS", "ADANIENSOL.NS", "ADANIENT.NS", 
"ADANIGREEN.NS", "ADANIPORTS.NS", "ADANIPOWER.NS", "ATGL.NS", "AWL.NS", "ABCAPITAL.NS", 
"ABFRL.NS", "AEGISLOG.NS", "AETHER.NS", "AFFLE.NS", "AJANTPHARM.NS", "APLLTD.NS", "ALKEM.NS", 
"ALKYLAMINE.NS", "ALLCARGO.NS", "ALOKINDS.NS", "ARE&M.NS", "AMBER.NS", "AMBUJACEM.NS", 
"ANANDRATHI.NS", "ANGELONE.NS", "ANURAS.NS", "APARINDS.NS", "APOLLOHOSP.NS", "APOLLOTYRE.NS", 
"APTUS.NS", "ACI.NS", "ASAHIINDIA.NS", "ASHOKLEY.NS", "ASIANPAINT.NS", "ASTERDM.NS", 
"ASTRAZEN.NS", "ASTRAL.NS", "ATUL.NS", "AUROPHARMA.NS", "AVANTIFEED.NS", "DMART.NS", 
"AXISBANK.NS", "BEML.NS", "BLS.NS", "BSE.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", 
"BAJAJHLDNG.NS", "BALAMINES.NS", "BALKRISIND.NS", "BALRAMCHIN.NS", "BANDHANBNK.NS", 
"BANKBARODA.NS", "BANKINDIA.NS", "MAHABANK.NS", "BATAINDIA.NS", "BAYERCROP.NS", "BERGEPAINT.NS", 
"BDL.NS", "BEL.NS", "BHARATFORG.NS", "BHEL.NS", "BPCL.NS", "BHARTIARTL.NS", "BIKAJI.NS", 
"BIOCON.NS", "BIRLACORPN.NS", "BSOFT.NS", "BLUEDART.NS", "BLUESTARCO.NS", "BBTC.NS", 
"BORORENEW.NS", "BOSCHLTD.NS", "BRIGADE.NS", "BRITANNIA.NS", "MAPMYINDIA.NS", "CCL.NS", 
"CESC.NS", "CGPOWER.NS", "CIEINDIA.NS", "CRISIL.NS", "CSBBANK.NS", "CAMPUS.NS", "CANFINHOME.NS", 
"CANBK.NS", "CAPLIPOINT.NS", "CGCL.NS", "CARBORUNIV.NS", "CASTROLIND.NS", "CEATLTD.NS", 
"CELLO.NS", "CENTRALBK.NS", "CDSL.NS", "CENTURYPLY.NS", "CENTURYTEX.NS", "CERA.NS", "CHALET.NS", 
"CHAMBLFERT.NS", "CHEMPLASTS.NS", "CHENNPETRO.NS", "CHOLAHLDNG.NS", "CHOLAFIN.NS", "CIPLA.NS", 
"CUB.NS", "CLEAN.NS", "COALINDIA.NS", "COCHINSHIP.NS", "COFORGE.NS", "COLPAL.NS", "CAMS.NS", 
"CONCORDBIO.NS", "CONCOR.NS", "COROMANDEL.NS", "CRAFTSMAN.NS", "CREDITACC.NS", "CROMPTON.NS", 
"CUMMINSIND.NS", "CYIENT.NS", "DCMSHRIRAM.NS", "DLF.NS", "DOMS.NS", "DABUR.NS", "DALBHARAT.NS", 
"DATAPATTNS.NS", "DEEPAKFERT.NS", "DEEPAKNTR.NS", "DELHIVERY.NS", "DEVYANI.NS", "DIVISLAB.NS", 
"DIXON.NS", "LALPATHLAB.NS", "DRREDDY.NS", "EIDPARRY.NS", "EIHOTEL.NS", "EPL.NS", 
"EASEMYTRIP.NS", "EICHERMOT.NS", "ELECON.NS", "ELGIEQUIP.NS", "EMAMILTD.NS", "ENDURANCE.NS", 
"ENGINERSIN.NS", "EQUITASBNK.NS", "ERIS.NS", "ESCORTS.NS", "EXIDEIND.NS", "FDC.NS", "NYKAA.NS", 
"FEDERALBNK.NS", "FACT.NS", "FINEORG.NS", "FINCABLES.NS", "FINPIPE.NS", "FSL.NS", 
"FIVESTAR.NS", "FORTIS.NS", "GAIL.NS", "GMMPFAUDLR.NS", "GMRINFRA.NS", "GRSE.NS", "GICRE.NS", 
"GILLETTE.NS", "GLAND.NS", "GLAXO.NS", "GLS.NS", "GLENMARK.NS", "MEDANTA.NS", "GPIL.NS", 
"GODFRYPHLP.NS", "GODREJCP.NS", "GODREJIND.NS", "GODREJPROP.NS", "GRANULES.NS", "GRAPHITE.NS", 
"GRASIM.NS", "GESHIP.NS", "GRINDWELL.NS", "GAEL.NS", "FLUOROCHEM.NS", "GUJGASLTD.NS", 
"GMDCLTD.NS", "GNFC.NS", "GPPL.NS", "GSFC.NS", "GSPL.NS", "HEG.NS", "HBLPOWER.NS", 
"HCLTECH.NS", "HDFCAMC.NS", "HDFCBANK.NS", "HDFCLIFE.NS", "HFCL.NS", "HAPPSTMNDS.NS", 
"HAPPYFORGE.NS", "HAVELLS.NS", "HEROMOTOCO.NS", "HSCL.NS", "HINDALCO.NS", "HAL.NS", 
"HINDCOPPER.NS", "HINDPETRO.NS", "HINDUNILVR.NS", "HINDZINC.NS", "POWERINDIA.NS", 
"HOMEFIRST.NS", "HONASA.NS", "HONAUT.NS", "HUDCO.NS", "ICICIBANK.NS", "ICICIGI.NS", 
"ICICIPRULI.NS", "ISEC.NS", "IDBI.NS", "IDFCFIRSTB.NS", "IDFC.NS", "IIFL.NS", "IRB.NS", 
"IRCON.NS", "ITC.NS", "ITI.NS", "INDIACEM.NS", "INDIAMART.NS", "INDIANB.NS", "IEX.NS", 
"INDHOTEL.NS", "IOC.NS", "IOB.NS", "IRCTC.NS", "IRFC.NS", "INDIGOPNTS.NS", "IGL.NS", 
"INDUSTOWER.NS", "INDUSINDBK.NS", "NAUKRI.NS", "INFY.NS", "INOXWIND.NS", "INTELLECT.NS", 
"INDIGO.NS", "IPCALAB.NS", "JBCHEPHARM.NS", "JKCEMENT.NS", "JBMA.NS", "JKLAKSHMI.NS", 
"JKPAPER.NS", "JMFINANCIL.NS", "JSWENERGY.NS", "JSWINFRA.NS", "JSWSTEEL.NS", "JAIBALAJI.NS", 
"J&KBANK.NS", "JINDALSAW.NS", "JSL.NS", "JINDALSTEL.NS", "JIOFIN.NS", "JUBLFOOD.NS", 
"JUBLINGREA.NS", "JUBLPHARMA.NS", "JWL.NS", "JUSTDIAL.NS", "JYOTHYLAB.NS", "KPRMILL.NS", 
"KEI.NS", "KNRCON.NS", "KPITTECH.NS", "KRBL.NS", "KSB.NS", "KAJARIACER.NS", "KPIL.NS", 
"KALYANKJIL.NS", "KANSAINER.NS", "KARURVYSYA.NS", "KAYNES.NS", "KEC.NS", "KFINTECH.NS", 
"KOTAKBANK.NS", "KIMS.NS", "LTF.NS", "LTTS.NS", "LICHSGFIN.NS", "LTIM.NS", "LT.NS", 
"LATENTVIEW.NS", "LAURUSLABS.NS", "LXCHEM.NS", "LEMONTREE.NS", "LICI.NS", "LINDEINDIA.NS", 
"LLOYDSME.NS", "LUPIN.NS", "MMTC.NS", "MRF.NS", "MTARTECH.NS", "LODHA.NS", "MGL.NS", 
"MAHSEAMLES.NS", "M&MFIN.NS", "M&M.NS", "MHRIL.NS", "MAHLIFE.NS", "MANAPPURAM.NS", 
"MRPL.NS", "MANKIND.NS", "MARICO.NS", "MARUTI.NS", "MASTEK.NS", "MFSL.NS", "MAXHEALTH.NS", 
"MAZDOCK.NS", "MEDPLUS.NS", "METROBRAND.NS", "METROPOLIS.NS", "MINDACORP.NS", "MSUMI.NS", 
"MOTILALOFS.NS", "MPHASIS.NS", "MUTHOOTFIN.NS", "NATCOPHARM.NS", "NBCC.NS", 
"NCC.NS", "NHPC.NS", "NLCINDIA.NS", "NMDC.NS", "NSLNISP.NS", "NTPC.NS", "NH.NS", 
"NATIONALUM.NS", "NAVINFLUOR.NS", "NESTLEIND.NS", "NETWORK18.NS", "NAM-INDIA.NS", 
"NUVAMA.NS", "NUVOCO.NS", "OBEROIRLTY.NS", "ONGC.NS", "OIL.NS", "OLECTRA.NS", "PAYTM.NS", 
"OFSS.NS", "POLICYBZR.NS", "PCBL.NS", "PIIND.NS", "PNBHOUSING.NS", "PNCINFRA.NS", 
"PVRINOX.NS", "PAGEIND.NS", "PATANJALI.NS", "PERSISTENT.NS", "PETRONET.NS", "PHOENIXLTD.NS", 
"PIDILITIND.NS", "PEL.NS", "PPLPHARMA.NS", "POLYMED.NS", "POLYCAB.NS", "POONAWALLA.NS", 
"PFC.NS", "POWERGRID.NS", "PRAJIND.NS", "PRESTIGE.NS", "PRINCEPIPE.NS", "PRSMJOHNSN.NS", 
"PGHH.NS", "PNB.NS", "QUESS.NS", "RRKABEL.NS", "RBLBANK.NS", "RECLTD.NS", "RHIM.NS", 
"RITES.NS", "RADICO.NS", "RVNL.NS", "RAILTEL.NS", "RAINBOW.NS", "RAJESHEXPO.NS", "RKFORGE.NS", 
"RCF.NS", "RATNAMANI.NS", "RTNINDIA.NS", "RAYMONDLSL.NS", "RAYMOND.NS", "REDINGTON.NS", 
"RELIANCE.NS", "RBA.NS", "ROUTE.NS", "SBFC.NS", "SBICARD.NS", "SBILIFE.NS", "SJVN.NS", 
"SKFINDIA.NS", "SRF.NS", "SAFARI.NS", "SAMMAANCAP.NS", "MOTHERSON.NS", "SANOFICONR.NS", 
"SANOFI.NS", "SAPPHIRE.NS", "SAREGAMA.NS", "SCHAEFFLER.NS", "SCHNEIDER.NS", "SHREECEM.NS", 
"RENUKA.NS", "SHRIRAMFIN.NS", "SHYAMMETL.NS", "SIEMENS.NS", "SIGNATURE.NS", "SOBHA.NS", 
"SOLARINDS.NS", "SONACOMS.NS", "SONATSOFTW.NS", "STARHEALTH.NS", "SBIN.NS", "SAIL.NS", 
"SWSOLAR.NS", "STLTECH.NS", "SUMICHEM.NS", "SPARC.NS", "SUNPHARMA.NS", "SUNTV.NS", 
"SUNDARMFIN.NS", "SUNDRMFAST.NS", "SUNTECK.NS", "SUPREMEIND.NS", "SUVENPHAR.NS", "SUZLON.NS", 
"SWANENERGY.NS", "SYNGENE.NS", "SYRMA.NS", "TV18BRDCST.NS", "TVSMOTOR.NS", "TVSSCS.NS", 
"TMB.NS", "TANLA.NS", "TATACHEM.NS", "TATACOMM.NS", "TCS.NS", "TATACONSUM.NS", "TATAELXSI.NS", 
"TATAINVEST.NS", "TATAMOTORS.NS", "TATAPOWER.NS", "TATASTEEL.NS", "TATATECH.NS", "TTML.NS", 
"TECHM.NS", "TEJASNET.NS", "NIACL.NS", "RAMCOCEM.NS", "THERMAX.NS", "TIMKEN.NS", "TITAGARH.NS", 
"TITAN.NS", "TORNTPHARM.NS", "TORNTPOWER.NS", "TRENT.NS", "TRIDENT.NS", "TRIVENI.NS", 
"TRITURBINE.NS", "TIINDIA.NS", "UCOBANK.NS", "UNOMINDA.NS", "UPL.NS", "UTIAMC.NS", 
"UJJIVANSFB.NS", "ULTRACEMCO.NS", "UNIONBANK.NS", "UBL.NS", "UNITDSPR.NS", "USHAMART.NS", 
"VGUARD.NS", "VIPIND.NS", "VAIBHAVGBL.NS", "VTL.NS", "VARROC.NS", "VBL.NS", "MANYAVAR.NS", 
"VEDL.NS", "VIJAYA.NS", "IDEA.NS", "VOLTAS.NS", "WELCORP.NS", "WELSPUNLIV.NS", "WESTLIFE.NS", 
"WHIRLPOOL.NS", "WIPRO.NS", "YESBANK.NS", "ZFCVINDIA.NS", "ZEEL.NS", "ZENSARTECH.NS", 
"ZOMATO.NS", "ZYDUSLIFE.NS", "ECLERX.NS"


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
df_summary_sorted.to_excel("NIFTY_500_1_3_6.xlsx", index=False, engine='openpyxl')


