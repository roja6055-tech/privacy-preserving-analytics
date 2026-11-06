"""Educational CKKS encrypted aggregation demo using TenSEAL.

Run: python src/fhe_demo.py

This is a single-process learning example, not a production client/server
architecture. The secret key is present here so the demo can decrypt results.
"""
from __future__ import annotations

from typing import Sequence

try:
    import tenseal as ts
except ImportError as exc:
    raise SystemExit(
        "TenSEAL is not installed. Run: python -m pip install -r requirements.txt"
    ) from exc


SAMPLE_VALUES = [82_000.0, 91_500.0, 76_250.0, 104_000.0]


def encrypt_values(values: Sequence[float]):
    """Create a CKKS context and encrypt a vector of numeric values."""
    if not values:
        raise ValueError("At least one value is required.")

    context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60, 40, 40, 60],
    )
    context.global_scale = 2**40
    context.generate_galois_keys()
    encrypted_vector = ts.ckks_vector(context, list(map(float, values)))
    return context, encrypted_vector


def encrypted_sum_and_average(encrypted_vector, count: int):
    """Compute sum and average without decrypting the encrypted vector."""
    if count <= 0:
        raise ValueError("count must be positive.")
    encrypted_sum = encrypted_vector.sum()
    encrypted_average = encrypted_sum * (1.0 / count)
    return encrypted_sum, encrypted_average


def run_demo(values: Sequence[float] = SAMPLE_VALUES) -> dict[str, float]:
    _context, encrypted_values = encrypt_values(values)
    encrypted_sum, encrypted_average = encrypted_sum_and_average(
        encrypted_values, len(values)
    )
    return {
        "decrypted_sum": float(encrypted_sum.decrypt()[0]),
        "decrypted_average": float(encrypted_average.decrypt()[0]),
        "plaintext_sum": float(sum(values)),
        "plaintext_average": float(sum(values) / len(values)),
    }


def main() -> None:
    results = run_demo()
    print("FHE encrypted aggregation demo (fictional sample data)")
    print("-" * 55)
    print(f"Decrypted encrypted sum:     {results['decrypted_sum']:,.2f}")
    print(f"Decrypted encrypted average: {results['decrypted_average']:,.2f}")
    print(f"Plaintext sum for checking:  {results['plaintext_sum']:,.2f}")
    print(f"Plaintext average for check: {results['plaintext_average']:,.2f}")
    print("\nSmall differences are expected because CKKS uses approximate arithmetic.")


if __name__ == "__main__":
    main()
