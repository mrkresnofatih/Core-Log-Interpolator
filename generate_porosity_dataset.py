import coreloginterpolate as cli


def execute():
    # POROSITY PREDICTION
    # Collect PORHE & PORFLU As Output, RHOB & NPHI As Input
    # Note: ASDJ10 does not have a RHOB data. So just skip for this specific well

    # 1 - Well GRH2
    cli.interpolate_core_with_log(
        "T1-GRH2.txt",
        ["DEPTH", "PORHE", "PORFLU"],
        0,
        "L1-GRH2.txt",
        ["DEPTH", "NPHI", "RHOB"],
        0,
        "POROSITY-PREDICTION-SET-1.csv"
    )

    # 2 - Well GRH1
    cli.interpolate_core_with_log(
        "T2-GRH1.txt",
        ["DEPTH", "PORHE", "PORFLU"],
        0,
        "L2-GRH1.txt",
        ["DEPTH", "NPHI", "RHOB"],
        0,
        "POROSITY-PREDICTION-SET-2.csv"
    )

    # 3 - Well GRH5
    cli.interpolate_core_with_log(
        "T3-GRH5.txt",
        ["DEPTH", "PORHE", "PORFLU"],
        0,
        "L3-GRH5.txt",
        ["DEPTH", "NPHI", "RHOB"],
        0,
        "POROSITY-PREDICTION-SET-3.csv"
    )

    # 4 - Well GRH7
    cli.interpolate_core_with_log(
        "T4-GRH7.txt",
        ["DEPTH", "PORHE", "PORFLU"],
        0,
        "L4-GRH7.txt",
        ["DEPTH", "NPHI", "RHOB"],
        0,
        "POROSITY-PREDICTION-SET-4.csv"
    )

    # 5 - Well MDL2
    cli.interpolate_core_with_log(
        "T5-MDL2.txt",
        ["DEPTH", "PORHE", "PORFLU"],
        0,
        "L5-MDL2.txt",
        ["DEPTH", "NPHI", "RHOB"],
        0,
        "POROSITY-PREDICTION-SET-5.csv"
    )

    # 6 - Well ASDJ2
    cli.interpolate_core_with_log(
        "T6-ASDJ2.txt",
        ["DEPTH", "PORHE", "PORFLU"],
        0,
        "L6-ASDJ2.txt",
        ["DEPTH", "NPHI", "RHOB"],
        0,
        "POROSITY-PREDICTION-SET-6.csv"
    )

    # 7 - Well ASDJ3
    cli.interpolate_core_with_log(
        "T7-ASDJ3.txt",
        ["DEPTH", "PORHE", "PORFLU"],
        0,
        "L7-ASDJ3.txt",
        ["DEPTH", "NPHI", "RHOB"],
        0,
        "POROSITY-PREDICTION-SET-7.csv"
    )

    # 8 - Well ASDJ23
    cli.interpolate_core_with_log(
        "T9-ASDJ23.txt",
        ["DEPTH", "PORHE", "PORFLU"],
        0,
        "L9-ASDJ23.txt",
        ["DEPTH", "NPHI", "RHOB"],
        0,
        "POROSITY-PREDICTION-SET-8.csv"
    )