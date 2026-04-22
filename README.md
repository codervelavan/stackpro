# StackScope++

🧠 A High-Performance C++ Stack-Based Expression Evaluator with Web UI, AI Integration, and Visual Debugging

[![Build and Test](https://github.com/codervelavan/StackScopePlusPlus/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/codervelavan/StackScopePlusPlus/actions)
[![Code Quality](https://github.com/codervelavan/StackScopePlusPlus/actions/workflows/code-quality.yml/badge.svg)](https://github.com/codervelavan/StackScopePlusPlus/actions)

## 🚀 Overview

StackScope++ is a production-ready expression evaluator featuring:
- **Lightning-fast** infix-to-postfix conversion using the Shunting Yard Algorithm
- **Beautiful web UI** with Streamlit for interactive evaluation
- **Comprehensive error handling** with detailed feedback
- **Full floating-point support** for scientific computing
- **Real-time visualization** of stack operations
- **AI integration** to convert natural language to expressions
- **Extensive unit tests** with Google Test framework
- **CI/CD pipeline** with GitHub Actions

> 📌 Built as part of preparation for CERN, Adobe Hackathons, and Microsoft internship drives

---

## ✨ Key Features

### Core Functionality
- ✅ **Infix to Postfix Conversion**: Using proven Shunting Yard algorithm
- ✅ **Stack-Based Evaluation**: Full support for expressions with +, -, *, /
- ✅ **Operator Precedence**: Correct handling of * and / before + and -
- ✅ **Parentheses Support**: Unlimited nesting and grouping
- ✅ **Floating-Point Numbers**: 64-bit double precision
- ✅ **Input Validation**: Comprehensive syntax checking
- ✅ **Error Handling**: Detailed error messages for debugging

### User Interface
- 🎨 **Modern Web UI**: Built with Streamlit
- 📊 **Interactive Visualizations**: Stack evolution charts with Plotly
- 📚 **Expression History**: Track previous evaluations
- 💡 **Quick Examples**: Pre-loaded common expressions
- 📖 **Inline Help**: Documentation and tips throughout

### Development Tools
- 🧪 **40+ Unit Tests**: Comprehensive test coverage
- 🏗️ **CMake Build System**: Professional build configuration
- 🔍 **CI/CD Pipeline**: Automated testing on multiple platforms
- 📋 **API Documentation**: Complete function reference
- 📚 **Examples**: Basic and advanced usage patterns

---

## 📊 Quick Comparison

| Feature | StackScope++ | Calculator | Wolfram Alpha |
|---------|-------------|-----------|----------------|
| **Infix Parsing** | ✅ | ✅ | ✅ |
| **Visual Debugging** | ✅ | ❌ | ⚠️ |
| **Web Interface** | ✅ | ❌ | ✅ |
| **Open Source** | ✅ | ⚠️ | ❌ |
| **Educational** | ✅ | ⚠️ | ❌ |
| **Stack Visualization** | ✅ | ❌ | ❌ |
| **AI Integration** | ✅ | ❌ | ✅ |

---

## 🎯 Quick Start

### 1️⃣ Installation (5 minutes)

```bash
# Clone repository
git clone https://github.com/codervelavan/StackScopePlusPlus.git
cd StackScopePlusPlus

# Build C++ project
mkdir build && cd build
cmake ..
cmake --build . --config Release
cd ..

# Install Python dependencies
pip install -r requirements.txt
```

### 2️⃣ Run CLI

```bash
# Interactive mode
./stackscope
# Enter: 3 + 4 * 2

# Direct evaluation
./stackscope "3 + 4 * 2"
# Output: 11
```

### 3️⃣ Run Web UI

```bash
streamlit run app.py
# Opens http://localhost:8501
```

---

## 📸 Features in Action

### Example 1: Simple Expression
```bash
$ ./stackscope "3 + 4 * 2"

============================================
📊 Expression Evaluation Results
============================================
✓ Infix:    3 + 4 * 2
✓ Postfix:  3 4 2 * + 
✓ Result:   11

📈 Evaluation Steps: 4
🔢 Operands Used: 3
🔧 Operators Used: 2
============================================
```

### Example 2: Complex Expression
```bash
$ ./stackscope "(10 - 5) * (3 + 2)"

✓ Infix:    (10 - 5) * (3 + 2)
✓ Postfix:  10 5 - 3 2 + * 
✓ Result:   25
```

### Example 3: Floating-Point
```bash
$ ./stackscope "2.5 * 4 + 1.5"

✓ Infix:    2.5 * 4 + 1.5
✓ Postfix:  2.5 4 * 1.5 + 
✓ Result:   11.5
```

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | C++17, CMake, OpenMP |
| **Frontend** | Streamlit, Plotly |
| **AI** | Google Gemini API |
| **Testing** | Google Test (GTest) |
| **CI/CD** | GitHub Actions |
| **Visualization** | ROOT (optional), JSON logging |

---

## 📂 Project Structure

```
StackScopePlusPlus/
├── CMakeLists.txt              ⚙️  Build configuration
├── requirements.txt            📦 Python dependencies
├── app.py                       🎨 Streamlit web UI
├── .env.example                 🔐 Configuration template
│
├── 📁 include/
│   └── evaluator.h             📜 API headers
│
├── 📁 src/
│   ├── main.cpp                🚀 CLI entry point
│   └── evaluator.cpp           ⚡ Core implementation
│
├── 📁 tests/
│   └── test_evaluator.cpp      ✅ 40+ unit tests
│
├── 📁 docs/
│   ├── API_REFERENCE.md        📖 Complete API docs
│   └── INSTALLATION.md         💻 Setup guide
│
├── 📁 examples/
│   ├── basic_usage.py          🏠 Beginner examples
│   ├── advanced_usage.py       🚀 Advanced patterns
│   └── README.md               📚 Examples guide
│
├── 📁 agent/
│   ├── agent.py                🤖 Gemini AI agent
│   ├── runner.py               🏃 Runner script
│   └── translator.py           🔄 Expression translator
│
└── 📁 .github/
    └── workflows/
        ├── build-and-test.yml  ✅ Build pipeline
        └── code-quality.yml    🔍 Quality checks
```

---

## 🚀 Usage Examples

### Command Line
```bash
# Basic operations
./stackscope "3 + 4"           # → 7
./stackscope "10 - 5"          # → 5
./stackscope "3 * 4"           # → 12
./stackscope "12 / 3"          # → 4

# Complex expressions
./stackscope "3 + 4 * 2"       # → 11
./stackscope "(10 - 5) * 2"    # → 10
./stackscope "2.5 * 4 + 1.5"   # → 11.5

# Error handling
./stackscope "5 / 0"           # Error: Division by zero
./stackscope "(3 + 4"          # Error: Unmatched parenthesis
```

### Python API
```python
from evaluator import infixToPostfix, evaluatePostfix

# Convert to postfix
postfix = infixToPostfix("3 + 4 * 2")  # "3 4 2 * + "

# Evaluate
result = evaluatePostfix(postfix)
if result.success:
    print(f"Result: {result.value}")  # 11
    print(f"Steps: {result.evaluation_log}")
```

### Web Interface
1. Open `http://localhost:8501`
2. Enter expression: `3 + 4 * 2`
3. Click "🚀 Evaluate"
4. View results, postfix notation, and visualizations
5. Explore step-by-step stack evolution

---

## 🧪 Testing

### Run All Tests
```bash
cd build
ctest --verbose

# Or run specific tests
./stackscope_tests --gtest_filter=InfixToPostfixTest
```

### Test Coverage
- **Basic Arithmetic**: +, -, *, /
- **Operator Precedence**: * and / before + and -
- **Parentheses**: Single, nested, complex grouping
- **Floating-Point**: Precision, rounding, edge cases
- **Error Handling**: Division by zero, invalid syntax
- **Validation**: Expression syntax checking
- **Edge Cases**: Empty input, large numbers, very small numbers

---

## 📊 Performance

| Operation | Complexity | Speed |
|-----------|-----------|-------|
| `infixToPostfix()` | O(n) | <1ms for typical expressions |
| `evaluatePostfix()` | O(n) | <1ms for typical expressions |
| `isValidExpression()` | O(n) | <0.1ms |

---

## 🔐 Security Features

- ✅ Input validation and sanitization
- ✅ Bounds checking for array operations
- ✅ Error handling without exceptions
- ✅ Memory safety checks in CI/CD
- ✅ Dependency vulnerability scanning
- ✅ Code quality analysis with SonarCloud

---

## 📖 Documentation

| Document | Purpose |
|----------|---------|
| [API Reference](docs/API_REFERENCE.md) | Complete function documentation |
| [Installation Guide](docs/INSTALLATION.md) | Setup and configuration |
| [Examples](examples/README.md) | Usage examples and patterns |
| [Web UI Guide](#-web-ui-streamlit) | Interactive interface features |

---

## 🤝 Contributing

Contributions are welcome! Areas for contribution:

- 🆕 New features (more operators, functions)
- 🐛 Bug fixes and improvements
- 📝 Documentation enhancements
- 🧪 Additional test cases
- 🎨 UI/UX improvements
- 🌍 Localization

---

## 📝 License

[MIT License](LICENSE) - Feel free to use in your projects!

---

## 🙏 Acknowledgments

- **Dijkstra's Shunting Yard Algorithm** for expression parsing
- **Google Test Framework** for testing infrastructure
- **Streamlit** for the interactive web UI
- **Plotly** for data visualization
- **CMake** for build system

---

## 📞 Support & Contact

- 🐛 **Report Bugs**: [GitHub Issues](https://github.com/codervelavan/StackScopePlusPlus/issues)
- 💡 **Request Features**: [GitHub Discussions](https://github.com/codervelavan/StackScopePlusPlus/discussions)
- 📧 **Email**: [Your Contact]
- 🌐 **Website**: [Your Website]

---

## 📈 Roadmap

- [ ] Support for more operators (^, %, sin, cos, etc.)
- [ ] Scientific calculator mode
- [ ] Expression history export
- [ ] Desktop application (Qt/wxWidgets)
- [ ] Mobile support
- [ ] Advanced visualizations with ROOT
- [ ] Performance benchmarking suite
- [ ] Docker containerization
- [ ] Multi-language UI
- [ ] Cloud deployment

---

<div align="center">

**[⬆ Back to Top](#stackscope)**

Built with ❤️ for scientific computing and educational purposes

</div>
g++ main.cpp evaluator.cpp -o evaluate
./evaluate "3 + 4 * (2 - 1)"
# Output: 7
