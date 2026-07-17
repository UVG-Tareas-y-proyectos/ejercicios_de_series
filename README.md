# Hoja de ejercicios - Series de tiempo

Temperatura promedio de la tierra (1950-2026) en la región de Guatemala.
Todos los ejercicios están en `notebooks/ejercicios.ipynb`.

## Correr

```bash
python -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/jupyter notebook notebooks/ejercicios.ipynb
```

## Estructura

- `notebooks/ejercicios.ipynb` - todos los ejercicios (1 al 8)
- `data/raw/` - csv original, no se modifica
- `data/processed/` - train/test y salidas generadas por el notebook (no se versiona)
- `src/preparar_datos.py` - limpieza y separación train/test (genera lo de `data/processed/`)
