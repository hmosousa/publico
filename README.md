# Tradutor

Training a model to translate from English to European Portuguese.

## Build data

First, download the data:

```sh
sh scripts/download_data.sh
```

Then process the dataset:

```sh
python scripts/parse_publico.py
```

And translate the corpus from Portuguese to English.

```sh
python scripts/translate_publico.py
```

This will produce a series of folders on the `resources` directory with the data required to fine-tune the model.


