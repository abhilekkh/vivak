from api import get_anime_details,get_character_details

def format_anime_list(data):
    return [
        {
            "mal_id": item.get("mal_id"),
            "title": item.get("title"),
            "image_url": item.get("images", {}).get("jpg", {}).get("image_url"),
            "score": item.get("score") or "N/A"
        }
        for item in data.get("data", [])
    ]

def format_anime_detailed_list(mal_id):
    data=get_anime_details(mal_id)
    character_data=get_character_details(mal_id)

    item=data["data"]
    char_item=character_data["data"]
    return  {

            "image": item.get("images",{}).get("jpg",{}).get("image_url") or "N/A",
            "youtube_embed": item.get("trailer",{}).get("embed_url") or "N/A",

            "title": item.get("title") or "N/A",
            "episodes": item.get("episodes") or "N/A",
            "source": item.get("source") or "N/A",
            "type": item.get("type") or "N/A",

            "genres": [ genre.get("name") for genre in item.get("genres",[])],


           "themes": [ theme.get("name") for theme in item.get("themes",[])],
            "status": item.get("status"),
            "airing_start": item.get("aired",{}).get("from") or "N/A",
            "airing_end" : item.get("aired",{}).get("to") or "N/A",

            "score": item.get("score") or "N/A",
            "rating": item.get("rating") or "N/A",
            "ranking" :item.get("rank") or "N/A",
            "popularity": item.get("popularity") or "N/A",
            "synopsis": item.get("synopsis") or "N/A",
            "season": item.get("season") or "N/A",
            "demographics": [ demographic.get("name") for demographic in item.get("demographics",[])],
            "licensors": [ licensor.get("name") for licensor in item.get("licensors",[])],
            "studios": [ studio.get("name") for studio in item.get("studios",[])],
            "producers": [ producer.get("name") for producer in item.get("producers",[])],

            "character": [
             {
              "name": entry.get("character", {}).get("name"),
              "image": entry.get("character", {}).get("images", {}).get("jpg", {}).get("image_url"),
               "role": entry.get("role")
             }
           for entry in char_item
            ]
            
    }