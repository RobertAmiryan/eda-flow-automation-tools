# eda-flow-automation-tools

A small, realistic collection of EDA automation examples that mimic parts of an ASIC physical-design flow.
The repository showcases:

- Flow orchestration (Python)
- Log parsing and reporting (Python)
- SDC generation using Tcl (gen_sdc.tcl)
- Dummy step runner to simulate EDA tool runs
- Configuration-driven design (YAML)

## Quick start

1. Create a Python virtual environment and install dependencies:
   ```
   python -m venv .venv
   source .venv/bin/activate   # on Windows use: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Run the example flow:
   ```
   python scripts/run_flow.py --config configs/example_flow.yaml
   ```
3. Generate an SDC from the example SDC config:
   ```
   tclsh scripts/gen_sdc.tcl configs/example_sdc_config.yaml > flow/step_5_sta/generated_example.sdc
   ```

## Repo layout
```
eda-flow-automation-tools/
├── README.md
├── LICENSE
├── requirements.txt
├── configs/
├── scripts/
├── flow/
└── logs/
```

## Contributing
Feel free to open issues or add small utilities that model additional EDA steps.
