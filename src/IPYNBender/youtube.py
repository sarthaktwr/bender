from IPython import display
from py_youtube import Data
from ensure import ensure_annotations
from IPYNBender.logger import logger
from IPYNBender.custom_exception import InvalidURLException

@ensure_annotations
def get_time_info(URL: str) -> int:
    def _verify_vid_id_len(vid_id, __excepted_len = 11):
        len_of_vid_id = len(vid_id)
        if len_of_vid_id != __excepted_len:
            raise InvalidURLException(
                f'Invalid video id with length: {len_of_vid_id}, excepted: {__excepted_len}'
            )
    try:
        split_val = URL.split('=')
        if 'watch' in URL:
            if ('&t' in URL):
                vid_id, time = split_val[-2][: -2], int(split_val)[-1][:-1]
                _verify_vid_id_len(vid_id)
                logger.info(f'Video starts at: {time}')
                return time
            else:
                vid_id, time = split_val[-2][: -2], 0
                _verify_vid_id_len(vid_id)
                logger.info(f'Video starts at: {time}')
                return time
        else:
            if '=' in URL and '?t' in URL:
                vid_id, time = split_val[0].split('/')[-1][: -2], int(split_val[-1])
                _verify_vid_id_len(vid_id)
                logger.info(f'Video starts at: {time}')
                return time
            else:
                vid_id, time = URL.split('/')[-1], 0

    except Exception:
        raise InvalidURLException            

@ensure_annotations
def render_Youtube_video(URL: str, width: int = 780, height: int = 1280) -> str:
    try:
        if URL in None:
            raise InvalidURLException("URL cannot be none")
        data = Data(URL).data()
        if data['publishdate'] is not None:
            time = get_time_info()
            vid_ID = data['id']
            embed_URL = f'https://www.youtube/embed/{vid_ID}?start={time}'
            logger.info(f'embed URL: {embed_URL}')
            iframe = f'''<iframe 
            width="{width}" height="{height}" 
            src="https://www.youtube.com/embed/toQmgWrfiOw" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; 
            autoplay; clipboard-write;
            encrypted-media; gyroscope; 
            picture-in-picture; 
            web-share" allowfullscreen>
            </iframe>'''
            display.display(display.HTML(iframe))
            return 'Success'
    except Exception as e:  
        raise e
    
