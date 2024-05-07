import pandas as pd


def replace_accents(df: pd.DataFrame, cols: list = None) -> pd.DataFrame:
    if cols:
        df = df[cols]
        for c in df.columns:
            if 'Total' in c:
                df = df.rename(columns={c: c.split('Total')[0]})

        df = df.replace(['á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'ä', 'ë', 'ï', 'ö', 'ü', 'š', 'ć', 'ý'],
                        ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 's', 'c', 'y'],
                        regex=True)
    else:
        df = df.replace(['á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'ä', 'ë', 'ï', 'ö', 'ü', 'š', 'ć', 'ý'],
                        ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 's', 'c', 'y'],
                        regex=True)

    return df


def rename_cols(df: pd.DataFrame, cols: list = None) -> pd.DataFrame:
    if cols:

        df = df[cols]
        for c in df.columns:
            if 'Total' in c:
                df = df.rename(columns={c: c.split('Total')[0]})
    else:

        pass

    return df
