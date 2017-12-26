# Audio-Mining-in-python
In this repo I'm taking an audio file generate its transcript by using Liv.ai API's. You can use any API or tools to generate transcript. On generated output I am going to do text mining.


CURL REQUEST TO GENERATE TRANSCRIPT
I'm using Liv.ai you can also use the same or any other API.

curl   -H "Authorization: Token bae38f09a489fc109ae35886e73574225b10aebe"   --form "user=1997353"   --form "language=EN"   --form "audio_file=@/SO001.wav" -o output.txt  https://dev.liv.ai/liv_transcription_api/recordings/


