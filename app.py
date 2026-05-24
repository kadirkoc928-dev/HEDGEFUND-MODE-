import streamlit as st
from universe import get_universe
from data_feed import get_realtime
from alpha_engine import generate_alpha

st.set_page_config(page_title="HEDGEFUND MODE", layout="wide")

st.title("🏦 HEDGEFUND MODE TERMINAL")

symbols = get_universe()

if st.button("🚀 RUN SIGNAL SCAN"):

    results = []

    for s in symbols:
        try:
            df = get_realtime(s)
            if df is None or len(df) < 20:
                continue

            score, signal = generate_alpha(df)

            results.append({
                "symbol": s,
                "score": score,
                "signal": signal
            })

        except:
            continue

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    st.dataframe(results)

    st.markdown("### 🔥 TOP SIGNALS")

    for r in results[:5]:
        st.write(f"{r['symbol']} → {r['signal']} ({r['score']})")
