import pandas as pd

def compare():
    base = pd.read_csv('exportGroupMembers_2026-2-9.csv')
    users = pd.read_csv('users_09_02_2026 20_21_52.csv')

    # Normalizar llaves de búsqueda
    group_emails = set(base['userPrincipalName'].dropna().str.lower().unique())
    if 'mail' in base.columns:
        group_emails.update(base['mail'].dropna().str.lower().unique())

    # Filtrar faltantes
    missing = users[~users['User principal name'].str.lower().isin(group_emails)]
    missing.to_csv('usuarios_faltantes.csv', index=False)
    print(f"Completado. {len(missing)} usuarios nuevos encontrados.")

if __name__ == "__main__":
    compare()