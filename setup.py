#!/usr/bin/env python3
"""
Setup and Environment Check Script for Agentic RAG with Gemini Flash Thinking

This script helps users set up the environment and verify all dependencies
are properly installed and configured.
"""

import sys
import subprocess
import importlib
import os
from typing import List, Tuple

def print_header(text: str):
    """Print a formatted header."""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}")

def print_step(step: int, text: str):
    """Print a formatted step."""
    print(f"\n{step}. {text}")
    print("-" * 40)

def check_python_version() -> bool:
    """Check if Python version is compatible."""
    version = sys.version_info
    required_major, required_minor = 3, 8
    
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= required_major and version.minor >= required_minor:
        print("✅ Python version is compatible")
        return True
    else:
        print(f"❌ Python {required_major}.{required_minor}+ is required")
        return False

def install_package(package: str) -> bool:
    """Install a package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def check_and_install_dependencies() -> List[Tuple[str, bool]]:
    """Check and install required dependencies."""
    required_packages = [
        ("streamlit", "streamlit"),
        ("google-generativeai", "google.generativeai"),
        ("langchain", "langchain"),
        ("langchain-community", "langchain_community"),
        ("langchain-core", "langchain_core"),
        ("langchain-qdrant", "langchain_qdrant"),
        ("qdrant-client", "qdrant_client"),
        ("pypdf", "pypdf"),
        ("beautifulsoup4", "bs4"),
        ("agno", "agno"),
        ("requests", "requests"),
        ("numpy", "numpy"),
        ("python-dotenv", "dotenv"),
    ]
    
    results = []
    
    for package_name, import_name in required_packages:
        try:
            importlib.import_module(import_name)
            print(f"✅ {package_name} is installed")
            results.append((package_name, True))
        except ImportError:
            print(f"❌ {package_name} is not installed. Installing...")
            if install_package(package_name):
                print(f"✅ Successfully installed {package_name}")
                results.append((package_name, True))
            else:
                print(f"❌ Failed to install {package_name}")
                results.append((package_name, False))
    
    return results

def check_environment_variables():
    """Check if environment variables are set."""
    env_vars = [
        ("GOOGLE_API_KEY", "Google AI API Key"),
        ("QDRANT_API_KEY", "Qdrant API Key"),
        ("QDRANT_URL", "Qdrant URL"),
        ("EXA_API_KEY", "Exa AI API Key (Optional)"),
    ]
    
    for var_name, description in env_vars:
        value = os.getenv(var_name)
        if value:
            masked_value = value[:8] + "..." if len(value) > 8 else value
            print(f"✅ {description}: {masked_value}")
        else:
            optional = "(Optional)" in description
            status = "⚠️" if optional else "❌"
            print(f"{status} {description}: Not set")

def test_streamlit():
    """Test if Streamlit can be run."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "streamlit", "version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print("✅ Streamlit is working correctly")
            print(f"   Version: {result.stdout.strip()}")
            return True
        else:
            print("❌ Streamlit test failed")
            return False
    except Exception as e:
        print(f"❌ Streamlit test error: {e}")
        return False

def create_env_template():
    """Create a .env template file."""
    env_template = """# API Keys for Agentic RAG Application
# Copy this file to .env and fill in your actual API keys

# Required: Google AI API Key
# Get from: https://aistudio.google.com/
GOOGLE_API_KEY=your_google_api_key_here

# Required: Qdrant Vector Database
# Get from: https://cloud.qdrant.io/
QDRANT_API_KEY=your_qdrant_api_key_here
QDRANT_URL=https://your-cluster.cloud.qdrant.io:6333

# Optional: Exa AI for web search
# Get from: https://exa.ai/
EXA_API_KEY=your_exa_api_key_here
"""
    
    try:
        with open(".env.template", "w") as f:
            f.write(env_template)
        print("✅ Created .env.template file")
        print("   Copy this to .env and fill in your API keys")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env.template: {e}")
        return False

def main():
    """Main setup function."""
    print_header("Agentic RAG Setup and Environment Check")
    
    # Step 1: Check Python version
    print_step(1, "Checking Python Version")
    if not check_python_version():
        print("\n❌ Setup failed: Incompatible Python version")
        return False
    
    # Step 2: Install dependencies
    print_step(2, "Checking and Installing Dependencies")
    results = check_and_install_dependencies()
    
    failed_packages = [pkg for pkg, success in results if not success]
    if failed_packages:
        print(f"\n❌ Failed to install packages: {', '.join(failed_packages)}")
        print("Please install them manually using:")
        for pkg in failed_packages:
            print(f"   pip install {pkg}")
    else:
        print("\n✅ All dependencies are installed")
    
    # Step 3: Test Streamlit
    print_step(3, "Testing Streamlit")
    test_streamlit()
    
    # Step 4: Check environment variables
    print_step(4, "Checking Environment Variables")
    check_environment_variables()
    
    # Step 5: Create environment template
    print_step(5, "Creating Environment Template")
    create_env_template()
    
    # Final instructions
    print_header("Setup Complete!")
    print("\nNext steps:")
    print("1. Copy .env.template to .env")
    print("2. Fill in your API keys in the .env file")
    print("3. See API_KEYS_SETUP.md for detailed instructions on getting API keys")
    print("4. Run the application with: streamlit run main.py")
    print("\nFor help with API keys, see: API_KEYS_SETUP.md")
    
    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Setup failed with error: {e}")
        sys.exit(1)
