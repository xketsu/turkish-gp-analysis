# Turkish Grand Prix Analysis (2005-2011, 2020-2021)

Analysis of Formula 1 Turkish Grand Prix results from Istanbul Park circuit.

## Overview

This project analyzes F1 Turkish GP data to find:
- Most successful drivers (wins & podiums)
- Most successful constructors (podiums)
- Race results visualization

## Data Source

Uses F1 data from https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020?resource=download

Required CSV files:
- `races.csv`
- `results.csv` 
- `drivers.csv`
- `constructors.csv`

## Installation

```bash
git Clone the repository
cd turkish_gp_list
pip install pandas matplotlib
```

## Usage

```bash
python main.py
```

## Features

- ✅ Driver wins analysis
- ✅ Driver podium statistics  
- ✅ Constructor podium analysis
- ✅ Data visualization with charts
- ✅ Clean formatted output

## Sample Output

```
=== DRIVERS - WINS ===
Massa: 3
Hamilton: 2
Räikkönen: 1

=== DRIVERS - PODIUMS ===
Alonso: 4
Massa: 3
Hamilton: 3
```

## Turkish GP History

- **2005-2011**: Regular races at Istanbul Park
- **2020-2021**: Return during COVID-19 calendar changes

## Requirements

- Python 3.6+
- pandas
- matplotlib

## License

MIT License
