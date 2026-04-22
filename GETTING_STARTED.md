# Getting Started with StackScope++

Welcome! This guide will get you up and running in **5 minutes**.

---

## 🚀 Super Quick Start (5 minutes)

### Step 1: Clone & Build (2 min)
```bash
git clone https://github.com/codervelavan/StackScopePlusPlus.git
cd StackScopePlusPlus
mkdir build && cd build
cmake ..
cmake --build . --config Release
cd ..
```

### Step 2: Try the CLI (1 min)
```bash
./stackscope "3 + 4 * 2"
# Output: 11
```

### Step 3: Try the Web UI (2 min)
```bash
pip install -r requirements.txt
streamlit run app.py
# Opens http://localhost:8501
```

---

## 📚 Next Steps

### 👤 For Users
1. **Explore Examples**
   ```bash
   python examples/basic_usage.py
   ```

2. **Try the Web Interface**
   - Open http://localhost:8501
   - Enter: `(10 - 5) * (3 + 2)`
   - Click "🚀 Evaluate"

3. **Read the Docs**
   - [Installation Guide](docs/INSTALLATION.md)
   - [API Reference](docs/API_REFERENCE.md)

### 👨‍💻 For Developers
1. **Review the Code**
   ```bash
   cat include/evaluator.h      # API headers
   cat src/evaluator.cpp        # Implementation (~700 lines)
   cat src/main.cpp             # CLI entry point
   ```

2. **Run Tests**
   ```bash
   cd build
   ctest --verbose
   ```

3. **Explore Examples**
   ```bash
   python examples/basic_usage.py
   python examples/advanced_usage.py
   ```

---

## 🧮 Common Expressions

### Basic Operations
```bash
./stackscope "3 + 4"           # 7
./stackscope "10 - 5"          # 5
./stackscope "3 * 4"           # 12
./stackscope "12 / 3"          # 4
```

### Operator Precedence
```bash
./stackscope "3 + 4 * 2"       # 11 (not 14!)
./stackscope "10 / 5 * 2"      # 4
./stackscope "2 + 3 * 4 - 1"   # 13
```

### With Parentheses
```bash
./stackscope "(3 + 4) * 2"     # 14
./stackscope "((5 + 3) * 2)"   # 16
./stackscope "2 * (3 + 4 * 5)" # 46
```

### Floating-Point
```bash
./stackscope "3.5 + 2.5"       # 6
./stackscope "10 / 3"          # 3.333...
./stackscope "2.5 * 4"         # 10
```

---

## 🎓 Understanding the Process

### What Happens When You Evaluate "3 + 4 * 2"?

```
Input: 3 + 4 * 2

Step 1: Validate
✓ Balanced parentheses
✓ Valid operators
✓ Valid operands

Step 2: Convert to Postfix (Shunting Yard Algorithm)
3 + 4 * 2  →  3 4 2 * +

Step 3: Evaluate using Stack
[3]
[3, 4]
[3, 4, 2]
[3, 8]        ← 4 * 2 = 8
[11]          ← 3 + 8 = 11

Result: 11
```

---

## 🌐 Web UI Features

### Main Interface
1. **Input Box**: Enter your expression
2. **Quick Examples**: Pre-loaded examples to try
3. **Evaluate Button**: Process the expression

### Results Tabs

**📊 Results Tab**
- Infix expression (original)
- Postfix notation (RPN)
- Final result

**🔍 Detailed View**
- Step-by-step conversion process
- Stack state at each step
- Operator and operand counts

**📈 Visualization Tab**
- Interactive stack evolution chart
- Operand distribution chart
- Hover over data for details

**ℹ️ Info Tab**
- How StackScope++ works
- Algorithm explanation
- Visual flowchart

### Sidebar Features
- Settings and configuration
- About the project
- Quick example selector
- Copy-to-input functionality

---

## 🧪 Testing

### Run All Tests
```bash
cd build
ctest --verbose
```

