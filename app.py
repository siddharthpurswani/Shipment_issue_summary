import streamlit as st
import requests
import json

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ShipSense AI",
    page_icon="🚚",
    layout="centered",
)

# ─── Hardcoded n8n Webhook URL ─────────────────────────────────────────────────
N8N_WEBHOOK_URL = "http://localhost:5678/webhook/shipment-lookup"  # ← update path if needed

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

  html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0B0F1A;
    color: #E8EAF0;
  }

  /* Hide sidebar entirely */
  [data-testid="stSidebar"] { display: none; }
  [data-testid="collapsedControl"] { display: none; }

  /* Background grid */
  .stApp {
    background-color: #0B0F1A;
    background-image:
      linear-gradient(rgba(99,179,237,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(99,179,237,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
  }

  .hero-title {
    font-family: 'Space Mono', monospace;
    font-size: 2.4rem;
    font-weight: 700;
    letter-spacing: -1px;
    color: #FFFFFF;
    margin-bottom: 0;
  }
  .hero-sub {
    font-size: 0.95rem;
    color: #7A8BAA;
    margin-top: 4px;
    margin-bottom: 32px;
  }
  .accent { color: #63B3ED; }

  .divider {
    height: 1px;
    background: linear-gradient(90deg, #63B3ED33, transparent);
    margin: 24px 0;
  }

  .ai-box {
    background: linear-gradient(135deg, #0F1E35 0%, #0B1628 100%);
    border: 1px solid #2A4A6B;
    border-left: 3px solid #63B3ED;
    border-radius: 12px;
    padding: 28px 30px;
    margin-top: 8px;
    line-height: 1.85;
    font-size: 1rem;
    color: #CBD5E0;
  }
  .ai-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #1A3A5C;
    border: 1px solid #2A5A8A;
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 0.7rem;
    font-family: 'Space Mono', monospace;
    color: #63B3ED;
    margin-bottom: 16px;
  }
  .pulse {
    width: 7px; height: 7px;
    background: #63B3ED;
    border-radius: 50%;
    display: inline-block;
    animation: pulse 1.5s infinite;
  }
  @keyframes pulse {
    0%,100% { opacity: 1; }
    50%      { opacity: 0.3; }
  }

  div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(99,179,237,0.2) !important;
    border-radius: 8px !important;
    color: #E8EAF0 !important;
  }

  .stButton > button {
    background: linear-gradient(135deg, #1A4A7A, #0F3260) !important;
    color: #FFFFFF !important;
    border: 1px solid #2A6AAA !important;
    border-radius: 8px !important;
    padding: 10px 28px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.78rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    transition: all 0.2s ease !important;
    width: 100%;
  }
  .stButton > button:hover {
    background: linear-gradient(135deg, #1E5A90, #122E6E) !important;
    border-color: #4A9ADA !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 20px rgba(99,179,237,0.2) !important;
  }
</style>
""", unsafe_allow_html=True)

# ─── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-title">🚚 Ship<span class="accent">Sense</span> AI</div>
<div class="hero-sub">Intelligent Shipment Diagnostics — Powered by GenAI</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ─── Shipment IDs ──────────────────────────────────────────────────────────────
SHIPMENT_IDS = [
    690,933,261,445,722,129,489,165,164,364,469,158,337,634,577,907,870,982,351,328,
    242,421,6,384,286,892,558,481,155,771,945,719,493,998,968,738,912,782,140,702,
    284,199,228,908,594,542,586,636,581,336,504,346,135,822,95,597,340,905,250,400,
    877,97,12,353,856,1,390,446,32,420,708,227,595,211,650,45,201,564,138,57,128,33,
    936,762,838,215,818,780,40,366,678,703,180,214,408,902,763,168,723,438,162,246,
    105,308,172,775,333,548,665,305,938,714,251,330,69,969,974,526,510,444,503,109,
    823,147,625,695,983,82,397,599,306,536,20,515,332,127,958,42,977,460,659,197,540,
    178,202,632,25,990,913,371,514,707,473,847,815,928,210,793,872,298,941,731,500,
    142,787,749,304,30,477,52,73,691,786,68,630,357,455,947,589,863,668,206,835,315,
    553,861,279,75,895,866,792,191,59,748,693,955,538,169,924,579
]

# ─── Dropdown + Button ─────────────────────────────────────────────────────────
col1, col2 = st.columns([3, 1])
with col1:
    selected_id = st.selectbox(
        "Select Shipment ID",
        options=SHIPMENT_IDS,
        index=0,
        format_func=lambda x: f"SH_{x}"
    )
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_btn = st.button("🔍 Analyze")

# ─── Main Logic ────────────────────────────────────────────────────────────────
if analyze_btn:
    with st.spinner("Fetching shipment data and generating insights…"):
        try:
            response = requests.post(
                N8N_WEBHOOK_URL,
                json={"shipment_id": selected_id},
                timeout=30,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            result = response.json()
        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to n8n. Make sure your workflow is active.")
            st.stop()
        except requests.exceptions.Timeout:
            st.error("⏱️ Request timed out.")
            st.stop()
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()

    # ── Normalize response ─────────────────────────────────────────────────────
    def safe_parse(val):
        if isinstance(val, str):
            try:
                return json.loads(val)
            except Exception:
                return val
        return val

    result = safe_parse(result)
    if isinstance(result, list):
        result = result[0] if result else {}
    result = safe_parse(result)

    if not isinstance(result, dict):
        st.error(f"❌ Unexpected response from n8n: `{result}`")
        st.stop()

    # Extract AI text — checks all common key names
    ai_text = (
        result.get("text", "")
        or result.get("ai_response", "")
        or result.get("output", "")
        or result.get("message", "")
    )

    # ── Display AI Response ────────────────────────────────────────────────────
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if ai_text:
        st.markdown(f"""
        <div class="ai-box">
          <div class="ai-badge"><span class="pulse"></span> GenAI Reasoning</div><br>
          {ai_text}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ n8n responded but returned no text. Check your AI node output key.")
        with st.expander("🗂️ Raw n8n Response"):
            st.json(result)