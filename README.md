<h1>Download lyrics from Netease Music</h1>
<h2>Steps:</h2>
<li>Start with a music file downloaded from Netease Music</li>
<li>Load the id3v2 tag from the file, read section "comment"</li>
<li>Decrypt the comment using AES base64 to get the details</li>
<li>Retrieve title, singer and song id from the decrypted text</li>
<li>Search for lyrics using the song id. Url format: http://music.163.com/api/song/media?id=[song id]</li>
<li>Process on the text, save it to a file named "[title] - [singer].lrc"</li>