### Run Specific Tests
```bash
./stackscope_tests --gtest_filter=InfixToPostfixTest
./stackscope_tests --gtest_filter=ErrorHandling
./stackscope_tests --gtest_filter=EdgeCase
```

### Test Categories
- Basic arithmetic (+, -, *, /)
- Operator precedence
- Parentheses handling
- Floating-point operations
- Error scenarios
- Edge cases

---

## 🐛 Troubleshooting

### Issue: Binary not found
```bash
# Make sure build completed successfully
cd build && cmake --build . && cd ..
```

### Issue: "Permission denied"
```bash
chmod +x stackscope
```

### Issue: Python module errors
```bash
pip install -r requirements.txt
```

### Issue: Streamlit port in use
```bash
streamlit run app.py --server.port 8502
```

### Issue: Cannot import json library
```bash
# Make sure visualize/ directory exists
mkdir -p visualize
```

---

## 📖 Documentation Map

| Want to... | Read This |
|-----------|-----------|
| Install and setup | [INSTALLATION.md](docs/INSTALLATION.md) |
| Use the API | [API_REFERENCE.md](docs/API_REFERENCE.md) |
| Learn by example | [examples/README.md](examples/README.md) |
| See what's new | [IMPROVEMENTS.md](IMPROVEMENTS.md) |
| Understand features | [README.md](README.md) |

---

## 💡 Tips & Tricks

### Command Line Tips
```bash
# Evaluate from another script
result=$(./stackscope "3 + 4")
echo "Result: $result"

# Test multiple expressions
for expr in "3+4" "10-5" "3*4" "12/3"; do
    echo "Testing: $expr"
    ./stackscope "$expr"
done
```

### Web UI Tips
- **Save expressions**: Use browser history
- **Share results**: Take screenshots or copy from results
- **Batch testing**: Run multiple tests by re-entering

### Python Integration
```python
import subprocess

def evaluate(expr):
    result = subprocess.run(
        ["./stackscope", expr],
        capture_output=True,
        text=True
    )
    return result.stdout
```

---

## 🚀 Next Learning Steps

### Beginner
1. ✅ Run basic operations
2. ✅ Try web UI
3. ✅ Read examples/basic_usage.py

### Intermediate
1. ✅ Run examples/advanced_usage.py
2. ✅ Read API documentation
3. ✅ Understand error handling

### Advanced
1. ✅ Review source code
2. ✅ Run test suite
3. ✅ Study the Shunting Yard algorithm
4. ✅ Implement new features

---

## 🎯 Feature Overview

### Current Features ✅
- Infix to Postfix conversion
- Stack-based evaluation
- Floating-point arithmetic
- Comprehensive error handling
- Input validation
- Web UI with visualizations
- 40+ unit tests
- Professional documentation

### Coming Soon 🚧
- Support for more operators (^, %, sin, cos, etc.)
- Variable support
- Function definitions
- Mobile interface
- Desktop application

---

## 🤝 Getting Help

- 📖 **Read Documentation**: [docs/](docs/)
- 💡 **Check Examples**: [examples/](examples/)
- 🐛 **Report Bugs**: [GitHub Issues](https://github.com/codervelavan/StackScopePlusPlus/issues)
- 💬 **Ask Questions**: [GitHub Discussions](https://github.com/codervelavan/StackScopePlusPlus/discussions)

---

## ✨ What Makes StackScope++ Special

1. **Beautiful UI**: Streamlit web interface with visualizations
2. **Educational**: Perfect for learning DSA concepts
3. **Reliable**: Comprehensive error handling and 40+ tests
4. **Well-Documented**: API reference, guides, and examples
5. **Professional**: CMake build system and CI/CD pipeline
6. **Production-Ready**: Used in real applications

---

## 🎉 You're All Set!

You now have:
✅ StackScope++ installed
✅ CLI working
✅ Web UI running
✅ Understanding of the project
✅ Pathways for learning

**Next**: Pick an interesting expression and try it!

```bash
./stackscope "((10 + 5) * 2) - 3"
```

---

**Happy Evaluating! 🧮**

For detailed information, see the [README](README.md).
