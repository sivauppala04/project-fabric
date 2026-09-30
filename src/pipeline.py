import os
import pandas as pd

def run_medallion(base='data'):
    raw = os.path.join(base,'raw')
    bronze = os.path.join(base,'bronze')
    silver = os.path.join(base,'silver')
    gold = os.path.join(base,'gold')

    os.makedirs(raw, exist_ok=True)
    os.makedirs(bronze, exist_ok=True)
    os.makedirs(silver, exist_ok=True)
    os.makedirs(gold, exist_ok=True)

    # create raw sample
    df = pd.DataFrame({'id':[1,2,3], 'value':[10,20,30]})
    df.to_csv(os.path.join(raw,'sample.csv'), index=False)

    # bronze
    df = pd.read_csv(os.path.join(raw,'sample.csv'))
    df['value'] = df['value'].astype(float)
    df.to_csv(os.path.join(bronze,'sample.csv'), index=False)

    # silver
    df = pd.read_csv(os.path.join(bronze,'sample.csv'))
    df['value_usd'] = df['value'] * 1.0
    df.to_csv(os.path.join(silver,'sample_enriched.csv'), index=False)

    # gold
    agg = df['value_usd'].sum()
    with open(os.path.join(gold,'summary.txt'),'w') as f:
        f.write(str(agg))

if __name__ == '__main__':
    run_medallion()
