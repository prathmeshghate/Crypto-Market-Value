# Importing required libraries

import requests
import json
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkcalendar import DateEntry

# API Key
API_Key= #Api

# GUI Code
root=tk.Tk()
root.title("Cryptocurrency Values")
root.resizable(False,False)
root.configure(bg='purple')

#Main Label 
Main_label=ttk.Label(root,text="Coin's Name",font=('arial',12,'bold'),background='purple',foreground='coral')
Main_label.grid(column=0,row=0,padx=2)

# Combobox for all coins
text=tk.StringVar()
input_crypto=ttk.Combobox(root,width=25,textvariable=text)
input_crypto['values']=['ABC', 'ACP', 'ACT', 'ACT*', 'ADA', 'ADCN', 'ADL', 'ADX', 'ADZ', 'AE', 'AGI', 'AIB', 'AIDOC', 'AION', 'AIR', 'ALT', 'AMB', 'AMM', 'ANT', 'APC', 'APPC', 'ARC', 'ARCT', 'ARDR', 'ARK', 'ARN', 'ASAFE2', 'AST', 'ATB','ATM', 'AURS', 'AVT', 'BAR', 'BASH', 'BAT', 'BAY', 'BBP', 'BCD', 'BCH', 'BCN', 'BCPT', 'BEE', 'BIO', 'BLC', 'BLOCK','BLU', 'BLZ', 'BMC', 'BNB', 'BNT', 'BOST', 'BQ', 'BQX', 'BRD', 'BRIT', 'BT1', 'BT2', 'BTC', 'BTCA', 'BTCS', 'BTCZ', 'BTG', 'BTLC', 'BTM', 'BTM*', 'BTQ', 'BTS', 'BTX', 'BURST', 'CALC', 'CAS', 'CAT', 'CCRB', 'CDT', 'CESC', 'CHAT', 'CJ','CL', 'CLD', 'CLOAK', 'CMT*', 'CND', 'CNX', 'CPC', 'CRAVE', 'CRC', 'CRE', 'CRW', 'CTO', 'CTR', 'CVC', 'DAS', 'DASH', 'DAT', 'DATA', 'DBC', 'DBET', 'DCN', 'DCR', 'DCT', 'DEEP', 'DENT', 'DGB', 'DGD', 'DIM', 'DIME', 'DMD', 'DNT', 'DOGE', 'DRGN', 'DRZ', 'DSH', 'DTA', 'EC', 'EDG', 'EDO', 'EDR', 'EKO', 'ELA', 'ELF', 'EMC', 'EMGO', 'ENG', 'ENJ', 'EOS', 'ERT', 'ETC','ETH', 'ETN', 'ETP', 'ETT', 'EVR', 'EVX', 'FCT', 'FLP', 'FOTA', 'FRST', 'FUEL', 'FUN', 'FUNC', 'FUTC', 'GAME', 'GAS', 'GBYTE', 'GMX', 'GNO', 'GNT', 'GNX', 'GRC', 'GRS', 'GRWI', 'GTC', 'GTO', 'GUP', 'GVT', 'GXS', 'HAC', 'HNC', 'HSR', 'HST','HVN', 'ICN', 'ICOS', 'ICX', 'IGNIS', 'ILC', 'INK', 'INS', 'INSN', 'INT', 'IOP', 'IOST', 'ITC', 'KCS', 'KICK', 'KIN','KLC', 'KMD', 'KNC', 'KRB', 'LA', 'LEND', 'LEO', 'LINDA', 'LINK', 'LOC', 'LOG', 'LRC', 'LSK', 'LTC', 'LUN', 'LUX', 'MAID', 'MANA', 'MCAP', 'MCO', 'MDA', 'MDS', 'MIOTA', 'MKR', 'MLN', 'MNX', 'MOD', 'MOIN', 'MONA', 'MTL', 'MTN*','MTX', 'NAS', 'NAV', 'NBT', 'NDC', 'NEBL', 'NEO', 'NEU', 'NEWB', 'NGC', 'NKC', 'NLC2', 'NMC', 'NMR', 'NULS', 'NVC', 'NXT','OAX', 'OBITS', 'OC', 'OCN', 'ODN', 'OK', 'OMG', 'OMNI', 'ORE', 'ORME', 'OST', 'OTN', 'OTX', 'OXY', 'PART', 'PAY', 'PBT', 'PCS', 'PIVX', 'PIZZA', 'PLBT', 'PLR', 'POE', 'POLY', 'POSW', 'POWR', 'PPC', 'PPT', 'PPY', 'PRC', 'PRES', 'PRG', 'PRL', 'PRO', 'PURA', 'PUT', 'QASH', 'QAU', 'QSP', 'QTUM', 'QUN', 'R', 'RBIES', 'RCN', 'RDD', 'RDN', 'RDN*', 'REBL', 'REE', 'REP', 'REQ', 'REV', 'RGC', 'RHOC', 'RIYA', 'RKC', 'RLC', 'RPX', 'RUFF', 'SALT', 'SAN', 'SBC', 'SC', 'SENT', 'SHIFT', 'SIB', 
'SMART', 'SMLY', 'SMT*', 'SNC', 'SNGLS', 'SNM', 'SNT', 'SPK', 'SRN', 'STEEM', 'STK', 'STORJ', 'STRAT', 'STU', 'STX', 'SUB', 'SUR', 'SWFTC', 'SYS', 
'TAAS', 'TESLA', 'THC', 'THETA', 'THS', 'TIO', 'TKN', 'TKY', 'TNB', 'TNT', 'TOA', 'TRC', 'TRIG', 'TRST', 'TRUMP', 'TRX', 'UBQ', 'UNO', 'UNRC', 
'UQC', 'USDT', 'UTK', 'UTT', 'VEE', 'VEN', 'VERI', 'VIA', 'VIB', 'VIBE', 'VOISE', 'VOX', 'VRS', 'VTC', 'VUC', 'WABI', 'WAVES', 'WAX', 'WC', 'WGR', 'WINGS', 'WLK', 'WOP', 'WPR', 'WRC', 'WTC', 'XAUR', 'XBP', 'XBY', 'XCP', 'XCXT', 'XDN', 'XEM', 'XGB', 'XHI', 'XID', 'XLM', 
'XMR', 'XNC', 'XRB', 'XRP', 'XTO', 'XTZ', 'XUC', 'XVG', 'XZC', 'YEE', 'YOC', 'YOYOW', 'ZBC', 'ZCL', 'ZEC', 'ZEN', 'ZIL','ZNY', 'ZRX', 'ZSC', '611']
input_crypto.grid(column=2,row=1)

