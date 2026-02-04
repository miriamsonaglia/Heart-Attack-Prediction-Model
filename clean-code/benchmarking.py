import pandas as pd
import numpy as np

def format_bytes(size):
    """Converte i byte in un formato leggibile (KB, MB)."""
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'KB', 2: 'MB', 3: 'GB'}
    while size > power:
        size /= power
        n += 1
    return f"{size:.2f} {power_labels[n]}"

def get_detailed_stats(df):
    """Estrae statistiche dettagliate da un DataFrame."""
    mem_usage = df.memory_usage(deep=True)
    return {
        "total_bytes": mem_usage.sum(),
        "columns_bytes": mem_usage,
        "dtypes": df.dtypes.astype(str).to_dict(),
        "rows": len(df),
        "cols": len(df.columns)
    }

def compare(df_raw, df_optimized, name="Dataset"):
    """
    Confronta due dataframe (prima e dopo l'ottimizzazione)
    e restituisce un report strutturato.
    """
    stats_raw = get_detailed_stats(df_raw)
    stats_opt = get_detailed_stats(df_optimized)

    raw_bytes = stats_raw["total_bytes"]
    opt_bytes = stats_opt["total_bytes"]

    # Calcolo riduzione
    reduction_pct = (1 - (opt_bytes / raw_bytes)) * 100
    optimization_factor = raw_bytes / opt_bytes if opt_bytes > 0 else 0

    print(f"\n{'='*18} REPORT: {name} {'='*18}")
    print(f"Righe: {stats_opt['rows']:,} | Colonne: {stats_opt['cols']}")
    print(f"Memoria Pre:  {format_bytes(raw_bytes)}")
    print(f"Memoria Post: {format_bytes(opt_bytes)}")
    print(f"Risparmio:    {reduction_pct:.2f}% (Fattore: {optimization_factor:.1f}x)")

    # Confronto Dtypes (il cuore dell'ottimizzazione)
    print("-" * 18 + " Cambiamenti Tipi " + "-" * 18)

    # Creiamo un piccolo dataframe per visualizzare i cambiamenti delle colonne comuni
    comparison_data = []
    common_cols = set(stats_raw["dtypes"].keys()) & set(stats_opt["dtypes"].keys())

    for col in sorted(common_cols):
        dtype_old = stats_raw["dtypes"][col]
        dtype_new = stats_opt["dtypes"][col]
        mem_old = format_bytes(stats_raw["columns_bytes"][col])
        mem_new = format_bytes(stats_opt["columns_bytes"][col])

        # Mostra solo se c'è stato un cambiamento significativo
        if dtype_old != dtype_new:
            comparison_data.append([col, dtype_old, dtype_new, mem_old, mem_new])

    if comparison_data:
        comp_df = pd.DataFrame(comparison_data, columns=["Colonna", "Tipo Old", "Tipo New", "Mem Old", "Mem New"])
        # Formattazione per la stampa
        print(comp_df.to_string(index=False))
    else:
        print("Nessun cambiamento di tipo rilevato nelle colonne comuni.")

    print("="*55 + "\n")

    return {
        "dataset": name,
        "memory_start": raw_bytes,
        "memory_end": opt_bytes,
        "reduction_pct": reduction_pct
    }