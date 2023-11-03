from typing import List, Dict, Any
import numpy as np
import pandas as pd

def records2df(records: List[Dict[str,float]]) -> pd.DataFrame:
    if len(records) != 21 or (len(records) > 0 and records[0].keys() != {'x', 'y', 'z'}):
        raise ValueError('records must be a list of dicts with keys x, y, z')
    df = pd.DataFrame(records)
    return df

def landmark2df(landmarks: list) -> pd.DataFrame:
    lns = dict(x=[], y=[], z=[])
    for landmark in landmarks:
        lns['x'].append(landmark.x)
        lns['y'].append(landmark.y)
        lns['z'].append(landmark.z)
    df = pd.DataFrame(lns, dtype=np.float32)
    return df

def landmark2records(landmarks: list) -> List[Dict[str,float]]:
    lns = []
    for landmark in landmarks:
        lns.append(dict(x=landmark.x, y=landmark.y, z=landmark.z))
    return lns