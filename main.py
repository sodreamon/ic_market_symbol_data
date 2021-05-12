'''
종가 데이터로 피어슨 상관계수 추출
'''
################################ 임포팅 ################################
for _importing in [0]:
    # import investpy
    import pandas as pd
    import FinanceDataReader as fdr
    # from scipy import stats
    # import statsmodels.tsa.stattools as ts 
    # import pprint
    import json
    import os
    import numpy as np
    #차트
    # import chart_studio.plotly as py
    # import plotly.graph_objs as go
    # import cufflinks as cf
    # cf.go_offline(connected=True)
    # 데이터베이스
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    # 인디케이터
    # import ta

################################### 사전작업 ###################################
for _base in [0]:
    # pd.set_option("display.max_rows",10000000)
    # pp = pprint.PrettyPrinter(indent=4)

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///symbol_data.db'
    db = SQLAlchemy(app)

    symbol_list = [
        # 채권
        "FLG,LIFFE", "FV,None", "US,None", "TY,None", "FGBL,None", "FGBM,None", "FGBS,None", "FBTP,None", "JGB,None",  
        
        # 지수
        "AUS200,None", "SXFc1,None", "HCEIc1,None", "CHINA50,None", "DE30,None", "ES35,None", "F40,None", "invhk50,None", "invit40,None", "JP225,None", "MDE50,None", "AEX,None", "OBX,None", "JTOPI,None", "OMXS30,None", "STOXX50,None", "SWI20,None", "DETEC30,None", "UK100,None", "US2000,None", "US30,None", "US500,None", "USTEC,None",

        # 원자재
        "B,ICE", "CC,ICE", "KC,ICE", "ZC,None", "OJ,ICE", "SOYB,None", "SB,ICE", "WEAT,None", "T,ICE", "XBR/USD,None", "WTI/USD,None",

        #외환
        "EUR/USD,None","GBP/USD,None","USD/JPY,None","AUD/USD,None","USD/CAD,None","USD/CHF,None","AUD/CAD,None","AUD/CHF,None","AUD/JPY,None","AUD/NZD,None","CAD/CHF,None","EUR/CAD,None","CAD/JPY,None","CHF/JPY,None","EUR/AUD,None","EUR/CHF,None","EUR/GBP,None","EUR/JPY,None","EUR/NZD,None","GBP/AUD,None","GBP/CAD,None","GBP/CHF,None","GBP/JPY,None","GBP/NZD,None","GBP/TRY,None","NZD/CAD,None","NZD/CHF,None","NZD/JPY,None","NZD/USD,None","USD/SGD,None","AUD/SGD,None","CHF/SGD,None","EUR/DKK,None","EUR/HKD,None","EUR/NOK,None","EUR/PLN,None","EUR/SEK,None","EUR/SGD,None","EUR/TRY,None","EUR/ZAR,None","GBP/DKK,None","GBP/NOK,None","GBP/SEK,None","GBP/SGD,None","NOK/JPY,None","NOK/SEK,None","SEK/JPY,None","SGD/JPY,None","USD/CNH,None","USD/CZK,None","USD/DKK,None","USD/HKD,None","USD/HUF,None","USD/MXN,None","USD/NOK,None","USD/PLN,None","USD/RUB,None","USD/SEK,None","USD/THB,None","USD/TRY,None","USD/ZAR,None",

        # 암호화폐
        "BTC/USD,None","BCH/USD,None","ETH/USD,None","LTC/USD,None","XRP/USD,None","EOS/USD,None","NMC/USD,None","PPC/USD,None","DASH/USD,None",

        # 주식
        # NYSE
        "A,NYSE","AAP,NYSE","ABBV,NYSE","ABC,NYSE","ABT,NYSE","ACB,NYSE","ADM,NYSE","AEE,NYSE","AES,NYSE","AFL,NYSE","AGR,NYSE","AIG,NYSE","AIZ,NYSE","AJG,NYSE","ALB,NYSE","ALK,NYSE","ALL,NYSE","ALLE,NYSE","ALLY,NYSE","AMCR,NYSE","AME,NYSE","AMP,NYSE","AMT,NYSE","ANET,NYSE","ANTM,NYSE","AON,NYSE","AOS,NYSE","APD,NYSE","APH,NYSE","APO,NYSE","APTV,NYSE","ARE,NYSE","ATO,NYSE","ATUS,NYSE","AVB,NYSE","AVLR,NYSE","AVY,NYSE","AWK,NYSE","AXP,NYSE","AZO,NYSE","BA,NYSE","BABA,NYSE","BAC,NYSE","BAH,NYSE","BAX,NYSE","BBY,NYSE","BDX,NYSE","BEN,NYSE","BFAM,NYSE","BG,NYSE","BIO,NYSE","BK,NYSE","BKR,NYSE","BLK,NYSE","BLL,NYSE","BMY,NYSE","BR,NYSE","BRKb,NYSE","BRO,NYSE","BSX,NYSE","BWA,NYSE","BX,NYSE","BXP,NYSE","C,NYSE","CAG,NYSE","CAH,NYSE","ACN,NYSE","CARR,NYSE","CAT,NYSE","CB,NYSE","CBRE,NYSE","CCI,NYSE","CCIV,NYSE","CCK,NYSE","CCL,NYSE","CDAY,NYSE","CE,NYSE","CF,NYSE","CFG,NYSE","CGC,NASDAQ","CHD,NYSE","CI,NYSE","CL,NYSE","CLX,NYSE","CMA,NYSE","CMG,NYSE","CMI,NYSE","CMS,NYSE","CNC,NYSE","CNP,NYSE","COF,NYSE","COG,NYSE","COO,NYSE","COP,NYSE","CPB,NYSE","CPT,NYSE","CRL,NYSE","CRM,NYSE","CTLT,NYSE","CTVA,NYSE","CUK,NYSE","CVNA,NYSE","CVS,NYSE","CVX,NYSE","D,NYSE","DAL,NYSE","DAR,NYSE","DD,NYSE","DE,NYSE","DEO,NYSE","DFS,NYSE","DG,NYSE","DGX,NYSE","DHI,NYSE","DHR,NYSE","DIS,NYSE","DLR,NYSE","DOV,NYSE","DOW,NYSE","DPZ,NYSE","DRE,NYSE","DRI,NYSE","DT,NYSE","DTE,NYSE","DUK,NYSE","DVA,NYSE","DVN,NYSE","DXC,NYSE","ECL,NYSE","ED,NYSE","EEM,NYSE","EFX,NYSE","EIX,NYSE","EL,NYSE","ELAN,NYSE","ELS,NYSE","EMN,NYSE","EMR,NYSE","EOG,NYSE","EPAM,NYSE","EPD,NYSE","EQH,NYSE","EQR,NYSE","ES,NYSE","ESS,NYSE","ESTC,NYSE","ET,NYSE","ETN,NYSE","ETR,NYSE","EVRG,NYSE","EW,NYSE","EWH,NYSE","EWW,NYSE","EWZ,NYSE","EXR,NYSE","F,NYSE","FBHS,NYSE","FCX,NYSE","FDS,NYSE","FDX,NYSE","FE,NYSE","FICO,NYSE","FIS,NYSE","FLS,NYSE","FLT,NYSE","FMC,NYSE","FNF,NYSE","FRC,NYSE","FRT,NYSE","FTI,NYSE","FTV,NYSE","FXI,NYSE","GD,NYSE","GDDY,NYSE","GDX,NYSE","GE,NYSE","GIS,NYSE","GL,NYSE","GLW,NYSE","GM,NYSE","GNRC,NYSE","GPN,NYSE","GPS,NYSE","GS,NYSE","GWRE,NYSE","GWW,NYSE","HAL,NYSE","HBI,NYSE","HCA,NYSE","HD,NYSE","HEI,NYSE","HES,NYSE","HFC,NYSE","HIG,NYSE","HII,NYSE","HLT,NYSE","HON,NYSE","HPE,NYSE","HPQ,NYSE","HRL,NYSE","HSY,NYSE","HUBS,NYSE","HUM,NYSE","HWM,NYSE","IBM,NYSE","ICE,NYSE","IEMG,NYSE","IEX,NYSE","IFF,NYSE","INFO,NYSE","INVH,NYSE","IP,NYSE","IPG,NYSE","IQV,NYSE","IR,NYSE","IRM,NYSE","IT,NYSE","ITW,NYSE","IVZ,NYSE","J,NYSE","JCI,NYSE","JNJ,NYSE","JNPR,NYSE","JPM,NYSE","K,NYSE","KEY,NYSE","KEYS,NYSE","KIM,NYSE","KKR,NYSE","KMB,NYSE","KMI,NYSE","KMX,NYSE","KO,NYSE","KR,NYSE","KSU,NYSE","L,NYSE","LAD,NYSE","LB,NYSE","LDOS,NYSE","LEG,NYSE","LEN,NYSE","LH,NYSE","LHX,NYSE","LII,NYSE","LIN,NYSE","LLY,NYSE","LMT,NYSE","LNC,NYSE","LOW,NYSE","LQD,NYSE","LUMN,NYSE","LUV,NYSE","LVS,NYSE","LW,NYSE","LYB,NYSE","LYV,NYSE","MA,NYSE","MAA,NYSE","MAS,NYSE","MCD,NYSE","MCK,NYSE","MCO,NYSE","MDT,NYSE","MET,NYSE","MGM,NYSE","MGP,NYSE","MHK,NYSE","MJ,NYSE","MKC,NYSE","MKL,NYSE","MLM,NYSE","MMC,NYSE","MMM,NYSE","MO,NYSE","MOH,NYSE","MOS,NYSE","MPC,NYSE","MPLX,NYSE","MPW,NYSE","MRK,NYSE","MRO,NYSE","MS,NYSE","MSCI,NYSE","MSI,NYSE","MTB,NYSE","MTD,NYSE","MTN,NYSE","NCLH,NYSE","NEE,NYSE","NEM,NYSE","NET,NYSE","NI,NYSE","NKE,NYSE","NLSN,NYSE","NLY,NYSE","NOC,NYSE","NOV,NYSE","NOW,NYSE","NRG,NYSE","NSC,NYSE","NUE,NYSE","NVR,NYSE","O,NYSE","OKE,NYSE","OMC,NYSE","ORCL,NYSE","OSH,NYSE","OTIS,NYSE","OXY,NYSE","PANW,NYSE","PAYC,NYSE","PCG,NYSE","PEAK,NYSE","PEG,NYSE","PFE,NYSE","PG,NYSE","PGR,NYSE","PH,NYSE","PHM,NYSE","PINS,NYSE","PKG,NYSE","PKI,NYSE","PLAN,NYSE","PLD,NYSE","PM,NYSE","PNC,NYSE","PNR,NYSE","PNW,NYSE","PPG,NYSE","PPL,NYSE","PRGO,NYSE","PRU,NYSE","PSA,NYSE","PSX,NYSE","PVH,NYSE","PWR,NYSE","PXD,NYSE","QS,NYSE","RCL,NYSE","RE,NYSE","RF,NYSE","RH,NYSE","RHI,NYSE","RJF,NYSE","RKT,NYSE","RMD,NYSE","ROK,NYSE","ROL,NYSE","ROP,NYSE","RPM,NYSE","RSG,NYSE","RTX,NYSE","RYN,NYSE","SAM,NYSE","SCCO,NYSE","SCHW,NYSE","SE,NYSE","SEE,NYSE","SHW,NYSE","SJM,NYSE","SLB,NYSE","SLG,NYSE","SMAR,NYSE","SMG,NYSE","SNA,NYSE","SNAP,NYSE","SNOW,NYSE","SO,NYSE","SPG,NYSE","SPGI,NYSE","SQ,NYSE","SRE,NYSE","STE,NYSE","STT,NYSE","STZ,NYSE","SUI,NYSE","SWK,NYSE","SYF,NYSE","SYK,NYSE","SYY,NYSE","T,NYSE","TAP,NYSE","TDG,NYSE","TDOC,NYSE","TDY,NYSE","TEL,NYSE","TFC,NYSE","TFX,NYSE","TGT,NYSE","TJX,NYSE","TMO,NYSE","TPR,NYSE","TREX,NYSE","TRU,NYSE","TRV,NYSE","TSN,NYSE","TT,NYSE","TTC,NYSE","TWLO,NYSE","TWTR,NYSE","TXT,NYSE","TYL,NYSE","UA,NYSE","UAA,NYSE","UBER,NYSE","UDR,NYSE","UHS,NYSE","UI,NYSE","UNG,NYSE","UNH,NYSE","UNM,NYSE","UNP,NYSE","UPS,NYSE","URA,NYSE","URI,NYSE","USB,NYSE","USO,NYSE","V,NYSE","VAR,NYSE","VFC,NYSE","VLO,NYSE","VMC,NYSE","VMW,NYSE","VNO,NYSE","VTR,NYSE","VYM,NYSE","VZ,NYSE","W,NYSE","WAB,NYSE","WAT,NYSE","WEC,NYSE","WELL,NYSE","WFC,NYSE","WHR,NYSE","WLK,NYSE","WM,NYSE","WMB,NYSE","WMT,NYSE","WPC,NYSE","WRB,NYSE","WRK,NYSE","WST,NYSE","WTRG,NYSE","WU,NYSE","WY,NYSE","XLE,NYSE","XLF,NYSE","XLI,NYSE","XLP,NYSE","XLU,NYSE","XOM,NYSE","XOP,NYSE","XRX,NYSE","XYL,NYSE","YUM,NYSE","YUMC,NYSE","ZBH,NYSE","ZTS,NYSE","BFb,NYSE",
        # NASDAQ
        "AAL,NASDAQ","AAPL,NASDAQ","ABMD,NASDAQ","ABNB,NASDAQ","ADBE,NASDAQ","ADI,NASDAQ","ADP,NASDAQ","ADSK,NASDAQ","AEP,NASDAQ","AFRM,NASDAQ","AKAM,NASDAQ","ALGN,NASDAQ","ALNY,NASDAQ","ALXN,NASDAQ","AMAT,NASDAQ","AMD,NASDAQ","AMED,NASDAQ","AMGN,NASDAQ","AMZN,NASDAQ","ANSS,NASDAQ","APA,NASDAQ","APPN,NASDAQ","ATVI,NASDAQ","AVGO,NASDAQ","AZPN,NASDAQ","BIIB,NASDAQ","BKNG,NASDAQ","BMRN,NASDAQ","BSY,NASDAQ","BYND,NASDAQ","CDNS,NASDAQ","CDW,NASDAQ","CERN,NASDAQ","CG,NASDAQ","CGNX,NASDAQ","CHRW,NASDAQ","CHTR,NASDAQ","CINF,NASDAQ","CMCSA,NASDAQ","CME,NASDAQ","COST,NASDAQ","COUP,NASDAQ","CPRT,NASDAQ","CREE,NASDAQ","CRON,NASDAQ","CRWD,NASDAQ","CSCO,NASDAQ","CSGP,NASDAQ","CSX,NASDAQ","CTAS,NASDAQ","CTSH,NASDAQ","CTXS,NASDAQ","CZR,NASDAQ","DBX,NASDAQ","DDOG,NASDAQ","DISCA,NASDAQ","DISCK,NASDAQ","DISH,NASDAQ","DKNG,NASDAQ","DLTR,NASDAQ","DOCU,NASDAQ","DXCM,NASDAQ","EA,NASDAQ","EBAY,NASDAQ","ENPH,NASDAQ","ENTG,NASDAQ","EQIX,NASDAQ","ERIE,NASDAQ","ETSY,NASDAQ","EXAS,NASDAQ","EXC,NASDAQ","EXPD,NASDAQ","EXPE,NASDAQ","EXPI,NASDAQ","FANG,NASDAQ","FAST,NASDAQ","FB,NASDAQ","FFIV,NASDAQ","FISV,NASDAQ","FITB,NASDAQ","FIVE,NASDAQ","FIVN,NASDAQ","FLIR,NASDAQ","FOX,NASDAQ","FOXA,NASDAQ","FSLR,NASDAQ","FTNT,NASDAQ","FWONK,NASDAQ","GDRX,NASDAQ","GILD,NASDAQ","GLPI,NASDAQ","GOOG,NASDAQ","GPC,NYSE","GRMN,NASDAQ","HAS,NASDAQ","HBAN,NASDAQ","HOLX,NASDAQ","HSIC,NASDAQ","HST,NASDAQ","IAC,NASDAQ","IBKR,NASDAQ","IDXX,NASDAQ","IEP,NASDAQ","ILMN,NASDAQ","INCY,NASDAQ","INTC,NASDAQ","INTU,NASDAQ","IPGP,NASDAQ","ISRG,NASDAQ","JBHT,NASDAQ","JBHT,NASDAQ","KDP,NASDAQ","KHC,NASDAQ","KLAC,NASDAQ","LAZR,NASDAQ","LBRDA,NASDAQ","LBRDK,NASDAQ","LKQ,NASDAQ","LNT,NASDAQ","LOGI,NASDAQ","LPLA,NASDAQ","LRCX,NASDAQ","LSXMK,NASDAQ","LYFT,NASDAQ","MAR,NASDAQ","MASI,NASDAQ","MCHP,NASDAQ","MDB,NASDAQ","MDLZ,NASDAQ","MKTX,NASDAQ","MNST,NASDAQ","MORN,NASDAQ","MPWR,NASDAQ","MRNA,NASDAQ","MRTX,NASDAQ","MSFT,NASDAQ","MTCH,NASDAQ","MU,NASDAQ","MXIM,NASDAQ","NBIX,NASDAQ","NDAQ,NASDAQ","NDSN,NASDAQ","NFLX,NASDAQ","NLOK,NASDAQ","NTAP,NASDAQ","NTRA,NASDAQ","NTRS,NASDAQ","NUAN,NASDAQ","NVAX,NASDAQ","NVDA,NASDAQ","NWL,NASDAQ","NWS,NASDAQ","NWSA,NASDAQ","ODFL,NASDAQ","OKTA,NASDAQ","OLED,NASDAQ","ON,NASDAQ","OPEN,NASDAQ","ORLY,NASDAQ","PAYX,NASDAQ","PBCT,NASDAQ","PCAR,NASDAQ","PCTY,NASDAQ","PEGA,NASDAQ","PENN,NASDAQ","PEP,NASDAQ","PFG,NASDAQ","PLUG,NASDAQ","PODD,NASDAQ","POOL,NASDAQ","PPD,NASDAQ","PTC,NASDAQ","PTON,NASDAQ","PYPL,NASDAQ","QCOM,NASDAQ","QQQ,NASDAQ","QRVO,NASDAQ","RDWR,NASDAQ","REG,NASDAQ","REGN,NASDAQ","RGEN,NASDAQ","ROKU,NASDAQ","ROST,NASDAQ","RPRX,NASDAQ","RUN,NASDAQ","SBAC,NASDAQ","SBNY,NASDAQ","SBUX,NASDAQ","SGEN,NASDAQ","SIRI,NASDAQ","SIVB,NASDAQ","SNPS,NASDAQ","SPLK,NASDAQ","SPWR,NASDAQ","SSNC,NASDAQ","STX,NASDAQ","SWKS,NASDAQ","TECH,NASDAQ","TER,NASDAQ","TLRY,NASDAQ","TLT,NASDAQ","TMUS,NASDAQ","TRMB,NASDAQ","TROW,NASDAQ","TSCO,NASDAQ","TSLA,NASDAQ","TTD,NASDAQ","TTWO,NASDAQ","TXG,NASDAQ","TXN,NASDAQ","UAL,NASDAQ","ULTA,NASDAQ","VIAC,NASDAQ","VRSK,NASDAQ","VRSN,NASDAQ","VRTX,NASDAQ","VTRS,NASDAQ","WBA,NASDAQ","WDAY,NASDAQ","WDC,NASDAQ","WISH,NASDAQ","WLTW,NASDAQ","WMG,NASDAQ","WYNN,NASDAQ","XEL,NASDAQ","XLNX,NASDAQ","XRAY,NASDAQ","Z,NASDAQ","ZBRA,NASDAQ","ZG,NASDAQ","ZI,NASDAQ","ZION,NASDAQ","ZM,NASDAQ","ZNGA,NASDAQ","ZS,NASDAQ"
    ]
    _5y_ago_datetime = "2016-04-20"

