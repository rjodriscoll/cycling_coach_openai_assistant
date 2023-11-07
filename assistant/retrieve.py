from pytube import Playlist
from youtube_transcript_api import YouTubeTranscriptApi
import argparse

def get_playlist_transcripts(playlist_url):
    playlist = Playlist(playlist_url)
    transcripts = {}
    for url in playlist.video_urls:
        video_id = url.split("watch?v=")[-1]
        try:
            transcripts[video_id] = YouTubeTranscriptApi.get_transcript(video_id)
        except Exception as e:
            print(f"An error occurred: {e}")
    return transcripts

transcripts = get_playlist_transcripts('your_playlist_url_here')
