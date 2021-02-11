mkdir -p ~/.streamlit/
echo "[general]
email = \"joris.cosentino.pro@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml