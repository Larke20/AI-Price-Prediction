#!/bin/bash

# Navigate to the project directory
cd /Users/landonclarke/VS_Code/AI-Price-Prediction

# Create Python environment
mkdir -p env
conda create --prefix ./env python=3.10 -y
source activate ./env
conda install tensorflow pandas numpy plotly -y

# Verify pip path
pip_path=$(which pip)
expected_path="/Users/landonclarke/VS_Code/AI-Price-Prediction/env/bin/pip"

if [ "$pip_path" != "$expected_path" ]; then
    export PATH="/Users/landonclarke/VS_Code/AI-Price-Prediction/env/bin:$PATH"
fi

# Install dependencies using pip
pip install alpaca_trade_api nltk yfinance

# Install qt
brew install qt

# Create a data directory if it doesn't exist
mkdir -p /Users/landonclarke/VS_Code/AI-Price-Prediction/data

# Run project.cpp
mkdir -p build
cd build
cmake .. && make
./project
