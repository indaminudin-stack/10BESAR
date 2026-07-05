import pandas as pd
def export_excel(results):
    df = pd.DataFrame(results)
    df = df.sort_values(by="Score",ascending=False)

    df.to_excel("hasil_screening.xlsx", index=False)
    print("hasil_screening.xlsx berhasil dibuat")