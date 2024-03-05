from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import time

class MFEMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, root_path:str):
        super().__init__(app)
        self.root_path = root_path
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        if "Hx-Request" in request.headers:
            # add hx_request to state so JINJA2 use this to add css and js files
            request.state.hx_request = True
        else:
            request.state.hx_request = False
        # When local dev mode, set this to serve js and other static files
        request.state.root_path=self.root_path
        # Call the next middleware or route handler
        response = await call_next(request)
        # Modify the response headers
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response

# Add the middleware to the application

