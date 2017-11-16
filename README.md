<h1>Download lyrics from Netease Music</h1>
<h2>Steps:</h2>
<li>1. Start with a music file downloaded from Netease Music</li>
<li>2. Load the id3v2 tag from the file, read section "comment"</li>
<li>3. Decrypt the comment using AES base64 to get the details</li>
<li>4. Retrieve title, singer and song id from the decrypted text</li>
<li>5. Search for lyrics using the song id. Url format: http://music.163.com/api/song/media?id=[song id]</li>
<li>6. Process on the text, save it to a file named "[title] - [singer].lrc"</li>