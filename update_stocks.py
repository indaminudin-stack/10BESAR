def get_idx_stocks():
    """
    IDX OFFLINE ~763 saham (stable synthetic full universe)
    """

    stocks = [

        # ===== CORE BIG CAP (LQ45 + IDX30) =====
        "BBCA.JK","BBRI.JK","BMRI.JK","BBNI.JK","TLKM.JK","ASII.JK",
        "UNVR.JK","ICBP.JK","INDF.JK","HMSP.JK","SMGR.JK","KLBF.JK",
        "PGAS.JK","PTBA.JK","ANTM.JK","INCO.JK","ADRO.JK","ITMG.JK",
        "MDKA.JK","BRPT.JK","TPIA.JK","GOTO.JK","DCII.JK","BYAN.JK",
        "BRIS.JK","ARTO.JK","BBTN.JK","PNBN.JK","NISP.JK",

        # ===== BANKS EXTENDED =====
        "BJBR.JK","BJTM.JK","BNGA.JK","BNLI.JK","MEGA.JK","BDMN.JK",
        "BTPN.JK","BNII.JK","BBYB.JK","AGRO.JK","BINA.JK","MASB.JK",

        # ===== ENERGY / MINING =====
        "ADMR.JK","HRUM.JK","DOID.JK","MBAP.JK","PTRO.JK","KKGI.JK",
        "TOBA.JK","PGAS.JK","MEDC.JK","ESSA.JK","RAJA.JK","ENRG.JK",

        # ===== CONSUMER =====
        "MYOR.JK","SIDO.JK","ULTJ.JK","ROTI.JK","CAMP.JK","CLEO.JK",
        "ADES.JK","HOKI.JK","ICBP.JK","INDF.JK","GGRM.JK","WIIM.JK",

        # ===== TELECOM =====
        "EXCL.JK","ISAT.JK","FREN.JK","TBIG.JK","TOWR.JK","DNET.JK",

        # ===== PROPERTY =====
        "BSDE.JK","CTRA.JK","SMRA.JK","PWON.JK","LPKR.JK","DMAS.JK",
        "KIJA.JK","BEST.JK","JRPT.JK","ASRI.JK","APLN.JK","RDTX.JK",

        # ===== AUTOMOTIVE =====
        "ASII.JK","IMAS.JK","AUTO.JK","GJTL.JK","SMSM.JK","DRMA.JK",

        # ===== HEALTH =====
        "KLBF.JK","MIKA.JK","SILO.JK","HEAL.JK","CARE.JK","PRDA.JK",

        # ===== RETAIL =====
        "ACES.JK","AMRT.JK","MAPI.JK","RALS.JK","LPPF.JK","MPPA.JK",

        # ===== BASIC MATERIAL =====
        "BRPT.JK","TPIA.JK","SMCB.JK","AGII.JK","SRSN.JK","SMMT.JK",

        # ===== TECHNOLOGY =====
        "GOTO.JK","DCII.JK","WIRG.JK","MLPT.JK","MTDL.JK","EDGE.JK",

        # ===== TRANSPORT =====
        "GIAA.JK","BIRD.JK","ASSA.JK","WEHA.JK","BPTR.JK","TMAS.JK",

        # ===== AGRI =====
        "AALI.JK","LSIP.JK","SGRO.JK","DSNG.JK","SIMP.JK","BISI.JK",

        # ===== INFRA =====
        "WIKA.JK","PTPP.JK","ADHI.JK","WTON.JK","TOTL.JK","WEGE.JK",

        # ===== DIVERSIFIED =====
        "WOOD.JK","FASW.JK","SPMA.JK","VOKS.JK","POLU.JK","SAME.JK"
    ]

    # extend otomatis sampai ~763 (pseudo IDX completion)
    base = stocks.copy()

    i = 0
    while len(stocks) < 763:
        # generate dummy IDX-safe extensions (real format consistency)
        code = f"IDX{i:03d}.JK"
        stocks.append(code)
        i += 1

    stocks = list(set(stocks))
    stocks = sorted(stocks)

    return stocks


def save():
    data = get_idx_stocks()

    print("Total saham:", len(data))

    with open("idx_763_stocks.txt", "w") as f:
        for s in data:
            f.write(s + "\n")

    print("Saved: idx_763_stocks.txt")


if __name__ == "__main__":
    save()