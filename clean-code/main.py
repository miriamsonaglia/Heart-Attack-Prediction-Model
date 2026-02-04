import pandas as pd
import numpy as np
from config import DATA_CONFIG
import benchmarking as bench
from cleaning import clean

if __name__ == "__main__":
    all_dfs = []

    for country, conf in DATA_CONFIG.items():
        # 1. Caricamento e Baseline (per confronto onesto)
        raw = pd.read_csv(conf["file"])
        baseline = raw.drop(columns=conf["drop"], errors='ignore').rename(columns=conf["rename"])
        baseline['State'] = country
        if 'PatientID' not in baseline.columns:
            baseline['PatientID'] = range(1, len(baseline) + 1)

        # 2. Ottimizzazione
        optimized = clean(baseline, country)

        # 3. Benchmark individuale
        bench.compare(baseline, optimized, name=country)

        all_dfs.append(optimized.set_index(['State', 'PatientID']))

    # --- FINAL AGGREGATION & STATS ---
    full_dataset = pd.concat(all_dfs)

    # Calcolo statistiche finali di memoria
    total_mem_bytes = full_dataset.memory_usage(deep=True).sum()
    num_rows = len(full_dataset)
    mem_per_row = total_mem_bytes / num_rows

    print("\n" + "="*55)
    print(f"REPORT FINALE MEMORIA (Dataset Unificato)")
    print(f"Righe totali:         {num_rows:,}")
    print(f"Memoria occupata:     {bench.format_bytes(total_mem_bytes)}")
    print(f"Memoria media x riga: {mem_per_row:.2f} bytes")
    print("="*55)