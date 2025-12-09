# === UI STYLE - SOFT OCEAN THEME ===
import streamlit as st


def inject_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        * {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* Ultra soft pastel gradient background */
        .stApp {
            background: linear-gradient(135deg, #e0f2fe 0%, #f0f9ff 25%, #fffbeb 60%, #fef3c7 100%) !important;
        }
        
        .main .block-container {
            background: transparent !important;
        }

        /* Banner */
        .header-image {
            width: 100%;
            max-height: 380px;
            border-radius: 20px;
            object-fit: cover;
            margin-bottom: 32px;
            box-shadow: 0 10px 30px rgba(186, 230, 253, 0.4);
            border: 4px solid rgba(255, 255, 255, 0.95);
        }

        /* Title with softer colors */
        .main-title {
            font-size: 48px;
            font-weight: 800;
            text-align: center;
            background: linear-gradient(135deg, #0891b2, #06b6d4, #f59e0b, #fbbf24);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: 15px;
            margin-bottom: 10px;
            letter-spacing: -0.5px;
            filter: drop-shadow(0 2px 4px rgba(255,255,255,0.5));
        }

        .subtitle {
            font-size: 18px;
            text-align: center;
            color: #0369a1;
            font-weight: 600;
            margin-bottom: 32px;
            text-shadow: 0 2px 4px rgba(255,255,255,0.8);
        }

        /* Divider */
        .divider {
            height: 3px;
            background: linear-gradient(to right, transparent, #bae6fd, #e0f2fe, #fde68a, transparent);
            margin: 40px 0 28px;
            box-shadow: 0 2px 8px rgba(186, 230, 253, 0.15);
        }

        /* Result Card - Very Soft theme */
        .result-card {
            padding: 24px;
            border-radius: 18px;
            background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 50%, #fffbeb 100%);
            border: 3px solid #e0f2fe;
            margin-bottom: 28px;
            transition: all 0.3s ease;
            box-shadow: 0 6px 20px rgba(186, 230, 253, 0.15);
        }

        .result-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 16px 36px rgba(186, 230, 253, 0.25), 0 8px 16px rgba(253, 230, 138, 0.15);
            border-color: #bae6fd;
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 50%, #fef3c7 100%);
        }

        /* Thumbnail with soft pastel vibe */
        .thumb {
            width: 100%;
            height: 220px;
            border-radius: 14px;
            object-fit: cover;
            background: linear-gradient(135deg, #e0f2fe, #bae6fd, #fef3c7);
            border: 3px solid #e0f2fe;
            box-shadow: 0 4px 12px rgba(186, 230, 253, 0.2);
        }

        /* Snippet text */
        .snippet {
            color: #0369a1;
            line-height: 1.8;
            font-size: 15px;
            margin-bottom: 14px;
            font-weight: 400;
        }

        /* Mark/highlight */
        mark {
            background: linear-gradient(135deg, #fef9c3, #fef3c7);
            color: #ca8a04;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 600;
        }

        /* Streamlit input styling */
        .stTextInput input {
            border-radius: 12px !important;
            border: 2px solid #e0f2fe !important;
            background: rgba(255, 255, 255, 0.98) !important;
            font-size: 16px !important;
            padding: 12px 16px !important;
            transition: all 0.3s ease !important;
        }

        .stTextInput input:focus {
            border-color: #bae6fd !important;
            box-shadow: 0 0 0 3px rgba(186, 230, 253, 0.2) !important;
        }

        /* Slider styling */
        .stSlider {
            padding: 10px 0 !important;
        }

        /* Sidebar ultra soft pastel theme */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #e0f2fe 0%, #f0f9ff 50%, #fffbeb 100%) !important;
        }

        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] div {
            color: #0369a1 !important;
            text-shadow: 0 1px 2px rgba(255,255,255,0.8);
        }

    </style>
    """, unsafe_allow_html=True)