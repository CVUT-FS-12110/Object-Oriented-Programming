"""
Decorator pattern example.
"""

class MarketService():

    def get_pairs(self): pass # list all symbols

    def get_price(self, pair): pass

    def trade(self, pair, volume): pass

class ForexMarket(MarketService): pass

class ForexSuperExchange(MarketService): pass

class CryptoExchange(MarketService): pass

class CryptoAlternativeMarket(MarketService): pass

class PaymentMethod():

    def get_supported_symbols(self): pass

    def deposit(self, volume, symbol): pass

    def withdraw(self, volume, symbol): pass

class CreditCardGate(PaymentMethod): pass

class WiredTransfer(PaymentMethod): pass

class CryptoWallet(PaymentMethod): pass

class ExchangeFacade():

    def __init__(self):
        self._exchanges = [
            ForexMarket(),
            CryptoExchange(),
            ForexSuperExchange(),
            CryptoAlternativeMarket(),
        ]
        self._payment_gates = [
            CreditCardGate,
            WiredTransfer,
            CryptoWallet,
        ]

    def _find_payment_gate(self, symbol):
        """ Find gate that supports given symbol
        """

    def _find_best_price(self, symbol):
        """ Find best market service for the symbol
        """

    def _make_order(self, pair, volume, exchange):
        """
        1. Call _find_payment_gate for both symbols in pair
        2. withdraw from source payment gate
        3. trade via exchange
        4. deposit to target payment gate
        """

    def limit_order(self, pair, volume, price):
        """ 
        1. Call _find_best_price till required price appears
        2. Call _make_order
        """

    def market_order(self, pair, volume):
        """
        1. Call _find_best_price once
        2. Call _make_order
        """
