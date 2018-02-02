# dstm-discord-integration
discord integration for dstm miner

## Installation instructions
1. Download this repository by your favourite means
2. Copy `integration.py` and `rpc.py` to your miner's folder (Optional, recommended)
3. Edit your miner batch file (`*.bat`) to include `--telemetry`
4. Start the miner
5. Open up a new `cmd` prompt and do `python /path/to/your/miner/integration.py`

## Requirements
- DSTM Miner v0.5.8+
- Python 3.6.4+
- `requests` module
