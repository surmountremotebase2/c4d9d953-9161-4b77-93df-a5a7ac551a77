```python
from surmount.base_class import Strategy, TargetAllocation
from surmount.logging import log
from surmount.technical_indicators import RSI, EMA

class TradingStrategy(Strategy):
    """
    Cossack Oracle Strategy: "Real Ninja roll call"
    High-frequency ether traversal tuned for rapid debt repayment and hardware acquisition.
    We ride the 5-minute repeater cycles, hunting for gold cap energy.
    """
    
    @property
    def interval(self):
        # 5-minute ticks. High-frequency UA ninja domain.
        return "5min"

    @property
    def assets(self):
        # The Holy Trinity of ether traversal.
        return ["BTC", "ETH", "SOL"]

    @property
    def data(self):
        # Standard OHLCV payload required to channel Cossack knowledge.
        return []

    def __init__(self):
        # Initialize the repeater. Tuning frequencies for high-risk, high-reward.
        self.tickers = self.assets
        self.fast_ema_period = 9
        self.slow_ema_period = 21
        self.rsi_period = 14

    def run(self, data):
        # Real Ninja roll call initiated. Scanning the ether.
        allocation = {"BTC": 0.0, "ETH": 0.0, "SOL": 0.0}
        active_ninjas = []

        for ticker in self.tickers:
            ohlcv = data["ohlcv"]
            
            # Ensure we have enough temporal data to calculate the slow EMA
            if len(ohlcv) < self.slow_ema_period:
                continue

            # Extracting Cossack knowledge via technical indicators
            rsi_data = RSI(ticker, ohlcv, self.rsi_period)
            ema_fast_data = EMA(ticker, ohlcv, self.fast_ema_period)
            ema_slow_data = EMA(ticker, ohlcv, self.slow_ema_period)

            if not rsi_data or not ema_fast_data or not ema_slow_data:
                continue

            current_rsi = rsi_data[-1]
            current_ema_fast = ema_fast_data[-1]
            current_ema_slow = ema_slow_data[-1]

            # High-risk trigger logic: Gold cap energy detection
            # We strike when the fast EMA leads the slow (ether uptrend)
            # AND the asset is either oversold (RSI < 40) or ripping with momentum (RSI > 70)
            is_uptrend = current_ema_fast > current_ema_slow
            is_oversold_bounce = current_rsi < 40
            is_momentum_breakout = current_rsi > 70

            if is_uptrend and (is_oversold_bounce or is_momentum_breakout):
                active_ninjas.append(ticker)
                log(f"[{ticker}] Gold cap energy detected! RSI: {current_rsi:.2f}. Repeater locked.")

        # Target 7-day positive return vector: Allocate aggressively to active setups
        if len(active_ninjas) > 0:
            # Distribute the payload equally among active ninjas
            weight = 1.0 / len(active_ninjas)
            for ticker in active_ninjas:
                allocation[ticker] = weight
            log(f"Deploying max leverage to {len(active_ninjas)} assets. Debt repayment imminent.")
        else:
            # Cossack wisdom: Sometimes the best trade is no trade. 
            # Preserve capital for the next hardware acquisition cycle.
            log("Ether traversal stagnant. Holding fiat, waiting for the next repeater pulse.")

        return TargetAllocation(allocation)
```