# This two list are used to make dictionaries for autocompletebox
values1=['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 
'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 
'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 
'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 
'YER', 'ZAR', 'ZMW']

key1=['UAE Dirham', 'Afghan Afghani', 'Albanian Lek', 'Armenian Dram', 'Netherlands Antillian Guilder', 'Angolan Kwanza', 'Argentine Peso', 'Australian Dollar', 'Aruban Florin', 'Azerbaijani Manat', 'Bosnia and Herzegovina Convertible Mark', 'Barbados Dollar', 'Bangladeshi Taka', 'Bulgarian Lev', 'Bahraini Dinar', 'Burundian Franc', 'Bermudian Dollar', 'Brunei Dollar', 'Bolivian Boliviano', 'Brazilian Real', 'Bahamian Dollar', 'Bhutanese Ngultrum', 'Botswana Pula', 'Belarusian Ruble', 'Belize Dollar', 'Canadian Dollar', 'Congolese Franc', 'Swiss Franc', 'Chilean Peso', 'Chinese Renminbi', 'Colombian Peso', 'Costa Rican Colon', 'Cuban Convertible Peso', 'Cuban Peso', 'Cape Verdean Escudo', 'Czech Koruna', 'Djiboutian Franc', 'Danish Krone', 'Dominican Peso', 'Algerian Dinar', 'Egyptian Pound', 'Eritrean Nakfa', 'Ethiopian Birr', 'Euro', 'Fiji Dollar', 'Falkland Islands Pound', 'Faroese Króna', 'Pound Sterling', 'Georgian Lari', 'Guernsey Pound', 'Ghanaian Cedi', 'Gibraltar Pound', 'Gambian Dalasi', 'Guinean Franc', 'Guatemalan Quetzal', 'Guyanese Dollar', 'Hong Kong Dollar', 'Honduran Lempira', 'Croatian Kuna', 'Haitian Gourde', 'Hungarian Forint', 'Indonesian Rupiah', 'Israeli New Shekel', 'Manx Pound', 'Indian Rupee', 'Iraqi Dinar', 'Iranian Rial', 'Icelandic Króna', 'Jamaican Dollar', 'Jordanian Dinar', 'Japanese Yen', 'Kenyan Shilling', 'Kyrgyzstani Som', 'Cambodian Riel', 'Kiribati Dollar', 'Comorian Franc', 'South Korean Won', 'Kuwaiti Dinar', 'Cayman Islands Dollar', 'Kazakhstani Tenge', 'Lao Kip', 'Lebanese Pound', 'Sri Lanka Rupee', 'Liberian Dollar', 'Lesotho Loti', 'Libyan Dinar', 'Moroccan Dirham', 'Moldovan Leu', 'Malagasy Ariary', 'Macedonian Denar', 'Burmese Kyat', 'Mongolian Tögrög', 'Macanese Pataca', 'Mauritanian Ouguiya', 'Mauritian Rupee', 'Maldivian Rufiyaa', 'Malawian Kwacha', 'Mexican Peso', 'Malaysian Ringgit', 'Mozambican Metical', 'Namibian Dollar', 'Nigerian Naira', 'Nicaraguan Córdoba', 'Norwegian Krone', 'Nepalese Rupee', 
'New Zealand Dollar', 'Omani Rial', 'Panamanian Balboa', 'Peruvian Sol', 'Papua New Guinean Kina', 
'Philippine Peso', 'Pakistani Rupee', 'Polish Złoty', 'Paraguayan Guaraní', 'Qatari Riyal', 'Romanian Leu', 
'Serbian Dinar', 'Russian Ruble', 'Rwandan Franc', 'Saudi Riyal', 'Solomon Islands Dollar', 'Seychellois Rupee', 'Sudanese Pound', 'Swedish Krona', 'Singapore Dollar', 'Saint Helena Pound', 'Sierra Leonean Leone', 
'Somali Shilling', 'Surinamese Dollar', 'South Sudanese Pound', 'São Tomé and Príncipe Dobra', 'Syrian Pound', 'Eswatini Lilangeni', 'Thai Baht', 'Tajikistani Somoni', 'Turkmenistan Manat', 'Tunisian Dinar', 'Tongan Paʻanga', 'Turkish Lira', 'Trinidad and Tobago Dollar', 'Tuvaluan Dollar', 'New Taiwan Dollar', 'Tanzanian Shilling', 'Ukrainian Hryvnia', 'Ugandan Shilling', 'United States Dollar', 'Uruguayan Peso', "Uzbekistani So'm", 'Venezuelan Bolívar Soberano', 'Vietnamese Đồng', 'Vanuatu Vatu', 'Samoan Tālā', 'Central African CFA Franc', 'East Caribbean Dollar', 'Special Drawing Rights', 'West African CFA franc', 'CFP Franc', 'Yemeni Rial', 'South African Rand', 'Zambian Kwacha']

