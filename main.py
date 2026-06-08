import streamlit as st

# STORAGE INITIALIZATION: Prevent application state amnesia across runtime ticks
if "total_spent" not in st.session_state:
    st.session_state.total_spent = 0.0
if "expense_history" not in st.session_state:
    st.session_state.expense_history = []

# Application Layout Branding
st.title("🚀 DecodeLabs Processing Engine")
st.subheader("Project 2: The Expense Tracker (Web Dashboard)")
st.caption("Status: Active | Multi-Type Validation Layer Deployed")
st.divider()

# Live System Metric Board
st.metric(
    label="Consolidated Total Spent", 
    value=f"${st.session_state.total_spent:.2f}",
    delta=f"+{st.session_state.expense_history[-1]:.2f}" if st.session_state.expense_history else None
)

st.markdown("### 📥 Gatekeeper Intake Form")
with st.form(key="expense_gatekeeper_form", clear_on_submit=True):
    raw_expense_input = st.text_input(
        label="Input raw numeric feed amount:",
        placeholder="e.g., 4.50, 50, 120.75"
    )
    submit_expense = st.form_submit_button(label="Process Data Transmission")

# DEFENSIVE PROCESSING PATHWAY
if submit_expense:
    cleaned_input = raw_expense_input.strip()
    
    # DIGITAL POKA-YOKE PROTECTION LAYER
    try:
        # Transformation test
        parsed_expense = float(cleaned_input)
        
        if parsed_expense <= 0:
            st.warning("Operational Note: Logged values must be positive numbers greater than zero.")
        else:
            # Mathematical accumulation commitment
            st.session_state.total_spent += parsed_expense
            st.session_state.expense_history.append(parsed_expense)
            st.success(f"Validated transaction of ${parsed_expense:.2f} passed safely down the calculation stream!")
            # Force refresh to update the metrics panel view instantly
            st.rerun()
            
    except ValueError:
        # Prevent input failure from taking down the interface loop
        st.error("💥 **Digital Barrier Triggered:** Garbage Input Detected! Input string could not be safely parsed to a mathematical primitive float.")

st.divider()

# DISPLAY REFINED VIEW BLOCK
st.markdown("### 📊 Active Audit Trail Stream")
if not st.session_state.expense_history:
    st.info("No numerical records processed during this active runtime sequence.")
else:
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Sequence Stream Log:**")
        for idx, item in enumerate(st.session_state.expense_history, 1):
            st.text(f"Transaction Link #{idx:03d} -> Added +${item:.2f}")
    with col2:
        # Quick Reset option to flush active values back to base state
        st.write("**Engine Controls:**")
        if st.button("Flush State Memory"):
            st.session_state.total_spent = 0.0
            st.session_state.expense_history = []
            st.success("Volatile storage records wiped clean.")
            st.rerun()