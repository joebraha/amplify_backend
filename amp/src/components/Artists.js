import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from 'axios';

const CLIENT_ID = "c0e9c73676684f3e8d10acc56b94be60";
const REDIRECT_URI = "http://localhost:3000/artists"; // TODO: add url/spotify to redirect_url allow list
const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize";
const RESPONSE_TYPE = "token";

function grabToken () {
    return window.location.hash.substring(1).split('&').reduce((initial, item)=>{
      let parts = item.split("=");
      initial[parts[0]] = decodeURIComponent(parts[1]);
      return initial
    }, {});
}

function Artists() {
    const [token, setToken] = useState("");
    const [searchKey, setSearchKey] = useState("");
    const [artists, setArtists] = useState([]);

    useEffect(() => {
        const token = grabToken();
        console.log(token);
        setToken(token);
    }, []);

    const logout = () => {
        setToken("");
        window.localStorage.removeItem("token");
    };

    const searchArtists = async (e) => {
        e.preventDefault();
        if (!token) {
            console.error("No valid token found.");
            return;
        }
        try {
            const { data } = await axios.get("https://api.spotify.com/v1/search", {
                headers: {
                    Authorization: `Bearer ${token.access_token}`, // Use the access token
                },
                params: {
                    q: searchKey,
                    type: "artist",
                },
            });
            setArtists(data.artists.items);
        } catch (error) {
            console.error("Error searching for artists:", error);
        }
    };
    

    const renderArtists = () => {
        return artists.map((artist) => (
            <div key={artist.id}>
                {artist.images.length ? (
                    <img width={"100%"} src={artist.images[0].url} alt={artist.name} />
                ) : (
                    <div>No Image</div>
                )}
                {artist.name}
            </div>
        ));
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Spotify Login</h1>
                <a href={`${AUTH_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=${RESPONSE_TYPE}`}>Login
                        to Spotify</a>

                    <button onClick={logout}>Logout</button>
                    <Link to="/">Return to Home</Link> {}

                {token ? (
                    <form onSubmit={searchArtists}>
                        <input type="text" onChange={(e) => setSearchKey(e.target.value)} />
                        <button type={"submit"}>Search</button>
                    </form>
                ) : (
                    <h2>Please login</h2>
                )}

                {renderArtists()}
            </header>
        </div>
    );
};

export default Artists;
