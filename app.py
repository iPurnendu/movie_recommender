import pickle
import streamlit as st
import requests
import pandas as pd

similarity = pickle.load(open("similarity,pkl","rb"))
movie_dict= pickle.load(open("moive_to_dict.pkl","rb"))
movies_dataset= pd.DataFrame(movie_dict)

movie_others_dict = pickle.load(open("movie_details.pkl","rb"))
movie_others = pd.DataFrame(movie_others_dict)

def recommend(movie):
    recommend_movie=[]
    poster=[]
    genres=[]
    overview=[]
    production_companies=[]
    release_date=[]
    vote_average=[]
    vote_count=[]
    credits=[]
    movie_index = movies_dataset[movies_dataset["title"] == movie].index[0]
    angle_distance = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    for i in angle_distance[1:11]:
        recommend_movie.append(movies_dataset.loc[i[0]]["title"])
        poster.append(movies_dataset.loc[i[0]]["poster_path"])
        genres.append(movie_others.loc[i[0]]["genres"])
        overview.append(movie_others.loc[i[0]]["overview"])
        production_companies.append(movie_others.loc[i[0]]["production_companies"])
        release_date.append(movie_others.loc[i[0]]["release_date"])
        vote_average.append(movie_others.loc[i[0]]["vote_average"])
        vote_count.append(movie_others.loc[i[0]]["vote_count"])
        credits.append(movie_others.loc[i[0]]["credits"])
    return recommend_movie,poster,credits,genres,overview,production_companies,release_date,vote_average,vote_count
page_bg_image= """
<style>
[class="main css-uf99v8 egzxvld5"]{
background-image: url("https://img.freepik.com/free-vector/realistic-polygonal-background_52683-61087.jpg?w=1380&t=st=1682151680~exp=1682152280~hmac=c40567dea6d267757df65f6f13c080282b2d20eb929d21662756176e779b2459");
background-size: cover;
   }
[class="css-1avcm0n e8zbici2"]{
background-color: rgba(0,0,0,0);
}
</style>
"""

st.markdown(page_bg_image,unsafe_allow_html=True)

st.title("Best Movie Recommendations for You !!")


