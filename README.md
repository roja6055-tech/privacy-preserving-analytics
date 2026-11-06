# Privacy-Preserving Analytics

A beginner-friendly learning project exploring fully homomorphic encryption (FHE) through encrypted numeric aggregation.

> **Status:** Educational prototype / hackathon starter. Not production-ready cryptography.

## What it demonstrates
- Plaintext versus ciphertext.
- Encrypting numeric values with CKKS using TenSEAL.
- Computing a sum and average on encrypted values.
- Decrypting results for comparison with ordinary arithmetic.

## Quick start

Python 3.10–3.11 is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/fhe_demo.py
```

## How it works
1. Create a CKKS context and keys.
2. Encrypt fictional numeric values.
3. Compute encrypted sum and average.
4. Decrypt results and compare with plaintext calculations.

CKKS supports approximate arithmetic, so small floating-point differences are expected. This first demo keeps key creation, computation, and decryption in one process for clarity; it is not a secure client/server architecture.

## Structure
- `src/fhe_demo.py` — encrypted aggregation demo.
- `tests/test_plaintext_baseline.py` — arithmetic baseline tests.
- `requirements.txt` — Python dependency.

## Security notes
This is a learning example, not a security audit. FHE does not automatically hide traffic patterns, timing, outputs, or metadata. Production use requires a threat model, carefully selected parameters, key lifecycle, authorization, and operational controls. Use synthetic data only; never add employer, customer, health, or personal data.

## Roadmap
- Separate key-owning client and untrusted compute service.
- Add an API for ciphertext input and encrypted results.
- Benchmark encrypted operations against plaintext calculations.
- Explore parameter choices and precision/performance trade-offs.
- Build a construction analytics example using synthetic data only.

## Learning resources
- [TenSEAL](https://github.com/OpenMined/TenSEAL)
- [OpenFHE documentation](https://openfhe-development.readthedocs.io/en/latest/)
- [Microsoft SEAL](https://github.com/microsoft/SEAL)
