# Hotvids 0.1

from moviepy.editor import *
from textwrap3 import wrap
from random import randint, randrange
import json
from datetime import datetime

tempototal = datetime.now()
ready_news = json.load(open('data/data.json', 'r'))
metatags = ready_news[1]
ready_news = ready_news[0]
all_clips = []
for i in ready_news:  # Set random values for pick, flip_x, rotate, overlay color
    video_bg = VideoFileClip(f'vids/minivids/{str(randint(1,26))}.mp4').set_opacity(0.3)
    if randint(0,1) == 1:
        video_bg = video_bg.fx(vfx.mirror_x)
    else: pass
    if randint(0,1) == 1:
        video_bg = video_bg.rotate(180)
    else: pass
    img_bg = ImageClip(f'{i[3][:-4]}blur.jpg')
    video_bg = CompositeVideoClip([img_bg,video_bg],use_bgclip=True).set_duration(7.0)
    mrg = 0.32  #%
    paragf = wrap(i[2], 26)
    paragf.append(' '), paragf.append(' '), paragf.append(' ')
    # Add texts to the video
    clip_img = ImageClip(i[3]).set_start(0.5).set_position((0.05,0.29), relative=True)
    comp_data = TextClip(i[4],font='FreeMono', fontsize=50,method='label',
                    color='yellow').set_start(0.6).set_position((mrg,0.28), relative=True)
    comp_font = TextClip(i[1],font='FreeMono', fontsize=40,method='label',
                    color='orange').set_start(0.7).set_position((mrg,0.34), relative=True)
    t0 = TextClip(paragf[0],font='FreeSerif',fontsize=65,color='white',
                    method='label').set_start(0.8).set_position((mrg,0.41), relative=True)
    t1 = TextClip(paragf[1],font='FreeSerif',fontsize=60,color='white',
                    method='label').set_start(0.9).set_position((mrg,0.50), relative=True)
    t2 = TextClip(paragf[2],font='FreeSerif',fontsize=57,color='white',
                    method='label').set_start(0.95).set_position((mrg,0.58), relative=True)
    t3 = TextClip(paragf[3],font='FreeSerif',fontsize=53,color='white',
                    method='label').set_start(1).set_position((mrg,0.65), relative=True)
    desc_text = TextClip("Check link in the description",font='FreeMono',fontsize=40,method='label',
                    color='white').set_start(4).set_position(('center',0.88), relative=True)
    video_news = CompositeVideoClip([video_bg,clip_img,comp_data,comp_font,t0,t1,t2,t3,desc_text],
                use_bgclip=True).set_duration(7.0).crossfadein(0.3).fadeout(0.3)
    all_clips.append(video_news)
# Deal with thumbnail, opening and closing parts
thumbnail = ImageClip('imgs/thumbnail.jpg')
opening = VideoFileClip('vids/opening.mp4').set_start(0.2)
opening = CompositeVideoClip([thumbnail,opening]).set_duration(4.0).fadeout(0.3)
temp_grp = [opening]
all_clips = temp_grp + all_clips
closing = VideoFileClip('vids/closing.mp4')
closing = CompositeVideoClip([closing]).set_duration(randrange(7.0,10.0))
all_clips.append(closing)
# Render video and audio as a file and saves it
final_clip = concatenate_videoclips(all_clips, method='compose')
audioclip = AudioFileClip(f"audio/{randint(1,24)}.aac").subclip(0, int(final_clip.duration)).audio_fadeout(3)
final_clip = final_clip.set_audio(audioclip)
final_clip.write_videofile('vids/youtube_final.mp4',fps=24,preset='veryfast',ffmpeg_params=['-c:a','copy','-metadata', f'''comment={str(metatags)[1:-1].replace("'","")}'''])