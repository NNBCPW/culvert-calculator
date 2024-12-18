import streamlit as st
import datetime

# Title of the app
st.title("BCPW Culvert Pipe Set Calculator")

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

    # Display Set Length result with larger font size
    st.markdown("<h3>Set Length (feet)</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:40px; color:red;'>{round(set_length, 2)}</p>", unsafe_allow_html=True)

    # Display Diameter + 12 result with larger font size
    st.markdown("<h3>Diameter + 12\" (inches)</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:40px; color:red;'>{round(diameter_plus_12, 2)}</p>", unsafe_allow_html=True)

# Notes
st.markdown("### Notes")
st.write("""
1. Add the pipe diameter (Pipe Size) to the cover.
2. Multiply the result by the ratio (e.g., 4:1 or 6:1).
3. Divide by 12 to convert inches to feet.
4. The result is the Set Length in feet.
5. The 'Diameter + 12"' is simply the entered Pipe Size plus 12 inches.
""")

# Footer directly added at the end
st.markdown(
    """
    <div style="width: 100%; background-color: black; color: white; text-align: center; padding: 10px; margin-top: 20px;">
        Created by: NN <br>
        <a href="mailto:Nicholas.nabholz@bexar.org?subject=Feedback%20on%20BCPW%20Elevation%20Calc&body=Hello,%0A%0AI%20would%20like%20to%20provide%20feedback%20on%20the%20app.%0A%0A" 
           style="color: white; text-decoration: none;">
            For support, please click this. Thanks!
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
