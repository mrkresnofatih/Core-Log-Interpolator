import coreloginterpolate as cli

cli.interpolate_core_with_log(
    "T1-GRH2.txt",
    ["DEPTH", "KHINF", "KHAIR", "PORHE", "KVINF"],
    0,
    "L1-GRH2.txt",
    ["DEPTH", "CLI", "DCOR", "GR", "LLD", "LLD"],
    0,
    "M1-GRH2.csv"
)