movie_list = movies_dataset["title"].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)
name=recommend(selected_movie)[0]
posters= recommend(selected_movie)[1]
credits =recommend(selected_movie)[2]
genres=recommend(selected_movie)[3]
overview=recommend(selected_movie)[4]
production_companies=recommend(selected_movie)[5]
release_date=recommend(selected_movie)[6]
vote_average=recommend(selected_movie)[7]
vote_count=recommend(selected_movie)[8]
if st.button("Recommend"):
    st.header("Here is your Recommend List")

    tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs([name[0],name[1],name[2],name[3],name[4],name[5],name[6],name[7],name[8],name[9]])


    tab1.header(name[0])
    tab1.header("Overview")
    tab1.subheader(overview[0])
    tab1.image(posters[0],width=400)
    tab1.header("Release Year")
    tab1.subheader(release_date[0])
    tab1.header("Rating")
    tab1.subheader(vote_average[0])
    tab1.header("Actor/Actress")
    tab1.subheader(credits[0])
    tab1.header("Movie Type")
    tab1.subheader(",".join(genres[0]))
    tab1.header("Production Companies")
    tab1.subheader(production_companies[0])

    tab2.header(name[1])
    tab2.header("Overview")
    tab2.subheader(overview[1])
    tab2.image(posters[1],width=400)
    tab2.header("Release Year")
    tab2.subheader(release_date[1])
    tab2.header("Rating")
    tab2.subheader(vote_average[1])
    tab2.header("Actor/Actress")
    tab2.subheader(credits[1])
    tab2.header("Movie Type")
    tab2.subheader(",".join(genres[1]))
    tab2.header("Production Companies")
    tab2.subheader(production_companies[1])

    tab3.header(name[2])
    tab3.header("Overview")
    tab3.subheader(overview[2])
    tab3.image(posters[2],width=400)
    tab3.header("Release Year")
    tab3.subheader(release_date[2])
    tab3.header("Rating")
    tab3.subheader(vote_average[2])
    tab3.header("Actor/Actress")
    tab3.subheader(credits[2])
    tab3.header("Movie Type")
    tab3.subheader(",".join(genres[2]))
    tab3.header("Production Companies")
    tab3.subheader(production_companies[2])

    tab4.header(name[3])
    tab4.header("Overview")
    tab4.subheader(overview[3])
    tab4.image(posters[3],width=400)
    tab4.header("Release Year")
    tab4.subheader(release_date[3])
    tab4.header("Rating")
    tab4.subheader(vote_average[3])
    tab4.header("Actor/Actress")
    tab4.subheader(credits[3])
    tab4.header("Movie Type")
    tab4.subheader(",".join(genres[3]))
    tab4.header("Production Companies")
    tab4.subheader(production_companies[3])

    tab5.header(name[4])
    tab5.header("Overview")
    tab5.subheader(overview[4])
    tab5.image(posters[4],width=400)
    tab5.header("Release Year")
    tab5.subheader(release_date[4])
    tab5.header("Rating")
    tab5.subheader(vote_average[4])
    tab5.header("Actor/Actress")
    tab5.subheader(credits[4])
    tab5.header("Movie Type")
    tab5.subheader(",".join(genres[4]))
    tab5.header("Production Companies")
    tab5.subheader(production_companies[4])

    tab6.header(name[5])
    tab6.header("Overview")
    tab6.subheader(overview[5])
    tab6.image(posters[5],width=400)
    tab6.header("Release Year")
    tab6.subheader(release_date[5])
    tab6.header("Rating")
    tab6.subheader(vote_average[5])
    tab6.header("Actor/Actress")
    tab6.subheader(credits[5])
    tab6.header("Movie Type")
    tab6.subheader(",".join(genres[5]))
    tab6.header("Production Companies")
    tab6.subheader(production_companies[5])

    tab7.header(name[6])
    tab7.header("Overview")
    tab7.subheader(overview[6])
    tab7.image(posters[6],width=400)
    tab7.header("Release Year")
    tab7.subheader(release_date[6])
    tab7.header("Rating")
    tab7.subheader(vote_average[6])
    tab7.header("Actor/Actress")
    tab7.subheader(credits[6])
    tab7.header("Movie Type")
    tab7.subheader(",".join(genres[6]))
    tab7.header("Production Companies")
    tab7.subheader(production_companies[6])

    tab8.header(name[7])
    tab8.header("Overview")
    tab8.subheader(overview[7])
    tab8.image(posters[7],width=400)
    tab8.header("Release Year")
    tab8.subheader(release_date[7])
    tab8.header("Rating")
    tab8.subheader(vote_average[7])
    tab8.header("Actor/Actress")
    tab8.subheader(credits[7])
    tab8.header("Movie Type")
    tab8.subheader(",".join(genres[7]))
    tab8.header("Production Companies")
    tab8.subheader(production_companies[7])

    tab9.header(name[8])
    tab9.header("Overview")
    tab9.subheader(overview[8])
    tab9.image(posters[8],width=400)
    tab9.header("Release Year")
    tab9.subheader(release_date[8])
    tab9.header("Rating")
    tab9.subheader(vote_average[8])
    tab9.header("Actor/Actress")
    tab9.subheader(credits[8])
    tab9.header("Movie Type")
    tab9.subheader(",".join(genres[8]))
    tab9.header("Production Companies")
    tab9.subheader(production_companies[8])

    tab10.header(name[9])
    tab10.header("Overview")
    tab10.subheader(overview[9])
    tab10.image(posters[9],width=400)
    tab10.header("Release Year")
    tab10.subheader(release_date[9])
    tab10.header("Rating")
    tab10.subheader(vote_average[9])
    tab10.header("Actor/Actress")
    tab10.subheader(credits[9])
    tab10.header("Movie Type")
    tab10.subheader(",".join(genres[9]))
    tab10.header("Production Companies")
    tab10.subheader(production_companies[9])

