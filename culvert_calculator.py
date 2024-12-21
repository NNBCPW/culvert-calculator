import streamlit as st

# Title of the app
st.title("BCPW Culvert Pipe Set Calculator")

# Blue and White DOS-style design
st.markdown("""
    <style>
        body {
            background-color: blue;
            color: white;
            font-family: 'Courier New', Courier, monospace;
        }
        .result {
            font-size: 20px;
            color: white;
            background-color: blue;
            border: 2px solid white;
            padding: 10px;
            display: inline-block;
        }
        .input-field {
            color: white;
            background-color: blue;
            border: 2px solid white;
            padding: 5px;
            margin-bottom: 10px;
            width: 100%;
        }
        h3, h1, h2, label {
            color: white;
        }
        .notes {
            font-size: 14px;
            color: white;
            background-color: blue;
            padding: 10px;
            border: 2px solid white;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Input fields
pipe_size = st.number_input("Pipe Size (inches)", min_value=1, value=15, step=1)
cover = st.number_input("Cover (inches)", min_value=1, value=9, step=1)
ratio = st.slider("Ratio (e.g., 4 for 4:1)", min_value=1, max_value=10, value=4, step=1)

# Validating Inputs
if pipe_size <= 0 or cover <= 0 or ratio <= 0:
    st.error("All inputs must be greater than 0.")
else:
    # Calculations
    set_length = (pipe_size + cover) * ratio / 12
    diameter_plus_12 = pipe_size + 12

    # Display Set Length result in DOS-style format
    st.markdown("<h3>Set Length (feet)</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='result'>Set Length: {round(set_length, 2)} feet</div>", unsafe_allow_html=True)

    # Display Diameter + 12 result in DOS-style format
    st.markdown("<h3>Diameter + 12\" (inches)</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='result'>Diameter + 12: {round(diameter_plus_12, 2)} inches</div>", unsafe_allow_html=True)

# Notes
st.markdown("### Notes")
st.markdown("""
    <div class='notes'>
        1. Add the pipe diameter (Pipe Size) to the cover.<br>
        2. Multiply the result by the ratio (e.g., 4:1 or 6:1).<br>
        3. Divide by 12 to convert inches to feet.<br>
        4. The result is the Set Length in feet.<br>
        5. The 'Diameter + 12"' is simply the entered Pipe Size plus 12 inches.
    </div>
""", unsafe_allow_html=True)

# Footer directly added at the end
st.markdown(
    """
    <div style="width: 100%; background-color: blue; color: white; text-align: center; padding: 10px; margin-top: 20px;">
        Created by: NN <br>
        <a href="mailto:Nicholas.nabholz@bexar.org?subject=Feedback%20on%20BCPW%20Elevation%20Calc&body=Hello,%0A%0AI%20would%20like%20to%20provide%20feedback%20on%20the%20app.%0A%0A" 
           style="color: white; text-decoration: none;">
            For support, please click this. Thanks!
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