#Dictionary for above lists
currency_dict={}

# Code used to create two lists into dictionary
for key in key1:
    for value in values1:
        currency_dict[key] = value
        values1.remove(value)
        break 

# Label for value of coin 
value_label=ttk.Label(root,text='Value of coin',font=('arial',12,'bold'),background='purple',foreground='coral')
value_label.grid(column=0,row=9)

# Label for period "live or historic"
period_label=ttk.Label(root,text="Live value Or Historical value?",font=('arial',12,'bold'),background='purple',foreground='coral')
period_label.grid(column=0,row=2)

# Label for target currency
to_label=ttk.Label(root,text="Coin's output currency",font=('arial',12,'bold'),background='purple',foreground='coral')
to_label.grid(column=0,row=6)

#Label for Date
Date_label=ttk.Label(root,text="Please enter a date if specific date",font=('arial',12,'bold'),background='purple',foreground='coral')
Date_label.grid(column=0,row=4)

# Calender 
cal = DateEntry(root, width=25, background='purple',foreground='coral', borderwidth=2, year=2021, date_pattern='YYYY-MM-DD')
cal.grid(column=2,row=5,pady=3)

# Combobox selecting 'live or specific date'
period=tk.StringVar()
live_box=ttk.Combobox(root,width=25,textvariable=period)
live_box['values']=["LIVE","Specific Date"]
live_box.grid(column=2,row=3)

# Autocompletebox for currency
text2=tk.StringVar()
base_currency_name=key1
Currency_box=AutocompleteCombobox(root,width=25,textvariable=text2,completevalues=base_currency_name)
Currency_box.grid(column=2,row=7,padx=3)

# Function for getting the value of coin
def value_of_coin():
    if (period.get()== "LIVE"):
        #z = response.json()['rates'][text.get()]
        response=requests.get('http://api.coinlayer.com/live?access_key='+API_Key,params={'symbols':text.get(),'target':currency_dict[text2.get()]})
        price_coin=response.json()['rates'][text.get()]
        output_box.insert(tk.INSERT,price_coin)
    else:
        response1=requests.get('http://api.coinlayer.com/'+str(cal.get_date())+'?access_key='+ API_Key,params={'symbols':text.get(),'target':currency_dict[text2.get()]})
        price_coin1=response1.json()['rates'][text.get()]
        output_box.insert(tk.INSERT,price_coin1)
        
# Function for clearing all inputs and result
def clear():
    input_crypto.delete(0,'end')
    output_box.delete(0,'end')
    Currency_box.delete(0,'end')
    live_box.delete(0,'end')
    cal.delete(0,'end')

# Clear button for clearing all data in GUI
clear_button=ttk.Button(root,text='Clear All',command=clear)
clear_button.grid(column=1,row=11)

# Get value button for getting value of particular coin
show_button=ttk.Button(root,text="Get Value",command=value_of_coin)
show_button.grid(column=1,row=8,pady=3)

# The output got from API displays here
output_box=ttk.Entry(root,width=25)
output_box.grid(column=2,row=10,padx=0,pady=3)

root.mainloop()

#END