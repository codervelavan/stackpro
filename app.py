"""
StackScope++ - Interactive Expression Evaluator with Streamlit UI
A beautiful, user-friendly interface for infix expression evaluation and visualization
"""

import streamlit as st
import subprocess
import json
import os
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import sys

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="StackScope++",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/codervelavan/StackScopePlusPlus',
        'Report a bug': "https://github.com/codervelavan/StackScopePlusPlus/issues",
    }
)

# Custom CSS for enhanced UI
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 16px;
        font-weight: 600;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# ==================== SESSION STATE ====================
if 'expression_history' not in st.session_state:
    st.session_state.expression_history = []
if 'results_cache' not in st.session_state:
    st.session_state.results_cache = {}

# ==================== SIDEBAR ====================
with st.sidebar:
    st.header("⚙️ Settings")
    
    st.markdown("---")
    st.subheader("📚 About StackScope++")
    st.markdown("""
    **StackScope++** is a powerful expression evaluator featuring:
    - ✅ Infix to Postfix conversion
    - ✅ Real-time evaluation with visual debugging
    - ✅ Support for floating-point numbers
    - ✅ Comprehensive error handling
    - 🚀 Built for scientific computing and DSA learning
    """)
    
    st.markdown("---")
    st.subheader("💡 Example Expressions")
    examples = {
        "Basic": [
            "3 + 4",
            "10 - 5",
            "3 * 4",
            "12 / 3"
        ],
        "Advanced": [
            "3 + 4 * 2",
            "(10 - 5) * 2",
            "100 / 5 + 2",
            "(3.5 * 2) + 1.5"
        ],
        "Complex": [
            "((10 + 5) * 2) - 3",
            "(100 / 4) * (3 + 2)",
            "2.5 * (4 + 1) / 2.5"
        ]
    }
    
    selected_category = st.selectbox("Quick Examples:", list(examples.keys()))
    if st.button("📋 Copy Example"):
        selected_example = st.selectbox(
            "Select an example:",
            examples[selected_category],
            key="example_select"
        )
        st.session_state.input_expression = selected_example
        st.rerun()

# ==================== HELPER FUNCTIONS ====================

