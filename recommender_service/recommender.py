import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

DATA_PATH = os.path.join(os.path.dirname(__file__), "Meta_df0524.csv")


df_test = pd.read_csv(DATA_PATH, sep="\t", encoding='utf-8')
df_final = df_test.copy()

X = df_final.select_dtypes('number')
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

model = NearestNeighbors(n_neighbors=6).fit(X_scaled)

def search_movies(title):
    """
    Recherche des films correspondant au titre saisi.
    """
    target = df_final.loc[
        df_test['originalTitle'].str.contains(title, case=False, na=False) |
        df_test['primaryTitle'].str.contains(title, case=False, na=False)
    ].sort_values(by="numVotes", ascending=False)

    return target.reset_index()

def recommend_movies(index):
    """
    Génère des recommandations basées sur un index de film choisi.
    """
    target_final_2d_array = X_scaled[index, :].reshape(1, -1)
    distance, ids = model.kneighbors(target_final_2d_array)
    reco = ids[:, 1:]  # Exclure le film d'origine

    return df_final.iloc[reco[0], :]
























# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.neighbors import NearestNeighbors


# df_test = pd.read_csv(
#     r'C:\Users\WCS_L\Documents\My_py\WCS\projets\recommander_system\Meta_df0524.csv', 
#     sep="\t", 
#     encoding='utf-8'
# )

# df_final = df_test.copy()

# X = df_final.select_dtypes('number')
# scaler = MinMaxScaler()
# X_scaled = scaler.fit_transform(X)

# model = NearestNeighbors(n_neighbors=6).fit(X_scaled)

# while True:
#     titre = input('Veuillez saisir un titre de film: ')
#     target = df_final.loc[df_test['originalTitle'].str.contains(titre, case=False, na=False) |
#                          df_test['primaryTitle'].str.contains(titre, case=False, na=False)
#                          ].sort_values(by="numVotes", ascending=False)
#     if target.shape[0] == 0:
#         print('Nous ne parvenons pas à identifier ce film, merci de préciser votre demande.')

#     elif target.shape[0] > 1:
#         affichage = target.reset_index()
#         print('Films en lien avec le titre saisi: ')
#         display(affichage[['primaryTitle', 'originalTitle', 'startYear']])
#         try:
#             ligne = int(input("Plusieurs films correspondent à votre recherche, merci de nous indiquer le numéro du film dans cette liste : "))
#             target_final = target.loc[target['tconst'] == affichage.at[ligne, 'tconst']]
#             break
#         except ValueError:
#             print("Entrée non valide. Veuillez entrer un numéro valide.")
#         except IndexError:
#             print("Numéro hors limite. Veuillez entrer un numéro valide.")
#     else:
#         target_final = target
#         break

# target_final_2d_array = X_scaled[target_final.index[0],:].reshape(1,-1)

# distance, id  = model.kneighbors(target_final_2d_array)
# reco = id[:,1:]

# df_reco = df_final.iloc[reco[0],:]


# selected_cols = ['primaryTitle','originalTitle','startYear','averageRating', 'genres']  

# print("film recherché")
# display(target_final[selected_cols])

# print('\nrecherche en cours...\n')

# print('Notre selection de films basé sur votre recherche')
# display(df_reco[selected_cols])