####################################### db 모델 #######################################
for _db_model in[0]:

    class SymbolData(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        symbol = db.Column(db.String(80), unique=True, nullable=False)
        data = db.Column(db.PickleType)

        def __repr__(self):
            return '<SymbolData %r>' % self.symbol

    if not os.path.isfile("symbol_data.db") :
        db.create_all()

################################## 함수 ##################################
for _def_box in [0]:
    # 심볼별 데이터 구하기
    def fdr_df_maker(symbol_list, start_date=None) :

        df_dict = {}

        num_of_all_symbol = len(symbol_list)
        print("all_symbols: ", num_of_all_symbol)
        count_n = 0

        for symbol_exchange in symbol_list :

            if SymbolData.query.filter_by(symbol=symbol_exchange).first() is None:

                symbol_exchange_pack = symbol_exchange.split(",")
                _symbol = symbol_exchange_pack[0]
                exchange = symbol_exchange_pack[1]
                if exchange == "None":
                    exchange=None

                if start_date==None:
                    data_df = fdr.DataReader(_symbol, exchange=exchange)
                else :
                    data_df = fdr.DataReader(_symbol, start_date, exchange=exchange)
                if len(data_df) < 1 :
                    continue
                
                new_SymbolData = SymbolData(symbol=symbol_exchange, data=data_df)
                db.session.add(new_SymbolData)
                db.session.commit()                

            else:
                pass
                # data_df = SymbolData.query.filter_by(symbol=symbol_exchange).first().data

            # data_df["CloseChange"] = data_df["Close"].diff()

            # # data_df["PreCloseChange"] = data_df["CloseChange"].shift(1)
            # data_df = data_df.dropna()

            # df_dict[symbol_exchange] = data_df
            count_n += 1
            print("\r", str(count_n).zfill(6), end="")
        print()

        return df_dict
    

################################# 본작업 #################################
for _main_process in [0]:
    # 데이터프레임 딕셔너리 만들기
    data_df_dict = fdr_df_maker(symbol_list)
    # pp.pprint(data_df_dict)

print('done!')    
