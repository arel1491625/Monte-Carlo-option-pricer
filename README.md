# Monte-Carlo-option-pricer
Monte Carlo European Option Pricer.  A vectorised Monte Carlo simulation for pricing European call and put options using Geometric Brownian Motion. Includes put-call parity verification.
Uses numpy vectorisation in order to perform Monte Carlo simulation for pricing European call and put options using Geometric Brownian Motion efficiently. Also includes put-call parity verification.
Stock prices follow Geometric Brownian Motion: S(t+dt) = S(t)·exp((μ - ½σ²)dt + σ√dt·Z) where Z is a random number|{Z~N(0,1)}. This program eapproximates the integral: ∫ dS/S) as a sum with step size: dt.
