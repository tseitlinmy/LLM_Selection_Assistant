import streamlit as st

def button(label: str, isBold: bool = False) -> bool:
    weight = "700" if isBold else "400"

    # Custom CSS for the button
    st.markdown("""
    <style>
    /* Target the button container */
    div.stButton > button {
        background-color: #7E3D01 !important;
        color: #DDD9C3 !important;
        
        /* Text centering */
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        
        /* Margins - min and max horizontal */
        margin-top: 0px !important;
        margin-bottom: 0px !important;
        margin-left: clamp(10px, 5vw, 12px) !important;
        margin-right: clamp(10px, 5vw, 12px) !important;
        
        /* Additional styling */
        /* Border */
        border: 2px solid #DDD9C3 !important;
        border-radius: 8px !important;
        padding: 0 24px !important;
        width: calc(100% - clamp(20px, 10vw, 24px)) !important;
        line-height: 1.2 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        white-space: nowrap !important;
    }

    div.stButton button p {
        /* Typography */
        font-family: "Arial", sans-serif;
        font-size: 26px !important;
        font-weight: """ + weight + """ !important;
    }

    /* Hover effect */
    div.stButton > button:hover {
        background-color: #9A4D02 !important;
        transform: scale(1.02) !important;
        box-shadow: 0 4px 15px rgba(126, 61, 1, 0.4) !important;
    }

    /* Active/click effect */
    div.stButton > button:active {
        transform: scale(0.98) !important;
    }

    /* Focus state for accessibility */
    div.stButton > button:focus {
        outline: 2px solid #DDD9C3 !important;
        outline-offset: 2px !important;
    }

    /* Ensure container doesn't add extra margins */
    div.stButton {
        margin: 0 !important;
        padding: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Create the button
    return st.button(label, use_container_width=False)


if __name__ == "__main__":
    if button("Click Me"):
        st.write("Button clicked!")