def evaluate_expression_cpp(infix_expr):
    """Call C++ evaluator binary and return result"""
    try:
        # Check if compiled binary exists
        if not os.path.exists("./stackscope"):
            return None, "❌ C++ evaluator not compiled. Run: cmake build && make"
        
        # Run the C++ evaluator
        result = subprocess.run(
            ["./stackscope", infix_expr],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode != 0:
            return None, result.stderr.strip()
        
        return result.stdout, None
    except subprocess.TimeoutExpired:
        return None, "⏱️ Evaluation timed out"
    except Exception as e:
        return None, f"Error: {str(e)}"

def parse_cpp_output(output):
    """Parse C++ evaluator output"""
    try:
        lines = output.strip().split('\n')
        result_dict = {}
        
        for line in lines:
            if "Infix:" in line:
                result_dict['infix'] = line.split("Infix:")[1].strip()
            elif "Postfix:" in line:
                result_dict['postfix'] = line.split("Postfix:")[1].strip()
            elif "Result:" in line:
                result_dict['result'] = float(line.split("Result:")[1].strip())
        
        return result_dict
    except:
        return None

def load_visualization_logs():
    """Load JSON logs from visualization directory"""
    logs = {}
    viz_dir = Path("visualize")
    
    if viz_dir.exists():
        if (viz_dir / "graph.json").exists():
            with open(viz_dir / "graph.json") as f:
                logs['steps'] = json.load(f)
        if (viz_dir / "operators.json").exists():
            with open(viz_dir / "operators.json") as f:
                logs['operators'] = json.load(f)
        if (viz_dir / "operands.json").exists():
            with open(viz_dir / "operands.json") as f:
                logs['operands'] = json.load(f)
    
    return logs

def create_stack_visualization(steps):
    """Create an interactive visualization of stack operations"""
    if not steps:
        return None
    
    fig = go.Figure()
    
    for i, step in enumerate(steps):
        stack_values = step.get('stack', [])
        action = step.get('action', 'Unknown')
        
        fig.add_trace(go.Scatter(
            y=stack_values,
            mode='markers+lines',
            name=f"Step {i+1}: {action}",
            marker=dict(size=12, symbol='circle'),
            visible=(i == len(steps) - 1)  # Show only last step by default
        ))
    
    fig.update_layout(
        title="📊 Stack Evolution During Evaluation",
        xaxis_title="Element Index",
        yaxis_title="Stack Values",
        hovermode='closest',
        height=400,
        showlegend=True,
        template='plotly_white'
    )
    
    return fig

def create_operand_chart(operands):
    """Create a visualization of operands used"""
    if not operands:
        return None
    
    fig = px.bar(
        x=list(range(len(operands))),
        y=operands,
        labels={'x': 'Operand Index', 'y': 'Value'},
        title="📈 Operands Used in Expression",
        template='plotly_white'
    )
    fig.update_layout(height=300, showlegend=False)
    return fig

# ==================== MAIN CONTENT ====================

st.markdown("<h1 style='text-align: center; color: #667eea;'>🧮 StackScope++ Expression Evaluator</h1>", 
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Transform, evaluate, and visualize mathematical expressions</p>", 
            unsafe_allow_html=True)

st.markdown("---")

# ==================== INPUT SECTION ====================
st.subheader("📝 Enter Expression")

col1, col2 = st.columns([4, 1])

with col1:
    expression = st.text_input(
        "Expression (e.g., 3 + 4 * 2):",
        placeholder="Enter a mathematical expression using +, -, *, / and parentheses",
        key="input_expression",
        help="Supports floating-point numbers and nested parentheses"
    )

with col2:
    evaluate_btn = st.button("🚀 Evaluate", use_container_width=True)

st.markdown("---")

# ==================== EVALUATION LOGIC ====================
if evaluate_btn and expression:
    # Add to history
    if expression not in st.session_state.expression_history:
        st.session_state.expression_history.insert(0, expression)
    
    with st.spinner("⏳ Evaluating expression..."):
        output, error = evaluate_expression_cpp(expression)
        
        if error:
            st.error(f"**Evaluation Error:** {error}")
        elif output:
            parsed = parse_cpp_output(output)
            
            if parsed:
                # ==================== RESULTS TAB ====================
                tab1, tab2, tab3, tab4 = st.tabs(["📊 Results", "🔍 Detailed View", "📈 Visualization", "ℹ️ Info"])
                
                with tab1:
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric(
                            "**Infix Expression**",
                            parsed.get('infix', 'N/A'),
                            help="Original mathematical expression"
                        )
                    
                    with col2:
                        st.metric(
                            "**Postfix Notation**",
                            parsed.get('postfix', 'N/A'),
                            help="Reverse Polish Notation (RPN)"
                        )
                    
                    with col3:
                        result_value = parsed.get('result', 0)
                        st.metric(
                            "**Final Result**",
                            f"{result_value:.10g}",
                            help="Evaluated result"
                        )
                
                with tab2:
                    st.markdown("### Conversion Steps")
                    
                    infix = parsed.get('infix', '')
                    postfix = parsed.get('postfix', '')
                    
                    col_infix, col_arrow, col_postfix = st.columns([2, 1, 2])
                    
                    with col_infix:
                        st.info(f"**Infix:**\n\n```\n{infix}\n```")
                    
                    with col_arrow:
                        st.markdown("### ➜")
                        st.markdown("\n\n*Shunting Yard*\n*Algorithm*")
                    
                    with col_postfix:
                        st.success(f"**Postfix (RPN):**\n\n```\n{postfix}\n```")
                    
                    st.markdown("### Evaluation Details")
                    
                    logs = load_visualization_logs()
                    if logs.get('steps'):
                        steps_data = logs['steps']
                        
                        col_steps, col_operands, col_operators = st.columns(3)
                        
                        with col_steps:
                            st.metric("Total Steps", len(steps_data))
                        
                        with col_operands:
                            operand_count = len(logs.get('operands', []))
                            st.metric("Operands", operand_count)
                        
                        with col_operators:
                            operator_count = len(logs.get('operators', []))
                            st.metric("Operators", operator_count)
                        
                        st.markdown("#### Step-by-step Breakdown")
                        for i, step in enumerate(steps_data):
                            with st.expander(f"Step {step.get('step', i+1)}: {step.get('action', 'Unknown')}"):
                                stack_state = step.get('stack', [])
                                st.write(f"**Stack State:** {stack_state}")
                
                with tab3:
                    logs = load_visualization_logs()
                    
                    if logs.get('steps'):
                        st.markdown("### Stack Evolution")
                        stack_fig = create_stack_visualization(logs['steps'])
                        if stack_fig:
                            st.plotly_chart(stack_fig, use_container_width=True)
                    
                    if logs.get('operands'):
                        st.markdown("### Operand Distribution")
                        operand_fig = create_operand_chart(logs['operands'])
                        if operand_fig:
                            st.plotly_chart(operand_fig, use_container_width=True)
                
                with tab4:
                    st.markdown("""
                    ### 🤔 How StackScope++ Works
                    
                    **Step 1: Validation**
                    - Checks for balanced parentheses
                    - Validates operator placement
                    - Ensures proper syntax
                    
                    **Step 2: Conversion (Shunting Yard Algorithm)**
                    - Converts infix to postfix notation
                    - Respects operator precedence
                    - Handles parentheses correctly
                    
                    **Step 3: Evaluation**
                    - Uses stack data structure
                    - Processes postfix tokens
                    - Tracks all operations
                    
                    **Step 4: Logging & Visualization**
                    - Records each stack state
                    - Saves JSON logs
                    - Enables debugging
                    """)

st.markdown("---")

# ==================== HISTORY SECTION ====================
if st.session_state.expression_history:
    st.subheader("📚 Evaluation History")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_history = st.selectbox(
            "Previous expressions:",
            st.session_state.expression_history,
            key="history_select"
        )
    
    with col2:
        if st.button("Load", use_container_width=True):
            st.session_state.input_expression = selected_history
            st.rerun()

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #999; font-size: 12px;'>
    <p>🚀 <b>StackScope++</b> v1.0 | 
    <a href='https://github.com/codervelavan/StackScopePlusPlus'>GitHub</a> | 
    Built for CERN, Adobe & Microsoft Internship Preparation</p>
</div>
""", unsafe_allow_html=True)
