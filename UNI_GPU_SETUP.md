# Uni GPU Setup (RAG Project)

## 1. Repository holen
```bash
git clone <YOUR_REPO_URL>
cd rag_project
```

## 2. Conda-Umgebung erstellen
```bash
conda env create -f environment.yml
conda activate rag-project
python -m ipykernel install --user --name rag-project --display-name "rag-project"
```

## 3. GPU prüfen
```bash
nvidia-smi
python -c "import torch; print('torch:', torch.__version__, 'cuda:', torch.cuda.is_available())"
```

Hinweis:
- Falls `torch.cuda.is_available()` `False` ist, installiere eine passende CUDA-Version von PyTorch
  entsprechend der Uni-Treiber.

## 4. Basis-Smoke-Test
```bash
python -c "import src.processing as p; import src.indexing as i; print('imports ok')"
```

## 5. Pipeline-Reihenfolge
1. `notebooks/proccesing.ipynb` laufen lassen (clean pages + chunks + stats)
2. `notebooks/build_index.ipynb` laufen lassen (Index bauen)
3. `notebooks/rag_playground.ipynb` testen (Queries)

## 6. Für reproduzierbare Bachelor-Ergebnisse
- Immer gleiche Modellnamen/Parameter verwenden.
- Output-Dateien mit Zeitstempel behalten.
- Final verwendete Commit-ID + Environment notieren.
- Ergebnisse und Metriken (z. B. hit@k) dokumentieren.
