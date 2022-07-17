import uvicorn

from app import create_app
from app.config import config
from app.utils import PLATFORM

app = create_app()
use_colors = PLATFORM not in ('android', 'win')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=config.port,
                use_colors=use_colors, debug=config.debug)
